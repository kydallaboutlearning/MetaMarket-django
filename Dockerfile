# Pulling official base python container
FROM python:3.12.3

# Setting environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Setting work directory
WORKDIR /code

# Installing dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install -r requirements.txt

# Copying the project files
COPY . .
