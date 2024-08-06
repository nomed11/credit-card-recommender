from typing import Dict, Any
import re

def get_user_preferences() -> Dict[str, Any]:
    """
    Collect user preferences for credit card recommendations.

    Returns:
        Dict[str, Any]: A dictionary containing user preferences.
    """
    preferences = {}

    # Credit Score
    while True:
        score = input("What's your credit score? (300-850): ").strip()
        if score.isdigit() and 300 <= int(score) <= 850:
            preferences['credit_score'] = int(score)
            break
        print("Please enter a valid credit score between 300 and 850.")

    # Annual Fee
    while True:
        fee = input("What's the maximum annual fee you're willing to pay? ($): ").strip()
        if fee.isdigit():
            preferences['max_annual_fee'] = int(fee)
            break
        print("Please enter a valid number for the annual fee.")

    # Reward Types
    reward_types = ['Cash Back', 'Travel', 'Points', 'Miles', 'Dining']
    print("What types of rewards are you most interested in? (Select all that apply)")
    for i, reward in enumerate(reward_types, 1):
        print(f"{i}. {reward}")
    while True:
        selections = input("Enter the numbers of your choices, separated by commas: ").strip()
        if re.match(r'^[1-5](,[1-5])*$', selections):
            preferences['reward_types'] = [reward_types[int(i)-1] for i in selections.split(',')]
            break
        print("Please enter valid numbers separated by commas.")

    # Foreign Transactions
    preferences['foreign_transactions'] = input("Do you plan to use the card for foreign transactions? (y/n): ").lower().startswith('y')

    # Sign-up Bonus
    preferences['sign_up_bonus'] = input("Is a sign-up bonus important to you? (y/n): ").lower().startswith('y')

    return preferences

if __name__ == "__main__":
    # Test the function
    user_prefs = get_user_preferences()
    print("\nUser Preferences:")
    for key, value in user_prefs.items():
        print(f"{key}: {value}")