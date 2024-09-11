from Text_Summarization.logging import logger

# Call the pipeline  (src\Text_Summarization\pipeline\stage_01_data_ingestion.py) in main .py 

from Text_Summarization.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME="Data Ingestion stage"
try:
    logger.info(f"Stage {STAGE_NAME} Started")
    obj=DataIngestionTrainingPipeline()  # Calling the class
    obj.main()                           # Calling the main method,Start the data ingestion part
    logger.info(f" Stage {STAGE_NAME} Completed")

except Exception as e:
    logger.exception(e)
    raise e

# After executing , Artifacts folder , zip file download , unzip of the file will happen



# Call the pipeline  (src\Text_Summarization\pipeline\stage_02_data_validation.py) in main .py 

from Text_Summarization.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME="Data Validation Stage"
try:
    logger.info(f"Stage {STAGE_NAME} Started")
    obj=DataValidationTrainingPipeline()  # Calling the class
    obj.main()                           # Calling the main method,Start the data ingestion part
    logger.info(f" Stage {STAGE_NAME} Completed")

except Exception as e:
    logger.exception(e)
    raise e

# After executing , artifacts\data_validation\status.txt