# Program Capabilities:
#       - Abstract text from audio file
#       - Calculate program execution time

# Authors: Ala Chua, Jie Yao, Chris Wells, Brad Keiser
# Version: 0.1
# Last Modified: 09/7/23
import os
import sys
import whisper
import time

# start time used for comparing program processing duration
start_time = time.time()

# TODO: Help menu for command-line arguments
# -h, --help    -> display help menu
# -i, --input   -> specify input audio file
# -o, --output  -> specify output file name & directory
# OPTIONAL ADDITIONAL ARGUMENTS
# --language    -> specify language (input and/or output)
#                  (see whisper language capabilities)
# --model       -> set transcription model
#

# Using base whisper model
model = whisper.load_model("base")

# TODO: Catch errors
# Error check for file path argument
if len(sys.argv) <= 1:
    print("Insufficient arguments. Exiting program.")
    sys.exit(1)
# Error check file type (must be audio file)
if (sys.argv[1].split("."))[1] != "mp4":
    print("Invalid file type. Audio file must be *.mp4")
    sys.exit(1)

# Load the audio file
filepath = sys.argv[1]
if os.path.exists(filepath):
    print("Preparing to transcribe " + os.path.basename(filepath) + " audio to text...")
else:
    print(os.path.basename(filepath)+" not found.")
    sys.exit(1)

# Transcribe audio file
result = model.transcribe(filepath, fp16=False)
# Parse result for audio transcription
lines = result['text']
if len(lines) == 0:
    print("Error transcribing audio.")
    sys.exit(1)

# Write the transcription to a file using UTF-8 encoding
# TODO: change so output path can be specified, else default
output_path = os.getcwd()+"/text/"+os.path.basename(filepath).split(".")[0]+".txt"
print("Writing audio transcription to "+output_path+" ...")
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(lines)

# Print program execution time
print("Program execution time: %s seconds" % (time.time() - start_time))