FROM python:3.12.3-slim


#installing dependesies

RUN apt-get update -qq \
    && apt-get install -y build-essential python3-dev \
    python3-pip python3-setuptools python3-wheel python3-cffi \
    libcairo2 libpango-1.0-0 libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 libffi-dev shared-mime-info \
    && rm -rf /var/lib/apt/lists/*


# Setting up Python environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Create build directory for the app
WORKDIR /build



#getting code requirements
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python -m pip install psycopg[binary]



# Expose port 8000
EXPOSE 8000


# Copy the project files into the container
COPY . .

