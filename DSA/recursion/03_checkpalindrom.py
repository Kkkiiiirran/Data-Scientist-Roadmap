# ABCDCBA

def checkPalindrome(n, string, i, j):
    if i == n/2 or j == n/2:
        return True
    if string[i].lower() != string[j].lower():
        print(string[i].lower(), string[j].lower(), i)
        return False
    
    return checkPalindrome(n-1, string, i+1, j-1)
string = "A man a plan, a canal: Panama"
new_string = ""
for letter in string:
    if letter == " " or letter == "," or letter == ":":
        continue
    else:
        new_string+= letter

print(new_string)
print(checkPalindrome(len(new_string),new_string, 0, len(new_string)-1))

import re
def isPalindrome(s):
    pattern = r"[^A-Za-z0-9]+"
    sample_str = re.sub(pattern, '', s)
    converted = sample_str.lower()
    return converted == converted[::-1]

print(isPalindrome(string))