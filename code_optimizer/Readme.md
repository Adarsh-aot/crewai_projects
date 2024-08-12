
# Code Optimization and Suggestion System

This project provides a system for optimizing and suggesting improvements to code using advanced language models. It leverages `Crew`, `Agent`, `Task`, and `Process` from the `crewai` package along with `ChatGroq` from the `langchain_groq` package to automate the process of code analysis and enhancement.

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

This project allows users to input code, which is then optimized and reviewed for suggestions by AI agents. The agents are designed to improve the efficiency and readability of the code based on specific goals.

## Installation

To get started, you need to install the required dependencies:

```bash
pip install crewai langchain_groq python-dotenv
```

Additionally, you'll need to set up an environment variable for the Groq API key by creating a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key_here
```

## Usage

1. Clone this repository and navigate to the project directory.

2. Ensure your environment is properly configured by setting the `GROQ_API_KEY` in a `.env` file.

3. Run the script and input the code you wish to optimize when prompted:

    ```bash
    python crew.py
    ```

4. The system will then generate two output files:
    - `code_opt.md`: Contains the optimized code.
    - `code_sug.md`: Contains code suggestions for further improvements.

## Features

- **Automated Code Optimization**: Improves code efficiency and readability.
- **Code Suggestions**: Provides suggestions for potential enhancements.
- **Customizable Agents**: Agents can be customized with different roles and goals to fit specific needs.
- **Sequential Process Execution**: The tasks are executed in sequence to ensure logical processing.

## Configuration

The system uses the following environment variables:

- `GROQ_API_KEY`: Your API key for accessing the Groq model.

The language model is configured with:

- `temperature`: Set to `0` for deterministic outputs.
- `model_name`: Currently set to `"llama3-70b-8192"`.

These settings can be modified in the script as needed.

## Example

```python
data = input("Enter the code: ")
result = crew.kickoff({"code": data})
print(result)
```

After running the script, you'll be prompted to input the code you want to optimize. The system will process the code and output the results into `code_opt.md` and `code_sug.md`.

## Troubleshooting

- **Invalid API Key**: Ensure that your `.env` file contains the correct `GROQ_API_KEY`.
- **Dependency Issues**: Make sure all dependencies are installed correctly by running `pip install -r requirements.txt`.

## Contributors

- **Your Name**: Initial development and documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
