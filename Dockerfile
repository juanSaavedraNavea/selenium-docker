# Imagen base liviana con Python 3.11
FROM python:3.11-slim

# Evitar prompts en apt
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Instala Chromium y ChromeDriver emparejados + utilidades
RUN apt-get update && apt-get install -y --no-install-recommends \
    chromium \
    chromium-driver \
    xvfb \
    fonts-liberation \
    tzdata \
    ca-certificates \
    curl \
    tini \
  && rm -rf /var/lib/apt/lists/*

# Variables de entorno útiles
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER=/usr/bin/chromedriver
ENV TZ=America/Santiago

# Directorio de trabajo
WORKDIR /app

# Reqs primero (mejor cache)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos utilitarios (los scripts se montan como volumen)
COPY utils /app/utils

# tini como init para señales limpias
ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["bash"]
