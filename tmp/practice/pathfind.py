from pathlib import Path

log_dir = Path(
    "C:/Users/Jason/OneDrive/Personal Pursuits/Projects/"
    "Log Analyzer with AI/tmp/logs"
)
for file in log_dir.iterdir():
    if file.suffix == ".log":
        print(file)







