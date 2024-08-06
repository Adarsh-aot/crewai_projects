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
research_agent = Agent(
    role='Music Researcher',
    goal='Research topics and genre characteristics based on {topic}',
    backstory='You are an experienced music researcher with deep knowledge of various genres and songwriting techniques.',
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Create the Lyric Writing Agent
lyric_agent = Agent(
    role='Lyricist',
    goal='Write engaging and original song lyrics',
    backstory='You are a talented lyricist with a knack for creating memorable and emotive songs.',
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Create tasks
research_task = Task(
    description='Research the specified song topic and genre. Provide key characteristics, themes, and style elements.',
    expected_output = "detailed report on the topic and genre",
    agent=research_agent
)

writing_task = Task(
    description='Using the research provided, write original song lyrics that fit the genre and topic.',
    expected_output = "lyrics mathing report",
    agent=lyric_agent,
    output_file = "Lyrics.md"
)

# Create the crew
lyric_crew = Crew(
    agents=[research_agent, lyric_agent],
    tasks=[research_task, writing_task],
    verbose=2
)

# Run the crew
result = lyric_crew.kickoff({
    'topic': 'Rap on current society'
    })

print(result)