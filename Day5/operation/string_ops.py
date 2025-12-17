def reverse(s):
    return s[::-1]
def vowel(s):
    vowel='aeiouAEIOU'
    count=0
    for ch in s:
        if ch in vowel:
            count+=1
    return count
