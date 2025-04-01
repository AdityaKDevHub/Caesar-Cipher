import string

def body(text, mode, shift):
      ciphertext = []
      alphabets = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5,
                   "f" : 6, "g" : 7, "h" : 8, "i" : 9, "j" : 10,
                   "k" : 11, "l" : 12, "m" : 13, "n" : 14, "o" : 15,
                   "p" : 16, "q" : 17, "r" : 18, "s" : 19, "t" : 20,
                   "u" : 21, "v" : 22, "w" : 23, "x" : 24, "y" : 25, "z" : 26}

      if mode == 'd':
        shift = -shift

      for char in text:
            if char.isupper():
                  isupper_case = True
                  char = char.lower()
            else:
                  isupper_case = False
                  
            if (char == " ") or (char in string.punctuation) or (char.isnumeric()):
                  ciphertext.append(char)
                  continue
            
            value = alphabets[char]
            new_value = (value + shift) % 26
            if new_value == 0:
              new_value = 26

            if new_value in alphabets.values():
                  alphabet = [key for key, val in alphabets.items() if val == new_value][0]
                  ciphertext.append(alphabet.upper()) if isupper_case else ciphertext.append(alphabet)

      return ''.join(ciphertext)

def main():
  plaintext = input("Enter text:\n")
  mode = input("\nChoose mode - Encrypt (E) or Decrypt (D): ").strip().lower()
  if mode not in ("e", "d", "encrypt", "decrypt"):
    print("Invalid mode. Please Try again!\n\n")
    return

  shift = int(input("\nEnter shift value: ")) % 26

  result = body(plaintext, mode, shift)
  print(f"\n{'Ciphertext' if mode == 'e' else 'Decrypted Text'}:\n{result}\n\n")

if __name__ == "__main__":
      print("Caesar Cipher\nMade by ADITYA VN KADIYALA\n")
      while True:
        main()
