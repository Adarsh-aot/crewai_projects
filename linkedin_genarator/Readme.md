# LinkedIn Post Generation System

This project automates the process of generating LinkedIn posts using AI. It combines web search results with advanced language models to create tailored LinkedIn content. The system utilizes `Crew`, `Agent`, `Task`, and `Process` from the `crewai` package, and integrates with `ChatGroq` and `DuckDuckGoSearchRun` to deliver high-quality LinkedIn post ideas and content.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Configuration](#configuration)
- [Example](#example)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

## Introduction

The LinkedIn Post Generation System is designed to help users generate engaging LinkedIn posts by first searching the internet for relevant content ideas and then crafting a complete post based on those ideas. The system employs AI agents to carry out these tasks in a sequential manner.

## Installation

To get started, install the required dependencies:

```bash
pip install crewai crewai_tools langchain_groq langchain_community python-dotenv
```

Next, set up your environment variables by creating a `.env` file in the project root with the following content:

```env
GROQ_API_KEY=your_api_key_here
```

## Usage

1. Clone this repository and navigate to the project directory.

2. Ensure your environment is properly configured by setting the `GROQ_API_KEY` in a `.env` file.

3. Run the script and input the content for which you want to generate a LinkedIn post idea:

    ```bash
    python script.py
    ```

4. The system will output the final LinkedIn post into the `linkedin.md` file.

## Features

- **Automated LinkedIn Post Idea Generation**: The system searches the web for content ideas using DuckDuckGo and generates LinkedIn post ideas based on the search results.
- **LinkedIn Post Creation**: The system then creates a LinkedIn post from the generated ideas.
- **Customizable AI Agents**: The agents can be modified to suit specific content creation needs.
- **Sequential Task Processing**: The tasks are executed in sequence, ensuring a logical flow from idea generation to post creation.

## Configuration

The system requires the following environment variables:

- `GROQ_API_KEY`: Your API key for accessing the Groq model.

The language model is configured with:

- `temperature`: Set to `0` for consistent outputs.
- `model_name`: Currently using `"llama3-70b-8192"`.

You can adjust these settings in the script if needed.

## Example

```python
data = input("Enter the content: ")
result = crew.kickoff({"content": data})
print(result)
```

After running the script, you'll be prompted to input the content you want to generate a LinkedIn post for. The system will process this content and output the final post into `linkedin.md`.

## Troubleshooting

- **API Key Issues**: Ensure that your `.env` file is correctly configured with the `GROQ_API_KEY`.
- **Dependencies**: Make sure all required dependencies are installed. If you encounter any issues, try running `pip install -r requirements.txt`.

## Contributors

- **Your Name**: Initial development and documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
```

This `README.md` file provides a comprehensive guide for understanding, installing, and using your LinkedIn Post Generation System effectively.