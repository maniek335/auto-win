import argparse
import sys

import debugpy
import pyuac


def main(**kwargs):
    """
    Args:
        debugger (bool, optional): Not available in a PyInstaller bundle. Start debugger on port 5678 and wait for attach. Defaults to False.
    """

    # Debugging
    if kwargs.get("debugger", False) and not getattr(sys, "frozen", False):
        debugpy.listen(5678)

        print("Waiting for debugger attach")
        debugpy.wait_for_client()

    # Code
    print("Hello World!")

    input("Press Enter to continue...")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Automate installation of Windows apps",
        epilog="© 2023 Kubisz Mariusz (contact@kubiszmariusz.pl)",
    )

    # Debugging (not available in a PyInstaller bundle)
    if not getattr(sys, "frozen", False):
        parser.add_argument(
            "--debugger",
            help="Start debugger on port 5678 and wait for attach",
            action="store_true",
        )

    args = parser.parse_args()

    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
    else:
        main(**vars(args))
