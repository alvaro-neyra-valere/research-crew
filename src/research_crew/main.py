import sys

from dotenv import load_dotenv

from research_crew.crew import ResearchCrew

load_dotenv()


def run(topic: str = "artificial intelligence") -> None:
    inputs = {"topic": topic}
    ResearchCrew().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    topic = sys.argv[1] if len(sys.argv) > 1 else "artificial intelligence"
    run(topic)
