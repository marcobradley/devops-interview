FROM astral/uv:python3.12-trixie

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml uv.lock README.md ./
COPY src ./src

RUN uv sync --frozen --no-dev

COPY entrypoints ./entrypoints
RUN chmod +x entrypoints/*.sh

ENV VIRTUAL_ENV=/app/.venv
ENV PATH=/app/.venv/bin:$PATH
ENV PYTHONPATH=/app/src

ENTRYPOINT ["/app/entrypoints/docker-entrypoint.sh"]
CMD ["api"]
