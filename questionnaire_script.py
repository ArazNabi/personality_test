import pandas as pd
from rich.console import Console
from rich.prompt import IntPrompt
from rich.prompt import Prompt

# function to convert the dataframe into desired output format
def adapt_data(orig_df):
    user_answers = pd.DataFrame(columns=['Name','Feeling','Perceiving',
                                     'Introversion','Sensing','Thinking',
                                     'Judging','Extroversion','Intuition'])

    list_of_avgs = []

    for i in range(len(orig_df)):
        if i % 2 == 0:
            list_of_avgs.append(round((orig_df.loc[i,'Answer'] + orig_df.loc[i+1,'Answer']) / 2, 2))

    user_answers.loc[0,'Name'] = name
    user_answers.loc[0,'Feeling'] = list_of_avgs[0]
    user_answers.loc[0,'Perceiving'] = list_of_avgs[1]
    user_answers.loc[0,'Introversion'] = list_of_avgs[2]
    user_answers.loc[0,'Sensing'] = list_of_avgs[3]
    user_answers.loc[0,'Thinking'] = list_of_avgs[4]
    user_answers.loc[0,'Judging'] = list_of_avgs[5]
    user_answers.loc[0,'Extroversion'] = list_of_avgs[6]
    user_answers.loc[0,'Intuition'] = list_of_avgs[7]

    return user_answers


if __name__ == "__main__":
    console = Console()

    # read csv file
    survey_df = pd.read_csv(
        '16 questions.csv',
        delimiter=';')

    # define allowed choices
    allowed_choices = list(map(str, range(1,8)))

    console.print("\n")
    console.rule("TEST YOURSELF: Which type of programmer are you?")

    name = Prompt.ask("Enter your name")
    console.print("\n")

    # print questions one by one and take answers
    for i in range(len(survey_df)):
        console.print(f"[italic purple]Question {str(i+1)}: [/]")
        console.print(survey_df.loc[i,'Question'])
        # answer = 5
        answer = IntPrompt.ask("[italic]I do not agree (1) - I fully agree (7)[/]", choices=allowed_choices, show_choices=False)
        survey_df.loc[i,'Answer'] = answer # stores answer in a new column

    path = "output_data/answers_" + name + ".csv"
    # survey_df.to_csv(path)
    adapt_data(survey_df).to_csv(path)
    console.rule("TEST COMPLETE")

