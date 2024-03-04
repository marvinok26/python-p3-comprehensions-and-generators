#!/usr/bin/env python3

def return_evens(num_list):
    new_numlist = [n for n in num_list if n%2 == 0]
    return new_numlist

def make_exclamation(sentence_list):
    new_sentence_list = [n + '!' for n in sentence_list]
    return new_sentence_list