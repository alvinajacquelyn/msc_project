import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
# importing module
from pandas import *
import csv
# reading CSV file

x = "0053A79C784D2283AC4601DA1DDD00AC947B57C1F4E303A6F42DD0700EC36A9D"
data = read_csv(f"output_table/{x}.csv")

# converting column data to list
summ = data['summ'].tolist()
r5 = data['r5'].dropna().tolist()
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



for y in range(len(r5)):
    system ="Assign a score for r5 on a scale of 1 to 5 according to the fluency criteria. Fluency refers to the quality of individual sentences. r5 should have no formatting problems, capitalization errors or obviously ungrammatical sentences (e.g., fragments, missing components) that make r5 difficult to read."
    user = ( "[Start r5]\n"+str(r5[y] )+ "\n[End r5]\n" + 
            "\nOutput the fluency score for r5 on a scale of 1 to 5."
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


    with open(f"llmasjudge_r5/{x}_r5_fluency.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        writer.writerow([tokenizer.decode(output)])