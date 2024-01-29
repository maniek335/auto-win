import logging
from os import path

from pywinauto.application import Application


class SevenZip:
    _logger = logging.getLogger("7-Zip")
    _uninstaller_path = r"C:\Program Files\7-Zip\Uninstall.exe"

    def install(self, installer_path: str):
        """
        Args:
            installer_path (str): Path to 7-Zip installer.
        """
        self._logger.info("Installing 7-Zip")

        if not isinstance(installer_path, str):
            self._logger.error("Invalid installer path")
            return

        if not path.isfile(installer_path):
            self._logger.error("7-Zip installer not found")
            return

        self._logger.debug("Starting 7-Zip installer")
        app = Application().start(installer_path)
        window = app.window()

        self._logger.debug("Confirming 7-Zip installation")
        window["&Install"].wait("ready", timeout=30).click()

        self._logger.debug("Finishing 7-Zip installation")
        window["&Close"].wait("ready", timeout=30).click()

        self._logger.info("7-Zip installed")

    def uninstall(self):
        self._logger.info("Uninstalling 7-Zip")

        if not path.isfile(self._uninstaller_path):
            self._logger.info("7-Zip is not installed")
            return

        self._logger.debug("Starting 7-Zip uninstaller")
        Application().start(self._uninstaller_path)

        self._logger.debug("Connecting to 7-Zip uninstaller")
        app = Application().connect(title_re="7-Zip.*", timeout=30)
        window = app.window()

        self._logger.debug("Confirming 7-Zip uninstallation")
        window["&Uninstall"].wait("ready", timeout=10).click()

        self._logger.debug("Finishing 7-Zip uninstallation")
        window["&Close"].wait("ready", timeout=30).click()

        self._logger.info("7-Zip uninstalled")
