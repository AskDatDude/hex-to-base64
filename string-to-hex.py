import binascii

def string_to_hex(string):
    return binascii.hexlify(string.encode()).decode()

if __name__ == "__main__":
    print("Enter a string to convert to hex:")
    string = input()
    print("Hex of the string is:")
    print(string_to_hex(string))