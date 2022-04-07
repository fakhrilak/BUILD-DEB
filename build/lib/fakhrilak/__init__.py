# from __future__ import print_function
import argparse

print("This is my first build tkinter and build to .deb")
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("a",type=int,help="[-f] var a")
    parser.add_argument("b",type=int,help="[-l] var b")
    parser.add_argument("m",type=str,help="[-m] logiccontrol a b")
    return parser.parse_args()

def main():
    try:
        args = parse_args()
        a = int(args.a)
        b = int(args.b)
        if args.m == "+":
            print(a * b)
        elif args.m == "-":
            print(a - b)
        elif args.m == "x":
            print(a * b)
        elif args.m == "/":
            print(a/b)
        else:
            print("argument 3 is logic [+ , - , x , /]")
    except BaseException as err:
        print(err)
        print("fakhrilak -h to help command line")
    # print(args.text)