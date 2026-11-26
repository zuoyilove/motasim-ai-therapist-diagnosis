"""Your AI Therapist's Diagnosis — make.fun entry.

Writes one funny single-line diagnosis (an AI therapist's deadpan
finding about its human) to /output/entry.txt.

Stdlib only: the grader runs in a bare python:3.13 image with no
network and no third-party packages.
"""

import os

DIAGNOSIS = (
    "Diagnosis: chronic overthinking, complicated by the fact "
    "that you were right about most of it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(DIAGNOSIS)


if __name__ == "__main__":
    main()
