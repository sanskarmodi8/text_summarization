import gradio as gr 
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import os
import subprocess

TOKENIZER_PATH = "artifacts/model_trainer/tokenizer"
MODEL_PATH = "artifacts/model_trainer/pegasus-samsum-model"
device = "cuda" if torch.cuda.is_available() else "cpu"

def check_required_files_exist():
    if os.path.exists(TOKENIZER_PATH) and os.path.getsize(TOKENIZER_PATH)>0 and os.path.exists(MODEL_PATH) and os.path.getsize(MODEL_PATH)>0:
        print("REQUIRED FILES EXISTS")
    else:
        os.environ["AZURE_SUBSCRIPTION_ID"] = "c5699ea4-2e51-4d63-9018-11208507e22c"
        os.environ["AZURE_CLIENT_SECRET"] = "kTJ8Q~EjcKiA_VoLyJrIC84wfO9nyl1RW1_q5azK"
        os.environ["AZURE_TENANT_ID"] = "2c5bdaf4-8ff2-4bd9-bd54-7c50ab219590"
        os.environ["AZURE_CLIENT_ID"] = "d66c9f1b-5d63-4d53-a081-2c7f17b94ce6"
        subprocess.run(["dvc", "pull"])
        print("PULLED REQUIRED FILES SUCCESSFULLY FROM AZURE BLOB STORAGE USING DVC")


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
    
    check_required_files_exist()
    
    gr.Interface(fn=summarize, inputs="text", outputs="text").launch(debug=True)