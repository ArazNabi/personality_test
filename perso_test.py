import pandas as pd

def personality_type(csv_file_path):
    # categories to letters.
    category_to_letter = {
        "Feeling" : "F", 
        "Thinking" : "T",
        "Intuition" : "I",
        "Sensing" : "S",
        "Introversion" : "I",
        "Extroversion" : "E",
        "Judging": "J",
        "Perceving" : "P"
    }

    # Read the CSV file into a DataFrame.
    df = pd.read_csv(csv_file_path)

    # Initialize a dictionary to store the total scores per category.
    category_scores = {category: 0 for category in category_to_letter}

    #sum score per category to new dataframe

    new_data= df[["Category", "Answer"]].groupby("Category").sum()
    print(new_data.head())


    # Sort the DataFrame in descending order based on scores and pick the top 3.
    sorted_category_df = new_data.sort_values(by='Answer', ascending=False)
    top_3_categories = sorted_category_df.head(3)
    print(top_3_categories.head())

    # Map the top 3 categories to letters.
    top_3_letters = [category_to_letter[category] for category in top_3_categories['Category']]

    return category_df, top_3_categories, top_3_letters

personality_type('personality_test/output_data/answers_simon_test.csv')