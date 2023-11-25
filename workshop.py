import time
import random
import tkinter as tk
from gui import SlideShow


def generate_binary(length):
    return "".join(random.choice("01") for _ in range(length))


print("Welcome to LeetCode Mastery by Jesse Han :)\n\n")

time.sleep(3)

print("System hack initiated...")

time.sleep(2)

processes = [
    "Bypassing firewall...",
    "Accessing system...",
    "Retrieving system data...",
    "Overriding system control...",
]
for process in processes:
    print(process)
    line_amt = random.randint(5, 20)
    for _ in range(line_amt):
        print(generate_binary(40))
        time.sleep(0.15)
    print("-------------------------")
    time.sleep(1)

print("System hacked. Now controlling system.")
time.sleep(2)

print("https://shorturl.at/FHU28")
print("https://shorturl.at/wyNP6")
print("https://shorturl.at/otwRZ")

app = SlideShow()
app.attributes("-fullscreen", True)
app.mainloop()
