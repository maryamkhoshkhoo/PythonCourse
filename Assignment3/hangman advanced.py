import random

words = ['maryam', 'python', 'text', 'laptop', 'hand', 'book']

    
word = random.choice(words)
joon = 10
character = []
for i in range(len(word)):
    character.append('_')

while joon > 0:
    print(' '.join(character))
        
    if ((''.join(character)) == word):
        print("huraaaa you win")
        break
    
    user_character = input("please enter the character:")
    user_character = user_character.lower()
    
    if (user_character in word):
        print(joon)
        for i in range(len(word)):
            if (word[i] == user_character):
                character[i] = user_character        
                
    else:
        joon = joon - 1
        print(joon)   