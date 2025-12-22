from transformers.pipelines import pipeline #pipeline is a function that takes a model and a task and returns a model that can be used to perform the task

summarizer = pipeline("summarization") #summarizer is a function that takes a text and returns a summary of the text

sample_text = """
192.168.1.50 failed login 50 times.
10.0.0.8 failed login 3 times.
203.0.113.15 might be scanning SSH ports.
"""

#max_length is the maximum length of the summary
#do_sample is a boolean that determines if the summary should be sampled or not
summary = summarizer(sample_text, max_length=600, min_length=10, do_sample=False)

print("Summary: ", summary[0]['summary_text'])