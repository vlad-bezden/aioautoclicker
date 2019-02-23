import asyncio
import ctypes
import argparse
import time


left_down = lambda: ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
left_up = lambda: ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)


async def click(event, delay):
    while await event.wait():
        await asyncio.sleep(delay)
        if event.is_set():
            left_down()
            left_up()
            print(time.ctime())


def prompter(loop, event):
    while True:
        print(["Paused", "Running"][event.is_set()])
        input()
        loop.call_soon_threadsafe(event.clear if event.is_set() else event.set)
        time.sleep(0.1)


def main(interval):
    event = asyncio.Event()
    event.set()
    loop = asyncio.get_event_loop()
    loop.create_task(click(event, interval))
    loop.run_in_executor(None, prompter, loop, event)
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
        "Press Enter for pause and resume program\n"
    )
    main(interval)
