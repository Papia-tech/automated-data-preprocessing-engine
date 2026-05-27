import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

def detect_and_clean_outliers(df: pd.DataFrame, contamination: float = 0.05) -> pd.DataFrame:
    """
    Uses an Isolation Forest model to automatically identify and drop statistical outliers
    from numeric columns in the dataset.
    """
    cleaned_df = df.copy()
    numeric_cols = cleaned_df.select_dtypes(include=[np.number]).columns
    
    if len(numeric_cols) > 0:
        # Fill temp nulls briefly to allow the anomaly model to calculate spatial boundaries
        temp_filled = cleaned_df[numeric_cols].fillna(cleaned_df[numeric_cols].median())
        
        iso_forest = IsolationForest(contamination=contamination, random_state=42)
        # Predict array states: 1 = normal row, -1 = anomaly/outlier
        predictions = iso_forest.fit_predict(temp_filled)
        
        # Filter out the rows flagged as anomalies (-1)
        cleaned_df = cleaned_df[predictions == 1].reset_index(drop=True)
        
    return cleaned_df