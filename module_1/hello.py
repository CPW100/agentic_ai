import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

curr_dir_path = Path(__file__).parent.resolve()
env_path = curr_dir_path.parent / ".env"

load_dotenv(dotenv_path=env_path)

if not os.getenv("OPENROUTER_API_KEY"):
    raise ValueError(f"Failed to load OPENROUTER_API_KEY from {env_path}.")

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

raw_response = client.chat.completions.with_raw_response.create(
    model = os.environ.get("MODEL", "deepseek/deepseek-v4-flash-0731"),
    messages = [{"role": "user", "content": "Get me mid-autumn festival wishes in Chinese, word limit is 10."}],
    max_tokens=1000,
    extra_body = {"usage": {"include": True}}
)

provider = raw_response.headers.get("x-openrouter-provider", "Unknown")
print(f"Model provider: {provider}")

resp = raw_response.parse()
print(resp.choices[0].message.content)
u = resp.usage
print("tokens in/out:", u.prompt_tokens, u.completion_tokens)
print(f"cost: ${u.cost:.8f}")