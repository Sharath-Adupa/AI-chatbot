import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Sample training data
training_data = [
    ("Hi, how can I help you?", "greeting"),
    ("What’s your name?", "name"),
    ("Bye", "goodbye"),
    ("How’s the weather?", "weather"),
]

# Separate features (X) and labels (y)
X_train = [lemmatizer.lemmatize(nltk.word_tokenize(sentence.lower())) for sentence, label in training_data]
y_train = [label for _, label in training_data]

# Vectorize the input
vectorizer = CountVectorizer(tokenizer=lambda txt: txt, lowercase=False)
X_vectorized = vectorizer.fit_transform(X_train)

# Train the Naive Bayes model
model = MultinomialNB()
model.fit(X_vectorized, y_train)

# Chatbot response function
def chatbot_response(user_input):
    tokens = lemmatizer.lemmatize(nltk.word_tokenize(user_input.lower()))
    X_test = vectorizer.transform([tokens])
    prediction = model.predict(X_test)
    return prediction[0]

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
