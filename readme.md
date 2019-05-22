## Software used
- rasa NLU
- rasa core
- spacy
- sqlite3
- mongodb

## Installation
1. Create a conda enviorment:
`conda create -n rasa_chatbot python=3.7.1`

2. Conda activate the enviorment:
`conda activate rasa_chatbot`

3. Install the requirements:
`pip install -r requirements.txt`

4. Download the spacy english library:
`python -m spacy download en`

## Run the bot
Method 1-
- Command line:
`python -m rasa_core.run -d models/dialogue -u models/nlu/default/con_nlu --port 5005 --endpoints endpoints.yml --credentials credentials.yml`
- New terminal Command Line:
`php -S localhost:8080`

- Web browser goto: `localhost:8080`

Method 2-
- Command Line:
`python -m rasa_core_sdk.endpoint --actions actions`
- New terminal Command Line:
`python chat_session.py`

Demo Conversation-
`
- USER: Hi
- CHATBOT: Hey! I am a conference assistant. I can help you find the sessions to attend, or answer conference-related questions.
- USER: suggest me some machine learning sessions
- CHATBOT: I would recommend you attend: Building a production-scale ML platform
- USER: length of the session?
- CHATBOT: The session is 40 min
- USER: speaker?
- CHATBOT: The speaker is YU DONG.
- USER: thanks, bye
- CHATBOT: You are very welcome!
`

