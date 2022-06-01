def find_anagram(word,anagram):
    x = word.lower()
    y = anagram.lower()
    list_word =list(x)
    list_anagram = list(y)
    z = []
    for i in list_anagram:
        if i in list_word:
            list_word.remove(i)
            z.append(i)
            result = len(z) == len(list_anagram)
            if result is True:
                print("This is an Anagram")
                return True
            else:
                print("This is an Anagram")
                return False
                print("Try Again")

find_anagram("rescue","secure")