import pandas as pd

def personality_type(csv_file_path):
        #categories to letters.
    category_to_letter = {
        "Feeling": "F", 
        "Thinking": "T",
        "Intuition": "I",
        "Sensing": "S",
        "Introversion": "I",
        "Extroversion": "E",
        "Judging": "J",
        "Perceiving": "P"
    }

    # Read the CSV file into a DataFrame.
    df = pd.read_csv(csv_file_path)

    # Calculate the total score for each category. Unsure we need this now
    category_scores = {}
    for category in category_to_letter.keys():
        category_scores[category] = df[category].sum()

    # Sort categories by score in descending order.
    sorted_categories = sorted(category_scores.items(), key=lambda x: x[1], reverse=True)

    # Get the first 4 categories with the highest scores.
    top_4_categories = sorted_categories[:4]

    # Extract the first letter of each of the top 4 categories.
    top_4_letters = "".join([category_to_letter[category] for category, _ in top_4_categories])

    return top_4_letters

#Test
#print(personality_type("personality_test/output_data/answers_simon_test_new.csv"))