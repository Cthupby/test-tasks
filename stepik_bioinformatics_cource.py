"""
Здесь собраны некоторые мои решения
задач курса "Программирование на Python"
https://stepik.org/course/67/syllabus
"""

def get_points():
    points = []
    mid_a = 0
    mid_b = 0
    mid_c = 0
    f = open("dataset_3363_4(1).txt", "r", encoding="utf-8")
    for i in f:
        l = i.replace("\n", "").split(";")
        points.append(sum([int(i) for i in l[1:]]) / len(l[1:]))
        mid_a += int(l[1])
        mid_b += int(l[2])
        mid_c += int(l[3])
    w = open("dataset_3363_4_result.txt", "w", encoding="utf-8")
    result = []
    for i in points:
        w.write(f"{i}\n")
    w.write(f"{mid_a / len(points)} {mid_b / len(points)} {mid_c / len(points)}")

# print(get_points())

def try_requests():
    import requests

    r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
    prev = requests.get(f'https://stepic.org/media/attachments/course67/3.6.3/{r.text}')
    while prev:
        print(prev.text)
        prev = requests.get(f'https://stepic.org/media/attachments/course67/3.6.3/{prev.text}')

# try_requests()

def cypher(a, b, c, d):
    relation = dict(zip(a, b))
    c, d = list(c), list(d)
    for k, i in enumerate(c):
        if i in a:
            c[k] = relation[i]
    relation = dict(zip(b, a))
    for k, j in enumerate(d):
        if j in b:
            d[k] = relation[j]

    return f"{ ''.join(c) } \n { ''.join(d) } "

# a = "abcd"
# b = "*d%#"
# c = "abacabadaba"
# d = "#*%*d*%"
# print(cypher(a, b, c, d))

def try_sys():
    import sys

    list_arg = sys.argv[1:]
    print(*list_arg)

# try_sys()

def try_math():
    import math

    r = float(input())
    print(2 * r * math.pi)

# try_math()

def count_words(string):
    count_dict = {}
    count = ""
    for s in string.lower().split():
        if s in count_dict:
            count_dict[s] += 1
        else:
            count_dict[s] = 1
    for k, i in count_dict.items():
        count += f"{k} {i}\n"
    return count

# s = "a А abC aa ac abc bcd a"
# print(count_words(s))

def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif key * 2 in d:
        d[key * 2].append(value)
    else:
        d[key * 2] = [value]
    return d

# d = {2: [-1, 1]}
# print(update_dictionary(d, 1, -3))

def f(x):
    if x <= - 2:
        x = 1 - ((x + 2) ** 2)
    elif -2 < x <= 2:
        x = - x / 2
    elif 2 < x:
        x = ((x - 2) ** 2) + 1
    return x

# print(f(1))

def get_pos_b(a, b):
    list_a = []
    i = 0
    for i, item in enumerate(a.split(" ")):
        if item == b:
            list_a.append(i)
    return list_a if list_a else "Отсутствует"

# print(get_pos_b(input(), input()))

def get_list_a(a):
    if a == 1 or a == 0:
        return [a]
    sum_a = 1
    list_a = []

    for i in range(1, a + 1):
        while sum_a < a:
            sum_a += i
            list_a += [i] * i
            break

    len_a = len(list_a)
    if len_a > a:
        list_a = list_a[:(a - len_a)]
    elif len_a < a:
        list_a += [int(list_a[-1]) + 1] * (a - len_a)
    
    return list_a

# print(*get_list_a(int(input())))

def get_quad():
    a = int(input())
    sum_a = a
    quad_a = a*a

    while sum_a != 0:
        a = int(input())
        sum_a += a
        quad_a += a*a
    return quad_a

# print(get_quad())

def get_duplicates(s):
    s_list = [int(i) for i in s.split(" ")]
    duplicates = []
    s_list.sort()
    for i in range(len(s_list)-1):
        if s_list[i] == s_list[i + 1] and s_list[i] not in duplicates:
                duplicates.append(s_list[i])
    return duplicates

# s = "4 8 0 3 4 2 0 3"
# print(get_duplicates("1 1 2 2 3 3"))

def get_sum_neighbor(s):
    if len(s) == 1:
        return int(s)
    s_list = s.split(" ")
    s_sum = []
    for i in range(len(s_list)):
        print(f"{s_list[i]} - {i} - {len(s_list)}")
        if i == 0:
            s_sum.append(int(s_list[-1]) + int(s_list[i + 1]))
        elif i != 0 and i != len(s_list) - 1:
            s_sum.append(int(s_list[i - 1]) + int(s_list[i + 1]))
        else:
            s_sum.append(int(s_list[0]) + int(s_list[i - 1]))

    return s_sum

# s = '1 3 5 6 10'
# print(get_sum_neighbor(s))

def get_compression(a):
    code = []
    i = 1
    if len(a) == 1:
        code.append(f"{a[0]}1")
    for n in range(len(a) - 1):
        if a[n] == a[n + 1]:
            i += 1
        elif a[n] != a[n + 1]:
            code.append(f"{a[n]}{i}")
            i = 1
        if n == (len(a)-2):
            print(str(n+1)+" "+str(len(a)))
            code.append(f"{a[n+1]}{i}")

    return "".join(code)

# bb = 'a'
# print(get_compression(bb))
# aa = 'aaaaFbbcaaG\nfd'
#print(get_compression(aa))

# s = 'abcdefghijk'
# print(s[3:6]) # => def
# print(s[:6]) # => abcdef
# print(s[3:]) # => defghijk
# print(s[::-1]) # => kjihgfedcba
# print(s[-3:]) # => ijk
# print(s[:-6]) # => abcde
# print(s[-1:-10:-2]) # => kigec

def find_gc(a):
    g = a.upper().count('G')
    c = a.upper().count('C')
    return ((g + c) / len(a)) * 100

# a = 'acggtgttat'
# print(find_gc(a))

def get_middle(a, b):
    integers = []
    for i in range(a, b + 1):
        if i % 3 == 0:
            integers.append(i)
    return sum(integers) / len(integers)

# print(get_middle(int(input()), int(input())))

def get_multiples(a, b, c, d):
    multiples = " \t"
    for i in range(c, d + 1):
        multiples += f"{i}\t"
    multiples += f"\n"
    for j in range(a, b + 1):
        multiples += f"{j}\t"
        for i in range(c, d + 1):
            multiples += f"{j*i}\t"
        multiples += f"\n"

    return multiples

# a, b, c, d = 7, 10, 5, 6
# print(get_multiples(a, b, c, d))
