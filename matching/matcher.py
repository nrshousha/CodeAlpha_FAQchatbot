from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from data.faqs import faqs
from preprocessing.cleaner import preprocess

cleaned_questions = [preprocess(faq["question"]) for faq in faqs]

# for i, q in enumerate(cleaned_questions):
#     print(i, q)

vectorizer= TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(cleaned_questions)

def get_best_answer(user_input):
    cleaned_input= preprocess(user_input)
    input_vectors = vectorizer.transform([cleaned_input])

    similarities = cosine_similarity(input_vectors, faq_vectors)
    best_index = similarities.argmax()
    best_score = similarities[0][best_index]

    # print("Cleaned input:", cleaned_input)
    # print("Best score:", best_score)
    if best_score< 0.2:
        return "Sorry, I didn't understand that. Could you rephrase?"

    return faqs[best_index]["answer"]
