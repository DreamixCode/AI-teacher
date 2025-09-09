from agents import Agent, Runner
import os

os.environ["OPENAI_API_KEY"] = os.getenv("my-openai-key")

agent = Agent(name="Assistant", instructions="You are a helpful assistant"  )

result = Runner.run_sync(agent, "Write a very short 4 rows poem about AI.")
print(result.final_output)
