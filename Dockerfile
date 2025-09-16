FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY Modelo_churn.py .
RUN mkdir models
COPY models/ models/
COPY models/modelo_churn.joblib .
ENTRYPOINT ["uvicorn", "Modelo_churn:app", "--host", "0.0.0.0", "--port", "8000"]