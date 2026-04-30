# CrewAI — Research Crew

Implementación de un crew de investigación que puede importarse desde el Formato Genérico de Agente (GAF).

## Estructura

```
crewai/
├── pyproject.toml          # Dependencias y config [tool.crewai]
├── Dockerfile              # Imagen Docker
├── docker-compose.yml      # Orquestación Docker
├── .env.example            # Variables de entorno requeridas
├── import_from_gaf.py      # Script de importación desde formato GAF
└── src/
    └── research_crew/
        ├── config/
        │   ├── agents.yaml  # Configuración de agentes (generada por el parser)
        │   └── tasks.yaml   # Configuración de tareas (generada por el parser)
        ├── crew.py          # Clase principal @CrewBase
        └── main.py          # Entrypoint
```

## Correr localmente

```bash
# 1. Instalar dependencias
uv venv
source .venv/bin/activate
uv sync

# 2. Configurar variables de entorno
cp .env.example .env
# Editar .env con tus API keys

# 3. Ejecutar el crew
python -m research_crew.main "inteligencia artificial"
# O directamente:
crewai run
```

## Correr con Docker

```bash
# Construir y correr
docker-compose up --build

# Pasar un tema como argumento
docker-compose run crewai python -m research_crew.main "machine learning"
```

## Importar desde Formato GAF

El formato GAF (Generic Agent Format) permite definir agentes en texto plano y convertirlos automáticamente a la estructura CrewAI:

```bash
# Importar el ejemplo incluido
python import_from_gaf.py ../examples/investigador_noticias.gaf

# Esto sobreescribe agents.yaml y tasks.yaml con la estructura parseada
```

### Ejemplo de formato GAF
```
AGENTE: Mi Agente

PROPOSITO: Descripción del propósito

ROL: Analista de Datos
OBJETIVO: Analizar y reportar métricas
PERSONALIDAD: Analítico y preciso

TAREAS:
1. Recolectar datos
   RESULTADO ESPERADO: Dataset limpio y validado

2. Generar reporte
   RESULTADO ESPERADO: Reporte ejecutivo de 2 páginas

HERRAMIENTAS: python, pandas
```

## Variables de entorno

| Variable | Descripción |
|---|---|
| `OPENAI_API_KEY` | API key de OpenAI (para el LLM del crew) |
| `ANTHROPIC_API_KEY` | API key de Anthropic (para el parser GAF) |
