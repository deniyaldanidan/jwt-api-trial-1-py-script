# Define ANSI escape codes
RESET = "\033[0m"

BOLD = "\033[1m"
UNDERLINE = "\033[4m"
ITALIC = "\033[3m" # Support depends on used Terminal-Font

# Text Colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"

# Background Colors
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"

# Examples
# print(f"{BOLD}This text is bold.{RESET}")
# print(f"{RED}This text is red.{RESET}")
# print(f"{BOLD}{GREEN}This text is bold and green.{RESET}")
# print(f"{BG_RED}{BOLD}White bold text on red background{RESET}")
