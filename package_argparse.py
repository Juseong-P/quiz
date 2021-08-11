import math
import argparse

# parser = argparse.ArgumentParser(description='Calculation volume of a Cylinder')
# parser.add_argument('-r', '--radius', type=int, metavar='', required=True, help='Radius of Cylinder')
# parser.add_argument('-H', '--height', type=int, metavar='', required=True, help='Height of Cylinder')
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
#         print(f"Volume of a Cylinder with radius {args.radius} and height {args.height} is {volume}")
#     else:
#         print (f"Volume of Cylinder = {volume}")

# Fibonacci number
def fin(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

def Main ():
    parser = argparse.ArgumentParser()
    parser.add_argument("num", help = "The Fibonacci number you wish to calculate.", type=int)
    parser.add_argument('-o', '--output', help = 'Output the result to a file', action='store_true')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--verbose', action = 'store_true')
    group.add_argument('-q', '--quiet', action = 'store_true')
    args = parser.parse_args()
    result = fin(args.num)
    if args.verbose:
        print(f"The {args.num}th fib number is {result}")
    elif args.quiet:
        print(result)
    else:
        print(f"Fib({args.num}) = {result}")

    if args.output:
        f = open("fibonacci.txt", 'a')
        f.write(str(result) + '\n')

if __name__ == '__main__':
    Main()