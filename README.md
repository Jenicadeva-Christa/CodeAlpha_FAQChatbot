# PolyBot — FAQ Chatbot

PolyBot is an offline, NLP-powered college/university FAQ chatbot built using Flask, NLTK, and Scikit-Learn. It parses and maps user questions to a pre-defined database of over 400 FAQ entries using TF-IDF vectorization and cosine similarity matching, requiring zero external paid APIs.

## How It Works

1. **User Query Input**: The user asks a question in the chat interface.
2. **Text Preprocessing**: The backend uses **NLTK** to tokenize, lowercase, strip stopwords/punctuation, and lemmatize the input string (e.g. converting "admissions" and "admitted" to their root word "admit").
3. **TF-IDF & Vectorization**: Both the user question and the FAQ database questions are vectorized into a bag-of-words model using Scikit-Learn's `TfidfVectorizer`.
4. **Cosine Similarity Matching**: Cosine similarity is computed between the query vector and all FAQ question vectors.
5. **Threshold Filter**: If the highest similarity score is above `0.2`, the chatbot returns the corresponding answer. Otherwise, it falls back to a friendly message prompting the user to rephrase.

---

## Tech Stack

- **Backend**: Python (Flask)
- **Natural Language Processing (NLP)**:
  - **NLTK**: Tokenization, Stopwords filtering, and WordNet Lemmatization
  - **Scikit-Learn**: TF-IDF Vectorization and Cosine Similarity
  - **NumPy**: Matrix index math
- **Frontend**: Semantic HTML5, CSS3 (Glassmorphism & Flexbox), and Vanilla JS

---

## Folder Structure

```text
CodeAlpha_FAQChatbot/
├── app.py
├── faqs.py
├── chatbot.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
├── requirements.txt
└── README.md
```

---

## Features

- **High-Quality Custom Dataset**: Built-in repository of 412 Q&A pairs covering admissions, fees, hostel rooms, exams, library access, placements, and campus activities.
- **WhatsApp/ChatGPT-Style UI**: Modern dark navy theme featuring a glowing send button, animated typing indicator, and responsive bubble layouts.
- **Auto NLTK Downloader**: Automatically downloads NLTK packages (`punkt`, `stopwords`, `wordnet`, and `omw-1.4`) on the first run.
- **Enter-to-Send**: Supports standard keyboard triggers for quick sending.
- **Scroll Memory**: Auto-scrolls to the newest message bubbles.
- **No API Costs**: Executes entirely offline with no usage caps.

---

## Installation & Running

### Step 1: Navigate to the Project Folder
Open your terminal and enter the project folder:
```bash
cd CodeAlpha_FAQChatbot
```

### Step 2: Install Required Python Packages
Install the required packages listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### Step 3: Run the Flask Web Server
Start the local server:
```bash
python app.py
```
On first run, the terminal will log the NLTK downloads. Once completed, the server will launch.

### Step 4: Open in Web Browser
Open your browser and visit:
```text
http://127.0.0.1:5000/
```

---

## Author
**Jenicadeva Christa S** (CodeAlpha AI Intern)
