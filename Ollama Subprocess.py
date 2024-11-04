import subprocess

def chat_with_ollama():
    # Initial command to run the model
    command = ["ollama", "run", "llama3.2"]

    # Start the process
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    print("Type 'exit' to end the chat.")
    
    while True:
        # Get user input
        user_input = input("You: ")

        # Break the loop if the user types 'exit'
        if user_input.lower() == "exit":
            print("Ending the chat.")
            process.terminate()
            break

        # Send input to the model
        process.stdin.write(user_input + "\n")
        process.stdin.flush()

        # Read the model's response
        response = process.stdout.readline().strip()
        print("Llama3.2:", response)

# Run the chat function
chat_with_ollama()