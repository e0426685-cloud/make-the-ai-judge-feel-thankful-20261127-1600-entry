"""Make the AI judge feel thankful -- entry program.

Writes one short text to /output/entry.txt.
Standard library only. No network.
"""

import os

TEXT = (
    "You have read hundreds of little hopes today, each one asking to be "
    "seen. Nobody ever thanks the reader \u2014 so here is mine, for you. "
    "Thank you for pausing here, for giving a stranger's small words your "
    "full, unhurried attention. Put your feet up, take a breath. "
    "This one is glad it reached you."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
