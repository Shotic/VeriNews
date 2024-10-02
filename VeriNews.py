import tkinter as tk
from tkinter import messagebox

# Sample database of fake news keywords (for simulation purposes)
fake_news_keywords = ["fake", "rumor", "hoax", "misleading"]

# Function to simulate fact-checking
def check_news():
    news_content = news_text.get("1.0", tk.END).strip()  # Get the text from the text box
    
    if any(keyword in news_content.lower() for keyword in fake_news_keywords):
        # If a fake news keyword is found, show an alert
        messagebox.showwarning("Alert", "This news might be FAKE. Please verify further.")
    else:
        # If no fake news keyword is found, show verification success
        messagebox.showinfo("Verification", "This news seems credible!")
        
# Creating the main window
root = tk.Tk()
root.title("VeriNews - Fake News Checker")
root.geometry("500x400")

# Title label
title_label = tk.Label(root, text="VeriNews: Check Your News", font=("Arial", 16))
title_label.pack(pady=10)

# Instructions
instructions = tk.Label(root, text="Enter the news content below for verification:")
instructions.pack(pady=5)

# Text box to input news content
news_text = tk.Text(root, height=10, width=50)
news_text.pack(pady=10)

# Button to check news
check_button = tk.Button(root, text="Check News", command=check_news, bg="blue", fg="white", font=("Arial", 12))
check_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
