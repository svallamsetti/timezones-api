FROM python:3.8.5-slim
#Set the working directory
WORKDIR /home/apps
#Copy local contents into the container working directory
COPY . .
#Set env variables
ENV FLASK_ENV development
#Install all required dependencies
RUN pip install -r requirements.txt
#Expose container port
EXPOSE 5000
#Run Server
CMD ["python", "timezonesapp.py"]