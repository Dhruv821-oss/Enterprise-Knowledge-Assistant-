
console.log("✅ app.js loaded");
const chatWindow = document.getElementById("chat-window");
const input = document.getElementById("question");
const sendButton = document.getElementById("send");
const welcome = document.getElementById("welcome");

/* ------------------------- */
/* Utility Functions */
/* ------------------------- */

function scrollToBottom() {
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

function hideWelcome() {
    if (welcome) {
        welcome.style.display = "none";
    }
}

function escapeHTML(text) {
    const div = document.createElement("div");
    div.innerText = text;
    return div.innerHTML;
}

/* ------------------------- */
/* Message Rendering */
/* ------------------------- */

function addUserMessage(message) {

    hideWelcome();

    chatWindow.insertAdjacentHTML(
        "beforeend",
        `
        <div class="message user">
            <strong>You</strong>
            <p>${escapeHTML(message)}</p>
        </div>
        `
    );

    scrollToBottom();
}

function showTyping() {

    chatWindow.insertAdjacentHTML(
        "beforeend",
        `
        <div class="message bot" id="typing">

            <div class="typing">
                <span></span>
                <span></span>
                <span></span>
            </div>

        </div>
        `
    );

    scrollToBottom();
}

function removeTyping() {

    const typing = document.getElementById("typing");

    if (typing) {
        typing.remove();
    }
}

/* ------------------------- */
/* Confidence Badge */
/* ------------------------- */

function getConfidenceBadge(confidence) {

    let css = "low";
    let icon = "🔴";
    let label = "Low";

    if (confidence >= 0.85) {
        css = "high";
        icon = "🟢";
        label = "High";
    }
    else if (confidence >= 0.60) {
        css = "medium";
        icon = "🟡";
        label = "Medium";
    }

    return `
        <span class="badge ${css}">
            ${icon} ${label} Confidence (${Math.round(confidence * 100)}%)
        </span>
    `;
}

/* ------------------------- */
/* Sources */
/* ------------------------- */

function renderSources(sources = []) {

    if (!sources.length) return "";

    let html = `
        <div class="sources">

            <strong>Sources</strong>
    `;

    sources.forEach(source => {

        html += `
            <div class="source-card">

                📄 ${source.document}

                <br>

                Page ${source.page}

            </div>
        `;

    });

    html += "</div>";

    return html;
}

/* ------------------------- */
/* Assistant Message */
/* ------------------------- */

function addAssistantMessage(answer, confidence, sources) {

    removeTyping();

    chatWindow.insertAdjacentHTML(
        "beforeend",
        `
        <div class="message bot">

            <strong>Enterprise AI</strong>

            <p>${answer}</p>

            ${getConfidenceBadge(confidence)}

            ${renderSources(sources)}

        </div>
        `
    );

    scrollToBottom();
}

/* ------------------------- */
/* Error */
/* ------------------------- */

function showError(message) {

    removeTyping();

    chatWindow.insertAdjacentHTML(
        "beforeend",
        `
        <div class="message bot">

            <strong>Error</strong>

            <p>${message}</p>

        </div>
        `
    );

    scrollToBottom();
}

/* ------------------------- */
/* Flask API */
/* ------------------------- */

async function askAssistant(question) {

    try {

        const response = await fetch("/ask", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question
            })

        });

        const data = await response.json();

        if (!response.ok) {

            throw new Error(
                data.error || "Server Error"
            );

        }

        addAssistantMessage(
            data.answer,
            data.confidence ?? 0.8,
            data.sources ?? []
        );

    }

    catch (error) {

        showError(error.message);

    }

    finally {

        sendButton.disabled = false;

        input.focus();

    }

}

/* ------------------------- */
/* Send Question */
/* ------------------------- */

function sendQuestion() {

    const question = input.value.trim();

    if (!question) {

        input.focus();

        return;

    }

    sendButton.disabled = true;

    addUserMessage(question);

    input.value = "";

    showTyping();

    askAssistant(question);

}

/* ------------------------- */
/* Events */
/* ------------------------- */

sendButton.addEventListener("click", sendQuestion);

input.addEventListener("keydown", (event) => {

    if (event.key === "Enter") {

        event.preventDefault();

        sendQuestion();

    }

});
/* ------------------------- */
/* PDF Upload */
/* ------------------------- */

const uploadBtn = document.getElementById("uploadBtn");
const pdfInput = document.getElementById("pdfInput");

uploadBtn.addEventListener("click", () => {
    pdfInput.click();
});

pdfInput.addEventListener("change", async (event) => {

    const file = event.target.files[0];

    if (!file) return;

    if (!file.name.endsWith(".pdf")) {
        alert("Please select a PDF file.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    uploadBtn.disabled = true;
    uploadBtn.innerHTML = "⏳ Uploading...";

    try {

        const response = await fetch("/upload", {
            method: "POST",
            body: formData
        });

        const result = await response.json();

        if (response.ok) {

            alert(result.message);

        } else {

            alert(result.error);

        }

    } catch (err) {

        console.error(err);
        alert("Upload failed.");

    } finally {

        uploadBtn.disabled = false;
        uploadBtn.innerHTML = "📄 Upload PDF";

    }

});
async function loadDocuments() {

    const response = await fetch("/documents");

    const docs = await response.json();

    const list = document.querySelector(".documents ul");

    list.innerHTML = "";

    docs.forEach(doc => {

        list.innerHTML += `
            <li>📄 ${doc}</li>
        `;

    });

}
loadDocuments();
/* ------------------------- */
/* Theme Toggle */
/* ------------------------- */

const themeBtn = document.getElementById("themeBtn");

const savedTheme = localStorage.getItem("theme");

if (savedTheme === "light") {

    document.body.classList.add("light");

    themeBtn.textContent = "☀️ Light";

}

themeBtn.addEventListener("click", () => {

    document.body.classList.toggle("light");

    if (document.body.classList.contains("light")) {

        localStorage.setItem("theme", "light");

        themeBtn.textContent = "☀️ Light";

    } else {

        localStorage.setItem("theme", "dark");

        themeBtn.textContent = "🌙 Dark";

    }

});
/* ------------------------- */
/* Clear Chat */
/* ------------------------- */

const clearChatBtn = document.getElementById("clearChatBtn");

clearChatBtn.addEventListener("click", () => {

    if (!confirm("Clear all chat messages?")) {
        return;
    }

    chatWindow.innerHTML = `
        <div class="welcome" id="welcome">

            <h1>👋 Welcome</h1>

            <p>
                Upload your documents and start chatting with your AI assistant.
            </p>

        </div>
    `;

    input.focus();

});