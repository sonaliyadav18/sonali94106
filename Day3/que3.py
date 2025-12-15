def vowel(s):
    vowel="aeiouAEIOU"
    return sum (1 for ch in s if ch in vowel)
def consonants(s):
    return sum (1 for ch in s if ch.isalpha() and ch not in "aeiouAEIOU" )

def vowel_consonants_ratio(s):
    v=vowel(s)
    c=consonants(s)
    return v/c
s=input("Enter String :")
print("vowel :",vowel(s))
print("consonants :",consonants(s))
print("vowel_cononants_ratio :",vowel_consonants_ratio(s))