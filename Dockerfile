FROM python:3.11

# Create the application directory
RUN mkdir /app
RUN mkdir /app/staticfiles
RUN mkdir /app/media

# Install system dependencies
RUN apt-get update && apt-get install -y libgl1-mesa-glx


# Change the working directory to /app
WORKDIR /app

# Copy the application code to the container
COPY . /app

# Install Poetry and project dependencies
RUN apt-get update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Create the devops user
RUN addgroup --system devops && \
    adduser --system --group devops

# RUN chmod +x ./entrypoint.sh

# Specify the entrypoint and default command
#ENTRYPOINT ["./entrypoint.sh"]
CMD ["gunicorn", "djangoProject.wsgi:application", "--bind", "0:8000", "--timeout", "500"]