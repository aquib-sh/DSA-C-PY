def check_palindrome(s):
    if len(s) == 1:
        return True
    if s[0] == s[-1]:
        return check_palindrome(s[1:-1])
    else:
        return False

if __name__ == "__main__":
    s = input("String: ")
    print(check_palindrome(s))
