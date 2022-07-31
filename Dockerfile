FROM python:3.11.0b5-alpine3.16
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD [ "python", "merakiAPI/inventory.py" ]
