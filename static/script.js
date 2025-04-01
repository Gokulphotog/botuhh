async function sendMessage() {
    let inputField = document.getElementById("user-input");
    let userMessage = inputField.value.trim();
    if (!userMessage) return;

    let chatBox = document.getElementById("chat-box");

    // Show user message
    let userMsgElement = document.createElement("div");
    userMsgElement.className = "user-message";
    userMsgElement.innerText = userMessage;
    chatBox.appendChild(userMsgElement);

    // Clear input field
    inputField.value = "";

    // Fetch bot response
    let response = await fetch(`/chat/${userMessage}`);
    let data = await response.json();
    let botReply = data.response;

    // Show bot message
    let botMsgElement = document.createElement("div");
    botMsgElement.className = "bot-message";
    botMsgElement.innerText = botReply;
    chatBox.appendChild(botMsgElement);

    // Speak the bot's response
    speak(botReply);

    // Scroll chat to bottom
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Text-to-Speech function
function speak(text) {
    let speech = new SpeechSynthesisUtterance(text);
    speech.lang = "en-US"; // Set language
    speech.rate = 1; // Normal speed
    speech.pitch = 1; // Normal pitch
    window.speechSynthesis.speak(speech);
}
