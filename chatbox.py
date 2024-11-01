import customtkinter as ctk
import tkinter as tk

# Function to handle sending a message
def on_send():
    # Display a placeholder response in the chatbox
    user_message = entry.get()
    if user_message.strip():  # Only proceed if there's input
        chatbox.insert(tk.END, f"You: {user_message}\n")
        chatbox.insert(tk.END, "LLM Response Here\n")
        chatbox.yview(tk.END)  # Scroll to the bottom
        entry.delete(0, tk.END)  # Clear the entry field

# Initialize CustomTkinter appearance and settings
ctk.set_appearance_mode("Dark")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

# Create the main window
root = ctk.CTk()
root.title("Chatbox")
root.geometry("500x500")

# Chat display (Scrollable Textbox)
chatbox_frame = ctk.CTkFrame(root)
chatbox_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

chatbox = tk.Text(chatbox_frame, height=20, width=50, state=tk.NORMAL, wrap=tk.WORD, bg="#2e2e2e", fg="white", font=("Helvetica", 12))
chatbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Scrollbar for the chatbox
scrollbar = tk.Scrollbar(chatbox_frame, command=chatbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chatbox.config(yscrollcommand=scrollbar.set)

# Input area
input_frame = ctk.CTkFrame(root)
input_frame.pack(pady=10, padx=10, fill=tk.X)

entry = ctk.CTkEntry(input_frame, width=400)
entry.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.X, expand=True)

send_button = ctk.CTkButton(input_frame, text="Send", command=on_send)
send_button.pack(side=tk.RIGHT, padx=10)

# Start the main loop
root.mainloop()
