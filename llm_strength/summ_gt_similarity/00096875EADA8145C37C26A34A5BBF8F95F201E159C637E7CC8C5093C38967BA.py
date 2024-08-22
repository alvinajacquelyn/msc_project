import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
# importing module
from pandas import *
import csv
# reading CSV file

x = "00096875EADA8145C37C26A34A5BBF8F95F201E159C637E7CC8C5093C38967BA"
summ = """
The text describes the implementation of several custom classes in the Android framework, including "Fragment", "FragmentManagerState", and "FragmentTabHost". These classes extend and implement existing classes in the framework, such as "RuntimeException", "Parcelable", and "TabHost". The classes have constructors, fields, and methods that are used to create and manage fragments, save and restore the state of fragments, and add support for using fragments in tabs. The text is written in Java and uses the "org.eclipse.jdt.core.dom" package. The code defines several classes and interfaces, including "l", "m", "n", "o", "p", "q", "r", "SavedState", "t", and "u". The classes have methods for adding, removing, and checking the presence of elements, as well as methods for iterating over the elements and getting the size of the collection. Additionally, the text describes a class named "a" that has a static final field named "a" that is initialized to a new instance of either "d" or "c" depending on the value of "Build.VERSION.SDK_INT". The "a" method is defined to return the result of calling the "a" method on the "a" field, passing in two integer arguments. The code defines several classes and interfaces related to touch events and velocity tracking in Android. The main classes are "n" and "o", which implement the "p" interface and provide methods for retrieving information about touch events. The "p" interface has five methods, each with a different number of parameters. The "n" class overrides these methods with its own implementations, which call the corresponding methods of an object of type "q". The "q" class contains methods for retrieving information about touch events, such as the number of pointers, the index of a pointer, the ID of a pointer, the X and Y coordinates of a pointer, and the velocity of a touch event.
"""

groundtruth = """Feiwo is an advertisement library that is bundled with certain Android applications. It is an aggressive adware for Android mobile devices, which posts to its servers the victim's phone number, IMEI and list of installed applications. This is a typically unwanted SDK and should generally be removed from devices. Additionally, the adware implements several techniques to complexify its analysis. It is a malicious adware for Android devices that sends the victim’s phone number, IMEI, and list of installed apps to its servers. This is a common unwanted SDK that should be removed from devices. Furthermore, the adware employs several techniques to complicate its analysis."""


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

