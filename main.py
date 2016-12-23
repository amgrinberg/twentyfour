import itertools
import sys


def plus(x, y):
    return x + y


def minus(x, y):
    return x - y


def dividedby(x, y):
    if y == 0:
        return 0

    return x / float(y)


def times(x, y):
    return x * y
'''
hi
'''

def main(numbers):
    '''
    Leave comments, ya dope.
    '''
    numbers = [int(i) for i in numbers]
    functions = [plus, minus, dividedby, times]
    function_combinations = [f for f in itertools.product(functions, repeat=3)]

    combinations = set(i for i in itertools.permutations(numbers))

    answers = []
    for a, b, c, d in combinations:
        for f1, f2, f3 in function_combinations:
            res1 = round(f3(f2(f1(a, b), c), d), 7)
            if res1 == 24.0:
                answers.append('{a} {f1} {b} {f2} {c} {f3} {d}')

            res2 = round(f2(f1(a, b), f3(c, d)), 7)
            if res2 == 24.0:
                answers.append('({a} {f1} {b}) {f2} ({c} {f3} {d})')

            res3 = round(f1(a, f3(f2(b, c), d)), 7)
            if res3 == 24.0:
                answers.append('{a} {f1} (({b} {f2} {c}) {f3} {d})')

            res4 = round(f3(f1(a, f2(b, c)), d), 7)
            if res4 == 24.0:
                answers.append('({a} {f1} ({b} {f2} {c})) {f3} {d}')

            res5 = round(f1(a, f2(b, f3(c, d))), 7)
            if res5 == 24.0:
                answers.append('{a} {f1} ({b} {f2} ({c} {f3} {d}))')

    for answer in answers:
        print answer.format(a=a, b=b, c=c, d=d, f1=f1.func_name, f2=f2.func_name, f3=f3.func_name)


if __name__ == "__main__":
    main(sys.argv[1:])
