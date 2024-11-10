import binascii

hex1 = "1c0111001f010100061a024b53535009181c"
hex2 = "686974207468652062756c6c277320657965"

def fixed_XOR(hex1, hex2):

    byte_data1 = binascii.unhexlify(hex1)
    byte_data2 = binascii.unhexlify(hex2)

    xor_output = bytes([a ^ b for a, b in zip(byte_data1, byte_data2)])

    return xor_output.hex()

if __name__ == "__main__":
    print(fixed_XOR(hex1, hex2))    
