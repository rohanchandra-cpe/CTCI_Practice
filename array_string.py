############
# 1.1
############

# O(n) but it uses a hash table
def all_unique_characters_hash_table(s):
    dict_ = {}
    for letter in s:
        if(dict_.get(letter) is not None):
            return False
        dict_[letter] = 1
    return True

# O(n log(n))
def all_unique_characters_no_hash_table(s):
    if(len(s) < 2):
        return True
    s = list(s) # In Python you can only call sort() on lists, not strings 
    s.sort()
    for i in range(len(s) - 1):
        if(s[i] == s[i + 1]):
            return False
    return True

def test_function_1_1(l):
    for s in l:
        print(all_unique_characters_no_hash_table(s))

############
# 1.2
############

# O(n) w/ a hash table
def is_permutation(a, b):
    if(len(a) != len(b)):
        return False
    dict_ = {}
    for letter in a:
        if(dict_.get(letter) is None):
            dict_[letter] = 1
        else:
            dict_[letter] += 1
    for letter in b:
        if(dict_.get(letter) is None or dict_.get(letter) < 1):
            return False
        dict_[letter] -= 1
    return True

# O(n * log(n))
def is_permutation_log(a, b):
    if(len(a) != len(b)):
        return False
    a = list(a)
    b = list(b)
    a.sort()
    b.sort()
    for i in range(len(a)):
        if(a[i] != b[i]):
            return False
    return True

a = input("a: ")
b = input("b: ")
print(is_permutation(a, b))
print(is_permutation_log(a, b))