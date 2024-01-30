import argparse
import logging
import sys
import warnings
from tkinter import filedialog as fd

import debugpy
import pyuac
from modules.seven_zip import SevenZip
from pywinauto.timings import Timings


def main(**kwargs):
    """
    Args:
        debugger (bool, optional): Not available in a PyInstaller bundle. Start debugger on port 5678 and wait for attach. Defaults to False.
        7zip_path (str, optional): Path to 7-Zip installer. Defaults to None.
    """

    # Debugging
    if kwargs.get("debugger", False) and not getattr(sys, "frozen", False):
        debugpy.listen(5678)

        print("Waiting for debugger attach")
        debugpy.wait_for_client()

    # Logging
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
    warnings.filterwarnings(
        "ignore", category=UserWarning
    )  # pywinauto 32bit on 64bit Windows

    # Pywinauto timings
    Timings.fast()

    # Modules
    seven_zip = SevenZip()

    # Code
    try:
        seven_zip_installer_path = kwargs.get("7zip_path", None)

        if seven_zip_installer_path is None:
            seven_zip_installer_path = fd.askopenfilename(
                title="Select 7-Zip installer", filetypes=[("7-Zip", "*.exe")]
            )

        seven_zip.uninstall()
        seven_zip.install(seven_zip_installer_path)
    except Exception as e:
        logging.exception(e)

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

    parser.add_argument("--7zip-path", help="Path to 7-Zip installer")

    args = parser.parse_args()

    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
    else:
        main(**vars(args))
