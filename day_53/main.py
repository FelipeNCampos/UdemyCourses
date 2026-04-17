from pathlib import Path

import dotenv

BASE_DIR = Path(__file__).resolve().parent
dotenv.load_dotenv(BASE_DIR / ".env", override=True)

from getContent import getContent
from fillForms import fillForms


def routine():
    try:
        content = getContent()
    except Exception as e:
        print("An error occurred while fetching the content:", e)
        return 1

    if not content:
        print("No content was fetched. Check TARGET_URL and the scraper output.")
        return 1

    try:
        fillForms(content)
    except Exception as e:
        print("An error occurred while filling the forms:", e)
        return 1

    return 0


if __name__ == "__main__":
    routine()
