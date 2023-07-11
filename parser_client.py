from src.cron_parser import CronParser
import sys


if __name__ == "__main__":
    expression = " ".join(sys.argv[1:])

    try:
        store = CronParser().parse(expression)
        for key, val in store.items():
            print(key + (" " * (14-len(key))), end=":")
            print(val, end="\n")
    except Exception as e:
        print(f"Error: {str(e)}")
        print(f"Invalid Expression: {expression}")
