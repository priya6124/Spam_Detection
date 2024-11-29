

Spam Detection is a machine learning-based project that classifies messages as spam or not spam. This project is implemented using Python and includes a web-based user interface created with Streamlit.

Features

- Preprocesses and cleans input text data.
- Uses a trained machine learning model for classification.
- Web-based UI for easy interaction.
- Efficiently detects spam emails or SMS messages.

Project Structure


Spam Detection/

├── app.py               
├── vectorizer.pkl       
├── model.pkl            
├── requirements.txt     


Installation

Follow these steps to set up and run the project locally:

1.  Clone the repository :

git clone https://github.com/your-username/spam-detection.git
cd spam-detection
    

3.  Install dependencies :
Make sure Python is installed. Then, install the required Python packages:
  
pip install -r requirements.txt
    

4.  Run the application :
Start the Streamlit application:
   
streamlit run app.py
    

5.  Access the application :
Open your browser and go to:
    
http://localhost:8501
    

   Deployment

This project can be deployed to Heroku or other cloud platforms. To deploy to Heroku:

1. Ensure `Procfile` is correctly configured:
    
   web: streamlit run app.py --server.port=$PORT
    

2. Follow [Heroku deployment instructions](https://devcenter.heroku.com/articles/deploying-python).

   Usage

1. Enter the message you want to classify in the text input box.
2. The app will classify the message as either  Spam  or  Not Spam .



   Technologies Used

-  Python : Programming language
-  NLTK : Natural language processing
-  Scikit-learn : Machine learning
-  Streamlit : Web application framework
-  Pickle : For model serialization

   Model Training

The model was trained using a dataset of SMS messages with labeled classes (spam or not spam). Preprocessing steps included:
- Text normalization
- Stopword removal
- Stemming
- TF-IDF vectorization

The classification model is a machine learning algorithm trained on this preprocessed data.



- Dataset sourced from [Spam SMS Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset).

