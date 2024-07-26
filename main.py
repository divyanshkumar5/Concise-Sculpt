from ConciseSculpt.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeIine
from ConciseSculpt.pipeline.stage_02_data_validation import DataValidationTrainingPipeIine
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