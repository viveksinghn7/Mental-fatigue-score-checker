import streamlit as st

# Define the questions and their corresponding weights
questions = [
    ("How often do you feel mentally exhausted?", 1),
    ("How often do you have trouble concentrating?", 1),
    ("How often do you feel irritable or impatient?", 1),
    ("How often do you feel unmotivated to do tasks?", 1),
    ("How often do you feel overwhelmed by your responsibilities?", 1)
]

# Define the response options and their corresponding scores
response_options = {
    "Never": 0,
    "Rarely": 1,
    "Sometimes": 2,
    "Often": 3,
    "Always": 4
}

# Streamlit app
st.title("Mental Fatigue Score Checker")

# Initialize the total score
total_score = 0

# Create a dictionary to store user responses
user_responses = {}

# Display the questions and collect responses using dropdowns
for question, weight in questions:
    response = st.selectbox(question, list(response_options.keys()), key=question)
    user_responses[question] = response

# Create a submit button
if st.button('Submit'):
    # Calculate the total score
    for question, weight in questions:
        total_score += response_options[user_responses[question]] * weight

    # Normalize the score to be between 0.0 and 10.0
    max_score = len(questions) * 4  # Maximum possible score
    normalized_score = (total_score / max_score) * 10

    # Display the mental fatigue score
    st.write(f"Your mental fatigue score is: {normalized_score:.1f}")

    # Provide feedback based on the score
    if normalized_score <= 3.3:
        st.write("You have low mental fatigue. Keep up the good work!")
    elif normalized_score <= 6.6:
        st.write("You have moderate mental fatigue. Consider taking breaks and practicing self-care.")
    else:
        st.write("You have high mental fatigue. It's important to prioritize rest and seek support if needed.")
