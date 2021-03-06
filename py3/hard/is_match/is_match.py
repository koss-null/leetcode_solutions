def _saved_score(func):
    def wrapper(*args, **kwargs):
        obj = args[0]
        if len(args) > 2:
            place = args[2]
        else:
            place = kwargs["place"]
        if place in obj.answers:
            return obj.answers[place]
        res = func(*args, **kwargs)
        obj.answers[place] = res
        return res
    return wrapper


class Solution(object):
    class Rune:
        def __new__(cls, c, prev):
            if c == "*":
                prev.any_quantity = True
                return prev
            return super(Solution.Rune, cls).__new__(cls)

        def __init__(self, c, prev):
            if c != "*":
                self.c = c
                self.prev = prev
                self.any = c == "."
                self.next = None
                self.any_quantity = False
                self.answers = {}
                if prev:
                    prev.next = self

        @_saved_score
        def match(self, s, place):
            if place >= len(s):
                if self.any_quantity:
                    if self.next:
                        return self.next.match(s, place)
                    return True
                return False

            if self.any:
                if self.any_quantity:
                    if not self.next:
                        return True  # .* at the end matches everything
                    try_this = self.next.match(s, place+1)
                    if try_this:
                        return True
                    try_this = self.next.match(s, place)
                    if try_this:
                        return True
                    return self.match(s, place+1)
                if not self.next:
                    return place+1 == len(s)
                return self.next.match(s, place+1)

            if self.c != s[place]:
                if self.any_quantity:
                    if not self.next:
                        return False
                    return self.next.match(s, place)
                return False

            if self.any_quantity:
                if not self.next:
                    return self.match(s, place+1)
                try_this = self.next.match(s, place+1)
                if try_this:
                    return True
                try_this = self.next.match(s, place)
                if try_this:
                    return True
                return self.match(s, place+1)

            if not self.next:
                return place+1 == len(s)

            return self.next.match(s, place+1)

    def isMatch(self, s, p):
        head = None
        tail = None
        for c in p:
            r = self.Rune(c, tail)
            if not head:
                head = r
            tail = r
        if not head:
            return not s
        return head.match(s, 0)


def main(a, b):
    return Solution().isMatch(a, b)


def get_input(inp):
    return inp.split("\n")


def format_output(a):
    return str(a)
