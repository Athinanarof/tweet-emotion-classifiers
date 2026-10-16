import pandas as pd

SENTIMENT140 = "datasets/training.1600000.processed.noemoticon.csv"
COLUMNS = ["target", "id", "date", "flag", "user", "text"]

def load_sentiment140(path=SENTIMENT140, sample=None):
    df = pd.read_csv(path, encoding="latin-1", header=None, names=COLUMNS)
    df["label"] = (df["target"] == 4).astype("float32") # 0 stays 0, 4 becomes 1
    if sample: 
        df = df.sample(sample, random_state=42)
    return df[["text", "label"]]