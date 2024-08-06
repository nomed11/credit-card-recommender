from typing import List, Dict, Any
import pandas as pd

def score_card(card: pd.Series, preferences: Dict[str, Any]) -> float:
    """
    Score a credit card based on how well it matches user preferences.

    Args:
        card (pd.Series): A series containing credit card information.
        preferences (Dict[str, Any]): User preferences.

    Returns:
        float: A score representing how well the card matches preferences.
    """
    score = 0.0

    # Credit Score
    credit_scores = {"Excellent": 750, "Good": 700, "Fair": 650}
    if preferences['credit_score'] >= credit_scores.get(card['credit_score_required'], 800):
        score += 20

    # Annual Fee
    if card['annual_fee'] <= preferences['max_annual_fee']:
        score += 20
    else:
        score -= (card['annual_fee'] - preferences['max_annual_fee']) / 10

    # Reward Types
    if card['rewards_type'] in preferences['reward_types']:
        score += 30

    # Foreign Transactions
    if preferences['foreign_transactions'] and card['foreign_transaction_fee'] == 0:
        score += 15

    # Sign-up Bonus
    if preferences['sign_up_bonus'] and card['sign_up_bonus'] != '0':
        score += 15

    return max(score, 0)  # Ensure the score is not negative

def match_cards(df: pd.DataFrame, preferences: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Match credit cards to user preferences.

    Args:
        df (pd.DataFrame): DataFrame containing credit card information.
        preferences (Dict[str, Any]): User preferences.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing matched cards and their scores.
    """
    matches = []
    for _, card in df.iterrows():
        score = score_card(card, preferences)
        if score > 0:
            matches.append({
                "name": card['name'],
                "score": score,
                "annual_fee": card['annual_fee'],
                "rewards_type": card['rewards_type'],
                "sign_up_bonus": card['sign_up_bonus']
            })
    
    # Sort matches by score in descending order
    matches.sort(key=lambda x: x['score'], reverse=True)
    
    return matches[:5]  # Return top 5 matches

if __name__ == "__main__":
    # Test the function
    from data_preparation import load_credit_card_data
    from user_input import get_user_preferences

    df = load_credit_card_data("../data/credit_cards.csv")
    preferences = get_user_preferences()
    matches = match_cards(df, preferences)
    
    print("\nTop 5 Matches:")
    for match in matches:
        print(f"{match['name']} (Score: {match['score']:.2f})")