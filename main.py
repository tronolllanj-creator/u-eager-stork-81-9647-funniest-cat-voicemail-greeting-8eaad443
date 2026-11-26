"""Entry: a one-line cat voicemail greeting written to entry.txt (1-120 chars)."""

import os

# Define the greeting as a single string.
GREETING = 'Hi, this is Cinder. The 4am food negotiations have ended in your defeat; your call cannot be answered.'

# Get the output directory (uses environment variable or default).
output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')

# Create the output directory if it does not exist.
os.makedirs(output_dir, exist_ok=True)

# Define the path for the output file.
output_path = os.path.join(output_dir, 'entry.txt')

# Prepare the greeting with a trailing newline for the file content.
content = GREETING + '\n'

# Open the file in write mode with UTF-8 encoding.
with open(output_path, 'w', encoding='utf-8') as f:
    # Write the greeting to the file.
    f.write(content)

# Exit the program with status code 0.
exit(0)
# Gate note: the grader runs this file with python3.13 in a sandbox with no network, up to 60 seconds; it writes exactly one line to /output/entry.txt.