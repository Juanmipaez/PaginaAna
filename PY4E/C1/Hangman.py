word = "Juankgjtr"

for name in word:
    get_word = input("Enter word: ")
    if get_word == name:
        print("Great",name)
    else:     
        while get_word != name:
            get_word = input("Enter word: ")
            if get_word == name:
                print("Great",name) 
                break

