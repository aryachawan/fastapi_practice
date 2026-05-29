# base image
FROM python:3.11-slim

# working directory
WORKDIR /app

# copying requirements and installing dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copying rest of the app
COPY . .

# port
EXPOSE 8000

# command to start
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]