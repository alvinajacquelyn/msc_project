import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
# importing module
from pandas import *
import csv
# reading CSV file

x = "00076CF9D074F00DEA55AF490B9EE8766F8E98382F070AFF6A02D15954DC6C9D"
summ = """
This text is a summary of a Java code snippet that defines several classes and methods for interacting with the Android operating system and the OpenFeint API. The code defines classes for retrieving receivers, interacting with the Peewr SDK, and performing various actions related to the Android platform. The classes include "a" for retrieving receivers, "b" for interacting with the Peewr SDK, "c" for interacting with the Peewr SDK, "d" for interacting with the Peewr SDK, "e" for interacting with the Peewr SDK, "f" for interacting with the Peewr SDK, "g" for interacting with the Peewr SDK, and "Peew" for performing various actions related to the Android platform. The methods include "a(Context, int, int, String)" for checking if a given date or time is within a certain range, "get(String)" for retrieving a date or time from a string, "a(Context, Intent)" for sending a broadcast, "b(Context)" for setting a preference, "c.a()" for starting an activity, "c.b(Context)" for sending a broadcast, "d.a(Context)" for registering the d class as a receiver for certain actions, "d.b(Context)" for unregistering the d class as a receiver, and "e.a(Context)" for retrieving a list of receivers in the app's package. The code also defines several constants and variables used by the methods. The most important method in this class is the onDrawFrame method, which is called repeatedly to render the game's graphics. The onDrawFrame method checks the value of the mLoadingObjectFlag field, which is used to determine whether the game is still loading resources or whether it is ready to start rendering. If the game is still loading resources, the method sets the mLoadingObjectFlag field to 2 and plays a sound effect. If the game is ready to start rendering, the method calls the nativeRender method to render the game's graphics. The nativeRender method is a native method that is implemented in the native code of the game and is responsible for rendering the game's graphics, including the background, the fruit, and the game objects.
"""

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

