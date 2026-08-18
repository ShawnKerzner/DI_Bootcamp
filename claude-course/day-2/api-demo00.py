import anthropic
client = anthropic.Anthropic()
MODEL = "claude-sonnet-5"
# PROMPT = ("Classify the ticket into exactly one category: BILLING, SHIPPING,"
#           " PRODUCT, or OTHER. Reply with the category word only.\n\nTIcket {t}")

# PROMPT2 = "Reply to the ticket as if you were a customer service officer.\n\nTicket: {t}"

# PROMPT3 = "Write a japanese haiku"

PROMPT4 = "Give a catchy 5-word slogan for a coffe shop. Reply with a slogan only"

# ticket = [
#     "My card was charged 3 times for the order #123",
#     "Package was delivered to the wrong address",
#     "I bought a mug, and it doesn't work",
#     "Do you have a land phone?"
# ]
# for _ in range(5):
# for ticket in tickets:
message = client.messages.create(
    model=MODEL,
    max_tokens=100,
    thinking={"type": "adaptive"},
    output_config={"effort": "high"},
    messages=[{"role": "user", "content": PROMPT4}]
)
print(message.content[0].text)
