import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
# importing module
from pandas import *
import csv
# reading CSV file

x = "00005BE947A8F108382B59CED7D1E95871A68539C00FF53FD3E1D93C58E2BA6C"
summ = """
The text describes several Java classes with various methods and fields. The classes include:

* "a" class: Implements the Serializable interface and has several private fields and methods.
* "aa" class: Extends AsyncTask and has a static method for registering a receiver to listen for package-related events on the Android platform.
* "ab" class: Extends RelativeLayout and has a constructor that sets the background color of the view to a dark gray color.
* "ad" class: Extends AsyncTask and has several private fields and methods.
* "ag" class: Extends LinearLayout and has a constructor that sets various properties and adds two child views.
* "ah" class: Implements the AnimationListener interface and has three methods.
* "aj" class: Extends the default WebViewClient class and overrides three methods.
* "al" class: Extends the BaseAdapter class and is used to display a list of items in a ListView.
* "am" class: Implements the OnClickListener interface and has two fields and a constructor that takes two arguments.
* "an" class: Has a final field named "a" of type "ak" and three private fields named "b", "c", and "d" of type "ImageView", "TextView", and "LinearLayout", respectively.
* "c" class: Implements the LocationListener interface and has a final field "a" that is an instance of the class "a" and a constructor that takes an instance of "a" as a parameter.
* "d" class: Has 24 fields, including a constructor, getters, and setters for each field, and a toString method that returns a string representation of the object.
"""

#dowgin
groundtruth = """Dowgin is an advertisement library that is bundled with certain Android applications. It is a malicious advertising module that is distributed and bundled with other (usually legitimate) programmes. The advertising module is used to display advertising content while also silently gathering and forwarding information from the device. Dowgin provides users with advertising content. If the user is unaware of the module’s presence or objects to the nature of the advertising materials displayed, this behaviour may be considered unwanted. The module may also silently leak or harvest sensitive device information such as the device’s International Mobile Equipment Identity (IMEI) number, location, contacts, and so on."""


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

