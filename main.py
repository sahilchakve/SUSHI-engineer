import os
import sys

import webview

APP_TITLE = "SUSHI - Study Helper"
PAGE = "sushi_study_helper_v46.html"


def resource_path(name):
    # When packed by PyInstaller, bundled files live in sys._MEIPASS
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, name)


def main():
    page = resource_path(PAGE)
    url = "file:///" + page.replace("\\", "/")
    webview.create_window(
        APP_TITLE,
        url,
        width=1280,
        height=820,
        min_size=(900, 600),
        background_color="#02080c",
    )
    webview.start()


if __name__ == "__main__":
    main()
