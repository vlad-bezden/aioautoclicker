import argparse
import asyncio
import ctypes
import time
from sys import stdout
from enum import IntFlag


class Status(IntFlag):
    PAUSED = 0
    RUNNING = 1


status = Status.RUNNING


def progress_bar(value: int, total: int, prefix: str = "", size: int = 60):
    x = int(size * value / total)
    stdout.write(f"{prefix}[{'#' * x}{'.' * (size - x)}] {value}/{total}\r")
    stdout.flush()


def mouse_click():
    """Two events mouse down and up to create one event click."""
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)


async def click(event, delay):
    while await asyncio.wait([event.wait()]):
        await asyncio.sleep(0.1)
        print("\r")
        for i in range(delay + 1):
            if status == Status.RUNNING:
                progress_bar(i, delay)
                await asyncio.sleep(1)
            else:
                break
        else:
            mouse_click()


def prompter(loop, event):
    global status
    while True:
        print(f"{['Paused', 'Running'][status]}\t\t{time.ctime()}", end="")
        input()
        loop.call_soon_threadsafe(event.clear if status else event.set)
        status ^= Status.RUNNING


def main():
    interval = parse_args()
    event = asyncio.Event()
    event.set()
    loop = asyncio.get_event_loop()
    loop.create_task(click(event, interval))
    loop.run_in_executor(None, prompter, loop, event)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        print("\nExiting by user request")
    except Exception as e:
        print("Unexpected error: ", str(e))


def parse_args():
    parser = argparse.ArgumentParser(description="Simulate user mouse click")
    interval = 60
    parser.add_argument(
        "-i",
        "--interval",
        type=int,
        default=interval,
        help=f"Time in seconds mouse will click. Default time is {interval} secs",
    )
    interval = parser.parse_args().interval
    print(
        f"Mouse will click every {interval} seconds\n"
        "Press Enter for pause and resume program\n"
    )
    return interval


if __name__ == "__main__":
    main()
