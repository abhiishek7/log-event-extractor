import os  # For creating folders and handling file paths
import re  # For searching patterns using regular expressions

# ✅ List of serial numbers to search login/logout for
serial_numbers = ["MXBCQ960YP", "CNBRP2P25F"]  # Add more serials here

# ✅ Directory where all the log files are present
log_dir = r"D:\TICODEANDFILES\CARDSWIPLOGIN_LOGOUT"

# ✅ All 8 log file names (with .log extension)
log_files = [
    "NEUF-DWS-Core.81.log",
    "NEUF-DWS-Core.83.log",
    "NEUF-DWS-jQuery-UI.main.49.log",
    "NEUF-DWS-jQuery-UI.main.50.log",
    "NEUF-HPOmniWeb-Bundle.main.229.log",
    "NEUF-HPOmniWeb-Bundle.main.224.log",
    "NEUF-Impl-Bundle.145.log",
    "NEUF-Impl-Bundle.149.log"
]

# ✅ Keywords to look for in each file
event_types = ["login", "logout"]

# ✅ Function to extract login/logout events
def extract_events(file_path, serial, file_label, event_type, serial_output_dir):
    """
    This function reads a file, searches for the specified event type (login/logout)
    related to the given serial number, and writes the matched lines to an output file.
    """

    # Regular expression pattern:
    # Matches lines like: 2023.08.14 12:30:45 ... <serial> ... login/logout
    pattern = re.compile(rf"(\d{{4}}\.\d{{2}}\.\d{{2}} \d{{2}}:\d{{2}}:\d{{2}}).*{re.escape(serial)}.*\b{event_type}\b", re.IGNORECASE)
    
    matched_lines = []  # List to store matched events
    count = 0  # Counter to track number of matched events

    # Open the log file in read mode
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            match = pattern.search(line)  # Search for login/logout with timestamp and serial
            if match:
                timestamp = match.group(1)  # Extract timestamp from the matched line
                matched_lines.append(f"{timestamp} - {serial} - {event_type.upper()}")
                count += 1  # Increase event count

    # Prepare output filename
    output_file = os.path.join(serial_output_dir, f"{event_type.lower()}_{file_label}.txt")

    # Write matched lines to the output file
    with open(output_file, 'w', encoding='utf-8') as out_file:
        out_file.write("\n".join(matched_lines))  # Write each matched line
        out_file.write(f"\n\nTotal {event_type.upper()} events: {count}")  # Add count at the end

    # Print status in terminal
    print(f"{event_type.upper()}s from {file_label} for {serial}: {count} events.")

# ✅ Main driver loop to process all serials and log files
for serial in serial_numbers:
    # Create folder for each serial inside the output directory
    serial_output_dir = os.path.join(log_dir, "output", serial)
    os.makedirs(serial_output_dir, exist_ok=True)

    for file_name in log_files:
        file_path = os.path.join(log_dir, file_name)  # Full path of the current log file
        file_label = file_name.replace(".log", "")  # Clean file name for output file label

        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue  # Skip to next file

        for event in event_types:
            # Call the function to extract the event from the current file
            extract_events(file_path, serial, file_label, event, serial_output_dir)
