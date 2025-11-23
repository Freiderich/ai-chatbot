async function sendMessage() {
    const input = document.getElementById("userInput");
    const msg = input.value.trim();
    if (!msg) return;

    addMessage(msg, "user");
    input.value = "";

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: msg })
        });

        const data = await response.json();
        addMessage(data.reply, "bot");
    } catch (err) {
        addMessage("Error: Cannot reach server.", "bot");
        console.error(err);
    }
}

function addMessage(text, sender) {
    const div = document.createElement("div");
    div.className = "message " + sender;
    div.innerText = text;

    const messagesDiv = document.getElementById("messages");
    messagesDiv.appendChild(div);
    messagesDiv.scrollTop = messagesDiv.scrollHeight; // auto scroll
}

// Press Enter to send
document.getElementById("userInput").addEventListener("keydown", e => {
    if (e.key === "Enter") sendMessage();
});
