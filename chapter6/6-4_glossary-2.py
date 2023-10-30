# Adding new key-value pairs to the existing dictionary and looping through them.

glossary = {
    'slice' : 'part of a list',
    'true' : 'boolean expression',
    'tuple' : 'immutable list',
    'pop' : 'method',
    'newline' : 'line break',
    }

glossary['whitespace'] = 'any nonprintable characters'
glossary['list'] = 'collection of items in a particular order'
glossary['index'] = 'position of an item in a list'
glossary['dictionary'] = 'collection of key-value pairs'
glossary['conditional test'] = 'expression that can be evaluated as True or False'

for word, meaning in glossary.items():
    print(f'{word.title()}: {meaning}\n')
