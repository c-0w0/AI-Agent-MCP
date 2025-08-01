# Standard imports
from dotenv import load_dotenv
# 3rd party imports
from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai import Agent
# Local imports
import tools

load_dotenv()
model = GeminiModel("gemini-2.0-flash")
agent = Agent(model,
              system_prompt="YOu are an experienced programmer",
              tools=[tools.read_file, tools.list_files, tools.rename_file])

def main():
    history = []
    while True:
        user_input = input("Input: ")
        resp = agent.run_sync(user_input, message_history=history)
        history = list(resp.all_messages())
        print(resp.output)

if __name__ == '__main__':
    main()
