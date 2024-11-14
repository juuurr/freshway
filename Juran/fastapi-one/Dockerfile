FROM python:3.12
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install  --no-cache-dir --upgrade -r requirements.txt
COPY . /app

CMD ["uvicorn", "main:app", "--host", "8000", "--port", "8000"]