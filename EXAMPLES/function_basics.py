from subprocess import run

def say_hello():  # Function takes no parameters
    print("Hello, world")
    print()


say_hello()  # Call function (arguments, if any, in () )


def get_hello():
    return "Goodbye, Norma Jean"  # Function returns value

def pi():
    return 3.1417

print(5 * pi(), '\n')

h = get_hello()  # Store return value in h
print(h)
print()


#  def function-name(parameter, ...):
def sqrt(num):  # Function takes exactly one argument
    return num ** .5


m = sqrt(1234)  # Call function with one argument
n = sqrt(2)
x = 10
m = sqrt(x)

print(f"m is {m:.3f} n is {n:.3f}")

# run external program
# run(["python", "if_else.py"])


def hello(*people):
    print(f"{people = }")
    
    for person in people:
        print(f"Hello, {person}")

hello('Mary')
hello('New York')
hello('Mom', 'Dad')
hello()

def h2(person1, person2):
    print(f"hello {person1}")
    print(f"hello {person2}")

def spam(r1, r2, *opt):
    pass

spam('a', 'b', 'c', 'd')

#         param=default-value
def greet(whom="world"):
    print(f"Hello, {whom}")

greet("Dolly")
greet("Dad")
greet()

def count_words(target, file_path):
    count = 0
    with open(file_path) as words_in:
        for raw_line in words_in:
            if target in raw_line:
                count += 1

    return count

word_count = count_words("bear", '../DATA/words.txt')
print(f"{word_count = }")



def get_words(target, file_path):
    words = []
    with open(file_path) as words_in:
        for raw_line in words_in:
            if target in raw_line:
                words.append(raw_line.rstrip())

    return words

print(get_words('mang', '../DATA/words.txt'))



