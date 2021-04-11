#!/usr/bin/python3 

import os
import re
import sys
import time
import json
import importlib
from collections import abc
import multiprocessing as mp

from collections import namedtuple as nt


class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def print_green(text):
    print(f"{bcolors.OKGREEN}{text}{bcolors.ENDC}")  


def print_red(text):
    print(f"{bcolors.FAIL}{text}{bcolors.ENDC}")  


Test = nt("Test", "solution result test_case name duration")
lock = mp.Lock()


def check_result(test):
    out = test.solution.format_output(*listify(test.result))
    lock.acquire()
    if test.test_case["output"] == out:
        print_green(f"Test: {test.name} is [OK]\tduration: {test.duration}")
        print_green(out)
        print("-" * 10)
    else:
        print_red(f"Test: {test.name} is [FAIL]\tduration: {test.duration}")
        print_red(f"Input:\n{test.test_case['input']}\n---")
        print_green(test.test_case["output"])
        print_red(out)
        print("-" * 10)
    lock.release()


def listify(a):
    if isinstance(a, str):
        return [a.strip()]
    if isinstance(a, abc.Iterable):
        return list(filter(None, a))
    return [a]


def run_test(program_path, test_path):
    with open(test_path, "r") as test:
        test_case = json.load(test)
        solution_module_name = ".".join(program_path.split("/")) + "." + program_path.split("/")[-1]
        solution = importlib.import_module(solution_module_name)
        try:
            # each solution should have main() function which returns the result solution
            # and get_input() function which accepts the input as str, returns the input in prepared for main format
            # and format_output() function which returns string to compare
            inp = solution.get_input(test_case["input"])
            started = time.time()
            res = solution.main(*listify(inp))
        except Exception as ex:
            lock.acquire()
            print_red("{} [FAIL]".format(test_path))
            lock.release()
            raise ex
        finished = time.time()
        check_result(Test(solution, res, test_case, test_path.split("/")[-1], finished - started))


SYSTEM_CORES_AMOUNT = 16


def flush_processes(procs):
    for p in procs:
        p.start()
    for p in procs:
        p.join()


def main(argv):
    """
    Assuming each program is in it's own folder containing "test" folder inside
    Each test is a json file with "input" and "output" string keys
    """
    cwd = os.getcwd()
    program_path = os.path.join(cwd, argv[1])
    test_processes = []
    for test_path in os.listdir(os.path.join(program_path, "test")):
        if not re.match(test_path, "_res$") and not re.match(test_path, "_test_res$"):
            full_path = os.path.join(program_path, "test", test_path)
            test_processes.append(mp.Process(target=run_test, args=(argv[1], full_path)))
            if len(test_processes) == SYSTEM_CORES_AMOUNT:
                flush_processes(test_processes)
                test_processes = []
    flush_processes(test_processes)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please select the program")
        exit(-1)
    main(sys.argv)
