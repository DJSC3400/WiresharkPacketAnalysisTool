import subprocess
import pyshark
import os

def live_capture(interface='Wi-Fi', number_of_packets=10, packet_filter=None):
    """
    Capture live packets on a specified network interface with an optional filter.
    
    Parameters:
    - interface (str): The name of the network interface to capture on.
    - number_of_packets (int): The number of packets to capture.
    - packet_filter (str): A display filter to apply (e.g., "tcp", "udp", "icmp").
    """
    # Initialize live capture on the specified interface with an optional filter
    capture = pyshark.LiveCapture(interface=interface, display_filter=packet_filter)
    
    # Start capturing packets
    print(f"Starting live capture on interface: {interface} for {number_of_packets} packets.")
    if packet_filter:
        print(f"Applying filter: {packet_filter}")
        
    packet_count = 1  # Start packet numbering at 1
    
    for packet in capture.sniff_continuously():
        # Attempt to print a basic summary using available layers
        try:
            protocol = packet.highest_layer  # Protocol layer (e.g., TCP, UDP)
            src_ip = packet.ip.src if 'IP' in packet else 'N/A'
            dst_ip = packet.ip.dst if 'IP' in packet else 'N/A'
            print(f"Packet #{packet_count}: {protocol} | Source: {src_ip} -> Destination: {dst_ip}")
        
        except AttributeError as e:
            print(f"Packet #{packet_count}: Unable to retrieve packet summary - {e}")
        
        packet_count += 1
        if packet_count > number_of_packets:
            print("Capture complete.")
            break


# Start live capture with a specified number of packets and a filter
live_capture(number_of_packets=20, packet_filter="http")  # Adjust number_of_packets and filter as needed
