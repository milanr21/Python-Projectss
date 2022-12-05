def replace_word():
    str = input("Enter the sentence :  ");
    word_to_replace = input("Enter the word to replace: ");
    word_replacement = input("ENter the word replacement: ");
    replace_completed = str.replace(word_to_replace, word_replacement)
    print(replace_completed)


replace_word();


