def digit_sum(n):
    if n == 0:
        return 0
    return (n % 10) + digit_sum(n//10)

if __name__ == "__main__":
    n = int(input("number: "))
    print(digit_sum(n))
    
