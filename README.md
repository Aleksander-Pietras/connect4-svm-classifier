# 📦 Connect-4 Support Vector Machine (SVM) Classifier

## 📌 Overview
In this project, I used a Support Vector Machine (SVM) algorithm to train a model that 
evaluates Connect-4 board states and predicts whether a position leads to a win for Player X or a loss/draw.

## 📊 Model Performance and Results 
The classifier was evaluated on 4,000 test positions after training on 30,400 positions,
from the UCI Connect-4 opening database

- **Overall Accuracy:** 81.03% 
- **Model Kernel:** Radial Basis Function (RBF) 
- **Feature Space:** 42 grid squares mapped from categorical (x, o, b) to numerical values (1, -1, 0).

### Confusion Matrix
Shows how many times model was successful and failed (confused).

| | Predicted Loss/Draw<br>($\hat{y} = 0$) | Predicted Win for X<br>($\hat{y} = 1$) |
| --- | :---: | :---: |
| **Actual Loss/Draw**<br>($y = 0$) | 810 | 555 |
| **Actual Win for X**<br>($y = 1$) | 204 | 2,431 |

### Classification Metrics
Shows model's accuracy across key performance metrics—**Precision** (correctness), **Recall** (completeness), and **F1-Score** (overall balance)—evaluated separately for each target class.

| Metric | Class 0 | Class 1 | Overall / Weighted Avg |
| --- | :---: | :---: | :---: |
| **Precision** | 0.80 | 0.81 | 0.81 |
| **Recall** | 0.59 | 0.92 | 0.81 |
| **F1-Score** | 0.68 | 0.86 | 0.80 |
| **Support (Samples)** | 1,365 | 2,635 | 4,000 |

> **Key Takeaway:** The model demonstrates strong predictive performance overall, particularly for Class 1 (0.86 F1-score), while Class 0 shows lower recall due to class imbalance in the test set.

## 📁 Repository Structure
```
connect4-svm-classifier/
├── dataset_connect4/
│   ├── connect-4_test.csv
│   ├── connect-4_training.csv
│   └── README
├── src/
│   ├── data_loader.py
│   └── svm_classifier.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## 🚀 Setup and Execution

### 1. Clone the repository
```bash
git clone https://github.com/Aleksander-Pietras/connect4-svm-classifier.git
cd connect4-svm-classifier
```

### 2. Environment Activation

#### 2.1 Windows (PowerShell)
```powershell
# Set policy if script execution is blocked
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# Activate environment
.venv\Scripts\Activate.ps1
```

#### 2.2 Linux (Bash)
```bash
# Activate environment
source .venv/bin/activate

# Deactivate environment
deactivate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Running the SVM
```bash
python -m src.svm_classifier
```

## Dataset Credit
This project uses the Connect-4 Opening Database donated by John Tromp to the UCI Machine Learning Repository (Licensed under CC BY 4.0).