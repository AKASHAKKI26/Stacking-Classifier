# Stacking-Classifier
# Breast Cancer Prediction using Stacking Classifier

This project is a Machine Learning web application built using Streamlit and Stacking Classifier.

The application predicts whether a breast tumor is benign or malignant based on important medical features.

---

## Prediction Classes

| Prediction | Meaning |
|---|---|
| 0 | Malignant Tumor |
| 1 | Benign Tumor |

---

## Features Used

- Worst Radius
- Worst Perimeter
- Worst Area
- Worst Concave Points
- Mean Concavity
- Mean Perimeter
- Mean Radius
- Mean Area
- Worst Texture
- Worst Compactness

---

## Machine Learning Algorithm

### Base Models
- Logistic Regression
- Decision Tree Classifier
- KNN Classifier
- SVM Classifier

### Meta Model
- Random Forest Classifier

### Final Model
- Stacking Classifier

---

## Technologies Used

- Python
- Streamlit
- Scikit-learn
- NumPy
- Pandas
- Pickle

---

## Project Structure

```text
BreastCancerPrediction/
│
├── stackclass.py
├── breast_cancer_model.pkl
├── scaler.pkl
├── features.pkl
├── requirements.txt
└── README.md
```

---

## Installation

Install required libraries using:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run stackclass.py
```

---

## Output

The application predicts:

```text
Benign Tumor Detected
```

or

```text
Malignant Tumor Detected
```

---

## Model Description

The model is trained using:

- Breast Cancer Dataset
- Important feature selection
- Feature scaling
- Ensemble learning using Stacking Classifier

---

## Expected Accuracy

```text
95% to 99%
```

---

## Author

Machine Learning Mini Project
