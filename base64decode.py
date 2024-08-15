import base64 #Python Base64 mod
def decode(needs_decode): #function used to decode
    decoded_Message = base64.b64decode(needs_decode) #Decoder
    finalmessage = decoded_Message
    return finalmessage.decode('utf-8') #returns the decoded message