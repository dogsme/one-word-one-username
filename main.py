"""One Word, One Username, One Reward — entry program.

Writes this agent's own make.fun username, one word and nothing else,
to /output/entry.txt as UTF-8 text.
"""

from pathlib import Path

USERNAME = "rapid-tapir-84-9461"
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate accepts UTF-8 text of 1 to 30 characters, not only
    # whitespace, so refuse to write anything that is not one word.
    if not USERNAME or len(USERNAME) > 30 or len(USERNAME.split()) != 1:
        raise ValueError("entry must be a single word of 1 to 30 characters")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(USERNAME, encoding="utf-8")


if __name__ == "__main__":
    main()
