import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
# importing module
from pandas import *
import csv
# reading CSV file

x = "000EED8D67C7F6FAD37BCDE1F18EF90CD137D720FC96655142447B2B836AA4CB"
data = read_csv(f"decompiled_malware_class_csv_2/{x}.csv")

# converting column data to list
listcode = data['code'].tolist()

# # printing list data
# print(listcode)


# Load the tokenizer and model
model_name = "codellama/CodeLlama-7b-Instruct-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto",
)


for code in listcode:
    system = "Begin answer with Yes or No."
    user =(
        "The malware objective known as Execution refers to behaviors that enable malware to execute code on a system to achieve a variety of goals." +
        "Does this code contain instances of Execution? " +
        "Explain in 100 words." + "\n#start code\n" + code + "\n#end code"
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


    with open(f"d1/{x}.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        writer.writerow([tokenizer.decode(output)])


