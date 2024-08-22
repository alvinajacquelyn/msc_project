import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
# importing module
from pandas import *
import csv
# reading CSV file

x = "0035A5643659FA79FE081675C43476E8BCDD4634E2AB262D152E4FF7A3331BA5"
summ = """
This code defines several classes and interfaces related to Android development, including `AccessibilityServiceInfoCompatIcs`, `AccessibilityServiceInfoIcsImpl`, `AccessibilityServiceInfoVersionImpl`, `Action`, `ActivityCompat`, `ActivityCompatHoneycomb`, `BackStackEntry`, `BackStackState`, `BigPictureStyle`, `BigTextStyle`, `Builder`, `DialogFragment`, `Fragment`, `FragmentManager`, `DialogInterface.OnCancelListener`, and `DialogInterface.OnDismissListener`. These classes and interfaces provide methods for creating and managing notifications, dialogs, and fragments in an Android app. The code also defines a private constructor for the `UnusedStub` class, which is used to prevent the class from being instantiated.

The code defines several utility classes for creating notifications on specific versions of Android, such as `NotificationCompatHoneycomb` and `NotificationCompatIceCreamSandwich`. These classes provide additional methods and functionality for building notifications on different versions of Android.

The code also defines an interface named `OnBackStackChangedListener` with a single method named `onBackStackChanged`. This method is called whenever the back stack changes, indicating that the user has navigated to a new fragment or activity.

The code defines a class called "Op" that represents a fragment operation in the Android FragmentManager. It has several fields, including "cmd", "enterAnim", "exitAnim", "fragment", "next", "popEnterAnim", "popExitAnim", "prev", and "removed", which are used to store information about the operation.

The code defines a class called SavedState that implements the Parcelable interface. It has a final Bundle field called mState, and two constructors: one that takes a Bundle as a parameter and another that takes a Parcel and a ClassLoader as parameters. The class also has a writeToParcel method that writes the mState field to a Parcel, and a describeContents method that returns 0.

The code defines a class called ServiceCompat, which has a public static final integer field called START_STICKY with a value of 1. The class also has a private constructor to prevent instantiation.

The code defines a class called "ShareCompat" that provides a way to share content between apps. It also defines an inner class called "IntentBuilder" that is used to build an intent to share content. The class also defines an inner class called "IntentReader" that is used to read the intent that was used to share content.

The code defines a class called ShareCompatICS that provides a method to configure a menu item to share an intent. The method takes an item, an activity, and an intent as parameters and sets the action provider of the item to a new ShareActionProvider instance. The ShareActionProvider instance is configured with the share history file name and the share intent.

The code defines an interface called `ShareCompatImpl` that has two methods: `configureMenuItem` and `escapeHtml`. The `configureMenuItem` method takes a `MenuItem` and an `IntentBuilder` as input and configures the menu item to share the content of the intent. The `escapeHtml` method takes a `CharSequence` and returns a string with any HTML tags escaped.

This code defines a static class called `ShareCompatImplICS` that extends `ShareCompatImplBase`. The class has a constructor and overrides the `configureMenuItem` method. The `configureMenuItem` method is used to configure a menu item with a share intent. The method first calls the `configureMenuItem` method of the `ShareCompatICS` class, which is a utility class for sharing content on Android. Then, the method checks if the menu item should have a chooser intent added to it. If it should, the method sets the intent of the menu item to the chooser intent. The provided text describes several classes and interfaces in Android, including TaskStackBuilderJellybean, AsyncTaskLoader, LoadTask, AsyncTaskResult, BroadcastRecord, ContextCompat, ContextCompatHoneycomb, ContextCompatJellybean, CursorLoader, ForceLoadContentObserver, IntentCompat, ActivityInfoCompat, DatabaseUtilsCompat, BaseTrafficStatsCompatImpl, ConnectivityManagerCompatImpl, TrafficStatsCompatImpl, ParcelableCompat, ParcelableCompatCreatorHoneycombMR2, ParcelableCompatCreatorHoneycombMR2Stub, TrafficStatsCompat, TrafficStatsCompatIcs, CompatCreator, ParcelableCompatCreatorCallbacks, Parcelable, LogWriter, LongSparseArray, LruCache, SparseArrayCompat, TimeUtils, and AccessibilityDelegateBridge. These classes and interfaces provide compatibility layers for several Android classes and interfaces, including TrafficStats, Parcelable, and AccessibilityDelegate. They also define utility classes for formatting durations, writing logs to the Android logcat, and handling accessibility events. This code defines several classes and interfaces for implementing accessibility features in Android, including compatibility with different versions of the Android API. The code provides compatibility layers for different versions of the Android operating system, including Jelly Bean, Honeycomb, and earlier versions. It also defines custom classes and interfaces for customizing various Android features, such as the PagerTitleStrip class and the OnPageChangeListener interface. The code provides methods for checking and setting the over scroll mode, important for accessibility, and transient state of a view, as well as methods for invalidating and posting actions to be run on the next animation frame. Additionally, the code provides a way to access the getScaledPagingTouchSlop() method of the ViewConfiguration class in a backwards compatible way using the ViewConfigurationCompat class. This code provides compatibility layers for various Android components, including `ViewGroup` and `AccessibilityEvent` classes. It allows developers to use these classes on different versions of the platform, including Android 4.0 and later. The code defines static methods for interacting with the accessibility manager API, including methods for adding and removing accessibility state change listeners, getting a list of enabled and installed accessibility services, and checking if touch exploration is enabled. It also provides compatibility layers for accessing and modifying accessibility information in Android, including classes and interfaces related to accessibility. The main classes are `AccessibilityNodeInfoIcsImpl`, `AccessibilityNodeProviderCompat`, and `AccessibilityRecordCompat`, which provide compatibility layers for the `AccessibilityNodeInfoCompatIcs`, `AccessibilityNodeProvider`, and `AccessibilityRecord` classes introduced in Android Jelly Bean (API level 16). The code is designed to work on Android versions 4.0 and later. The code defines an interface called SearchViewCompatImpl, which contains three methods for creating and setting a listener for a search view. The interface also includes a static class called SearchViewCompatStubImpl that implements the SearchViewCompatImpl interface and provides the same functionality.
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

