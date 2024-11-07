import base64
import binascii


def hex_to_base64(input):

    # Convert hex string to bytes
    bytes_data = binascii.unhexlify(input)

    # Convert bytes to base64
    base64_data = base64.b64encode(bytes_data)

    return base64_data
    

if __name__ == "__main__":  
    print("Enter your hex string here to convert it to base64: ")
    input = input()
    print("Base64 encoded string is: ")
    print(hex_to_base64(input).decode())
