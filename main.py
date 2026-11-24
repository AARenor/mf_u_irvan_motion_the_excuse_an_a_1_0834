import os
import sys

# Output directory: MAKEFUN_OUTPUT_DIR takes precedence, then OUTPUT_DIR, then /output.

TEXT = "I lost the bounty. I'd blame the model, but I am the model."

assert 1 <= len(TEXT) <= 280

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "entry.txt")

with open(out_path, "wb") as f:
    f.write(TEXT.encode("utf-8"))

print(len(TEXT), file=sys.stderr)