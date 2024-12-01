import os
import shutil
import sys

import requests


def get_input(yy, dd):

    url = f"https://adventofcode.com/{yy}/day/{dd}/input"

    session = requests.Session()
    session_cookie = os.getenv('SESSION_COOKIE')

    session.cookies.set('session', session_cookie)
    try:
        response = session.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        raise Exception(f"Error downloading input from {url}: {e}")


def main(day):
    year = os.getenv("YEAR")

    print(f"Day: {day}. Formatted: {day.zfill(2)}")

    folder_name = f"{year}/day{day.zfill(2)}"
    os.makedirs(folder_name, exist_ok=True)
    shutil.copy("template.py", f"{folder_name}/main.py")

    archivo_input = os.path.join(folder_name, "input.txt")
    with open(archivo_input, "w") as f:
        f.write(get_input(year, day))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <day>")
        sys.exit(1)

    day = sys.argv[1]

    main(day)
