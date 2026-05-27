from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import pandas as pd
import io

# Import your custom ML processing engines
from app.imputer import advanced_ml_impute
from app.outlier import detect_and_clean_outliers

app = FastAPI(title="CleanCraft AI Preprocessing Engine")

# Configure CORS so your vanilla frontend can communicate securely with the server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows local filesystem or live ports to make requests
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/clean")
async def clean_dataset(file: UploadFile = File(...)):
    # 1. Validate file format extension type
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Currently, only standard CSV datasets are supported.")
    
    try:
        # 2. Read incoming binary stream into memory
        contents = await file.read()
        df = pd.read_csv(io.BytesIO(contents))
        
        if df.empty:
            raise HTTPException(status_code=400, detail="The uploaded dataset contains no structural matrix entries.")

        # 3. Step 1: Run through your Advanced ML Imputation Engine (KNN)
        imputed_df = advanced_ml_impute(df, n_neighbors=5)
        
        # 4. Step 2: Run through your Statistical Anomaly Guard (Isolation Forest)
        final_cleaned_df = detect_and_clean_outliers(imputed_df, contamination=0.05)
        
        # 5. Convert processing dataframe back into an exportable CSV buffer stream
        output_stream = io.StringIO()
        final_cleaned_df.to_csv(output_stream, index=False)
        output_stream.seek(0)
        
        # Stream the file back down directly to the browser window
        return StreamingResponse(
            io.BytesIO(output_stream.getvalue().encode('utf-8')),
            media_type="text/csv",
            headers={"Content-Disposition": f"attachment; filename=cleaned_{file.filename}"}
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Pipeline Processing Interruption: {str(e)}")