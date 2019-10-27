
# 1 
FROM python:3.6

# 2
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# 3
COPY src/ /app
WORKDIR /app

# 4
ENV PORT 8080

# 5
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app