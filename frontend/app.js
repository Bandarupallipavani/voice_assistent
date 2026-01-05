const recognition = new webkitSpeechRecognition();
recognition.lang = "en-US";

function startListening() {
  recognition.start();
}

recognition.onresult = async (event) => {
  const text = event.results[0][0].transcript;

  const res = await fetch("/command", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text })
  });

  const data = await res.json();
  speak(data.response);

  if (data.url) {
    window.open(data.url, "_blank");
  }
};

function speak(text) {
  const speech = new SpeechSynthesisUtterance(text);
  speechSynthesis.speak(speech);
}
