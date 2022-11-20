def question_1(a, b):
    return (a**2 + b**2)**(1/2)

# a = int(input('please enter the first number '))
# b = int(input('please enter the second number '))
# print(gipotenuza(a,b))

def question_2(a):
    return (a%100)//10

# a = int(input('enter the integer number '))
# print(question_2(a))

def question_3(n):
    return (n//2)*2 + 2

# n = int(input('enter the integer number and get next even number '))
# print(question_3(n))

def question_4(n):
    minutes = (n)*45 + ((n-1)//2)*15 + ((n-1)//2 + (n-1)%2)*5
    h = minutes // 60 + 9
    m = minutes % 60
    h_m = f'{h} {m}'
    return h_m

# n = int(input('enter the lesson number and get next even number '))
# print(question_4(n))

def question_5(a, b):
    if a>b:
        return 1
    elif b>a:
        return 2
    else:
        return 0

# a = int(input('enter first number '))
# b = int(input('enter second number '))
# print(question_5(a, b))

def question_6(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# a = int(input('enter first number '))
# b = int(input('enter second number '))
# c = int(input('enter third number '))
# print(question_6(a, b, c))

def question_7(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        return 'YES'
    else:
        return 'NO'

# a = int(input('enter first number '))
# b = int(input('enter second number '))
# c = int(input('enter third number '))
# d = int(input('enter forth number '))
# print(question_7(a,b,c,d))

def question_8(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return 'YES'
    else:
        return 'NO'

# a = int(input('enter first number '))
# b = int(input('enter second number '))
# c = int(input('enter third number '))
# print(question_8(a, b, c))

def question_9(a, b, c):
    if a == b and b == c:
        return 3
    if a==b or b==c or a==c:
        return 2
    else:
        return 0

# a = int(input('enter first number '))
# b = int(input('enter second number '))
# c = int(input('enter third number '))
# print(question_9(a, b, c))

def question_10(a,b,c):
    if a <= b and a <= c:
        first = a
        if b <= c:
            second = b
            third = c
        else:
            second = c
            third = b
    elif b<=a and b<=c:
        first = b
        if a<=c:
            second = a
            third = c
        else:
            second = c
            third = a
    else:
        first = c
        if a<=b:
            second = a
            third = b
        else:
            second, third = b, a
    return first, second, third

# a = int(input('enter first number '))
# b = int(input('enter second number '))
# c = int(input('enter third number '))
# print(question_10(a, b, c))

def question_add_1(a, b, c):
    if question_8(a, b, c) == 'YES':
        f, s, t = question_10(a, b, c)
        cos_alpha = (s**2 + f**2 - t**2)/(2*s*f)
        if cos_alpha > 0:
            return 'acute'
        elif cos_alpha < 0:
            return 'obtuse'
        else:
            return 'right'
    else:
        return 'impossible'

# a = int(input('enter first number '))
# b = int(input('enter second number '))
# c = int(input('enter third number '))
# print(question_add_1(a, b, c))

def question_add_2(a,b,c):
    d = (b**2-4*a*c)
    if d > 0:
        x1 = (-b + d**(1/2))/(2*a)
        x2 = (-b - d**(1/2))/(2*a)
        return x1, x2
    elif d == 0:
        x = (-b)/(2*a)
        return x

# a = int(input('enter first number '))
# b = int(input('enter second number '))
# c = int(input('enter third number '))
# print(question_add_2(a, b, c))

def question_add_3(a,b):
    for_different_a_b = ((a//b)*b + (b//a)*a) + (((a%b)%a + (b%a)%b))
    equality_check = ((a//b)*b + (b//a)*a)//(a+b)
    max_of_two = equality_check*a + (1//(equality_check+1))*for_different_a_b
    return max_of_two

a = int(input('enter first number '))
b = int(input('enter second number '))
print(question_add_3(a, b))
