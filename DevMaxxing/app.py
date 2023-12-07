from transformers import pipeline, DistilBertTokenizer, DistilBertForQuestionAnswering
from youtube_transcript_api import YouTubeTranscriptApi
import re

video_url = "https://www.youtube.com/watch?v=j3OqAN4ISOw"
question = "Where is the airport located?"
print("Video URL and question recieved.")


def extract_video_id(youtube_url):
    # Define a regular expression pattern to match YouTube video IDs
    pattern = re.compile(r'(?:https?://)?(?:www\.)?(?:youtube\.com/.*?\bv=|youtu\.be/)([^"&?/\s]{11})', re.IGNORECASE)
    
    # Search for the pattern in the given URL
    match = pattern.search(youtube_url)
    
    # If a match is found, return the video ID; otherwise, return None
    if match:
        return match.group(1)
    else:
        return None

video_id = extract_video_id(video_url)
print("Video id extracted: "+video_id)

# Get the transcript
transcript = YouTubeTranscriptApi.get_transcript(video_id)
print("Transcript fetched.")

# Concatenate the text from each entry
readable = ' '.join(entry['text'] for entry in transcript)

text = readable

# Specify the model and revision
model_name = "distilbert-base-cased-distilled-squad"
revision = "626af31"
print("Now processing...")

qa_pipeline = pipeline("question-answering", model=model_name, revision=revision)
result = qa_pipeline(question=question, context=text)

print("Answer:", result["answer"])
