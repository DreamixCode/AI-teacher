from agents import Agent, Runner, WebSearchTool, GuardrailFunctionOutput, input_guardrail
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


@input_guardrail
def too_long_input_guardrail(context, agent, user_input):
    """Check if input is too long (over 50 words)"""
    if len(user_input.split()) > 50:
        return GuardrailFunctionOutput(
            output_info="Input exceeds 50 word limit.",
            tripwire_triggered=True
        )
    return GuardrailFunctionOutput(
        output_info="Input length is acceptable.",
        tripwire_triggered=False
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
        handoffs=[weather_agent, calculator_agent],
        input_guardrails=[too_long_input_guardrail]
        )

result = Runner.run_sync(general_purpose_agent, "What is the current weather and time in Sofia?")
print(result.final_output)

