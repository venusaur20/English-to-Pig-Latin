select = input("To Pig Latin text or to English text? ")


if select == "e":
    user_input = input("Enter text to be translated to Pig Latin! ")
    input_list = list(user_input)
    current_word = []
    current_sentence = []
    

    def english_to_pig():
        if current_word[0].lower() in ('a', 'e', 'i', 'o', 'u'):
                current_sentence.append((''.join(current_word)) + "ay ")
            
        else:
            current_word.append(current_word[0])
            current_word.remove(current_word[0])
            current_sentence.append(''.join(current_word) + "ay ")


    for i in range(len(input_list)):
        
        if (''.join(input_list)[i]) == " " or "":

            english_to_pig()
            current_word = []

        else:
            current_word.append(input_list[i])
            if i+1 == len(''.join(input_list)):
                english_to_pig()


    print(''.join(current_sentence))
                


elif select == "d":
    user_input = input("Enter text to be translated to English! ")
    input_list = list(user_input)
    current_word = []
    current_sentence = []

    def pig_to_english():
        translated_word = current_word[0:-2]
        if translated_word[0].lower() not in ('a', 'e', 'i', 'o', 'u'):
            translated_word.insert(0, current_word[-3])
            translated_word.pop()
        current_sentence.append(''.join(translated_word))

    for i in range(len(input_list)):
        
        if (''.join(input_list)[i]) == " " or "":

            pig_to_english()
            current_word = []
            continue

        else:
            current_word.append(input_list[i])
            if i+1 == len(''.join(input_list)):
                pig_to_english()

    print(''.join(current_sentence))