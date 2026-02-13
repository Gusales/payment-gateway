FROM python:3.11 AS builder

LABEL maintainer="dev.gussales@gmail.com" \
      description="Payment Gateway" \
      version="0.1.0"

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app ./app

FROM python:3.11 AS runner

WORKDIR /production

COPY --from=builder /usr/local /usr/local
COPY --from=builder /app /production

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]