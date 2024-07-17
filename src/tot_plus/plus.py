import sys

def plus():
   # print("sys.argv:", sys.argv)
    a=int(sys.argv[1])
    b=int(sys.argv[2])
    c=a+b
    print(f"{a} + {b} = {c}")
