log_messages = [
    "Error: Critical - System failure",
    "Warning: Low disk space",
    "Error: Minor - Network connectivity issue",
    "Error: Critical - No response from server",
    "Error: Minor - Low memory"
]

critical_errors = 0
minor_errors = 0

for message in log_messages:
    try:
        # Attempt to process the message
        if "Error: Critical" in message:
            critical_errors += 1
        elif "Error: Minor" in message:
            minor_errors += 1
    except Exception as e:
        # Handle potential exceptions, e.g., decoding error, etc.
        print(f"An error occurred while processing log messages: {e}")

print(f"Critical Errors: {critical_errors}")
print(f"Minor Errors: {minor_errors}")

