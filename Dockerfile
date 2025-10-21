#  base image 
From python:3.9
# working directory
WORKDIR /app
# copy
COPY . /app
# run
RUN pip install -r requirements.txt
# ports
EXPOSE 5000
# command to run on container start
CMD ["python", "./app.py"]