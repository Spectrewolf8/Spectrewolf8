#!/usr/bin/env python3
import sys

def filter_message(message):
    """Return empty string if commit should be dropped, otherwise return the message."""
    if b'[Skip GitHub Action]' in message:
        # Return a placeholder to mark for deletion
        return b''
    return message

# Read the message from stdin
message = sys.stdin.buffer.read()
result = filter_message(message)
sys.stdout.buffer.write(result)
