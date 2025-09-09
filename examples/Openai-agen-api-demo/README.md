# Agents SDK Examples

This repository contains examples demonstrating how to use the Agents framework to build AI assistants with various capabilities.

## Overview

The examples showcase different features of the Agents framework:

1. **Simple OpenAI Example** - Basic usage of the agents SDK with OpenAI models
2. **Model Settings** - Configuring model parameters like temperature
3. **Custom Tools** - Creating and using custom function tools
4. **Web Search Tool** - Integrating web search capabilities
5. **Agent Handoffs** - Creating specialized agents that can hand off tasks to each other
6. **Guardrails** - Implementing input validation and safety measures

## Getting Started

### Prerequisites

- Python 3.8 or higher
- An OpenAI API key

### Installation

```bash
# Install the Agents framework
pip install agents-python

# For web search functionality
pip install agents-python[web-search]
```

### Environment Setup

Set your OpenAI API key as an environment variable:

```bash
# For Linux/macOS
export OPENAI_API_KEY="your-api-key-here"

# For Windows (Command Prompt)
set OPENAI_API_KEY=your-api-key-here

# For Windows (PowerShell)
$env:OPENAI_API_KEY="your-api-key-here"
```

Alternatively, you can set it in your code as shown in the examples.

## Running the Examples

### 1. Simple OpenAI Example

A basic example showing how to create an agent and run a query.

```bash
python 01_simple-openai-example.py
```

### 2. Model Settings

Demonstrates how to configure model parameters like temperature.

```bash
python 02_model-settings-temperature.py
```

### 3. Custom Tools

Shows how to create and use custom function tools with your agent.

```bash
python 03_CustomTool.py
```

### 4. Web Search Tool

Demonstrates how to use the built-in web search capability.

```bash
python 04_WebSearchTool.py
```

### 5. Agent Handoffs

Shows how to create specialized agents that can hand off tasks to each other.

```bash
python 05_agents_handoff.py
```

### 6. Guardrails

Demonstrates how to implement input validation and safety measures.

```bash
python 05_guardrails.py
```

## Example Descriptions

### Simple OpenAI Example
Creates a basic agent using OpenAI's model to generate a short poem about AI.

### Model Settings
Shows how to configure model parameters like temperature to control the randomness of responses.

### Custom Tools
Demonstrates creating custom function tools (factorial and average calculators) that the agent can use to solve mathematical problems.

### Web Search Tool
Shows how to enable an agent to search the web for current information like weather and time.

### Agent Handoffs
Creates a system of specialized agents (calculator, weather, task splitter) that can hand off tasks to each other based on the query type.

### Guardrails
Implements input validation to ensure user queries meet certain criteria (e.g., not exceeding a word limit).

## Notes

- Make sure to replace `os.getenv("slavo-openai-key")` with your actual OpenAI API key or environment variable name in each example.
- The examples use different OpenAI models like "gpt-4o" and "gpt-4o-mini". Adjust these based on your API access.
- Web search functionality requires an internet connection.

```python:README.md
# Agents Framework Examples

This repository contains examples demonstrating how to use the Agents framework to build AI assistants with various capabilities.

## Overview

The examples showcase different features of the Agents framework:

1. **Simple OpenAI Example** - Basic usage with OpenAI models
2. **Model Settings** - Configuring model parameters like temperature
3. **Custom Tools** - Creating and using custom function tools
4. **Web Search Tool** - Integrating web search capabilities
5. **Agent Handoffs** - Creating specialized agents that can hand off tasks to each other
6. **Guardrails** - Implementing input validation and safety measures

## Getting Started

### Prerequisites

- Python 3.8 or higher
- An OpenAI API key

### Installation

```bash
# Install the Agents framework
pip install agents-python

# For web search functionality
pip install agents-python[web-search]
```

### Environment Setup

Set your OpenAI API key as an environment variable:

```bash
# For Linux/macOS
export OPENAI_API_KEY="your-api-key-here"

# For Windows (Command Prompt)
set OPENAI_API_KEY=your-api-key-here

# For Windows (PowerShell)
$env:OPENAI_API_KEY="your-api-key-here"
```

Alternatively, you can set it in your code as shown in the examples.

## Running the Examples

### 1. Simple OpenAI Example

A basic example showing how to create an agent and run a query.

```bash
python 01_simple-openai-example.py
```

### 2. Model Settings

Demonstrates how to configure model parameters like temperature.

```bash
python 02_model-settings-temperature.py
```

### 3. Custom Tools

Shows how to create and use custom function tools with your agent.

```bash
python 03_CustomTool.py
```

### 4. Web Search Tool

Demonstrates how to use the built-in web search capability.

```bash
python 04_WebSearchTool.py
```

### 5. Agent Handoffs

Shows how to create specialized agents that can hand off tasks to each other.

```bash
python 05_agents_handoff.py
```

### 6. Guardrails

Demonstrates how to implement input validation and safety measures.

```bash
python 05_guardrails.py
```

## Example Descriptions

### Simple OpenAI Example
Creates a basic agent using OpenAI's model to generate a short poem about AI.

### Model Settings
Shows how to configure model parameters like temperature to control the randomness of responses.

### Custom Tools
Demonstrates creating custom function tools (factorial and average calculators) that the agent can use to solve mathematical problems.

### Web Search Tool
Shows how to enable an agent to search the web for current information like weather and time.

### Agent Handoffs
Creates a system of specialized agents (calculator, weather, task splitter) that can hand off tasks to each other based on the query type.

### Guardrails
Implements input validation to ensure user queries meet certain criteria (e.g., not exceeding a word limit).

## Notes

- Make sure to replace `os.getenv("my-openai-key")` with your actual OpenAI API key or environment variable name in each example. Or To configure your api key in the environment variable.
- The examples use different OpenAI models like "gpt-4o" and "gpt-4o-mini". Adjust these based on your API access.
- Web search functionality requires an internet connection.
```
