from flask import Flask, request
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline, AutoTokenizer, BartForConditionalGeneration

app = Flask(__name__)

@app.get('/answer')
def answer_api():
    url = request.args.get('url', '')
    question = request.args.get('question', '')
    video_id = url.split('=')[1]
    get_transcript(video_id)
    answer = get_answer(get_transcript(video_id), question)
    return answer, 200


@app.get('/summarize')
def summarize_api():
    url = request.args.get('url', '')
    video_id = url.split('=')[1]
    get_transcript(video_id)
    summary = get_summary(get_transcript(video_id))
    return summary, 200

def get_transcript(video_id):
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    transcript = ' '.join([d['text'] for d in transcript_list])
    return transcript

def get_summary(transcript):
    qa_pipeline = pipeline('summarization')
    summary = ''
    for i in range(0, (len(transcript)//1000)+1):
        text = qa_pipeline(transcript[i*1000:(i+1)*1000])[0]['summary_text']
        summary = summary + text + ' '
    return summary

def get_answer(transcript, question):
    qa_pipeline = pipeline('question-answering', model='bert-large-uncased-whole-word-masking-finetuned-squad')
    answer = qa_pipeline(question=question, context=transcript)
    return answer['answer']

if __name__ == '__main__':
    app.run(debug=True)
