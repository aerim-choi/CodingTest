from itertools import product

def solution(word):
    word_set=set()
    alphabet = ["","A","E","I","O","U"]
    
    for p in product(["","A","E","I","O","U"], repeat=5):
        word_set.add("".join(p))

        
    word_set = sorted(word_set)
    
    for idx, w in enumerate(word_set):
        if word == w:
            return idx
