
### TD2

##Exercice 1
#a
def is_palindrome(mot):
    return mot[0:-1:1] == mot[-1:0:-1]
#b
def is_pangram(phrase):
    return set(phrase.lower()) >= set("abcdefghijklmonpqrstuvwxyz")
#c
def remove_adjacent(list):
    return [ list[i] for i in range(len(list)) if i<=1 or list[i-1]!=list[i]]

#d
def digit_sum(n):
    return sum([int(x) for x in str(n)])


print(is_palindrome(""))
print(is_palindrome("non"))
print(is_palindrome( "oui"))

print("----")
print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("Portez ce vieux whisky au juge blond qui fume"))
print(is_pangram("mangez moi"))

print("----")
print(remove_adjacent([1,2,2,3,3,1]))

print("----")
print(digit_sum(123))
print(digit_sum(1234))

