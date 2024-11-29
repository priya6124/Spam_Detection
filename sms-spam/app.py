import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()
nltk.data.path = [r'C:\\Users\\HP\\AppData\\Roaming\\nltk_data']
# Download the punkt tokenizer resource
nltk.download('punkt')
# Optional: You can download the stopwords as well if not already downloaded
nltk.download('stopwords')

# Append the path to the nltk data folder
nltk.data.path.append(r'C:\\Users\\HP\\AppData\\Roaming\\nltk_data')


# Function to preprocess the text
def transform_text(text):
    text = text.lower()  # Convert to lowercase
    text = nltk.word_tokenize(text)  # Tokenize the text
    y = []

    # Remove non-alphanumeric words
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]  # Copy y to text
    y.clear()  # Clear y

    # Remove stopwords and punctuation
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]  # Copy y to text
    y.clear()  # Clear y

    # Apply stemming
    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


# Load the trained TF-IDF vectorizer and model
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Streamlit interface
st.title("Email/SMS Classifier")
input_message = st.text_area("Enter the message")
if st.button('Predict'):

    # Preprocess the input message
    transform_sms = transform_text(input_message)

    # Vectorize the transformed text using the loaded TF-IDF vectorizer
    vector_input = tfidf.transform([transform_sms])

    # Predict the result (Spam or Not Spam)
    result = model.predict(vector_input)[0]

    # Display the result
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
