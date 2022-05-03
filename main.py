import pandas as pd


data = pd.read_csv("nato_phonetic_alphabet.csv")   # TODO Read the NATO phonetic alphabet into a data frame.

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}  # TODO Create a dictionary from the data frame.

# TODO  Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()   # TODO Get the user input.

output_list = [nato_dict[letter] for letter in word]     # TODO Create a list of the phonetic code words from the word.
print(output_list)