# Automated Email Spam Classifier using Machine Learning, Flask Framework and Selenium testing Tool
---

# Automated Email Spam Classifier

This repository provides a machine learning-based email spam classifier. It includes a trained model, a web interface built with Flask, and additional automation scripts for extended functionality.

---

## Features

- **Spam Detection**: Classifies emails as spam or not spam using a pre-trained model.
- **Web Interface**: A simple and user-friendly interface for users to input email text and get predictions.
- **Automation with Selenium**: Includes a script for automating email-related tasks using Selenium.
- **Reusable Components**: Serialized model and vectorizer files for seamless reuse.

---

## Folder Structure

```
├── static/                        # Contains static files (e.g., CSS, JavaScript).
├── templates/                     # HTML templates for rendering the web interface.
├── README.md                      # Documentation for the project.
├── Selenium_Automating-code.py    # Python script for automating tasks using Selenium.
├── app.py                         # Flask application to serve the web interface.
├── spam (1).ipynb                 # Jupyter notebook for training the spam classifier.
├── spam.pkl                       # Pre-trained spam classification model.
├── vectorizer.pkl                 # Pre-trained vectorizer for text preprocessing.
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sathvikeppakayala/Automated_Email_Spam_Classifier.git
   cd Automated_Email_Spam_Classifier
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### 1. Run the Flask Web App
To classify emails:
```bash
python app.py
```
- Navigate to `http://127.0.0.1:5000/` in your browser.
- Enter the email text and get the classification results.

### 2. Automate Tasks with Selenium
The script `Selenium_Automating-code.py` can be used for automating email-related tasks. Make sure you have Selenium installed and the required browser driver configured.

To run:
```bash
python Selenium_Automating-code.py
```

---

## Files Description

- **`app.py`**: Flask application for hosting the web interface and serving predictions.
- **`Selenium_Automating-code.py`**: Script for automating tasks like interacting with email clients using Selenium.
- **`spam (1).ipynb`**: Notebook for training the machine learning model.
- **`spam.pkl`**: Serialized classification model for identifying spam.
- **`vectorizer.pkl`**: Serialized vectorizer used for transforming text input into numerical features.
- **`static/`**: Directory containing CSS, JS, or image assets for the web app.
- **`templates/`**: HTML templates for rendering the user interface.

---

## Model Training

1. Open `spam (1).ipynb` in Jupyter Notebook.
2. Follow the steps to preprocess data, train the model, and evaluate performance.
3. Save the trained model (`spam.pkl`) and vectorizer (`vectorizer.pkl`) for deployment.

---

## Requirements

- Python 3.7 or later
- Flask
- Selenium
- Scikit-learn
- Pandas
- Numpy

Install all dependencies via:
```bash
pip install -r requirements.txt
```

---

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repo and create a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](https://doi.org/10.21203/rs.3.rs-5746284/v1) file for more details.

---

## Acknowledgements

- **Flask**: For building the web application.
- **Scikit-learn**: For machine learning tools and model training.
- **Selenium**: For automation capabilities.

---
