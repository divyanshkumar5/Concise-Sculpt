from ConciseSculpt.config.configuration import ConfigurationManager
from ConciseSculpt.components.model_evalution import ModelEvaluation
from ConciseSculpt.logging import logger 

class ModelEvaluationTrainingPipeIine:
    def __init__(self):
        pass


try:
    config = ConfigurationManager()
    model_evaluation_config = config.get_model_evaluation_config()
    model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
    model_evaluation_config.evaluate()
except Exception as e:
    raise e