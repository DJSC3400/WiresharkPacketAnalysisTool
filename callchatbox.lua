-- Lua script to create a dropdown menu and run chatbox.py silently from Wireshark's Tools menu

-- Get the current directory path
--This assumes both files are in same folder
local current_dir = debug.getinfo(1).source:match("@(.*[/\\])")
local python_script = current_dir .. "chatbox.py"

-- Function to run the python file
local function run_chatbox()
    -- Run the Python script using PowerShell to hide the command window - AI Helped
    local command = string.format('powershell -windowstyle hidden -command "Start-Process python -ArgumentList \'%s\' -WindowStyle Hidden"', python_script)
    local result = os.execute(command)

    --Use for debugging, will need to open Lua Console in Wireshark beforehand to see print output.
    --[[if result then
        print("chatbox.py executed successfully")
    else
        print("Failed to execute chatbox.py")
    end
    --]]
end

-- Register the menu item in Wireshark's Tools menu
if gui_enabled() then
    register_menu("Tools/LlamaShark", run_chatbox, MENU_TOOLS_UNSORTED)
end
