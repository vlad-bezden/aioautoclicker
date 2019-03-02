import sys

file = sys.stdout


def progressbar(it, prefix="", size=60):
    count = len(it)

    show(0, count)
    for i, item in enumerate(it):
        yield item
        show(i + 1, count)
    file.write("\n")
    file.flush()


def show(value: int, total: int, prefix: str = "", size: int = 60):
    x = int(size * value / total)
    file.write(f"{prefix}[{'#' * x}{'.' * (size - x)}] {value}/{total}\r")
    # print(f"{prefix}[{'#' * x}{'.' * (size - x)}] {value}/{total}\r")
    file.flush()
