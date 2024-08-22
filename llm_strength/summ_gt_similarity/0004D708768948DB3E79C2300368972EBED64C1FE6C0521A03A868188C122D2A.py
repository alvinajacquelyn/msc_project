import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
# importing module
from pandas import *
import csv
# reading CSV file

x = "0004D708768948DB3E79C2300368972EBED64C1FE6C0521A03A868188C122D2A"
summ = """
This code defines several classes and interfaces for a game, including a class called "Jewels" that extends the "Game" class, an interface called "Doodle" for interacting with the game, and a class called "Assets" for managing game assets. The code also defines classes for playing sounds and music, such as "Audios" and "Char", and a class called "Digit" with four fields. The code is written in Java and uses the libGDX library. The classes for drawing text and numbers on the screen use a texture atlas to store the images of the characters and digits, and they provide methods for drawing the characters and digits with different alignments, scales, and textures. The classes also provide methods for calculating the total width of a string of characters. The code is a Java class that extends the `TypeDeclaration` class from the `org.eclipse.jdt.core.dom` package, and it is used to represent a type declaration in the Eclipse JDT.
"""

#airpush
groundtruth = """Airpush is a very aggresive Ad-Network. It is an Android app that contains a third-party advertising component which displays advertising content in the device's notification panel. The module may also silently gather and forward details from the device. The third-party advertising component in Airpush programs displays advertising content in the device's notification panel. This behavior may be considered unwanted if the user is unaware of the presence of the module, objects to the nature of the advertising materials displayed, or finds the manner of the advertising display intrusive. The module may also silently leak or harvest sensitive details from the device, such as its International Mobile Equipment Identity (IMEI) number, location, contacts, etc."""


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

