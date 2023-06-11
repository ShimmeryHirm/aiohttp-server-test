FROM debian:11.3-slim

RUN apt update && \
    apt install -y --no-install-recommends python3 python3-pip default-jdk

WORKDIR /app
COPY . .
ENV TZ="Europe/Moscow"
RUN pip install --user -r requirements.txt
ENTRYPOINT ["python3", "bot/main.py"]