// Auto-scroll chat to bottom
// Auto-scroll chat to bottom
let chatBox = document.getElementById("chatBox");
if (chatBox) {
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Focus input after sending
function sendMessage() {
    setTimeout(() => {
        document.getElementById("messageInput").value = "";
        document.getElementById("messageInput").focus();
    }, 100);
    return true;
}

// 🎤 Voice input
function startListening() {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = "en-US";

    recognition.start();  // 🔥 THIS LINE STARTS LISTENING

    recognition.onresult = function (event) {
        const transcript = event.results[0][0].transcript;
        document.getElementById("messageInput").value = transcript;
        document.querySelector("form").submit();
    };

    recognition.onerror = function (event) {
        alert("Voice recognition failed: " + event.error);
    };
}
