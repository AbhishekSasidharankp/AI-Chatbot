import pandas as pd
import spacy
import time
import re

# Load a pre-trained spaCy model
nlp = spacy.load("en_core_web_sm")

# Define a function to handle user interactions
def ask_user(question):
    response = input(question)
    return response.strip()

# Define the conversation agents
def initiation_agent():
    return "Hello! I'm here to assist you. Can you please provide your name?"

def extraction_verification_agent(data_type):
    return f"Thanks for your {data_type}! Can you please verify it?"

def convincing_agent(data_type):
    return f"I understand your concern. Providing your {data_type} will help us assist you better. Can you please share it?"

# Initialize user data
user_data = {
    "Name": None,
    "Email": None,
    "Phone no": None,
    "Address": None,
    "Date of birth": None,
    "Education": None
}
current_info_needed = 'Name'

# Define the conversation flow
def start_conversation(user_input):
    global current_info_needed

    # Check if user input is a small talk request
    if 'small talk' in user_input.lower():
        current_info_needed = 'SmallTalk'
        return "Sure! Let's have a friendly chat. What's on your mind?"

    if current_info_needed == 'SmallTalk':
        # Handle small talk or switch to information extraction
        if 'name' in user_input.lower():
            current_info_needed = 'Name'
            return "Great! Now, please provide your name."
        elif 'email' in user_input.lower():
            current_info_needed = 'Email'
        elif 'no' in user_input.lower():
            current_info_needed = 'SmallTalk'  # Start small talk
            return initiate_small_talk()
        else:
            return "Now let me assist you. which information would you like to provide next? (Email,Address)"

    
    if current_info_needed == 'Name':
        name_match = re.match(r'^[A-Za-z\s]+$', user_input)
        if name_match:
            user_data['Name'] = user_input
            current_info_needed = 'Email'
            return "Great! Now, please provide your email."
        else:
            return "I'm sorry, the name you provided is not valid. Please enter a valid name."
    if current_info_needed == 'Email':
        email_match = re.match(r'^\S+@\S+\.\S+$', user_input)
        if email_match:
            user_data['Email'] = user_input
            current_info_needed = 'Phone'
            return "Thank you. What's your phone number?"
        elif 'no' in user_input.lower():
            current_info_needed = 'SmallTalk'  # Start small talk
            return initiate_small_talk()
        else:
            return "I'm sorry, the email you provided is not valid. Please enter a valid email."
        
    if current_info_needed == 'Phone':
        phone_match = re.match(r'^\d{10}$', user_input)
        if phone_match:
            user_data['Phone'] = user_input
            current_info_needed = 'Address'
            return "Got it. Please provide your address."
        else:
            return "I'm sorry, the phone number you provided is not valid. Please enter a valid phone number."

    if current_info_needed == 'Address':
        user_data['Address'] = user_input
        current_info_needed = 'Date of Birth'
        return "Thank you. What's your date of birth?"
    
    if current_info_needed == 'Date of Birth':
        dob_match = re.match(r'^\d{4}-\d{2}-\d{2}$', user_input)
        if dob_match:
            user_data['Date of Birth'] = user_input
            current_info_needed = 'Education'
            return "Great! Finally, what's your highest level of education?"
        else:
            return "I'm sorry, the date of birth you provided is not valid. Please enter a valid date of birth (YYYY-MM-DD)."

    

    if current_info_needed == 'Education':
        user_data['Education'] = user_input
        format_and_save_data()
        return "Thank you for providing your information. We have saved it."

def format_and_save_data():
    user_data_df = pd.DataFrame([user_data])
    # Check if the CSV file existsni
    try:
        existing_data = pd.read_csv("user_data.csv")
        # Append the new data to the existing data
        combined_data = pd.concat([existing_data, user_data_df], ignore_index=True)
        combined_data.to_csv("user_data.csv", index=False, mode="w")  # Use mode="w" to overwrite the existing file
        print("User data saved successfully!")
    except FileNotFoundError:
        # If the file doesn't exist, create a new one
        user_data_df.to_csv("user_data.csv", index=False)
        print("User data saved successfully!")

# Function to handle small talk
def initiate_small_talk():
    small_talk_questions = [
        "How's the weather where you are?",
        "Have you had a good day so far?",
        "Do you have any interesting plans for the weekend?",
        "What's your favorite hobby or activity?",
    ]

    for question in small_talk_questions:
        response = ask_user(question)
        if "weather" in question.lower():
            print("That's nice to hear.")
        elif "good day" in question.lower():
            print("Well, I hope you enjoy the day.")
        elif "interesting plans" in question.lower():
            print("Oh, I hope everything goes well.")
        elif "favorite hobby" in question.lower():
            print("Well, your hobbies are great.")

    print("Thank you for talking with me. Its completely safe to share your details with me.Now, let's get back to the information we need.")
    return conversation  # Switch back to information extraction

conversation = initiation_agent()
last_response_time = time.time()
while user_data['Education'] is None: 
    user_input = ask_user(conversation)
    last_response_time = time.time()
    current_time = time.time()
    response_time = current_time - last_response_time

    if response_time > 10:
        conversation = initiate_small_talk()
    else:
        conversation = start_conversation(user_input)

