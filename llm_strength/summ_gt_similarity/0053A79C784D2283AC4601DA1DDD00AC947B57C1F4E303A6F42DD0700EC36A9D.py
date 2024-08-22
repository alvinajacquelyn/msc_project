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
summ = """
The provided text describes several Java classes and interfaces related to managing fragments, intents, and loaders in Android. These classes include `FragmentTransaction`, `InboxStyle`, `InstantiationException`, `IntentBuilder`, `IntentReader`, `LoaderCallbacks`, `LoaderInfo`, `LoaderManager`, and `LoaderManagerImpl`. These classes provide methods for managing the transaction of fragments, setting the big content title and summary text, creating an intent for sharing content, reading information from an Intent, creating, managing, and resetting a Loader object, and managing loaders. The classes also have static initializers that set the implementation of the NavUtilsImpl interface based on the Android version.

The text also describes several classes and interfaces related to notifications and fragment operations in Android. The `NotificationCompatImpl` interface has a single method `build` that takes a `Builder` object as an argument and returns a `Notification` object. The `NotificationCompatImplHoneycomb` and `NotificationCompatImplIceCreamSandwich` classes implement this interface and provide a way to build notifications using the `NotificationCompatHoneycomb` and `NotificationCompatIceCreamSandwich` classes.

The `OnBackStackChangedListener` interface has a single method `onBackStackChanged` that is called whenever the back stack changes. The `Op` class represents a fragment operation in the Android FragmentManager and has several fields, including "cmd", "enterAnim", "exitAnim", "fragment", "next", "popEnterAnim", "popExitAnim", "prev", and "removed". The `SavedState` class extends `View.BaseSavedState` and has a constructor that takes a `Bundle` object as a parameter, as well as a `writeToParcel` method that writes the `Bundle` object to a `Parcel` object.

The `ServiceCompat` class has a public static final integer field called `START_STICKY` with a value of 1 and a private constructor to prevent instantiation. This code also defines several classes and interfaces related to sharing content between apps, including the "ShareCompat" class, the "IntentBuilder" class, the "IntentReader" class, the "ShareCompatICS" class, the "ShareCompatImpl" interface, the "ShareCompatImplBase" class, the "ShareCompatImplICS" class, the "ShareCompatImplJB" class, the "ShareCompatJB" class, and the "SlideDrawable" class.

These classes and interfaces provide a way to perform various tasks in Android, such as loading data asynchronously, accessing external storage directories, and sharing files between apps. This text provides a summary of several Java classes and interfaces related to internationalization and localization in Android. The classes and interfaces are used to provide compatibility layers for the ICU (International Components for Unicode) library, which is used for handling Unicode characters and text. The classes and interfaces include Builder, BidiFormatter, TextDirectionAlgorithm, TextDirectionHeuristicCompat, ICUCompatImpl, ICUCompatImplBase, and ICUCompatImplIcs. The ICU library is used in Android to handle internationalization and localization, and the classes and interfaces provide default implementations of the addLikelySubtags and getScript methods.

The text describes several custom implementations of Java classes in Android, including a custom `Writer` class called `LogWriter` that writes logs to the Android logcat, a `LongSparseArray` class that implements a sparse array of long keys and values, and a `MapCollections` class that provides a set of methods for managing a map. The text also describes a `SimpleArrayMap` class that is a map data structure that uses an array to store key-value pairs, and a `SparseArrayCompat` class that implements a sparse array data structure. Additionally, the text describes a `TimeUtils` class that provides utility methods for formatting durations.

The text also describes several classes and interfaces related to accessibility in Android, including AccessibilityDelegateBridge, AccessibilityDelegateBridgeJellyBean, AccessibilityDelegateCompat, AccessibilityDelegateCompatIcs, AccessibilityDelegateCompatJellyBean, AccessibilityDelegateIcsImpl, AccessibilityDelegateJellyBeanImpl, and AccessibilityDelegateIcsImpl. These classes and interfaces provide a way to handle accessibility events and actions in Android, and provide a compatibility layer for accessing the AccessibilityDelegate class on different versions of Android.

Finally, the text describes a Java code snippet for an abstract class called ActionProvider, which provides a base implementation for an action provider in the Android framework. The class has several abstract methods that must be implemented by subclasses, such as onCreateActionView() and onPerformDefaultAction(). It also has several utility methods for managing the visibility of the action provider and its submenu.

Overall, the text provides a summary of several Java classes and interfaces related to managing fragments, intents, loaders, notifications, fragment operations, sharing content between apps, internationalization and localization, accessibility, and custom implementations in Android.
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

