def loopy_loop1():
    a=1
    b=1
    while a is b:
        a+=1
        b+=1
    print(a)

def comparison01():
    try:
        a=5
        if 1 < a < 10:
            print('Yes')
        else:
            print('No')
    except:
        print('Fail')

def comparison02():
    try:
        a = b = c = 5
        if a == b == c:
            print('Yes')
        else:
            print('No')
    except:
        print('Fail')

def comparison03():
    try:
        a = b = c = 5
        if (a == b) == c:
            print('Yes')
        else:
            print('No')
    except:
        print('Fail')

def comparison04():
    try:
        a = 1
        b = 2
        c = a
        if a != b != c:
            print('Yes')
        else:
            print('No')
    except:
        print('Fail')


def list_madness():
    a = [1, 2, 3, 4, 5]
    b = list(map(lambda x: x*x, filter(lambda x: x%2==0, map(lambda x: x+1, a))))
    print(sum(b))

def nested_list_comprehension_madness():
    print([[j**2 for j in range(1, i) if j % 2 != 0] for i in range(2, 10) if i % 3 == 0])

def string_manipulation_extravaganza():
    print(''.join([chr(ord(c) + 1) if c.isalpha() and c.lower() <= 'y' else c for c in "Hello, World!"]))

def dictionary_comprehension_puzzle():
    print({i: i**2 for i in range(10) if i % 2 == 0})

def function_complexity_showcase(n):
    return sum([i for i in range(n) if i % 2 == 0]) if n > 0 else 0

def list_slicing_abstraction():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(a[::-2][:3])

def lambda_labyrinth():
    add = lambda x: (lambda y: x + y)
    print(add(5)(3))

def lamda_see_you(a):
    x = lambda n: n * x(n - 1) if n > 1 else 1
    return x(a)




def main():
    print('start')
    # loopy_loop1()
    # comparison04()
    # list_madness()
    nested_list_comprehension_madness()
    string_manipulation_extravaganza()
    dictionary_comprehension_puzzle()
    print(function_complexity_showcase(10))
    list_slicing_abstraction()
    lambda_labyrinth()
    lamda_see_you(4)
    


main()