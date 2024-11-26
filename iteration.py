#FOR
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

print('*************')
#WHILE
n = 0
while n < 3:
    print(n)
    n += 1 

print('************')
n = 5
while n > 0:
    n -= 1 
    print(n)

print('************')
number = int(input('Enter your number: '))
while number != 1:
    name = input('Your name is: ')
    break
    print(f'Number is {number}')

print('Finish')