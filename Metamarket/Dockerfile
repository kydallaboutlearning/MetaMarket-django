#pulling official base python container
FROM python:3.12.3

#setting environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


#setting work dir
WORKDIR /code

#installing dependecies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the Django project
COPY . .
