from agents import Agent, Runner, ModelSettings
import os

os.environ["OPENAI_API_KEY"] = os.getenv("my-openai-key")

agent = Agent(name="Assistant", instructions="You are a helpful assistant", 
        model="gpt-4o-mini", model_settings=ModelSettings(temperature=1))

result = Runner.run_sync(agent, "Write a very short 4 rows poem about AI.")
print(result.final_output)