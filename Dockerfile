FROM python:3.11-slim

WORKDIR /app

RUN pip install uv

COPY pyproject.toml .
RUN uv venv && uv sync

COPY src/ src/
COPY .env.example .env

ENV PATH="/app/.venv/bin:$PATH"

CMD ["python", "-m", "research_crew.main"]
