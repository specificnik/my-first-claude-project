import os
import sys

import anthropic

MODEL = "claude-opus-5"


def ask_claude(question: str) -> str:
    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment

    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        messages=[{"role": "user", "content": question}],
    )

    return next(block.text for block in response.content if block.type == "text")


if __name__ == "__main__":
    question = " ".join(sys.argv[1:]) or "What is Claude Code?"

    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("Set the ANTHROPIC_API_KEY environment variable first.")

    print(ask_claude(question))
