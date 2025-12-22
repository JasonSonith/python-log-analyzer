from pathlib import Path


def find_failed_passwords():
    log_dir = Path(
        "C:/Users/Jason/OneDrive/Personal Pursuits/Projects/"
        "Log Analyzer with AI/tmp/logs/auth.log"
    )

    with open(log_dir, "r") as file:
        for line in file:
            if "Failed password" in line:
                print(line)


# Call the function to execute it
find_failed_passwords()



