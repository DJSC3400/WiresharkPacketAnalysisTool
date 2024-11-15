import pyshark
import os



def live_packet_capture(interface='Wi-Fi', packet_count=10, display_filter=None):
    # Start live capture on the specified interface
    capture = pyshark.LiveCapture(interface=interface, display_filter=display_filter)
    
    # Initialize an empty string to store packet information
    packet_info = ""

    # Capture a specific number of packets
    for packet in capture.sniff_continuously(packet_count=packet_count):
        try:
            # Build the packet info string with relevant details
            packet_info += f"Packet {packet.number}:\n"
            packet_info += f"Source IP: {packet.ip.src}\n"
            packet_info += f"Destination IP: {packet.ip.dst}\n"
            packet_info += f"Protocol: {packet.highest_layer}\n"
            
            # Check for TCP layer to include sequence and acknowledgment numbers
            if 'TCP' in packet:
                packet_info += f"Sequence Number: {packet.tcp.seq}\n"
                packet_info += f"Acknowledgment Number: {packet.tcp.ack}\n"
                
            packet_info += "----\n"
        
        except AttributeError:
            # Some packets may not have IP or TCP layers
            packet_info += "Packet does not contain IP or TCP layer.\n----\n"

    capture.close()
    
    # Return the complete string with all packet information
    return packet_info

#for dynamically saving the full capture in a .pcapng
def create_binary_files_and_directories(filePath):
    # Ensure the directory exists for filePath
    capture_dir = os.path.dirname(filePath)
    os.makedirs(capture_dir, exist_ok=True)
    
    # Create an empty pcapng file if it doesn't exist
    if not os.path.exists(filePath):
        with open(filePath, 'wb') as f:
            pass  # Creates an empty .pcapng file

#for live text files
def create_files_and_directories(save_path):
    # Ensure the directory exists for save_path
    output_dir = os.path.dirname(save_path)
    os.makedirs(output_dir, exist_ok=True)
    
    # Create an empty txt file if it doesn't exist
    if not os.path.exists(save_path):
        with open(save_path, 'w') as f:
            pass  # Creates an empty .txt file



def savePacketInfo(save_path, packet_info):
   
    if packet_info is None:
        print("No packet information was captured.")
        return
    else:
        print("Packet data captured")
        #print(packet_info)

    try:
        with open(save_path, "w") as f:
            f.write("".join(packet_info))
        print(f"Packet information saved to {save_path}")
    except IOError as e:
        print("An error occurred while writing to {save_path}:", e)


#this saves a bunch of text files based of off a live capture
def bigPacketCatcher(fileQuantity, packetCount, savePath):
    fileCounter = 0
    # Check if there is an extension and remove if exists
    if os.path.splitext(savePath)[1]:  
        savePath = os.path.splitext(savePath)[0]  
    
    while(fileCounter<=fileQuantity):
        unique_save_path = f"{savePath}{fileCounter}.txt"
        create_files_and_directories( unique_save_path )

        output = live_packet_capture(interface='Wi-Fi', packet_count=packetCount, display_filter="ip")
        savePacketInfo(unique_save_path,output)
        fileCounter += 1

bigPacketCatcher(4, 20, "./bigOutput.txt")