import streamlit as st   # type: ignore
from ticket_analyser_agent import analyze 

# Streamlit app


def main():
    st.title("Customer Support Conversation Analyzer")

    # Introduction text
    st.write(
        "Enter a customer support conversation text, and the app will analyze it.")

    # User input text area
    user_input = st.text_area(
        "Enter customer support conversation text:", height=200)

    # Button to submit text
    if st.button("Analyze Text"):
        if user_input:
            # Call the llm_chain function with user input
            output = analyze(user_input)

            # Store the input in session state for consistency
            st.session_state.user_input = user_input

            # Display the output returned from llm_chain
            st.write("### Analysis Result")
            st.write(output)
        else:
            st.write("Please enter some text.")

    # Button to reset and allow new input
    if st.button("Re-enter New Text"):
        st.rerun()


if __name__ == "__main__":
    main()
