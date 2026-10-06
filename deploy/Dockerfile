# Public demo image: the band's stage-4 service, unchanged, plus demo data loaded at start.
# Build from the repository root:  docker build -f deploy/Dockerfile -t tablekeeper-demo .
# Judging never uses this file; it uses stage-4/Dockerfile and stage-4/RUN.md.
FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir tzdata
COPY stage-4/app.py /app/app.py
COPY stage-4/static /app/static
COPY deploy/demo-fixture.json /app/demo-fixture.json
COPY deploy/start.py /app/start.py
ENV PORT=8080
EXPOSE 8080
CMD ["python", "-u", "/app/start.py"]
