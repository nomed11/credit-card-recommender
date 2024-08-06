# Credit Card Recommender

## Overview
The Credit Card Recommender is an AI-powered application that provides personalized credit card recommendations based on user preferences. It utilizes data analysis, machine learning techniques, and natural language processing to match users with the most suitable credit card options.

## Features
- User preference collection through an interactive questionnaire
- Data-driven matching algorithm for credit card recommendations
- AI-generated personalized explanations for recommendations
- Comprehensive credit card database
- Efficient data loading and processing
- Fallback mechanism for API rate limit handling

## Project Structure
```
credit_card_recommender/
│
├── data/
│   └── credit_cards.csv
│
├── src/
│   ├── config.py
│   ├── data_preparation.py
│   ├── knowledge_base.py
│   ├── user_input.py
│   ├── matching_algorithm.py
│   ├── recommendation_generator.py
│   └── main.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/credit-card-recommender.git
   cd credit-card-recommender
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key:
   - Create a `.env` file in the project root
   - Add your OpenAI API key: `OPENAI_API_KEY=your_api_key_here`

## Important: API Key and Rate Limits
- You must have an OpenAI account and API key to use this application.
- Create a `.env` file in the project root and add your OpenAI API key as shown above.
- Be aware of OpenAI's rate limits. If you exceed these limits, the application will fall back to a simpler recommendation system.
- Monitor your API usage to avoid unexpected charges.

## Usage
Run the main application:
```
python src/main.py
```
Follow the prompts to input your preferences and receive personalized credit card recommendations.

## Components
1. **Data Preparation** (`data_preparation.py`): Loads and processes the credit card data from a CSV file.
2. **Knowledge Base** (`knowledge_base.py`): Creates a searchable knowledge base using LangChain and Chroma, with a fallback to a simple keyword-based system.
3. **User Input** (`user_input.py`): Collects user preferences through an interactive questionnaire.
4. **Matching Algorithm** (`matching_algorithm.py`): Scores and ranks credit cards based on user preferences.
5. **Recommendation Generator** (`recommendation_generator.py`): Uses OpenAI's language model to generate personalized recommendations.
6. **Main Application** (`main.py`): Orchestrates the entire recommendation process.

## Future Improvements
- Implement a web-based user interface
- Expand the credit card database
- Add more sophisticated matching algorithms
- Implement user accounts and recommendation history

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License.