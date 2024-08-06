from typing import List, Dict, Any
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from config import OPENAI_API_KEY

def generate_recommendations(matches: List[Dict[str, Any]], preferences: Dict[str, Any]) -> str:
    """
    Generate personalized credit card recommendations using OpenAI's language model.

    Args:
        matches (List[Dict[str, Any]]): A list of matched credit cards.
        preferences (Dict[str, Any]): User preferences.

    Returns:
        str: A string containing personalized recommendations.
    """
    llm = OpenAI(temperature=0.7, openai_api_key=OPENAI_API_KEY)

    template = """
    Based on the user's preferences and the top matched credit cards, provide personalized recommendations.
    Be concise but informative, highlighting the key features of each card that align with the user's preferences.

    User Preferences:
    - Credit Score: {credit_score}
    - Maximum Annual Fee: ${max_annual_fee}
    - Preferred Reward Types: {reward_types}
    - Foreign Transactions: {foreign_transactions}
    - Sign-up Bonus Important: {sign_up_bonus}

    Top Matched Cards:
    {matched_cards}

    Recommendations:
    """

    matched_cards_str = "\n".join([f"- {card['name']} (Score: {card['score']:.2f})" for card in matches])

    prompt = PromptTemplate(
        input_variables=["credit_score", "max_annual_fee", "reward_types", "foreign_transactions", "sign_up_bonus", "matched_cards"],
        template=template
    )

    recommendations = llm(prompt.format(
        credit_score=preferences['credit_score'],
        max_annual_fee=preferences['max_annual_fee'],
        reward_types=", ".join(preferences['reward_types']),
        foreign_transactions="Yes" if preferences['foreign_transactions'] else "No",
        sign_up_bonus="Yes" if preferences['sign_up_bonus'] else "No",
        matched_cards=matched_cards_str
    ))

    return recommendations.strip()

if __name__ == "__main__":
    # Test the function
    from data_preparation import load_credit_card_data
    from user_input import get_user_preferences
    from matching_algorithm import match_cards

    df = load_credit_card_data("../data/credit_cards.csv")
    preferences = get_user_preferences()
    matches = match_cards(df, preferences)
    recommendations = generate_recommendations(matches, preferences)
    
    print("\nPersonalized Recommendations:")
    print(recommendations)