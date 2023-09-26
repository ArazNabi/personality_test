import pandas as pd
import numpy as np

user_names = {'Name': [
    'Olivia', 'Liam', 'Emma', 'Noah', 'Ava', 'Sophia', 'Isabella', 'Mia', 'Jackson', 'Aiden',
    'Lucas', 'Ethan', 'Patricia', 'Harper', 'Henry', 'Khaqan', 'Lily', 'Grace', 'Samuel', 'Benjamin',
    'Henry', 'Tell', 'James', 'Oliver', 'Elijah', 'Mia', 'Sofia', 'Avery', 'Scarlett', 'Madison',
    'Avatar', 'Eleanor', 'Cruz', 'Elizabeth', 'Evelyn', 'Victoria', 'Amelia', 'Emily', 'Sebastian', 'Matthew',
    'Alexander', 'Danny', 'Joseph', 'David', 'Michael', 'Yat', 'Chloe', 'Zoe', 'Grace', 'Hannah',
    'Andrew', 'William', 'Felli', 'Anthony', 'Christopher', 'Jackson', 'Josephine', 'Natalie', 'Addison', 'Beckham',
    'Peter', 'Samantha', 'Araz', 'Nora', 'Ella', 'Scarlett', 'Grace', 'Evelyn', 'Aubrey', 'Camila', 'Thor',
    'Daniela', 'Sophia', 'Evelyn', 'Charlotte', 'Mia', 'Simon', 'Abigail', 'Emily', 'Elizabeth', 'Aria', 'Wayne',
    'Tawan', 'Scarlett', 'Amelia', 'Ali', 'Hussein', 'Penelope', 'Avery', 'Claire', 'Laila', 'Bond', 'Button',
    'Samuel', 'Alexander', 'Holly', 'Daniel', 'Tom', 'Yaya', 'Joseph','Hardy'
]}

user_answers = pd.DataFrame(columns=['Name', 'Question 1', 'Question 2', 'Question 3', 'Question 4', 'Question 5', 'Question 6', 'Question 7', 
                                     'Question 8', 'Question 9', 'Question 10', 'Question 11', 'Question 12', 'Question 13', 'Question 14', 'Question 15','Question 16', ])


def create_user():
    for name in user_names['Name']:
        random_answer = {
            'Name': name,
            'Question 1': np.random.randint(1, 8),
            'Question 2': np.random.randint(1, 8),
            'Question 3': np.random.randint(1, 8),
            'Question 4': np.random.randint(1, 8),
            'Question 5': np.random.randint(1, 8),
            'Question 6': np.random.randint(1, 8),
            'Question 7': np.random.randint(1, 8),
            'Question 8': np.random.randint(1, 8),
            'Question 9': np.random.randint(1, 8),
            'Question 10': np.random.randint(1, 8),
            'Question 11': np.random.randint(1, 8),
            'Question 12': np.random.randint(1, 8),
            'Question 13': np.random.randint(1, 8),
            'Question 14': np.random.randint(1, 8),
            'Question 15': np.random.randint(1, 8),
            'Question 16': np.random.randint(1, 8)
        }
        user_answers.loc[len(user_answers)] = random_answer


create_user()

mean_columns = ['Feeling', 'Perceiving', 'Introversion', 'Sensing', 'Thinking', 'Judging', 'Extroversion', 'Intuition']
mean_values = user_answers.iloc[:, 1::2].mean(axis=1)
user_feelings = pd.DataFrame({'Name': user_answers['Name']})
for col_name, mean_col in zip(mean_columns, range(0, 16, 2)):
    user_feelings[col_name] = mean_values
    mean_values = user_answers.iloc[:, mean_col + 2::2].mean(axis=1)

print(user_feelings)
user_feelings.to_csv("dummy_data.csv")