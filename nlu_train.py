from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter

def train_nlu_model(data, configs, model_dir):
    # loading the nlu training samples
    training_data = load_data(data)

    # trainer to educate our pipeline
    trainer = Trainer(config.load(configs))

    # train the model!
    interpreter = trainer.train(training_data)

    # store it for future use
    model_directory = trainer.persist(model_dir, fixed_model_name="con_nlu")

def run_nlu():
    interpreter = Interpreter.load('./models/nlu/default/con_nlu')
    print(interpreter.parse(u"Who is the speakers and how long is the session?"))

if __name__ == "__main__":
    train_nlu_model('./data/nlu.md', 'nlu_config.yml', './models/nlu')
    run_nlu()
