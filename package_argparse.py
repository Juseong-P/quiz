import math
import argparse

# parser = argparse.argumentparser(description='calculation volume of a cylinder')
# parser.add_argument('-r', '--radius', type=int, metavar='', required=true, help='radius of cylinder')
# parser.add_argument('-h', '--height', type=int, metavar='', required=true, help='height of cylinder')
# group = parser.add_mutually_exclusive_group()
# group.add_argument('-q', '--quiet', action = 'store_true', help='print quiet')
# group.add_argument('-v', '--verbose', action = 'store_true', help='print verbose')
# args = parser.parse_args()
#
# def cylinder_volume(radius, height):
#     vol = math.pi * radius**2 * height
#     return vol
#
# if __name__ == '__main__':
#     print (cylinder_volume(args.radius, args.height))
#     volume = cylinder_volume(args.radius, args.height)
#     if args.quiet:
#         print (volume)
#     elif args.verbose:
#         print(f"volume of a cylinder with radius {args.radius} and height {args.height} is {volume}")
#     else:
#         print (f"volume of cylinder = {volume}")

# fibonacci number
# def fin(n):
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, a+b
#     return a
#
# def main ():
#     parser = argparse.argumentparser()
#     parser.add_argument("num", help = "the fibonacci number you wish to calculate.", type=int)
#     parser.add_argument('-o', '--output', help = 'output the result to a file', action='store_true')
#     group = parser.add_mutually_exclusive_group()
#     group.add_argument('-v', '--verbose', action = 'store_true')
#     group.add_argument('-q', '--quiet', action = 'store_true')
#     args = parser.parse_args()
#     result = fin(args.num)
#     if args.verbose:
#         print(f"the {args.num}th fib number is {result}")
#     elif args.quiet:
#         print(result)
#     else:
#         print(f"fib({args.num}) = {result}")
#
#     if args.output:
#         f = open("fibonacci.txt", 'a')
#         f.write(str(result) + '\n')
#
# if __name__ == '__main__':
#     main()

# import argparse
#
# def main():
#     parser = argparse.argumentparser()
#     parser.add_argument('x', type=int, metavar='first number',
#                         help="what is the first number?")
#     parser.add_argument('y', type=int, metavar='second number',
#                         help="what is the second number?")
#     parser.add_argument('-op', '--option', type=str, default='add',
#                         choices=['add', 'sub', 'mul', 'div'], help='what operation?')
#     args = parser.parse_args()
#
#     x = args.x
#     y = args.y
#     op = args.option
#     print(calc(x, y, op))
#
# def calc (x, y, op):
#     if op == 'add':
#         return x + y
#     if op == 'sub':
#         return x - y
#     if op == 'mul':
#         return x * y
#     if op == 'div':
#         return x / y
#
#
# if __name__=="__main__":
#     main()

#add_mul.py 뒤 따라오는 정수들의 합을 출력한다.
import argparse
from functools import *

def main():
    parser = argparse.ArgumentParser(description='뒤 따라오는 정수들의 합 또는 곱을 출력합니다.')
    parser.add_argument('-a', '--add', type=int, metavar='n', nargs='+', help = 'to add number')
    parser.add_argument('-m', '--mul', type=int, metavar='n', nargs='+', help = 'to multiply number')
    args = parser.parse_args()

    if args.add:
        print(f'합은 {reduce(lambda x, y : x+y , args.add)}입니다.')
        print(addlist(args.add))
    if args.mul:
        print(f'곱은 {reduce(lambda x, y : x * y, args.mul)}입니다.')
        print(mullist(args.mul))

def addlist(addidi):
    sum = 0
    for i in addidi:
        sum += i
    return sum

def mullist(multiti):
    multi = 1
    for i in multiti:
        multi *= i
    return multi

if __name__ == '__main__':
    main()


