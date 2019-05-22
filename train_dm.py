from rasa_core.policies import KerasPolicy, MemoizationPolicy
from rasa_core.agent import Agent

def train_dialogue(domain_file, stories_file, dialogue_path):
    # loading our neatly defined training dialogues
    agent = Agent(domain_file, policies=[MemoizationPolicy(), KerasPolicy(epochs=200, max_history = 6)])
    training_data = agent.load_data(stories_file)


    agent.train(
        training_data)

    agent.persist(dialogue_path)

if __name__ == "__main__":
    train_dialogue('./domain.yml', './data/stories.md', './models/dialogue')