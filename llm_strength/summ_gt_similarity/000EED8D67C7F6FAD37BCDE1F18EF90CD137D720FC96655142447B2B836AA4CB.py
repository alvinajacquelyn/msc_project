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
summ = """
The text describes several Java classes and interfaces for an Android app, including:

* A class named "Cdo" that implements the "DialogInterface.OnClickListener" interface and has two fields.
* A class named "ce" that implements the "OnClickListener" interface and has a constructor that takes a "Navigator" object as a parameter.
* A class named "cf" that implements the "View.OnClickListener" interface and has a constructor that takes a "Navigator" object as a parameter.
* A class named "cg" with a static method named "a" that takes a "String" parameter and returns a "boolean" value indicating whether the length of the string is equal to 27.
* A Java annotation that specifies the type of a declaration, in this case, a type declaration.
* A Java class named "ci" that provides methods for playing and recording audio.
* A class named "cj" that implements the "OnCompletionListener" interface from the Android SDK.
* A class named "ck" that has a constructor that takes an "Activity" object as a parameter and has two methods.
* A class named "cl" that has a private static method named "a" that sets the "System.runFinalizersOnExit" property to "true" and then calls the "System.exit" method with a status code of "0".
* A Java class that provides a set of methods for accessing and modifying shared preferences. The class is named "cm" and it has a private constructor to prevent instantiation. The class has a number of static methods that can be used to access and modify shared preferences.
* A custom adapter class named "cx" that extends the "ArrayAdapter" class.
* A class named "cy" that implements the "OnClickListener" interface.
* A class named "cz" that also implements the "OnClickListener" interface.
* A class named "dc" that implements the "Runnable" interface.
* A class named "DownloadMoreSongsActivity" that extends the "Activity" class and implements the "y" interface.
* A class named "DownloadService" that extends the Android "Service" class and implements the "y" interface.

These classes are used for different purposes such as displaying a list of recordings in a list view, handling click events, and interacting with a database. They also implement various interfaces, including OnClickListener, View.OnClickListener, CompoundButton.OnCheckedChangeListener, SeekBar.OnSeekBarChangeListener, and y. This code defines an anonymous class that implements the AdListener and CatListener interfaces. The anonymous class has methods for handling ad requests and touch events, and a reference to a CatListener object. Additionally, the code defines a CatLayout class that extends RelativeLayout and implements the CatListener interface, responsible for displaying a cat image and handling touch events. The code also defines an interface called CatListener with three methods for notifying the listener of various events related to the ads.
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

