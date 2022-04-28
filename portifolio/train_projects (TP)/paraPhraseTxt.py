from os import truncate
from pyexpat import model
from sre_parse import Tokenizer
import torch
import transformers

model_name = 'turner007/pegasus_paraphrase'
torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = pegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.form_pretrained(model_name).to(torch_device)

def get_reeposnse(input_text, ):
    batch = tokenizer.prepare_seq2seq_batch([input_text], truncation = True)




