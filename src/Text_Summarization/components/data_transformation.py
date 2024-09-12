import os
from Text_Summarization.logging import logger
from transformers import AutoTokenizer
from datasets import  load_from_disk
from Text_Summarization.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name) # pretrained_model_name_or_path


    # From the dataset , dialogue and summary, convert to encodings with the help of tokenizier
    def convert_examples_to_features(self,example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'] , max_length = 1024, truncation = True )  #truncation:- making anything shorter and quick
        
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length = 128, truncation = True )
            
        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],   # Maintainig sequence
            'labels': target_encodings['input_ids']
        }
    

    # For starting ,fitting, saving
    def convert(self):
        dataset_samsum = load_from_disk(self.config.data_path)
        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched = True) # Apply mapping on my data with the help of the model and convert it
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir,"samsum_dataset"))