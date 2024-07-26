from ConciseSculpt.config.configuration import ConfigurationManager
from ConciseSculpt.components.data_validation import DataValiadtion
from ConciseSculpt.logging import logger 




class DataValidationTrainingPipeIine:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_files_exist()