############
# 1.1
############

def all_unique_characters_hash_table(s):
    dict_ = {}
    for letter in s:
        if(dict_.get(letter) is not None):
            return False
        dict_[letter] = 1
    return True

def all_unique_characters_no_hash_table(s):
    if(len(s) < 2):
        return True
    s = list(s) # In Python you can only call sort() on lists, not strings 
    s.sort()
    for i in range(len(s) - 1):
        if(s[i] == s[i + 1]):
            return False
    return True

def test_function(l):
    for s in l:
        print(all_unique_characters_no_hash_table(s))

l = ["abcd", "abcdd", "a", "abb", "aa", "djajkdi", "da"]
test_function(l)
