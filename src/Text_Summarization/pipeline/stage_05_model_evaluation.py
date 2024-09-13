from Text_Summarization.config.configuration import ConfigurationManager
from Text_Summarization.components.model_evaluation import ModelEvaluation
from Text_Summarization.logging import logger


STAGE_NAME= "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):  # initializing empty constructor
        pass


    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()


# For integrating DVC we will use in this way
if __name__ =='__main__':
    try:
        logger.info(f"Stage {STAGE_NAME} Started")
        obj=ModelEvaluationTrainingPipeline()  # Calling the class
        obj.main()                           # Calling the main method
        logger.info(f" Stage {STAGE_NAME} Completed")

    except Exception as e:
        logger.exception(e)
        raise e
    
# call the pipeline in main.py