#Fibonacci Sequence Generator: A Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.
# a, b = 0, 1
# while a < 10:
#     print(a)
#     a, b = b, a+b

# def generate_fibonacci(n):
#     n = int(input("Enter fibonacci number: "))
#     n, o = 0, 1
#     while n < 10:
#         print(n)
#         n, o = o, n+o

# generate_fibonacci(20) #Argument passed (20) is ignored by input()

def print_fibonacci():
    fib_list = []

    while True:
        fib_input = input("Enter your Fib number: ")
        fib_list.append(fib_input)

        if fib_input.lower() == '0':
            break
    print("your list: ", fib_list)

print_fibonacci()



