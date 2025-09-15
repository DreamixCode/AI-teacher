from agents import Agent, Runner, WebSearchTool
import os
import math 
from agents import function_tool

os.environ["OPENAI_API_KEY"] = os.getenv("my-openai-key")

@function_tool
def calculate_factorial(n:int)->int:
    """Calculates the factorial of a non-negative integer."""
    print(f"Calculating factorial for n={n}")
    return math.factorial(int(n))

@function_tool
def calculate_average(numbers:list[int])->float:
    """Calculates the average of a list of numbers."""
    print(f"Calculating average for numbers={numbers}")
    return sum(numbers) / len(numbers)

# First define agents without handoffs
calculator_agent = Agent(name="Calculator Agent", instructions="You are very efficient agent to calculate factorials and averages.", 
        model="gpt-4o-mini",
        tools=[calculate_factorial, calculate_average]
        )

weather_agent = Agent(name="Weather Agent", 
        instructions=(
            "You are a helpful assistant who can answer questions about the weather forecast. "
            "You don't speak about anything else than weather. By default you use celsius degrees."
            "You can use the WebSearchTool to get the weather forecast for a specific location."
            "You do not overshare information based on what asked."
        ),
        model="gpt-4o-mini",
        tools=[
            WebSearchTool()
        ]
        )

split_task_agent = Agent(name="Split task agent", 
        instructions=(
            "You are an AI prompt engineer agent. You are used to split the task into smaller tasks. " 
            "If the input sentences contains more than one parts or instructions or questions, "
            "you split it into smaller parts and return as separately executable tasks."
        ),
        model="gpt-4o"
        )

general_purpose_agent = Agent(name="General Purpose Agent", 
        instructions=(
            "You are a helpful assistant who can answer questions about anything, "
            "concrete straight to the point what is asked. No additional suggestion "
            "for questions is needed unles the user asks for it. You speak always "
            "in english unless asked otherwise. "
            "If you need to calculate something, you hand it over to the Calculator Agent."
        ),
        model="gpt-4o",
        handoffs=[weather_agent, calculator_agent, split_task_agent]
        )

result = Runner.run_sync(general_purpose_agent, "What is the current date and time in Sofia?")
print(result.final_output)

result = Runner.run_sync(general_purpose_agent, "What is the current weather and temperature in Sofia now?")
print(result.final_output)

result = Runner.run_sync(general_purpose_agent, "Calculate the average of factoriels of the expected temperature in Sofia for next 5 days. I need just one number.")
print(result.final_output)
