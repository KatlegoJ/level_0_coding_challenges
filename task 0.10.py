def letters (word1, word2):
    alphabet = 'abcdefghijklmnopqrstuvwxyz, ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for letter in alphabet :
        if letter in word1 and letter in word2:

            print (letter,",",end = " ")
            
letters('Enelo','Bonolo')
