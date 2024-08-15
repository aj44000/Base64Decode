from base64decode import decode
def determineDecode():
    message = input('Enter Code: ')
    print(decode(message))

if __name__ == '__main__':
    determineDecode()
