# Set datatype
vowels = {"a","e","i","o","u"}
print(vowels,'is the type of',type(vowels))
vowels.add("y") # adding element to set
print(vowels)
vowels.remove("o")# removing element from set
print(vowels)
consonents = {"a","b","c","d","f"}
print(consonents)
letter =vowels.union(consonents)# union of two sets
print(letter)