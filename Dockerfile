FROM python:3.9

# Set working directory
WORKDIR /app

# Copy current directory contents into the container
COPY . /app/

# Install pip dependencies
RUN pip install --upgrade pip
# RUN pip install --upgrade django
# RUN pip install django==5.1.5
RUN pip install -r requirements.txt

CMD ["python", "-c", "print('Hello, World!')"]
