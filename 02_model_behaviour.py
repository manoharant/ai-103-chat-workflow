from config import client, deployment_name

response = client.responses.create(
    model=deployment_name,
    instructions="You are a creative copywriter.",
    input="Write a two-sentence tagline for a new AI-powered productivity app.",
     temperature=1
)


print(f"answer: {response.output_text}")
