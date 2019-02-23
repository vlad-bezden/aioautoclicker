import asyncio
import ctypes
import argparse
import time
from enum import IntFlag


class State(IntFlag):
    PAUSED = 0
    RUNNING = 1


async def click(delay=5):
    while True:
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # left down
        ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)  # left up
        await asyncio.sleep(delay)
        print(time.ctime())


def prompter():
    state = State.RUNNING
    while True:
        print(["Paused", "Running"][state])
        input()
        state = ~state


def main(interval):
    loop = asyncio.get_event_loop()
    loop.create_task(click(interval))
    loop.run_in_executor(None, prompter)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        print("Exiting by user request")
    except Exception as e:
        print("Unexpected error: ", str(e))


def parse_args():
    parser = argparse.ArgumentParser(description="Simulate user mouse click")
    delay = 60
    parser.add_argument(
        "-i",
        "--interval",
        type=int,
        default=delay,
        help=f"Time in seconds mouse will click. Default time is {delay} secs",
    )
    return parser.parse_args()


if __name__ == "__main__":
    interval = parse_args().interval
    print(
        f"Mouse will click every {interval} seconds\n"
        "Press Enter for pause and resume program"
    )
    main(interval)
