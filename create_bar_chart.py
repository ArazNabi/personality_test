import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# generate letter combination label from dataframe
def set_letter_comb(data):
    letter_comb = ""
    if data['Extroversion'] > data['Introversion']:
        letter_comb += 'E'
    else:
        letter_comb += 'I'
    if data['Intuition'] > data['Sensing']:
        letter_comb += 'N'
    else:
        letter_comb += 'S'
    if data['Feeling'] > data['Thinking']:
        letter_comb += 'F'
    else:
        letter_comb += 'T'
    if data['Perceiving'] > data['Judging']:
        letter_comb += 'P'
    else:
        letter_comb += 'J'

    return letter_comb
    



# new_df = pd.read_csv('output_data/answers_simon_test_new.csv')
new_df = pd.read_csv('dummy_data1.csv')
list_of_letter_comb = []


for i in range(len(new_df)):
    list_of_letter_comb.append(set_letter_comb(new_df.loc[i,]))

possible_combinations = list(set(list_of_letter_comb))

# plt.bar(possible_combinations,list_of_letter_comb, color='green')
# plt.show()
# print(possible_combinations)


