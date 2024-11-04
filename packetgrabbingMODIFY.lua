-- define fields to capture
local ip_src = Field.new("ip.src")
local ip_dst = Field.new("ip.dst")
local tcp_srcport = Field.new("tcp.srcport")
local tcp_dstport = Field.new("tcp.dstport")
local protocol = Field.new("frame.protocols")

-- file path to save packet data
local packet_file_path = "C:\\Users\\School\\Documents\\PacketText\\captured_packets.txt"

-- table to store full packet data
local packet_data = {}
local packet_count = 0
-- modify if you want more, this is just for my testing
local max_packets = 1000

-- create a listener for all frames (packets)
local tap = Listener.new("frame")

-- function to capture packet details and store them
function tap.packet(pinfo, tvb)
    if packet_count >= max_packets then
        return  -- stop capturing after reaching the limit
    end

    local packet_info = {
        number = pinfo.number,
        time = tostring(pinfo.abs_ts),
        proto = tostring(protocol() or "N/A"),
        src_ip = tostring(ip_src() or "N/A"),
        dst_ip = tostring(ip_dst() or "N/A"),
        src_port = tostring(tcp_srcport() or "N/A"),
        dst_port = tostring(tcp_dstport() or "N/A"),
    }

    -- add packet info to the table and increase count
    table.insert(packet_data, packet_info)
    packet_count = packet_count + 1
end

-- function to save captured packets to a file
function save_packet_data()
    local file = io.open(packet_file_path, "w")
    if not file then
        print("error: unable to open file for writing.")
        return
    end

    for _, packet in ipairs(packet_data) do
        -- format the packet information into a string
        local line = string.format(
            -- more formatting
            "Packet %d:\nTime: %s\nProtocol: %s\nSource IP: %s\nDestination IP: %s\nSource Port: %s\nDestination Port: %s\n\n",
            packet.number, packet.time, packet.proto, packet.src_ip, packet.dst_ip, packet.src_port, packet.dst_port
        )
        -- write the formatted string to the file
        file:write(line)
    end

    file:close()
    print("captured packets saved to " .. packet_file_path)
end

-- function to clear packet data when the capture is reset
function tap.reset()
    packet_data = {}
    packet_count = 0
end

-- save the captured data when Wireshark stops
function tap.draw()
    save_packet_data()
end

print("packet capture initialized, capturing up to " .. max_packets .. " packets.")