from config import client, deployment_name

response = client.responses.create(
    model=deployment_name,
    instructions="You are a helpful research assistant. Always cite your sources.",
    input="What are the latest developments in AI regulation in the European Union?",
    tools=[{"type": "web_search"}],
    tool_choice="auto"
)

print(f"answer: {response.output_text}")
