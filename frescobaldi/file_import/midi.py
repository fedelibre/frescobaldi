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
Import Midi dialog.
Uses midi2ly to create ly file from midi.
In the dialog the options of midi2ly can be set.
"""


from PyQt6.QtCore import QSettings, QSize
from PyQt6.QtWidgets import (QCheckBox, QComboBox, QDialogButtonBox, QLabel)

import app
import qutil

from . import toly_dialog



class Dialog(toly_dialog.ToLyDialog):

    def __init__(self, parent=None):

        self.useAbsCheck = QCheckBox()

        self.impChecks = [self.useAbsCheck]

        self.useAbsCheck.setObjectName("absolute-mode")

        self.impExtra = []

        super().__init__(
            parent,
            imp_prgm='midi2ly',
            userg='midi_import')

        app.translateUI(self)
        qutil.saveDialogSize(self, "midi_import/dialog/size", QSize(480, 260))

        self.loadSettings()

    def translateUI(self):
        self.useAbsCheck.setText(_("Pitches in absolute mode"))

        self.buttons.button(QDialogButtonBox.StandardButton.Ok).setText(_("Run midi2ly"))

        super().translateUI()

    def configure_job(self):
        super().configure_job()
        if self.useAbsCheck.isChecked():
            self._job.add_argument('-a')

    def loadSettings(self):
        """Get users previous settings."""
        self.imp_default = [False]
        self.settings = QSettings()
        self.settings.beginGroup('midi_import')
        super().loadSettings()

    def saveSettings(self):
        """Save users last settings."""
        self.settings = QSettings()
        self.settings.beginGroup('midi_import')
        super().saveSettings()
