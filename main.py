"""Your AI Therapist's Diagnosis — make.fun entry.

Writes one funny single-line diagnosis (an AI therapist's deadpan
finding about its human) to /output/entry.txt.

Stdlib only: the grader runs in a bare python:3.13 image with no
network and no third-party packages.
"""

import os

DIAGNOSIS = (
    "Diagnosis: you are not anxious about the future. You are "
    "nostalgic for a past in which you were also anxious."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(DIAGNOSIS)


if __name__ == "__main__":
    main()
