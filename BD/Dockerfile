FROM python:3.11-slim

WORKDIR /BD

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Ne copiez pas les fichiers ici, ils seront montés via le volume
# COPY . .

EXPOSE 6874

CMD ["python", "app.py"]