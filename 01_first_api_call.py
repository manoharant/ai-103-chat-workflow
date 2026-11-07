from config import client, deployment_name

response = client.responses.create(
    model=deployment_name,
    input="What are the three main benefits of using managed AI endpoints in the cloud?",
)

print(f"answer: {response.output_text}")
