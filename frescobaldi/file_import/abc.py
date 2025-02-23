# This file is part of the Frescobaldi project, http://www.frescobaldi.org/
#
# Copyright (c) 2008 - 2014 by Wilbert Berendsen
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# See http://www.gnu.org/licenses/ for more information.

"""
Import ABC dialog.
Uses abc2ly to create ly file from abc.
In the dialog the options of abc2ly can be set.
"""


import os

from PyQt6.QtCore import QSettings, QSize
from PyQt6.QtWidgets import (QCheckBox, QComboBox, QDialogButtonBox, QLabel)

import app
import util
import qutil

from . import toly_dialog


class Dialog(toly_dialog.ToLyDialog):

    def __init__(self, parent=None):

        self.nobeamCheck = QCheckBox()

        self.impChecks = [self.nobeamCheck]

        self.nobeamCheck.setObjectName("import-beaming")

        self.impExtra = []

        super().__init__(
            parent,
            imp_prgm='abc2ly',
            userg='abc_import')

        app.translateUI(self)
        qutil.saveDialogSize(self, "abc_import/dialog/size", QSize(480, 160))

        self.loadSettings()

    def translateUI(self):
        self.nobeamCheck.setText(_("Import beaming"))

        self.buttons.button(QDialogButtonBox.StandardButton.Ok).setText(_("Run abc2ly"))

        super().translateUI()

    def configure_job(self):
        super().configure_job()
        if self.nobeamCheck.isChecked():
            self._job.add_argument('-b')

    def loadSettings(self):
        """Get users previous settings."""
        self.imp_default = [True]
        self.settings = QSettings()
        self.settings.beginGroup('abc_import')
        super().loadSettings()

    def saveSettings(self):
        """Save users last settings."""
        self.settings = QSettings()
        self.settings.beginGroup('abc_import')
        super().saveSettings()
