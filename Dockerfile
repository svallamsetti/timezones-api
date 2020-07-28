FROM python:3.8.5
#Setting the working directory to timezones
WORKDIR /home/apps
#Copy local contents into the container working directory
COPY . .
#Set env variables
ENV FLASK_ENV development
#Install all required dependencies
RUN pip install -r requirements.txt
#Expose container port
EXPOSE 5000
CMD ["python", "timezones.py"]