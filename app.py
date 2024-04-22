import gradio as gr 
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import os
import subprocess

TOKENIZER_PATH = "artifacts/model_trainer/tokenizer"
MODEL_PATH = "artifacts/model_trainer/pegasus-samsum-model"
device = "cuda" if torch.cuda.is_available() else "cpu"


def summarize(text):
    
    tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH).to(device)
    
    inputs = tokenizer([text], max_length=1024,  truncation=True, 
                    padding="max_length", return_tensors="pt")
    
    summaries = model.generate(input_ids=inputs["input_ids"].to(device),
                    attention_mask=inputs["attention_mask"].to(device), 
                    length_penalty=0.8, num_beams=8, max_length=128)
    
    decoded_summaries = [tokenizer.decode(s, skip_special_tokens=True, 
                            clean_up_tokenization_spaces=True) 
        for s in summaries]      
    
    decoded_summaries = [d.replace("", " ") for d in decoded_summaries]
    return decoded_summaries[0]


if __name__=="__main__":
    
    gr.Interface(fn=summarize, inputs="text", outputs="text", inputs_label="Enter your Text", outputs_label="Generated Summary").launch(debug=True, share=True)