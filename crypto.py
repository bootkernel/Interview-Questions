# Crypto Function
def crypto(string):
   # Using ASCII Table
   midpoint_float = 109.5
   decrypted = ""
   for char in string:
      if 97 <= ord(char) <= 122:                         # 97 to 122 is A - Z in Unicode

         calc = float(midpoint_float) - ord(char)        # ord() returns an integer which
                                                         # represents an Unicode character
         char = midpoint_float + calc
         decrypted = decrypted + chr(int(char))
      else:
         decrypted = decrypted + char
   return decrypted

# Testing
string = "z xzg"
print("\nCryptic Message:", string)
print("\nDecrypted Message: ", crypto(string))
