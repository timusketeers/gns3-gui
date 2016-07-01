#!/usr/bin/env python
#
# Copyright (C) 2016 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gns3.qt import QtGui, QtCore


from gns3.items.note_item import NoteItem


def test_dump():
    note = NoteItem()
    note.setPlainText("Test")
    font = QtGui.QFont()
    font.setPointSize(55)
    font.setFamily("Verdana")
    note.setFont(font)
    note.setDefaultTextColor(QtCore.Qt.red)

    assert note.dump() == {
        "text": "Test",
        "x": 0,
        "y": 0,
        "style": "font-family: Verdana"
    }