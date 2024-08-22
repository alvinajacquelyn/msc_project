import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
# importing module
from pandas import *
import csv
# reading CSV file

x = "0035C98CEC406051345DE5770AFBC9880C6512E2DE71D15E84CCC03A79EF3A38"
summ = """
The text describes several classes in a Java application for Android, including:

* ACall: a singleton class with native methods and a custom class loader that extends DexClassLoader.
* Util: a class with static methods for various tasks and private fields and methods.
* Lceceiver: a custom BroadcastReceiver class that overrides onReceive() and uses a custom class loader to load the receiver class.
* SR: a custom BroadcastReceiver class that overrides onReceive() and creates an instance of the real BroadcastReceiver using the loaded class.
* Application: a class that extends Android's Application class and overrides its methods to provide custom behavior.
* drawable: a static final class with a static final integer field called "icon" with the value 0x7f020000.
* layout: a class with a static final field called "main" that has a value of 0x7f030000.
* R: a class with three nested classes: drawable, layout, and string, each containing a set of integer constants that represent the identifiers for various resources in the Android application.
* string: a class with two static final fields called "hello" and "app_name".
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

