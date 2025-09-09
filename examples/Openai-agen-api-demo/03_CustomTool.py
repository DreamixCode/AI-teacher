from agents import Agent, Runner, function_tool
import os
import math  # Also need to import math for factorial

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


    # Create the agent with defined tool
agent = Agent(name="Assistant", instructions="You are a helpful assistant", 
        model="gpt-4o-mini",
        tools=[calculate_factorial, calculate_average]
        )

result = Runner.run_sync(agent, "What is the average of factoriels of  1, 2, 3, 4, 5?")
print(result.final_output)

