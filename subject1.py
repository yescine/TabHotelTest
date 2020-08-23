def toUpperCase(string):
   result = ''
   for char in string:
      if ord(char) >= 65:
         result += chr(ord(char) - 32)
   return result

print(toUpperCase('abcdé--#λ'))