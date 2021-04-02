
class Test:
    def __init__(self, inp, outp):
        self.input = inp
        self.output = outp


with open("./test/test4_large", "w") as f:
    a, b = list(range(1, 10 ** 5)), list(range(1, 1 << 20, 4))
    inp = "{}\n{}".format(" ".join([str(s) for s in a]), " ".join([str(s) for s in b]))
    merged = sorted(a + b)
    outp = "324289.0"
    f.write(str(Test(inp, outp).__dict__).replace("'", '"'))

