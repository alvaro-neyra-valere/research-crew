#!/bin/bash
# Expone Ollama (localhost:11434) via Cloudflare Tunnel HTTPS
# La URL pública cambia cada vez que se lanza el túnel.
# Para AMP: copia la URL y actualiza OLLAMA_BASE_URL en el dashboard.

set -e

OLLAMA_PORT="${OLLAMA_PORT:-11434}"

echo "Verificando que Ollama está corriendo en puerto $OLLAMA_PORT..."
if ! curl -s --max-time 2 "http://localhost:$OLLAMA_PORT/api/tags" > /dev/null; then
  echo "ERROR: Ollama no está corriendo. Inicia con: ollama serve"
  exit 1
fi

echo "Iniciando Cloudflare Tunnel para Ollama..."
echo "La URL pública HTTPS aparecerá abajo."
echo "Cópiala y configúrala en CrewAI AMP como:"
echo "  OLLAMA_BASE_URL=<url>/v1    (si usas endpoint OpenAI-compatible)"
echo "  OLLAMA_BASE_URL=<url>       (si usas endpoint nativo Ollama)"
echo "  OLLAMA_MODEL=ollama/gemma4:e4b"
echo ""

cloudflared tunnel --url "http://localhost:$OLLAMA_PORT" --no-autoupdate
