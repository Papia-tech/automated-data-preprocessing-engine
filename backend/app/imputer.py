import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

def advanced_ml_impute(df: pd.DataFrame, n_neighbors: int = 5) -> pd.DataFrame:
    """
    Intelligently fills missing numeric data using a K-Nearest Neighbors matrix algorithm.
    Leaves non-numeric categorical data untouched for downstream encoding.
    """
    cleaned_df = df.copy()
    
    # Isolate numeric features since KNN relies on distance metrics
    numeric_cols = cleaned_df.select_dtypes(include=[np.number]).columns
    
    if len(numeric_cols) > 0 and cleaned_df[numeric_cols].isnull().any().any():
        imputer = KNNImputer(n_neighbors=n_neighbors)
        # Apply the trained vector matrix back over the columns
        cleaned_df[numeric_cols] = imputer.fit_transform(cleaned_df[numeric_cols])
        
    return cleaned_df