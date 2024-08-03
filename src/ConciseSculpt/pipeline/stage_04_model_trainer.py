from ConciseSculpt.config.configuration import ConfigurationManager
from ConciseSculpt.components.model_trainer import ModelTrainer
from ConciseSculpt.logging import logger 

class ModelTrainerTrainingPipeIine:
    def __init__(self):
        pass

try:
    config = ConfigurationManager()
    model_trainer_config = config.get_model_trainer_config()
    model_trainer_config = ModelTrainer(config=model_trainer_config)
    model_trainer_config.train()
except Exception as e:
    raise e