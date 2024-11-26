#A palindrome is a word, sentence, verse, or even number that reads the same backward or forward.
def is_palindrome():
    item = input("Enter item: ")

    while True:
        if (item == item[::-1]):
            print(f'{item} is a palindrome.')
            break
        
        else:
            print(f'{item} is not a palindrome.')
            item = input("Enter item: ")

is_palindrome()


def check_palindromes():
    my_list = [
    'mummy', 
    'hannah', 
    'murder for a jar of red rum', 
    'mom', 
    'seagull', 
    'tomato', 
    'no lemon, no melon', 
    'some men interpret nine memos', 
    'madam'
    ]

    for i in my_list:
        # print(i) 
        if i == i[::-1]:
            print(f' {i} is a palindrome.')
        else:
            print(f'{i} is not a palindrome')

    
check_palindromes()


