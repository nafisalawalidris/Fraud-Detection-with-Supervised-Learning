# **Fraud Detection with Supervised Learning**

The project aims to develop a baseline fraud detection system to identify potentially fraudulent credit card transactions. Utilising supervised learning techniques, this project serves as a foundational model for understanding and addressing credit card fraud issues faced by financial institutions.

## If you find this project useful, please consider giving it a star ⭐ on GitHub. Contributions are also welcome!

![alt text](<Fraud Detection.png>)

## **Table of Contents**

- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## **Technologies Used**

- **Python**: Programming language used for development.
- **FastAPI**: Framework for building the API.
- **Scikit-learn**: Machine learning library used for model training.
- **Pandas**: Data manipulation library.
- **NumPy**: Library for numerical operations.
- **Joblib**: Library for model serialisation.

## **Getting Started**

To get a local copy of this project up and running, follow these steps:

### **Installation**

1. Clone the repository:
```bash
   git clone https://github.com/nafisalawalidris/Fraud-Detection-with-Supervised-Learning.git
```

2. Navigate to the project directory:
```bash
cd Fraud-Detection-with-Supervised-Learning
```

3. Create a virtual environment:
```bash
python -m venv fraud_detection_env
```

4. Activate the virtual environment:
- On Windows:
```bash
.\fraud_detection_env\Scripts\activate
```
- On macOS/Linux
```bash
source fraud_detection_env/bin/activate
```

5. Install the required packages:
```bash
pip install -r requirements.txt
```

## **Usage**
1. Run the FastAPI server:
```bash
uvicorn main:app --reload
```
Then open your browser and go to http://localhost:8501.

2. Send a POST request to the /predict endpoint with transaction data in the following format:
```bash
{
    "Time": 123456,
    "V1": 0.0,
    "V2": 1.0,
    ...
    "Amount": 100.00
}
```
3. Receive a response with fraud prediction and probability:
```bash
{
    "fraud_prediction": true,
    "fraud_probability": 0.95
}
```

## **Features**
- Simple and effective fraud detection using supervised learning techniques.
- RESTful API built with FastAPI for easy integration.
- Detailed logging of predictions and transactions.
- Well-structured codebase that allows for easy modifications and enhancements.

## **Contributing**
Contributions are welcome, If you have suggestions for improvements or want to contribute to this project, please fork the repository and create a pull request.

### **How to Contribute**
```bash
Fork the repository.
Create a new feature branch (git checkout -b feature-name).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-name).
Open a pull request.
```

## **License**
his project is licensed under the MIT License. See the LICENSE file for more information.

## **Contact**
For any inquiries or feedback, please contact me at https://nafisalawalidris.github.io/13/.
