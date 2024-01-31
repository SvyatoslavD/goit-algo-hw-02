from collections import deque

def is_palindrome(s):
    s = ''.join(c for c in s.lower() if c.isalnum())

    cd = deque(s)

    while len(cd) > 1:
        if cd.popleft() != cd.pop():
            return False

    return True


print(is_palindrome("Svyatoslav"))
print(is_palindrome("SvyatayvS"))
print(is_palindrome("SvyaayvS"))
