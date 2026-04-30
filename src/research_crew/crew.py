import os

from crewai import Agent, Crew, LLM, Process, Task
from crewai.project import CrewBase, agent, crew, task

_OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")
_OLLAMA_MODEL    = os.environ.get("OLLAMA_MODEL", "ollama/gemma4:e4b")

_llm = LLM(model=_OLLAMA_MODEL, base_url=_OLLAMA_BASE_URL)


@CrewBase
class ResearchCrew:
    agents_config = "config/agents.yaml"
    tasks_config  = "config/tasks.yaml"

    @agent
    def investigador_noticias(self) -> Agent:
        return Agent(
            config=self.agents_config["investigador_noticias"],
            llm=_llm,
            verbose=True,
        )

    @task
    def buscar_noticias(self) -> Task:
        return Task(config=self.tasks_config["buscar_noticias"])

    @task
    def generar_reporte(self) -> Task:
        return Task(config=self.tasks_config["generar_reporte"])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
