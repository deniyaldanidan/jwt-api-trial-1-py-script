import json
import ansiEscapeCodes


def handleResponse(data, filename, req_url):
    with open(filename, "w") as out:
        out.write(json.dumps(data, indent=2))
        print(f"{ansiEscapeCodes.GREEN}{ansiEscapeCodes.ITALIC}Success:{ansiEscapeCodes.RESET} Output of {ansiEscapeCodes.BLUE}{ansiEscapeCodes.BOLD}{ansiEscapeCodes.UNDERLINE}{req_url}{ansiEscapeCodes.RESET} written on {ansiEscapeCodes.BLUE}{ansiEscapeCodes.BOLD}{ansiEscapeCodes.UNDERLINE}{filename}{ansiEscapeCodes.RESET}")