From python:3.8-slim

WORKDIR /app

COPY requiremtents.txt .

RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 5000

# ENTRYPOINT ["python", "app.py"]

CMD ["python", "app.py"]

