vowels = frozenset({"a","e","i","o","u"})
print(vowels,"is the type of",type(vowels))
# vowels.add("y") can't be used in frozenset
consonents = frozenset({"a","b","c","d"})
letter = vowels.union(consonents)
print(letter)
