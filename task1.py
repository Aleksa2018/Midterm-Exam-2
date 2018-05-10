"""
===================   TASK 1   ====================
* Name: Caesar Cipher
*
* Caesar Cipher is encryption technique in which
* each letter in the plaintext is replaced by a
* letter some fixed number of positions down the
* alphabet. The method is named after Julius Caesar,
* who used it in his private correspondence.
*
* Write a script that will accept number of positions
* that should be shifted down the Unicode code points
* of character. White spaces and punctuation marks
* should be ignored during encryption process.
*
* Hint: `ord()` returns integer representing Unicode
* code point for single character.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

inp = input('Tekst koji treba da se kodira:\n')
inp = inp.lower()

key = int(input('Unijeti broj koji zelimo da koristimo od 7 do 31:\n'))
def rot13(input,key):
    if key > 31:
        key = 31
    elif key < 7:
        key = 7
    finaltext = ''
    for rijec in input:
        if rijec.isalpha():
            num = ord(rijec)
            if (num + key) > 122:
                x = (num + key) - 122
                finaltext += chr(x + ord('a') - 1)
            elif((num + key <= 122)):
                finaltext += chr(num + key)
        else:
            finaltext += rijec
    print(finaltext)

rot13(inp,key)
