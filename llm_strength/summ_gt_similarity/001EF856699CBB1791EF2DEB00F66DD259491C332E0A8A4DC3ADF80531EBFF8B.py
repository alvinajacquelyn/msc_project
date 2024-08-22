import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
# importing module
from pandas import *
import csv
# reading CSV file

x = "001EF856699CBB1791EF2DEB00F66DD259491C332E0A8A4DC3ADF80531EBFF8B"
summ = """
The provided text describes several Java classes and interfaces related to Android development, including `Loader`, `AsyncTaskLoader`, `LoadTask`, `AsyncTaskResult`, `BroadcastRecord`, `ContextCompat`, `ContextCompatFroyo`, `ContextCompatHoneycomb`, `ContextCompatJellybean`, `CursorLoader`, `FileProvider`, `PathStrategy`, and `SimplePathStrategy`. These classes and interfaces provide a way to access and manipulate data in Android applications, including loading data asynchronously in the background, canceling the load if it is no longer needed, and accessing external storage directories on Android devices. The code also defines several classes and interfaces related to media playback and audio management, including `TransportController`, `TransportMediatorCallback`, `TransportPerformer`, and `TransportStateListener`. These classes provide a way to control the playback of media content and handle audio focus changes. The code also defines several classes and interfaces related to printing and text direction, including `PrintHelper`, `PrintHelperKitkat`, and `AnyStrong`. These classes provide a way to print bitmaps and determine the text direction of a given character sequence. The code also provides compatibility layers for various Android classes, including `TrafficStats`, `ConnectivityManager`, `Environment`, and `Parcelable`. These classes provide a way to check whether the active network is metered or not, using different methods and classes depending on the Android version. The text describes several Java classes and their implementations, including:

* `TextDirectionHeuristicInternal`: a custom implementation of the `TextDirectionHeuristicImpl` class that determines the text direction based on the locale.
* `TextDirectionHeuristicLocale`: a subclass of `TextDirectionHeuristicImpl` that overrides the `defaultIsRtl()` method to return `true` if the default locale is set to a right-to-left language, and `false` otherwise.
* `ArrayIterator`: a custom iterator class that implements the `Iterator` interface and iterates over a collection of elements.
* `ArrayMap`: a custom implementation of the `Map` interface that extends the `SimpleArrayMap` class and provides additional methods and fields.
* `AtomicFile`: a Java class that provides a way to perform atomic file operations, allowing for either complete success or complete failure.
* `ContainerHelpers`: a Java class that contains several static methods for working with arrays, including idealIntArraySize, idealLongArraySize, idealByteArraySize, equal, and binarySearch.
* `buildShortClassTag`: a method that takes an object and a string builder as input and appends a string representation of the object's class name and its identity hash code to the string builder.

These classes and methods provide various functionality for working with arrays, maps, and other data structures in Java. The code provides compatibility for different versions of Android, allowing developers to write code that works across different versions. It defines several classes and interfaces, including `AccessibilityDelegateCompat`, `AccessibilityDelegateCompatIcs`, `AccessibilityDelegateCompatJellyBean`, `AccessibilityDelegateIcsImpl`, and `AccessibilityDelegateJellyBeanImpl`, which provide a bridge between the old and new versions of the `AccessibilityDelegate` class. The code also provides a base implementation for an action view in a menu item, as well as methods for handling key events, motion events, and view configuration. This code defines classes and interfaces for compatibility with different versions of Android. The main classes include ItemInfo, JbMr1ViewCompatImpl, KeyEventCompat, KeyEventCompatEclair, and KeyEventCompatHoneycomb. These classes provide compatibility layers for the KeyEvent class and other features in Android. The interfaces defined in this code include KeyEventVersionImpl, which contains methods for dispatching key events, getting the key dispatcher state, tracking key events, and normalizing meta states. The code also defines several static fields and methods that are used to provide compatibility with different versions of Android.
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

