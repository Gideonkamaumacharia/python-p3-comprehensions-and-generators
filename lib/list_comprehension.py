#!/usr/bin/env python3

def return_evens(num_list):
    even_nums = [num for num in num_list if num % 2 == 0]
    return (even_nums if even_nums else [])
    


def make_exclamation(sentence_list):
    exclamation = [(sentence + "!") for sentence in sentence_list]
    return exclamation