class A:
    def do_somethng(self, x):
        #print(f"do_something({self=}, {x=})")
        print(x**x)

def main():
    a = A()
    print(a.do_somethng(1))