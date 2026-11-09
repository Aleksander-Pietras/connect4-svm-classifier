import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

from src.data_loader import load_dataset

def preprocess(df: pd.DataFrame):
    """
    Converts categorical board representations inot 
    numeric features for the SVM algorithm
    """
    df.columns = df.columns.str.strip()

    # Seperate board attributes (all except "Class") from the target label
    feature_cols = [col for col in df.columns if col != "win_for_x"]

    # Map cateforical characters to integers
    X = df[feature_cols].replace({"x": 1, "o": -1, "b": 0})
    y = df["win_for_x"]

    return X, y

def main():
    train_df = load_dataset("connect-4_training.csv")
    test_df = load_dataset("connect-4_test.csv")

    X_train, y_train = preprocess(train_df)
    X_test, y_test = preprocess(test_df)

    model = SVC(kernel="rbf", C=1.0)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    # Calculate confusion matrix and overall accuracy
    cm = confusion_matrix(y_test, y_pred)
    acc = accuracy_score(y_test, y_pred)

    print("\n ---Results--- ")
    print(f"Accuracy: {acc * 100:.2f}%")
    print(f"\nConfusion Matrix:")
    print(cm)
    print("\nDetailed Classification Report:")
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    main()