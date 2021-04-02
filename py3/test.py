#!/usr/bin/python3 

import os
import re
import sys
import time
import json
import subprocess

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


Test = nt("Test", "process output expected name duration")


def check_result(test):
    out = test.output.decode("ascii").strip()
    if test.expected == out: 
        print_green(f"Test: {test.name} is [OK]\tduration: {test.duration}")
        print_green(out)
    else:
        print_red(f"Test: {test.name} is [FAIL]\tduration: {test.duration}")
        print_green(test.expected)
        print_red(out)
        print("-" * 10)


def run_test(program_path, test_path):
    with open(test_path, "r") as test:
        test_case = json.load(test)
        started = time.time()
        p = subprocess.Popen(["python3", program_path + "/" + program_path.split("/")[-1] + ".py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        finished = time.time()
        p = subprocess.Popen(["python3", program_path + "/" + program_path.split("/")[-1] + ".py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        outp, errs = p.communicate(str(test_case["input"]).encode("ascii"))
        if errs:
            print_red("[FAIL]")
            print(errs)
            return
        check_result(Test(p, outp, test_case["output"], test_path.split("/")[-1], finished - started))


def main(argv):
    """
    Assuming each program is in it's own folder containing "test" folder inside
    Each test is a json file with "input" and "output" string keys
    """
    cwd = os.getcwd()
    program_path = os.path.join(cwd, argv[1])
    for test_path in os.listdir(os.path.join(program_path, "test")):
        if not re.match(test_path, "_res$") and not re.match(test_path, "_test_res$"):
            full_path = os.path.join(program_path, "test", test_path)
            run_test(program_path, full_path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please select the program")
        exit(-1)
    main(sys.argv)
