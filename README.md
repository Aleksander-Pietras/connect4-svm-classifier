# connect4-svm-classifier
Simple algorithm that uses a support vector machine (SVM) to predict a state of a connect4 position.

Results: Confusion Matrix
> TODO: produce results to show model accuracy

## Dataset Credit
This project uses the Connect-4 Opening Database donated by John Tromp to the UCI Machine Learning Repository (Licensed under CC BY 4.0).

## Setup & Environment Activation

### 1. Clone the repository
```bash
git clone https://github.com/Aleksander-Pietras/connect4-svm-classifier.git
cd connect4-svm-classifier
```

### 2.1 Windows (PowerShell)
```powershell
# Set policy if script execution is blocked
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# Activate environment
.venv\Scripts\Activate.ps1
```

### 2.2 Linux (Bash)
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