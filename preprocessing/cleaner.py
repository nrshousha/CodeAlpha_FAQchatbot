import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
from data.faqs import faqs

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)

    tokens= [t for t in tokens if t.isalpha() and t not in stop_words]

    tokens= [lemmatizer.lemmatize(t) for t in tokens]

    return " ".join(tokens)

cleaned_faqs = [
    {
        "original": faq["question"],
        "cleaned":  preprocess(faq["question"]),
        "answer":   faq["answer"]
    }
    for faq in faqs
]