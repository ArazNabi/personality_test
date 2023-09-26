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
letter_comb_amounts = []


for i in range(len(new_df)):
    list_of_letter_comb.append(set_letter_comb(new_df.loc[i,]))

possible_combinations = list(set(list_of_letter_comb))

for comb in possible_combinations:
    letter_comb_amounts.append(list_of_letter_comb.count(comb) / 100)

df = pd.DataFrame(
   dict(
      label = possible_combinations,
      percent = letter_comb_amounts
   )
) 

df = df.sort_values('percent', ascending=True)

# how to change color scheme?
# add percentage sign and bar label
plt.barh('label', 'percent', data=df)

plt.show()


