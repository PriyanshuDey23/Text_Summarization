from Text_Summarization.config.configuration import ConfigurationManager
from Text_Summarization.components.data_validation import DataValidation
from Text_Summarization.logging import logger


STAGE_NAME= "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):  # initializing empty constructor
        pass


    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()



# For integrating DVC we will use in this way
if __name__ =='__main__':
    try:
        logger.info(f"Stage {STAGE_NAME} Started")
        obj=DataValidationTrainingPipeline()  # Calling the class
        obj.main()                           # Calling the main method
        logger.info(f" Stage {STAGE_NAME} Completed")

    except Exception as e:
        logger.exception(e)
        raise e
    
# call the pipeline in main.py