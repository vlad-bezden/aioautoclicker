"""
__main__ is required if it's called as a package

>>> python -m autoclicker

or

>>> autoclicker
"""

import autoclicker.autoclicker as clicker


def main():
    clicker.main()


if __name__ == "__main__":
    main()
