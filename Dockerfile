# Step 1: Base Image
FROM python:3.9-slim

# Step 2: Set Working Directory
WORKDIR /app

# Step 3: Copy Files
COPY . /app

# Step 4: Run the Application
CMD ["python", "Junaid.py"]
