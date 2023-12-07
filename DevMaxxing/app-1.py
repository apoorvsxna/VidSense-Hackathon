from flask import Flask, request
from transformers import pipeline, DistilBertTokenizer, DistilBertForQuestionAnswering
from youtube_transcript_api import YouTubeTranscriptApi
import re

app = Flask(__name__)

@app.route('/summary', methods=['GET'])
def summarize():
    video_url = request.args.get('url')
    question = request.args.get('question')

    if not video_url or not question:
        return "Invalid request. Both 'url' and 'question' parameters are required.", 400

    video_id = extract_video_id(video_url)
    if not video_id:
        return "Invalid YouTube URL.", 400

    # Get the transcript
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    # Concatenate the text from each entry
    text = ' '.join(entry['text'] for entry in transcript)

    # Specify the model and revision
    model_name = "distilbert-base-cased-distilled-squad"
    revision = "626af31"

    qa_pipeline = pipeline("question-answering", model=model_name, revision=revision)
    result = qa_pipeline(question=question, context=text)

    return "Answer: " + result["answer"]

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

if __name__ == '__main__':
    app.run(debug=True)
