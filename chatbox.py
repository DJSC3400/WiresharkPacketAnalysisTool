
import tkinter as tk
import customtkinter as ctk

# custom tkinter colors
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# process message aswell as strip for special syntax aswell as display.
def on_send(event=None):
    user_input = entry.get().strip()
    if not user_input:
        return  # Ignore empty messages

    # Clear the entry box
    entry.delete(0, tk.END)

    # Enable chatbox to insert message, then disable it again to prevent typing
    chatbox.config(state=tk.NORMAL)
    
    # Display the user input in the chatbox
    chatbox.insert(tk.END, f"You: {user_input}\n")
    chatbox.yview(tk.END)

    # Check for $message$ syntax and extract the content
    if user_input.startswith("$") and user_input.endswith("$"):
        protocol = user_input[1:-1]  # Extract the content inside $
        chatbox.insert(tk.END, f"Stripping working: Extracted Protocol - {protocol}\n")
    else:
        # Default response if no filter syntax
        chatbox.insert(tk.END, "LLM Response Here\n")

    chatbox.yview(tk.END)

    # Disable chatbox again to prevent user typing
    chatbox.config(state=tk.DISABLED)

# set up main chatbox window
root = ctk.CTk()
root.title("Chatbox")
root.geometry("500x500")

# display area state controller 
chatbox_frame = ctk.CTkFrame(root)
chatbox_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

chatbox = tk.Text(chatbox_frame, height=20, width=50, state=tk.DISABLED, wrap=tk.WORD, bg="#2e2e2e", fg="white", font=("Helvetica", 12))
chatbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Scrollbar for chatbox - AI MADE
scrollbar = tk.Scrollbar(chatbox_frame, command=chatbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chatbox.config(yscrollcommand=scrollbar.set)

# Input area - AI MADE
input_frame = ctk.CTkFrame(root)
input_frame.pack(pady=10, padx=10, fill=tk.X)

#allows for enter key to send msg
entry = ctk.CTkEntry(input_frame, width=400)
entry.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.X, expand=True)
entry.bind("<Return>", on_send)  # Bind Enter key to sending messages

send_button = ctk.CTkButton(input_frame, text="Send", command=on_send)
send_button.pack(side=tk.RIGHT, padx=10)

# Start the main event loop
root.mainloop()

