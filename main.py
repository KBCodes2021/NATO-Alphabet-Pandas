import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet_sort = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

#Sorts the nato alphabet into key value pairs

user_choice = input("Please type your name to return it in NATO Phonetic___:").upper()

#Compares selection between two lists

choice_list = [nato_alphabet_sort[letter] for letter in user_choice]

print(choice_list)





