def reverse_string(string):
    if len(string) == 1:
        print(string)
        return

    reverse_string(string[1:])
    print(string[0])


if __name__ == "__main__":
    string = input("String: ")
    reverse_string(string)
