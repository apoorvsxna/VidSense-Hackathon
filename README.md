_{under development}_**

# Installation-

As this is under development (and not uploaded on the Chrome web store/Edge add-ons yet), you must sideload the extension to your browser. As of now, the extension has been tested on Edge but it should work on all Chromium-based browsers (i.e. Chrome, Edge, Brave and so on.)

To sideload, first, download the entire code as a zip and extract it. Next, go to the "Manage Extensions" page, and enable developer options. Now, click on "Load unpacked" and select the "extension" folder from the code you just extracted. The extension should now show up in the list of extensions and is ready to use.


# Usage-

1. Open the YouTube video based on which you would like to ask a question.
2. Open the extension.
3. Type in a question and click on "Generate Answer".
4. The answer would now be displayed in the answer text box.


# Working-

1. When the question is entered in the extension input box, it is sent to an API endpoint of the backend python server via an http request along with the URL of the current tab.
2. The video id is extracted from the URL, which is then used to fetch the transcript of the video in the current tab by using the _youtube-transcript-api_
3. Once the transcript is fetched, it is provided to the language model, which has been finetuned, and is run locally. [This](https://huggingface.co/bert-large-uncased-whole-word-masking-finetuned-squad) is the language model in use. (It is a fine-tuned variant of the BERT language model).
4. The transcript (after processing to convert it into a string) and the question are passed as parameters to the "question-answering" pipeline of the language model.
5. Once processing is complete, the answer generated is returned and displayed in the output box of the extension popup.


# The extension in action-

![WhatsApp Image 2023-12-09 at 05 22 17_e41b21b9](https://github.com/apoorvsxna/VidSense/assets/112375644/2a7fc91f-83de-4f7f-977f-c72b9972f5bb)

![WhatsApp Image 2023-12-09 at 05 18 54_dc53eff5](https://github.com/apoorvsxna/VidSense/assets/112375644/cc1c32bd-9856-4a9a-9bd4-ff5f961287d5)

![WhatsApp Image 2023-12-09 at 05 18 54_d8e64f9f](https://github.com/apoorvsxna/VidSense/assets/112375644/0792a0f7-ff06-4fb2-b06c-6fbed8221790)

![WhatsApp Image 2023-12-09 at 05 22 17_1061e3a6](https://github.com/apoorvsxna/VidSense/assets/112375644/116655b6-d302-43ba-b5af-7de631510dfd)


# Planned features-

- An additional option to generate the summary of the entire transcript.
- A feature to provide the timestamp at which the answer is found.


# Possible enhancements-

- Better language model integration. (For example:- OpenAI models such as gpt-3.5-turbo or text-davinci-003).
- Server hosting for deployment. (Perhaps via Firebase)
