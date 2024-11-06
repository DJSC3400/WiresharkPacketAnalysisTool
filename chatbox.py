import tkinter as tk
import customtkinter as ctk
import subprocess

# Function to get response from the Ollama model
import subprocess

import subprocess

#Get ollama in chatbox, AI wrote the error handling.
def get_ollama_response(prompt):
    try:
        # Run Ollama with the prompt, suppressing stderr to avoid unwanted messages
        result = subprocess.run(
            ['ollama', 'run', 'llama3.2'],
            input=prompt,
            stdout=subprocess.PIPE,  # Capture standard output
            stderr=subprocess.DEVNULL,  # Suppress standard error
            text=True
        )
        return result.stdout.strip()  # Return the response text without leading/trailing whitespace
    except subprocess.CalledProcessError as e:
        return f"Error calling Ollama: {e}"

# Function to process and display messages in the chatbox
def on_send(event=None):
    user_input = entry.get().strip()
    if not user_input:
        return  # Ignore empty messages

    # Clear the entry box
    entry.delete(0, tk.END)

    # Display the user input in the chatbox
    chatbox.config(state=tk.NORMAL)  # Temporarily enable editing
    chatbox.insert(tk.END, f"You: {user_input}\n")
    chatbox.yview(tk.END)

    # Get response from the Ollama model
    response = get_ollama_response(user_input)
    #print(response)  # Debugging: Print response to console, USE THIS IF MODEL NEVER RESPONDS OR SOME SORT OF ERROR

    # Display the response in the chatbox
    chatbox.insert(tk.END, f"LLM: {response}\n")
    chatbox.yview(tk.END)
    chatbox.config(state=tk.DISABLED)  # Disable editing again

# Set up CustomTkinter appearance and color theme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# Set up main chatbox window
root = ctk.CTk()
root.title("LlamaShark")
root.geometry("500x500")

# Chat display area (scrollable text box)
chatbox_frame = ctk.CTkFrame(root)
chatbox_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

chatbox = tk.Text(chatbox_frame, height=20, width=50, state=tk.NORMAL, wrap=tk.WORD, bg="#2e2e2e", fg="white", font=("Helvetica", 12))
chatbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Disable direct typing in chatbox
chatbox.config(state=tk.DISABLED)

# Scrollbar for chatbox
scrollbar = tk.Scrollbar(chatbox_frame, command=chatbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chatbox.config(yscrollcommand=scrollbar.set)

# Input area
input_frame = ctk.CTkFrame(root)
input_frame.pack(pady=10, padx=10, fill=tk.X)

entry = ctk.CTkEntry(input_frame, width=400)
entry.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.X, expand=True)
entry.bind("<Return>", on_send)  # Bind Enter key to sending messages

send_button = ctk.CTkButton(input_frame, text="Send", command=on_send)
send_button.pack(side=tk.RIGHT, padx=10)

# Start the main event loop
root.mainloop()
