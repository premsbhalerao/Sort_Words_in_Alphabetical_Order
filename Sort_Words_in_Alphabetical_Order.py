str_1 = input ("Enter a string")
words = [word.lower () for word in str_1.split ()]
words.sort ()
for word in words:
     print (word)
