const btn = document.getElementById("summarise");
const inputQuestion = document.getElementById("question");

btn.addEventListener("click", function() {
    btn.disabled = true;
    btn.innerHTML = "Getting Answer...";

    chrome.tabs.query({ currentWindow: true, active: true }, function(tabs) {
        var url = tabs[0].url;
        var question = inputQuestion.value;
        var xhr = new XMLHttpRequest();

        xhr.open("GET", "http://127.0.0.1:5000/answer?url=" + url + "&question=" + encodeURIComponent(question), true);

        xhr.onload = function() {
            var answer = xhr.responseText;
            const p = document.getElementById("output");
            p.innerHTML = "Answer: " + answer;
            btn.disabled = false;
            btn.innerHTML = "Get Answer";
        };

        xhr.send();
    });
});
