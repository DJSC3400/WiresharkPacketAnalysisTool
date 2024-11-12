import pyshark
import json

def capture_packets_to_file(interface_name, output_file="captured_packets.json", packet_count=5):
    # Set up the capture on the specified interface
    capture = pyshark.LiveCapture(interface=interface_name)
    
    # Start capturing packets
    packets = []
    for packet in capture.sniff_continuously(packet_count=packet_count):
        packet_info = {"layers": {}}
        
        # Capture all layers' details
        for layer in packet.layers:
            layer_info = {}
            for field in layer.field_names:
                layer_info[field] = layer.get_field(field)
            
            # Add layer info to packet_info
            packet_info["layers"][layer.layer_name] = layer_info
        
        packets.append(packet_info)

    # Write captured packets to a JSON file
    with open(output_file, "w") as file:
        json.dump(packets, file, indent=4)
    
    print(f"Captured packet details saved to {output_file}")

# Example usage (interface name should match the user's selection in Wireshark)
interface_name = "Wi-Fi"  # Replace with your interface
capture_packets_to_file(interface_name)
