import os
import sys
import math


number = int(input())


def prime(num):
    # your code goes here
    # function to determine prime number
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


# prints whether an input is a prime number or not
for j in range(number):
    n = int(input())

    if n >= 2 and prime(n):
        print('The number you entered is a Prime number.')
    else:
        print('The number you entered is not a Prime number')


def solution(num):
    return prime(num)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))
