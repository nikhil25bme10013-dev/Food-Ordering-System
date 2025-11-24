def get_name():
    name = input("Enter your password: ")
    return name

def main():
    name = get_name()
    Special = "!@#$%^&*()_+[]{}|;:,.<>?/~"
    val = True

    length = False
    digit = False
    upper = False
    lower = False
    symbol = False
    for char in name:
        if len(name) > 7:
            length = True
        if ord(char) >= 48 and ord(char) <= 57:
            digit = True
        elif ord(char) >= 65 and ord(char) <= 90:
            upper = True
        elif ord(char) >= 97 and ord(char) <= 122:
            lower = True
        elif char in Special:
            symbol = True

    if length + digit + upper + lower + symbol == 5:
        print('Password is strong')
    if length + digit + upper + lower + symbol == 4:
        print('Password is Medium')
    if length + digit + upper + lower + symbol == 3:
        print('Password is Medium')
    if length + digit + upper + lower + symbol == 2:
        print('Password is Medium')
    if length + digit + upper + lower + symbol == 1:
        print('Password is Weak')
 
    return val

if __name__ == "__main__":
    main()