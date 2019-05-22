from rasa_core.agent import Agent
from rasa_core.interpreter import NaturalLanguageInterpreter
from rasa_core.utils import EndpointConfig
import time

def load_assistant():
    messages = ["Hi! you can chat in this window. Type 'stop' to end the conversation."]
    interpreter = NaturalLanguageInterpreter.create('./models/nlu/default/con_nlu')
    endpoint = EndpointConfig('http://localhost:5055/webhook')
    agent = Agent.load('./models/dialogue', interpreter=interpreter, action_endpoint = endpoint)

    print("Your bot is ready to talk! Type your messages here or send 'stop'")
    while True:
        a = input()
        if a == 'stop':
            break
        responses = agent.handle_text(a)
        for response in responses:
            print(response["text"])

if __name__ == "__main__":
    load_assistant()