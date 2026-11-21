import os
POEM = """Two hands on one rope, pulling opposite ways —
the knot only tightened.
Then one of us slackened, the other steadied,
and the rope became a bridge
we could both cross."""
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(POEM)
