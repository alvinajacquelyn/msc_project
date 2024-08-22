import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
# importing module
from pandas import *
import csv
# reading CSV file

x = "0035D4885301021E3C9F80EBBF040BCFFE61D64545B87ADBB039F915CC7F45D8"
summ = """
The provided text describes several classes and interfaces in Java for Android, including those related to compatibility with different versions of Android, managing data loading, fragments, and task stacks. The text also covers classes and interfaces related to the Android Support Library and ActionBarSherlock library. The provided text provides a comprehensive overview of the classes and interfaces used in Android development, with a focus on the Android Support Library and ActionBarSherlock.
"""

#revmob
groundtruth = """RevMob is an advertisement library that is bundled with certain Android applications. It collects the personal information and browser history of the victim and redirects victims to malicious websites. Furthermore, Revmob will display obnoxious ads and exhibit similar behaviour to Airpush"""


# Load the tokenizer and model
model_name = "codellama/CodeLlama-7b-Instruct-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto",
)



system = "Begin answer with Yes or No."
user = (
    f"Are there any similarities between the two texts? Each text starts after 'start' and ends before 'end':\n\nThis is first text: (start) {summ} (end)\nThis is second text: (start) {groundtruth} (end)\n"
)

prompt = f"<s>[INST] <<SYS>>\n{system}\n<</SYS>>\n\n{user}[/INST]"
# prompt = f"[INST]{user}[/INST]"
inputs = tokenizer(prompt, return_tensors="pt", add_special_tokens=False).to("cuda")

# Generate code with a specified max_length
output = model.generate(
        inputs["input_ids"],
        max_new_tokens=4096,
        do_sample=True,
        temperature=0.1,
        top_p=0.95,
)
output = output[0].to("cpu")
print(tokenizer.decode(output)) 


with open(f"summ_gt_similarity/{x}_malicious_sem_sim.csv", 'a', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')

    writer.writerow([tokenizer.decode(output)])

