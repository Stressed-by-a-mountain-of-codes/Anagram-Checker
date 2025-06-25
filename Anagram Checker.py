import tkinter as tk
from tkinter import messagebox
import pyttsx3
import re

engine = pyttsx3.init()
current_result = ""

def speak(text):
    engine.say(text)
    engine.runAndWait()

def normalize(text):
    cleaned = re.sub(r'[^a-z]', '', text.lower())
    return ''.join(sorted(cleaned))

def check_anagram(event=None):
    global current_result
    word1 = entry1.get()
    word2 = entry2.get()

    if not word1.strip() or not word2.strip():
        messagebox.showerror("Input Error", "Please enter both fields.")
        return

    norm1 = normalize(word1)
    norm2 = normalize(word2)

    sorted_label.config(text=f"Sorted A: {norm1}\nSorted B: {norm2}")

    if norm1 == norm2:
        result = "✅ Anagram: Both inputs are anagrams!"
        color = "green"
        voice = "Yes, they are anagrams."
    else:
        result = "❌ Not an Anagram: They are different."
        color = "red"
        voice = "No, they are not anagrams."

    result_label.config(text=result, fg=color)
    current_result = result
    speak(voice)
    root.after(3000, reset)

def swap_and_recheck():
    entry1_val = entry1.get()
    entry2_val = entry2.get()
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry1.insert(0, entry2_val)
    entry2.insert(0, entry1_val)
    check_anagram()

def reset():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="")
    sorted_label.config(text="")

root = tk.Tk()
root.title("Anagram Checker - Transparent & Swappable")
root.geometry("500x320")
root.resizable(False, False)

tk.Label(root, text="Enter first word or phrase:", font=("Arial", 12)).pack(pady=5)
entry1 = tk.Entry(root, font=("Arial", 14), justify="center", width=42)
entry1.pack(pady=5)

tk.Label(root, text="Enter second word or phrase:", font=("Arial", 12)).pack(pady=5)
entry2 = tk.Entry(root, font=("Arial", 14), justify="center", width=42)
entry2.pack(pady=5)
entry2.bind("<Return>", check_anagram)

tk.Button(root, text="Check Anagram", font=("Arial", 12), command=check_anagram).pack(pady=8)
tk.Button(root, text="🔄 Swap & Re-check", font=("Arial", 11), command=swap_and_recheck).pack(pady=2)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=5)

sorted_label = tk.Label(root, text="", font=("Courier", 11), justify="center", fg="darkblue")
sorted_label.pack()

entry1.focus()
root.mainloop()
