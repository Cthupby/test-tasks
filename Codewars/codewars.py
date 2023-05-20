text = 'Hello world! My name  is Sergey!'
flo = 6.7
numbers = ("11 2 33 4 5 2")


def reverse_words(text):
    r_words = []
    words = text.split(' ')
    for word in words:
        r_words.append(word[::-1])
    print(' '.join(r_words))


def disemvowels(string_):
    vowels = 'aeiouAEIOU'
    print(''.join([l for l in string_ if l not in vowels]))


def no_space(x):
    a = ''.join(x.split())
    print(a)


def litres(time):
    print(int(time*0.5))


def high_and_low(numbers):
    split_numbers = numbers.split()
    key = lambda i: int(i)
    max_numbers = max(split_numbers, key=key)
    min_numbers = min(split_numbers, key=key)
    print(max_numbers, min_numbers)

if __name__ == '__main__':
    reverse_words(text)
    disemvowels(text)
    no_space(text)
    litres(flo)
    high_and_low(numbers)
