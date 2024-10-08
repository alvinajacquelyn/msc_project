import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
# importing module
from pandas import *
import csv
import re
import networkx as nx

# reading CSV file

x = "001EF856699CBB1791EF2DEB00F66DD259491C332E0A8A4DC3ADF80531EBFF8B"
data = pd.read_csv(f"decompiled_malware_class_csv_2/{x}.csv")

file_path = f'apk/{x}.txt'

# Converting column data to list
listcode = data['code'].tolist()
listpath = data['filepath'].tolist()


def read_adjacency_list(file_path, class_name):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    adjacency_list = {}
    for line in lines:
        line = line.strip()
        if line:
            key, values = line.split(':')
            key = key.strip().strip("'")
            values = eval(values.strip())
            adjacency_list[key] = values

    related_adjacencies = {key: values for key, values in adjacency_list.items() if class_name in values or class_name == key}
    return related_adjacencies

def format_related_adjacencies(related_adjacencies):
    result = []
    for key, values in related_adjacencies.items():
        result.append(f"{key}: {values}")
    return "\n".join(result)

def extract_class_name(java_code):
    # Regular expression to match the class declaration
    class_pattern = re.compile(r'\bclass\s+(\w+)')
    match = class_pattern.search(java_code)
    if match:
        return match.group(1)
    else:
        return None
    
# Load the tokenizer and model
model_name = "codellama/CodeLlama-7b-Instruct-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto",
)


for y in range(len(listcode)):

    class_name = extract_class_name(listcode[y])
    
    related_adjacencies = read_adjacency_list(file_path, class_name)
    formatted_string = format_related_adjacencies(related_adjacencies)


    # print(graph_string)
    system = "Begin answer with Yes or No."
    user = (
        "The following is an APK function call graph provided as an edge list, focusing on the relationships between functions within specific classes. Each edge represents a caller/callee relationship where the first element is the caller function, and the second element is the callee function. Only the relationships relevant to the specific class context are included.\n"+ 
        str(formatted_string)+'\n'+
        "Given this, does the following snippet of code contain instances of the malware objective known as Execution?" + "\n#start code\n" + listcode[y] + "\n#end code\n"+
        "Explain in 100 words." 
    )

    prompt = f"<s>[INST] <<SYS>>\n{system}\n<</SYS>>\n\n{user}[/INST]"
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


    with open(f"s1_fcg/{x}_adjacencylist.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        writer.writerow([tokenizer.decode(output)])
