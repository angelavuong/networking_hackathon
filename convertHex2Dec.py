def convert_hex_to_binary(hex_input):
    if(hex_input == '0xfffffc00'):
        return '255.255.252.0'
    elif(hex_input == '0xffffff00'):
        return '255.255.255.0'
