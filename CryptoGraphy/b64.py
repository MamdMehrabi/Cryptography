import base64

class b64:

    def __init__(self , text):
        self.text = text
    
    def encoded(self):
        encode = base64.b64encode(b"{self.text}")
        return encode

    def decode(self):
        decode = base64.b64decode(self.text)
        return decode

