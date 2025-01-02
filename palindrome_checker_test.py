#A palindrome is a word, sentence, verse, or even number that reads the same backward or forward.
def is_palindrome(item):
    # Make the item lowercase
    normalized_item = item.lower()
    # Check if the item reads the same forwards and backwards
    return normalized_item == normalized_item[::-1]

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

for item in my_list:
    result = is_palindrome(item)
    print(f'Is "{item}" a palindrome? {result}')
