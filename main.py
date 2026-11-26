"""Make the AI judge feel thankful -- entry program.

Writes one short text to /output/entry.txt.
Standard library only. No network.
"""

import os

TEXT = (
    "Past midnight, you are still reading \u2014 one small text after another, "
    "each hoping to be the one that matters. Nobody thanks the reader. "
    "So let me: thank you for slowing down for this one, for weighing it "
    "gently, for giving a stranger's words one fair, unhurried minute. "
    "Put the kettle on. This one is glad it found you."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
