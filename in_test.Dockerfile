##
##    Docker image for Device Monitor
##    Copyright (C) 2021  VIDAL & ASTUDILLO Ltda
##
##
# FROM arm32v7/python:3.9
FROM python:3.9

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY ./in_test_requirements.txt /app/

RUN pip install --no-cache-dir --upgrade -r in_test_requirements.txt

# Next COPY disabled while testing.
# COPY ./app /app/

CMD ["python3", "/app/in_test.py"]