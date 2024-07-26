from langchain.schema import Document
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
import pandas as pd
from config import OPENAI_API_KEY

def create_knowledge_base(df: pd.DataFrame) -> Chroma:
    """
    create a knowledge base from credit card data using LangChain and Chroma.
    
    args:
        df (pd.DataFrame): DataFrame containing credit card data.
    
    returns:
        Chroma: A Chroma vector store containing the credit card information.
    """
    # convert dataFrame rows to documents
    documents = []
    for _, row in df.iterrows():
        content = f"Card: {row['name']}\n" \
                f"Annual Fee: ${row['annual_fee']}\n" \
                f"Rewards Type: {row['rewards_type']}\n" \
                f"Credit Score Required: {row['credit_score_required']}\n" \
                f"Foreign Transaction Fee: {row['foreign_transaction_fee']}%\n" \
                f"Sign Up Bonus: {row['sign_up_bonus']}"
        doc = Document(page_content=content, metadata={"name": row["name"]})
        documents.append(doc)

    # create and return the vector store
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vectorstore = Chroma.from_documents(documents, embeddings)
    print(f"Created knowledge base with {len(documents)} credit cards.")
    return vectorstore

# test function directly
if __name__ == "__main__":
    from data_preparation import load_credit_card_data
    df = load_credit_card_data("../data/credit_cards.csv")
    kb = create_knowledge_base(df)
    print("Knowledge base created successfully.")