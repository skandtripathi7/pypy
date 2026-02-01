"""Problem 4 — Palindrome

Write a function that:

Returns True if a string is a palindrome

Ignores spaces and case"""

s = "oyo"

def Pali(s):
    l_s = s.lower()

    l_s_1 = ""

    for ch in l_s:
        if ch != " ":
            l_s_1 = l_s_1 + ch

    for i in range(len(l_s_1) // 2):
        if l_s_1[i] != l_s_1[len(l_s_1)-i-1]:
            return False
        
    return True

print(Pali(s))

