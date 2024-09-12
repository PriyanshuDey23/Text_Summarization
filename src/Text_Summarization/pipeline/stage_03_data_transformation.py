from Text_Summarization.config.configuration import ConfigurationManager
from Text_Summarization.components.data_transformation import DataTransformation
from Text_Summarization.logging import logger


STAGE_NAME= "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):  # initializing empty constructor
        pass


    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()


# For integrating DVC we will use in this way
if __name__ =='__main__':
    try:
        logger.info(f"Stage {STAGE_NAME} Started")
        obj=DataTransformationTrainingPipeline()  # Calling the class
        obj.main()                           # Calling the main method
        logger.info(f" Stage {STAGE_NAME} Completed")

    except Exception as e:
        logger.exception(e)
        raise e
    
# call the pipeline in main.py