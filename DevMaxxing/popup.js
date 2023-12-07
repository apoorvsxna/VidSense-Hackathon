const btn = document.getElementById("generateAnswer");

btn.addEventListener("click", function() {
    const urlInput = document.getElementById("urlInput");
    const url = urlInput.value;

    if (url.trim() === "") {
        alert("Please enter a valid YouTube URL");
        return;
    }

    const questionInput = document.getElementById("questionInput");
    const question = questionInput.value;

    if (question.trim() === "") {
        alert("Please enter a question");
        return;
    }

    btn.disabled = true;
    btn.innerHTML = "Generating Answer...";

    // Assuming your Python server is running on http://127.0.0.1:5000
    const serverUrl = "http://127.0.0.1:5000/summary?url=" + encodeURIComponent(url) + "&question=" + encodeURIComponent(question);

    // Send a GET request to the server
    fetch(serverUrl)
        .then(response => response.text())
        .then(text => {
            const output = document.getElementById("output");
            output.innerHTML = text;
            btn.disabled = false;
            btn.innerHTML = "Generate Answer";
        })
        .catch(error => {
            console.error("Error fetching data from server:", error);
            alert("Error fetching data from server");
            btn.disabled = false;
            btn.innerHTML = "Generate Answer";
        });
});
