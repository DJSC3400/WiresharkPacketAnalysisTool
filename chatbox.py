import tkinter as tk
import customtkinter as ctk
import subprocess

<<<<<<< Updated upstream
# TEST CHANGE

# custom tkinter colors
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# process message aswell as strip for special syntax aswell as display.
=======
#call local ollama model
def get_ollama_response(prompt):
    try:
        # run Ollama with the prompt, suppressing stderr to avoid unwanted messages - AI added error catching
        result = subprocess.run(
            ['ollama', 'run', 'llama3.2'],
            input=prompt,
            stdout=subprocess.PIPE,  # capture standard output
            stderr=subprocess.DEVNULL,  # suppress standard error
            text=True
        )
        return result.stdout.strip()  # return the response text
    except subprocess.CalledProcessError as e:
        return f"Error calling Ollama: {e}"

# function to process and display messages in the chatbox
>>>>>>> Stashed changes
def on_send(event=None):
    user_input = entry.get().strip()
    if not user_input:
        return  # ignore empty messages

    # check for $ synax - will be used to apply filters to json data.
    if user_input.startswith('$') and user_input.endswith('$'):
        # strip $ and any surrounding whitespace
        stripped_message = user_input[1:-1].strip()

        # print message to console for debugging/testing if needed
        print(f"Processed Message: {stripped_message}")  # Debug output

        # update user_input to the stripped message
        user_input = stripped_message

    # clear the entry box
    entry.delete(0, tk.END)

<<<<<<< Updated upstream
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
=======
    # display the user input in the chatbox
    chatbox.config(state=tk.NORMAL)  # temporarily enable editing
    chatbox.insert(tk.END, f"You: {user_input}\n")
    chatbox.yview(tk.END)

    # get response from the Ollama model
    response = get_ollama_response(user_input)  # call the model with user input

    # display the response in the chatbox
    chatbox.insert(tk.END, f"LLM: {response}\n")
    chatbox.yview(tk.END)
    chatbox.config(state=tk.DISABLED)  # disable editing again

# set up CustomTkinter appearance and color theme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")
>>>>>>> Stashed changes

# set up main chatbox window
root = ctk.CTk()
root.title("Chatbox")
root.geometry("500x500")

<<<<<<< Updated upstream
# display area state controller 
=======
# chat display area (scrollable text box) - AI HELPED
>>>>>>> Stashed changes
chatbox_frame = ctk.CTkFrame(root)
chatbox_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

chatbox = tk.Text(chatbox_frame, height=20, width=50, state=tk.DISABLED, wrap=tk.WORD, bg="#2e2e2e", fg="white", font=("Helvetica", 12))
chatbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

<<<<<<< Updated upstream
# Scrollbar for chatbox - AI MADE
=======
# disable direct typing in chatbox - just looks better
chatbox.config(state=tk.DISABLED)

# scrollbar for chatbox
>>>>>>> Stashed changes
scrollbar = tk.Scrollbar(chatbox_frame, command=chatbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chatbox.config(yscrollcommand=scrollbar.set)

<<<<<<< Updated upstream
# Input area - AI MADE
input_frame = ctk.CTkFrame(root)
input_frame.pack(pady=10, padx=10, fill=tk.X)

#allows for enter key to send msg
=======
# input area
input_frame = ctk.CTkFrame(root)
input_frame.pack(pady=10, padx=10, fill=tk.X)

# added functionality for enter key to send messages
>>>>>>> Stashed changes
entry = ctk.CTkEntry(input_frame, width=400)
entry.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.X, expand=True)
entry.bind("<Return>", on_send) 

send_button = ctk.CTkButton(input_frame, text="Send", command=on_send)
send_button.pack(side=tk.RIGHT, padx=10)

<<<<<<< Updated upstream
# Start the main event loop
root.mainloop()
=======
# start the main event loop
root.mainloop()
>>>>>>> Stashed changes
