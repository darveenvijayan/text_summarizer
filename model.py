import nltk
import ssl
import re
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download('punkt')
nltk.download('stopwords')
from transformers import BartTokenizer, PegasusTokenizer
from transformers import BartForConditionalGeneration, PegasusForConditionalGeneration
from tqdm.notebook import tqdm



class Abstractive_Summarization_Model:
    def __init__(self):
        self.text = None
        self.IS_CNNDM = True # whether to use CNNDM dataset or XSum dataset
        self.LOWER = False
        self.max_length = 1024 if self.IS_CNNDM else 512
        self.model, self.tokenizer  = self.load_model()
        
    def load_model(self):
        # Load our model checkpoints
        print('[INFO]: Loading model ...')
        if self.IS_CNNDM:
            model = BartForConditionalGeneration.from_pretrained('Yale-LILY/brio-cnndm-uncased')
            tokenizer = BartTokenizer.from_pretrained('Yale-LILY/brio-cnndm-uncased')
        else:
            model = PegasusForConditionalGeneration.from_pretrained('Yale-LILY/brio-xsum-cased')
            tokenizer = PegasusTokenizer.from_pretrained('Yale-LILY/brio-xsum-cased')
        print('[INFO]: Model Successfully Loaded :)')    
        return model, tokenizer
        
        
    def summarize(self, text):
        # generation example
        if self.LOWER:
            article = text.lower()
        else:
            article = text
        inputs = self.tokenizer([article], max_length=self.max_length, return_tensors="pt", truncation=True)
        # Generate Summary
        summary_ids = self.model.generate(inputs["input_ids"])
        
        return self.tokenizer.batch_decode(summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
