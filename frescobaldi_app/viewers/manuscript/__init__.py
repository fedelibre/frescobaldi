# This file is part of the Frescobaldi project, http://www.frescobaldi.org/
#
# Copyright (c) 2011 - 2014 by Wilbert Berendsen
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
A tool to display an engraver's copy in a dock.
"""

from __future__ import unicode_literals

from PyQt4.QtCore import Qt
from PyQt4.QtGui import (
    QAction, QKeySequence, QVBoxLayout, QToolButton,
    QHBoxLayout, QPushButton, QFileDialog)

import actioncollection
import actioncollectionmanager
import app
import icons
import panel
import userguide.util

import viewers
from viewers import popplerwidget

class ManuscriptViewPanel(viewers.AbstractViewPanel):
    """Manuscript Viewer Tool."""
    def __init__(self, mainwindow):
        super(ManuscriptViewPanel, self).__init__(mainwindow, Actions)
        self.hide()
        self.toggleViewAction().setShortcut(QKeySequence("Meta+Alt+A"))
        mainwindow.addDockWidget(Qt.TopDockWidgetArea, self)

    def translateUI(self):
        self.setWindowTitle(_("Manuscript"))
        self.toggleViewAction().setText(_("Display Manuscript"))

    def createWidget(self):
        from . import widget
        return super(ManuscriptViewPanel, self).configureWidget(widget.Widget(self))

    @viewers.activate
    def reloadView(self):
        active_manuscript = self.widget().currentDocument()
        if active_manuscript:
            try:
                self.widget().openDocument(active_manuscript.filename())
            except OSError:
                # If the file is not present (anymore) simply don't do anything
                pass


class Actions(viewers.Actions):
    name = "manuscript"

    def createActions(self, parent=None):
        super(Actions, self).createActions(parent)
        # overridden actions
        self.music_document_select = DocumentChooserAction(parent)
        # new actions
        self.manuscript_open = QAction(parent)
        self.manuscript_open.setIcon(icons.get('document-open'))
        self.manuscript_close = QAction(parent)
        self.manuscript_close.setIcon(icons.get('document-close'))

    def translateUI(self):
        super(Actions, self).translateUI()
        self.music_document_select.setText(_("Select Manuscript Document"))
        self.manuscript_open.setText(_("Open document"))
        self.manuscript_open.setIconText(_("Open"))
        self.manuscript_close.setText(_("Close document"))
        self.manuscript_close.setIconText(_("Close"))


class DocumentChooserAction(viewers.DocumentChooserAction):
    """Extends the parent class and also keeps track of when a document is
    opened or closed in the manuscript viewer.
    """

    def __init__(self, panel):
        super(DocumentChooserAction, self).__init__(panel)

    def slotDocumentChanged(self, doc):
        """Called when the mainwindow changes its current document."""
        # for now do nothing
        pass

    def slotManuscriptChanged(self, doc):
        """Called when the ManuscriptView widget changes its current document."""
        # only switch our document if there are PDF documents to display
        if self._document is None or documents.group(doc).documents():
            self.setCurrentDocument(doc)

    def slotDocumentUpdated(self, doc, job):
        """Called when a Job, finished on the document, has created new PDFs."""
        # for now do nothing
        pass

    def setCurrentManuscript(self, document):
        """Displays the DocumentGroup of the given manuscript in our chooser."""
        self._documents.append(document)
        self._currentIndex = self._indices.get(document, 0)
        self.updateDocument()