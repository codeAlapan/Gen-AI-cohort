class tokenizer:
    def __init__(self):
        self.tokens = []
        self.tokens_number=[]
        self.decoded_text = ""
    def encoder(self,text):
        for char in text:
            self.tokens.append(char)
            self.tokens_number.append(ord(char))
    def decoder(self,array):
        for token_no in array:
            self.decoded_text += chr(token_no)




text = "The cat sat on the mat."
new_tokenizer = tokenizer()
new_tokenizer.encoder(text)
new_tokenizer.decoder(new_tokenizer.tokens_number)
print(new_tokenizer.tokens)
print(new_tokenizer.tokens_number)
print(new_tokenizer.decoded_text)

