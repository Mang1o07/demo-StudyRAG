# Riserva: la stessa cartella gira su qualsiasi hosting a container (Hugging Face Spaces, Render, Fly.io, un server).
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV STREAMLIT_SERVER_PORT=7860 STREAMLIT_SERVER_ADDRESS=0.0.0.0
EXPOSE 7860
CMD ["streamlit", "run", "streamlit_app.py"]
