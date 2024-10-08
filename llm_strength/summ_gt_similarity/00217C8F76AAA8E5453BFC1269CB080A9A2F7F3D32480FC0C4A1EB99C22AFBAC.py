import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
# importing module
from pandas import *
import csv
# reading CSV file

x = "00217C8F76AAA8E5453BFC1269CB080A9A2F7F3D32480FC0C4A1EB99C22AFBAC"
summ = """
The provided text describes a complex implementation of a Huffman decoder that can be used to decode a byte array and return the decoded values as a byte array or an int array. The code defines several classes and interfaces related to Android development, including `ActivityOptionsImplJB`, `BackStackEntry`, `BackStackState`, `BigPictureStyle`, and `ActionBarDrawerToggle`. These classes and interfaces provide additional methods for starting activities, managing the options menu, and creating `ActivityOptions` objects with custom animations, scaling up animations, and thumbnail scaling up animations. They also provide compatibility layers for accessing the various methods of the `AccessibilityServiceInfo` class, which were added in ICS and Jelly Bean MR2, respectively. The main classes are `ActivityOptionsImplJB`, `BackStackEntry`, and `BigPictureStyle`, which extend the `ActivityOptionsCompat` class and provide additional methods for setting the big picture and big large icon for a notification.

The text also describes several other classes and interfaces related to sharing content and loading data asynchronously, including `IntentBuilder`, `IntentReader`, `LoaderCallbacks`, and `LoaderInfo`. The code defines several classes and interfaces related to navigation, notifications, and sharing content between apps. The main classes are `LoaderManager`, `NavUtils`, and `NonConfigurationInstances`, which provide methods for managing loaders, navigating up the activity hierarchy, and storing non-configuration instance state.

The code defines several classes and interfaces for working with intents and drawables in Android, including `CursorLoader`, `FileProvider`, `ForceLoadContentObserver`, `IntentCompat`, `IntentCompatHoneycomb`, `WorkerRunnable`, `ActivityInfoCompat`, `DatabaseUtilsCompat`, `BaseDrawableImpl`, and `DrawableCompat`. These classes provide methods for creating intents, querying the file, getting the MIME type of the file, inserting, updating, deleting, and opening the file, as well as creating a content URI for a file and getting the file for a content URI. They also provide methods for starting activities, selecting activities, and restarting the activity task stack. The classes are designed to work with the Android Support Library and use the "Strategy Pattern" to provide compatibility with different versions of Android.

Overall, the code provides a set of classes and interfaces for working with intents and drawables in Android, as well as a compatibility layer for different versions of Android. The provided text describes several Java classes and interfaces related to Android development. These include `DisplayManagerCompat`, `TransportController`, `TransportMediatorCallback`, `TransportStateListener`, `ConnectivityManagerCompatImpl`, `ConnectivityManagerCompatJellyBean`, `GingerbreadConnectivityManagerCompatImpl`, `HoneycombMR2ConnectivityManagerCompatImpl`, `IcsTrafficStatsCompatImpl`, `JellyBeanConnectivityManagerCompatImpl`, `SocketTags`, `TrafficStatsCompat`, `TrafficStatsCompatIcs`, `TrafficStatsCompatImpl`, and `CompatCreator`. These classes and interfaces provide compatibility layers for different Android versions and provide methods for managing displays, controlling media playback, and checking the active network.
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

