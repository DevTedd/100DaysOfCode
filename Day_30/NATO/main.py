# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas

data = pandas.read_csv("C:/Users/tkmwangi/Documents/GitHub/100DaysOfCode/Day_30/nato_phonetic_alphabet.csv")
# 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phon():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phon()
    else:   
        print(output_list)
   
generate_phon()           
