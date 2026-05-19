# 🎨 Art Studio FAQ Chatbot

A conversational chatbot that answers frequently asked questions about an art studio. Built with Python, NLTK, scikit-learn, and Streamlit.

## What it does

The chatbot takes a user's question, preprocesses it using NLP techniques, and matches it against a set of predefined FAQs using TF-IDF vectorization and cosine similarity. The most relevant answer is returned as a chat response.

## Project structure

```
art studio chatbot/
├── data/
│   ├── __init__.py
│   └── faqs.py              # FAQ questions and answers
├── matching/
│   ├── __init__.py
│   └── matcher.py           # TF-IDF vectorization and cosine similarity
├── preprocessing/
│   ├── cleaner.py           # Tokenization, stopword removal, lemmatization
│   └── download_nltk_data.py  # Run once to download NLTK resources
├── ui/
│   └── app.py               # Streamlit chat interface
├── main.py                  # Entry point for terminal testing
└── README.md
```

## Setup

### 1. Clone the repository and navigate to the project folder

```bash
cd "art studio chatbot"
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install nltk spacy scikit-learn streamlit
```

### 4. Download NLTK data (run once)

```bash
python3 preprocessing/download_nltk_data.py
```

### 5. Run the chatbot

```bash
python3 -m streamlit run ui/app.py
```

## How it works

1. **Data** — FAQs are stored as a list of question/answer dictionaries in `data/faqs.py`
2. **Preprocessing** — each question is lowercased, tokenized, stripped of stopwords and punctuation, and lemmatized
3. **Vectorization** — all cleaned FAQ questions are converted into a TF-IDF matrix at startup
4. **Matching** — the user's input is cleaned and vectorized, then compared against the FAQ matrix using cosine similarity
5. **Response** — the FAQ with the highest similarity score is returned, provided it exceeds a minimum threshold of 0.2

## Technologies used

- [NLTK](https://www.nltk.org/) — tokenization, stopword removal, lemmatization
- [scikit-learn](https://scikit-learn.org/) — TF-IDF vectorization and cosine similarity
- [Streamlit](https://streamlit.io/) — chat interface

## Notes

- If you encounter an SSL error when downloading NLTK data on macOS, run `python3 preprocessing/download_nltk_data.py` which bypasses the SSL issue for the one-time download
- Always run commands from the project root, not from inside a subfolder
- Use `python3 -m streamlit run ui/app.py` instead of `streamlit run` to ensure the correct Python environment is used
