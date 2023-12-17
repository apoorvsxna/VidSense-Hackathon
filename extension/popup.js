const btn1 = document.getElementById("generateBtn");
const btn2 = document.getElementById("Summarize");
const inputQuestion = document.getElementById("question");

btn1.addEventListener("click", function() {
    btn1.disabled = true;
    btn1.innerHTML = "Getting Answer...";
    btn1.style.boxShadow = 'None';

    chrome.tabs.query({ currentWindow: true, active: true }, function(tabs) {
        var url = tabs[0].url;
        var question = inputQuestion.value;
        var xhr = new XMLHttpRequest();

        xhr.open("GET", "http://127.0.0.1:5000/answer?url=" + url + "&question=" + encodeURIComponent(question), true);

        xhr.onload = function() {
            var answer = xhr.responseText;
            const p = document.getElementById("output");
            p.innerHTML = "Answer: " + answer;
            btn1.disabled = false;
            btn1.innerHTML = "Answer";
            btn1.style.boxShadow = '5px 5px 5px rgba(0, 0, 0, 0.3)';
        };

        xhr.send();
    });
});

btn2.addEventListener("click", function() {
    btn2.disabled = true;
    btn2.innerHTML = "Getting Summary...";
    btn2.style.boxShadow = 'None';

    chrome.tabs.query({ currentWindow: true, active: true }, function(tabs) {
        var url = tabs[0].url;
        var xhr = new XMLHttpRequest();

        xhr.open("GET", "http://127.0.0.1:5000/summarize?url=" + url, true);

        xhr.onload = function() {
            var summary = xhr.responseText;
            const p = document.getElementById("output");
            p.innerHTML = "Summary: " + summary;
            btn2.disabled = false;
            btn2.innerHTML = "Summarize";btn2.style.boxShadow = '5px 5px 5px rgba(0, 0, 0, 0.3)';
        };

        xhr.send();
    });
});