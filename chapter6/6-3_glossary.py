# Print each word and its meaning as neatly formated output

glossary = {
    'slice' : 'part of a list',
    'true' : 'boolean expression',
    'tuple' : 'immutable list',
    'pop' : 'method',
    'newline' : 'line break',
    }

word = 'slice'
meaning = glossary[word]
print(f'{word.title()}: {meaning}')

word = 'tuple'
meaning = glossary[word]
print(f'\n{word.title()}: {meaning}')

word = 'newline'
meaning = glossary[word]
print(f'\n{word.title()}: {meaning}')

word = 'true'
meaning = glossary[word]
print(f'\n{word.title()}: {meaning}')

word = 'pop'
meaning = glossary[word]
print(f'\n{word.title()}: {meaning}')
