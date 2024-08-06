from data_preparation import load_credit_card_data
from knowledge_base import create_knowledge_base
from user_input import get_user_preferences
from matching_algorithm import match_cards
from recommendation_generator import generate_recommendations

def main():
    print("Welcome to the Credit Card Recommender!")
    print("--------------------------------------")

    # Load credit card data
    df = load_credit_card_data("data/credit_cards.csv")
    if df.empty:
        print("Error: Unable to load credit card data. Exiting.")
        return

    # Create knowledge base
    kb = create_knowledge_base(df)

    # Get user preferences
    print("\nLet's find the best credit card for you!")
    preferences = get_user_preferences()

    # Match cards to user preferences
    matches = match_cards(df, preferences)

    # Generate recommendations
    recommendations = generate_recommendations(matches, preferences)

    # Display results
    print("\nBased on your preferences, here are our top recommendations:")
    print(recommendations)

    print("\nThank you for using the Credit Card Recommender!")

if __name__ == "__main__":
    main()