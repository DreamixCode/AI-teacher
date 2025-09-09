from agents import Agent, Runner, WebSearchTool
import os

os.environ["OPENAI_API_KEY"] = os.getenv("my-openai-key")

agent = Agent(name="Assistant", instructions="You are a helpful assistant", 
        model="gpt-4o-mini",
        tools=[ WebSearchTool() ])

result = Runner.run_sync(agent, "What is the current date and time in Bursa?")
print(result.final_output)

result = Runner.run_sync(agent, "What is the current weather and temperature in Bursa now? Use celsius degrees. Skip any other daily forecast I need only the today's weather.")
print(result.final_output)
