#!/usr/bin/env python3
# Copyright © 2012-13 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version. It is provided for
# educational purposes and is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

import sys
if sys.version_info < (3, 2):
    print("requires Python 3.2+ for concurrent.futures")
    sys.exit(1)
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                             "..")))
import tkinter as tk
import Main
import TkUtil
import TkUtil.Settings
from Globals import *


def main():
    application = tk.Tk()
    application.withdraw() # hide until ready to show
    application.title(APPNAME)
    application.option_add("*tearOff", False) # Avoid ugly tear menu line
    TkUtil.Settings.DOMAIN = "Qtrac"
    TkUtil.Settings.APPNAME = APPNAME
    settings = TkUtil.Settings.load()
    TkUtil.set_application_icons(application, os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "images"))
    window = Main.Window(application)
    application.protocol("WM_DELETE_WINDOW", window.close)
    application.deiconify() # show
    application.mainloop()


if __name__ == "__main__":
    main()
