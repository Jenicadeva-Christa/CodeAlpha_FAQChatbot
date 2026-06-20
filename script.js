/**
 * PolyBot - FAQ Chatbot Client-Side Controller
 * Manages message display, asynchronous API communications, and scroll states.
 * Pure Vanilla JavaScript.
 */

document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements - Using exact requested IDs
    const chatWindow = document.getElementById('chat-window');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const typingIndicator = document.getElementById('typing-indicator');

    // Auto-scroll to the bottom of the chat window
    function scrollToBottom() {
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    // Toggle visibility of the bouncing typing indicator
    function setTypingState(isTyping) {
        if (isTyping) {
            typingIndicator.classList.remove('hidden');
        } else {
            typingIndicator.classList.add('hidden');
        }
        scrollToBottom();
    }

    /**
     * Appends a message bubble into the chat window.
     * @param {string} text - Message text or HTML response.
     * @param {boolean} isUser - True if sent by the user, false if from the bot.
     */
    function appendMessage(text, isUser = false) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;

        let innerHTML = '';
        if (!isUser) {
            // Append 🤖 bot avatar
            innerHTML += '<div class="avatar">🤖</div>';
        }
        
        // Append bubble content
        innerHTML += `<div class="bubble">${text}</div>`;
        messageDiv.innerHTML = innerHTML;

        // Insert new message directly before the typing indicator element
        chatWindow.insertBefore(messageDiv, typingIndicator);
        
        // Smooth scroll to focus on the new message
        scrollToBottom();
    }

    /**
     * Sends the user's message to the Flask /chat endpoint.
     */
    async function sendMessage() {
        const message = userInput.value.trim();
        
        // Validation: empty input check
        if (!message) return;

        // Append user bubble and clear input
        appendMessage(message, true);
        userInput.value = '';

        // Show typing indicator
        setTypingState(true);

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: message })
            });

            if (!response.ok) {
                throw new Error('API server returned an error');
            }

            const result = await response.json();
            
            // Artificial tiny delay to make the typing indicator feel realistic and satisfying
            setTimeout(() => {
                setTypingState(false);
                appendMessage(result.response, false);
            }, 600);

        } catch (error) {
            console.error('Chat API Error:', error);
            
            setTimeout(() => {
                setTypingState(false);
                appendMessage("I'm sorry, I'm having trouble connecting to my NLP engine right now. Please try again in a few moments.", false);
            }, 600);
        }
    }

    // Click Listener
    sendBtn.addEventListener('click', sendMessage);

    // Enter Keypress Listener
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            e.preventDefault();
            sendMessage();
        }
    });

    // Auto-focus input on page load
    userInput.focus();

    // Trigger Initial Bot Welcome Message after page load animation completes
    setTimeout(() => {
        const welcomeText = "Hello! 🤖 I am **PolyBot**, your personal University FAQ Assistant. " +
            "You can ask me questions about admission forms, registration fees, hostel services, academic exams, library limits, or campus placements. " +
            "How can I assist you today?";
        appendMessage(welcomeText, false);
    }, 400);
});
