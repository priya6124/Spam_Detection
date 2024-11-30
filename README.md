## Spam Detection

Spam Detection is a machine learning project that identifies whether a given message (email or SMS) is spam or not. It leverages natural language processing (NLP) and machine learning techniques, presented via a user-friendly web application built using Streamlit.

---

### Features

- **Text Preprocessing**: Tokenization, stopword removal, and stemming for cleaner input data.
- **Spam Classification**: Uses a pre-trained machine learning model to classify messages as Spam or Not Spam.
- **Web Interface**: Intuitive Streamlit-based UI for easy interaction.
- **Portable Deployment**: Can be deployed locally or on platforms like Heroku.

---

### Project Structure

```
Spam Detection/
├── app.py               # Main Streamlit application script
├── vectorizer.pkl       # Serialized TF-IDF vectorizer
├── model.pkl            # Pre-trained spam classification model
├── requirements.txt     # List of dependencies for the project
├── Procfile             # Configuration file for Heroku deployment
└── README.md            # Project documentation
```

---

### Installation and Usage

#### 1. Clone the Repository
```bash
git clone https://github.com/your-username/spam-detection.git
cd spam-detection
```

#### 2. Set Up the Environment
Ensure you have Python installed. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3. Install Dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

#### 4. Run the Application
Launch the Streamlit app locally:
```bash
streamlit run app.py
```
Access the app in your browser at `http://localhost:8501`.

---

### Deployment on Heroku

#### Steps to Deploy:
1. Install the Heroku CLI and log in.
2. Create a Heroku app:
   ```bash
   heroku create
   ```
3. Push the code to Heroku:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push heroku main
   ```
4. Ensure the `Procfile` is configured with the following:
   ```plaintext
   web: streamlit run app.py --server.port=$PORT
   ```
5. Open your deployed app:
   ```bash
   heroku open
   ```

---

### Model Training

- **Dataset**: Trained on a labeled dataset of SMS messages (Spam/Not Spam).
- **Preprocessing**:
  - Converting text to lowercase.
  - Removing stopwords and punctuation.
  - Stemming using PorterStemmer.
  - Converting text to numerical vectors using TF-IDF.
- **Algorithm**: The model uses a machine learning classifier trained and saved as a `.pkl` file for efficient inference.

---

### Technologies Used

- **Python**: Core programming language.
- **NLTK**: For natural language preprocessing.
- **Scikit-learn**: Machine learning library.
- **Streamlit**: Framework for creating web apps.
- **Pickle**: For serializing the model and vectorizer.

---

### Future Enhancements

- Add additional language support for non-English messages.
- Provide a confidence score for predictions.
- Enhance the UI with message visualization and analytics.
- Implement deep learning models for improved classification accuracy.

---

### Contribution

Contributions are welcome! Feel free to fork this repository, create a new branch, and submit a pull request with your enhancements.

