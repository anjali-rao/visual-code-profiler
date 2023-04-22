import sys

import tracer
import time


sys.settrace(tracer.my_tracer)
def is_positive(a, b):
    x = 100
    x = x+100
    TEST_CONSTANT = 1
    if a> 0 and b> 0:
        return True
    return False

def add(a, b):
    if is_positive(a,b):
        return a+b
    return False

def division():
    a = 1/0



def main():

    TEST_CONSTANT = 10
    print(add(-1,2))
    division()

main()
