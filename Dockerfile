# Dockerfile

# 1. Use an official lightweight Python base image
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the requirements file and install dependencies
# This is done first to leverage Docker's layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of your application code into the container
COPY . .

# 5. Expose the port the app runs on
EXPOSE 8000

# 6. Define the command to run your application
# This is the same command you use to start the server locally
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]