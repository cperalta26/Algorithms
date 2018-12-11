'''In this exercise, you will have to create a function named tiyFizzBuzz. 
This function will take on a string parameter and will return that string with some characters 
replaced, depending on the value:

If a letter is a upper case consonants, replace that character with "Iron".
If a letter is a lower case consonants or a non-alpha character, do nothing to that character
If a letter is a upper case vowel, replace that character with "Iron Yard".
If a letter is a lower case vowel, replace that character with "Yard".'''

def tiy_fizz_buzz(string):
    #your code here
    new_string = ''
    for i in range(len(string)):
        if string[i].isupper():
            if string[i] in 'AEIOU':
                new_string += 'Iron Yard'
            else:
                new_string += 'Iron'
        else:
            if string[i] in 'aeiou':
                new_string += 'Yard'
            else:
                new_string += string[i]
    #print(string, new_string)
    return new_string