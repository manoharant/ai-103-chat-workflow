from config import client, deployment_name

problem = """
A distributed e-commerce system is experiencing intermittent checkout failures 
during peak traffic. The failures appear random, affect roughly 3 percent of the transactions, 
and only occur when inventory checks and payment processing run concurrently. 
Identify the most likely root cause and propose a solution.
"""

response = client.responses.create(
    model=deployment_name,
    instructions="You are a senior software architect.",
    input=problem,
    reasoning={"effort": "high"}
)

print(f"answer: {response.output_text}")
