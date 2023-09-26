import pandas as pd
from rich.console import Console
from rich.prompt import IntPrompt
from rich.prompt import Prompt

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
survey_df.to_csv(path)
console.rule("TEST COMPLETE")

