from cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self): #this.name
       self.alphabet = ALPHABET

    def encrypt_text(self, plain_text: str,key: int) -> str:
        alphabet_len= len(self.alphabet) #26
        encrypted_text = []
        for letter in plain_text:
           letter_index = self.alphabet.index(letter)
           letter_cipher = (letter_index + key) %alphabet_len
           letter_output = self.alphabet[letter_cipher] 
           encrypted_text.append(letter_output) 
        return "".join(encrypted_text)  

    def decrypt_text(self, plain_text: str,key: int)-> str:
        alphabet_len= len(self.alphabet) #26
        plain_text = plain_text.upper()
        decrypted_text = []
        for letter in plain_text:
           letter_index = self.alphabet.index(letter)
           letter_cipher = (letter_index - key) %alphabet_len
           letter_output = self.alphabet[letter_cipher] 
           decrypted_text.append(letter_output) 
        return "".join(decrypted_text)   
 