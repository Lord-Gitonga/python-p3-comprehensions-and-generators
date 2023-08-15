#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers =  [num for num in num_list if num % 2 == 0] 
    print(even_numbers)
    pass
return_evens([0, 1, 3, 5, 7, 8, 9])

def make_exclamation(sentence_list):
    exclamation = [string + "!" for string in sentence_list]
    print(exclamation)
    pass
make_exclamation(["Hello", "I'm doing great", "Python is fun"])