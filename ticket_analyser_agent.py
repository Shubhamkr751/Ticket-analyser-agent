from cgitb import text
from langchain_google_genai import ChatGoogleGenerativeAI # type: ignore
from langchain.prompts import PromptTemplate  # type: ignore
from langchain.chains import LLMChain    # type: ignore


def analyze(customer_text) : 
    
    llm = ChatGoogleGenerativeAI(
    model='gemini-pro', google_api_key="google API key") # type: ignore

    reviewPrompt = PromptTemplate(
        input_variables=['customer_review'],

        template='''
        You are an AI customer support assistant. Your task is to analyze and summarize the customer's concerns and actions based on the following input.

            Input: 
            "{customer_review}"

            Provide a structured response in the following format:

            User concern:
            (Summarize the primary concern of the user)

            Steps taken by user:
            (Summarize the steps the user has already taken)

                '''
            )

    reviewChain = LLMChain(llm=llm, prompt=reviewPrompt, verbose=True)
    
    text_summary = reviewChain(customer_text)
    
    return text_summary['text']
        
