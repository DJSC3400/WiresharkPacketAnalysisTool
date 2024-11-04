
import subprocess
import pyshark
import os

def live_capture(interface='Wi-Fi'):
    # Initialize live capture on the specified interface
    capture = pyshark.LiveCapture(interface=interface)

    # Start capturing packets
    print("Starting live capture on interface:", interface)
    for packet in capture.sniff_continuously(packet_count=10):
        # Print packet summary (you can access more packet details if needed)
        print(packet)



def add_to_path(directory):
    # Check if directory already in PATH to avoid duplication
    current_path = os.environ.get("PATH", "")
    if directory not in current_path:
        try:
            # Run the command to add the directory to the system PATH
            subprocess.run(
                ["setx", "PATH", f"{current_path};{directory}"],
                check=True,
                shell=True
            )
            print(f"{directory} added to PATH.")
        except subprocess.CalledProcessError as e:
            print("Failed to add directory to PATH:", e)
    else:
        print(f"{directory} is already in the PATH.")


def applyDisplayFilter(filePath, displayFilter):
    
    try:
        result = subprocess.run(
            ["tshark", "-r", filePath, "-Y", displayFilter],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("An error occurred:", e)
        return None


# Example usage:
add_to_path(r"C:\Program Files\Wireshark")
output = applyDisplayFilter("C:/Users/cudoh/Desktop/testing.pcapng", "tcp")
print(output)

#live_capture()