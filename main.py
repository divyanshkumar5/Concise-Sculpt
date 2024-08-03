from ConciseSculpt.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeIine
from ConciseSculpt.pipeline.stage_02_data_validation import DataValidationTrainingPipeIine
from ConciseSculpt.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeIine
from ConciseSculpt.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeIine
from ConciseSculpt.pipeline.stage_05_model_evalution import ModelEvaluationTrainingPipeIine
from ConciseSculpt.logging import logger



STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>>stage{STAGE_NAME}started<<<<<<")
    data_ingestion = DataIngestionTrainingPipeIine()
    data_ingestion.main()
    logger.info(f">>>>>>stage{STAGE_NAME}completed<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeIine()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataTransformationTrainingPipeIine()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainerTrainingPipeIine()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e




STAGE_NAME = "Model Evaluation stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evaluation = ModelEvaluationTrainingPipeIine()
   model_evaluation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e