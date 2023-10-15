Documentation:
This Python software builds a chatbot that asks users questions and engages in light conversation using the pandas and spacy libraries. The chatbot starts the discussion, queries the user for particular information, verifies the input, and saves the data in a CSV file. If the user wants informal discussion, it also offers a small talk option.

Usage:

Verify that you have installed the required libraries, as stated in the requirements.txt file.

Run the application.

The chatbot starts the conversation by requesting the user's name.

Name, Email, Phone, Address, Date of Birth, and Education are just a few of the several data types it can manage.

The chatbot verifies the input once the user responds. For instance, it verifies that the email address is formatted properly or that the phone number has 10 digits.

Throughout the interaction, the chatbot provides options for small talk. To switch to small talk, type "small talk."

Small talk questions are predefined, and the bot responds based on the kind of inquiry the person asks.

The user may select "no" in order to proceed.

The collected user data is saved in a CSV file named "user_data.csv."


Functions:


ask_user(question) receives a question as input, waits for a response from the user, and then returns that response.
Returns the introductory welcome and request for the user's name via initiation_agent().
Data kinds like Name and Email can be extracted and verified using the extraction_verification_agent(data_type) function.
When the chatbot tries to persuade the user to input their data, the convincing_agent(data_type) provides response
start_conversation(user_input) controls the flow of the conversation based on input from the user. It keeps track of the most recent data required and verifies user input.
format_and_save_data() saves user information to a CSV file by adding to an already-existing file or by creating a new one if one doesn't already exist.
initiate_small_talk(): Starts small conversation by asking and answering predetermined questions.

Execution:

The initiation_agent, which welcomes the user and asks for their name, launches the software.
The dialogue is then managed by keeping track of the most up-to-date facts required and posing specific questions to the user.
It turns to small chat mode and offers predetermined questions and answers if the user requests to engage in small talk.
If the user selects "no," the program starts chit-chatting again.
The "user_data.csv" file contains the user information that was gathered.
The software continues to run in a loop until all user data has been gathered.
To execute the program successfully, please make sure you have the required libraries and the spaCy model "en_core_web_sm" installed. Using the command python -m spacy download en_core_web_sm, you can install SpaCy models.




