try:
    from transformers import pipeline
except ImportError:
    pipeline = None
import json
from json_logger import log_suspicious_events
from collections import defaultdict

summarizer = (
    pipeline("summarization", model="facebook/bart-large-cnn") if pipeline else None
)  # summarizer is a function that takes a text and returns a summary of the text

def summarize_text(text_input):
    if summarizer is None:
        print("Summarization disabled: install 'transformers' and 'torch' to enable it.")
        return [{"summary_text": ""}]
    return summarizer(text_input, max_length=700, min_length=80, do_sample=False)
events = []

#summarize everything in the json file
def summarize_results(json_file):
    if events:
        text_input = "\n".join(events) #joins events into a single text block
        summary = summarize_text(text_input)
        print("\n=== AI Summary ===")
        print(summary[0]['summary_text'])
    else:
        print("No events to summarize")

def process_logs(logfile):
    with open(logfile, 'r') as file:
        for line in file:
            if "Failed password" in line:
                print(line)
