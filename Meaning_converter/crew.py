from crewai import Agent, Task, Crew
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
# Initialize the language model
llm = ChatGroq(
    temperature=0,
    model_name="llama3-70b-8192",
    api_key=os.getenv("GROQ_API_KEY"),
)

# Create the Research Agent


# Create the Lyric Writing Agent
lyric_agent = Agent(
    role='Lyricist',
    goal='Write  {language}  lyrics from existing {lyrics}',
    backstory='You are a talented translating lyricist with a knack for creating memorable and emotive songs.',
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Create tasks


writing_task = Task(
    description='transalate the given {lyrics} into {language} and give suitable explanation for the translation',
    expected_output = "lyrics mathing report",
    agent=lyric_agent,
    output_file = "Lyrics.md"
)

# Create the crew
lyric_crew = Crew(
    agents=[lyric_agent],
    tasks=[writing_task],
    verbose=2
)

# Run the crew
result = lyric_crew.kickoff({
    "lyrics": "We're searching for a voice, in a world that's gone mad",
    "language": "malayalam"
    })

print(result)