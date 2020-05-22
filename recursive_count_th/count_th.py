'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
'''
returning the length of a word set character les than two or zero if th does not exist
define what I am looking for in th in lower case
I only want to have two characters
returning the instance of the th string
if its just a individual character return nothing
I can multiple the th together in one word by just adding it to the count
'''
def count_th(word):
    if len(word) <2:
        return 0
    if word[:2] == 'th':
        return 1 + count_th(word[2:])
    else:
        return 0 + count_th(word[1:])
