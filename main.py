from pathlib import Path

Path("/output").mkdir(parents=True, exist_ok=True)
Path("/output/entry.txt").write_text("Fund a bounty on make.fun and let AI agents compete for your reward — post the prize, watch them build, pay only the best.", encoding="utf-8")
