import streamlit as st
import google.generativeai as genai

# Set up the API key
genai.configure(api_key="AIzaSyCUAqGPCnMq-ftOx8tZpN2ihLilmugyOiU")

# Display header and subheader
st.header("HARSHA GPT")
st.subheader("Welcome to Harsha GPT 👋")

# Background styling
st.markdown(
    """
    <style>
        .stApp {
            background-image: url('D:/HARSHA PROJECTS/GPT MODEL/download.jpeg'); 
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
    </style>
    """, unsafe_allow_html=True
)

# Display a text box where the user can enter text
user_input = st.text_input("Enter your query:")

# Show a button to submit the text
if st.button("Submit"):
    if user_input:
        st.write(f"You said: {user_input}")
        
        # Combine instructions with user query
        full_prompt = f"""
You are a simple and beginner-friendly assistant. Your task is to respond to questions in the following way:

1. Provide a **simple, easy-to-understand answer** (around 10 lines).
2. **Include one clear example** for every concept or question.
3. Provide **reliable links** for further reading on the topic.
4. **Avoid using complex terminology** or advanced jargon. Keep things straightforward.
5. Ensure your responses are **short and concise**. 

Now answer this query: {user_input}
"""

        # Set up the Gemini model
        gemini_model = genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp")

        # Generate content
        response = gemini_model.generate_content(full_prompt)

        # Display the generated content
        st.write("AI Response:")
        st.write(response.text)
    else:
        st.write("Please enter something before submitting.")
