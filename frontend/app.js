const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.lang = "en-US";

function startListening() {
  recognition.start();
}

recognition.onresult = async (event) => {
  const text = event.results[0][0].transcript;
  document.getElementById("userText").innerText = text;

  const response = await fetch(
    "https://voice-assistent-mnx8.onrender.com/command",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ text })
    }
  );

  const data = await response.json();
  document.getElementById("aiText").innerText = data.response;

  speak(data.response);

  if (data.url) {
    window.open(data.url, "_blank");
  }
};

function speak(text) {
  const speech = new SpeechSynthesisUtterance(text);
  speechSynthesis.speak(speech);
}
