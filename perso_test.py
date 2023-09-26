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

    for category in category_scores.keys():
        category_scores[category] = df[category].sum()

    # Create a new DataFrame to store the category scores.
    category_df = pd.DataFrame(list(category_scores.items()), columns=['Category', 'Score'])

    # Sort the DataFrame in descending order based on scores and pick the top 3.
    sorted_category_df = category_df.sort_values(by='Score', ascending=False)
    top_3_categories = sorted_category_df.head(3)

    # Map the top 3 categories to letters.
    top_3_letters = [category_to_letter[category] for category in top_3_categories['Category']]

    return category_df, top_3_categories, top_3_letters

