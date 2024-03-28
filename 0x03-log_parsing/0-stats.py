#!/usr/bin/python3
""" A script that reads stdin line by line and computes metric. """


import sys
import signal


def signal_handler(sig, frame):
    """Signal handler function for handling SIGINT and SIGTERM signals.

    This function is called when the program receives a SIGINT
    (Ctrl+C) or SIGTERM signal.
    It prints the statistics and exits the program.

    Args:
        sig: The signal number.
        frame: The current stack frame at the time of the signal.
    """
    print_stats()
    sys.exit(0)


def print_stats():
    """Prints the computed statistics."""
    global total_size
    print("File size: {}".format(total_size))
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code] > 0:
            print("{}: {}".format(status_code, status_codes[status_code]))


# Global variables to store the total size and status code counts
total_size = 0
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0}

# Counter to track line count
line_count = 0

# Loop through each line from stdin
for line in sys.stdin:
    try:
        # Split the line by whitespace to extract status code and size
        parts = line.split()
        status_code = parts[-2]
        size = int(parts[-1])

        # Update status code count and total size
        if status_code in status_codes:
            status_codes[status_code] += 1
            total_size += size

        # Increment line count
        line_count += 1

        # Print statistics after every 10 lines
        if line_count == 10:
            print_stats()
            line_count = 0
    except Exception as e:
        pass

# Register signal handlers for SIGINT and SIGTERM
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# Print final statistics
print_stats()
