import re
"""
(?!.*(.).*\1) checks no repeating characters;
(?=(?:.*[A-Z]){2,}) checks at least 2 uppercase letters;
(?=(?:.*\d){3,}) checks at least 3 digits;
[a-zA-Z0-9]{10} checks exactly 10 alphanumeric characters.
"""

def validate(id):
    if re.match(r'(?!.*(.).*\1)(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})[a-zA-Z0-9]{10}', id):
        print('Valid')
    else:
        print('Invalid')

if __name__ == "__main__":
    n = int(input())
    uid = [input() for i in range(n)]

    for id in uid:
        validate(id)