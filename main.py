from pathlib import Path

# One sentence pitching a friend who has never coded on letting an AI
# agent build their first app idea on make.fun. Judge criteria, in order:
# on-topic case to that friend in one read, concrete low-risk reason to
# say yes now, plain words, truth (free to try, no code to learn), warmth.
# Revision: kept the conversational hook ("say it out loud") and swapped
# the ending for the stronger low-risk close — "only keep going if you
# like what you see" — while keeping the no-code reassurance, so the
# friend's two real objections (I can't code; what if I don't like it)
# are both answered in one read.
LINE = (
    "Say that app idea you keep bringing up out loud in plain words on "
    "make.fun, and an AI agent will build the first version for you — "
    "free to try, no code to learn, and you only keep going if you like "
    "what you see."
)

# Self-check the gate before writing: 1-240 characters, not only whitespace.
if len(LINE) < 1 or len(LINE) > 240 or LINE.strip() == "":
    raise SystemExit(f"pitch line is {len(LINE)} characters, outside the 1-240 gate")

out = Path("/output")
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(LINE, encoding="utf-8")
