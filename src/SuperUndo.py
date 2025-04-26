from PySide2.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QWidget, QPushButton, QLineEdit, QMainWindow
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont, QIntValidator
import shiboken2
import maya.OpenMayaUI as omui
import maya.cmds as cmds

def GetMayaMainWindow() -> QMainWindow:
    mainWindow = omui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(mainWindow), QMainWindow)

def DeleteWidgetWithName(name):
    for widget in GetMayaMainWindow().findChildren(QWidget, name):
        widget.deleteLater()

class MayaWindow(QWidget):
    def __init__(self):
        DeleteWidgetWithName(self.GetWidgetUniqueName())
        super().__init__(parent=GetMayaMainWindow())
        self.setWindowFlags(Qt.Window)
        self.setObjectName(self.GetWidgetUniqueName())
        self.setWindowTitle("SuperUndo Plugin")
        self.setMinimumSize(300, 200)
        self.InitUI()
        self.show()

    def GetWidgetUniqueName(self):
        return "shdkovcnaofojqefqiugfc"

    def InitUI(self):
        main_layout = QVBoxLayout(self)

        title_label = QLabel("SuperUndo", self)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        title_label.setFont(font)
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label, alignment=Qt.AlignCenter)

        Undos_Layout = QHBoxLayout()
        FiveUndosbtn = QPushButton("Undo x5", self)
        Undos_Layout.addWidget(FiveUndosbtn)
        FiveUndosbtn.clicked.connect(lambda: self.undo_action(5))
        TenUndosbtn = QPushButton("Undo x10", self)
        Undos_Layout.addWidget(TenUndosbtn)
        TenUndosbtn.clicked.connect(lambda: self.undo_action(10))
        FifteenUndosbtn = QPushButton("Undo x15", self)
        Undos_Layout.addWidget(FifteenUndosbtn)
        FifteenUndosbtn.clicked.connect(lambda: self.undo_action(15))

        Redos_Layout = QHBoxLayout()
        FiveRedosbtn = QPushButton("Redo x5", self)
        Redos_Layout.addWidget(FiveRedosbtn)
        FiveRedosbtn.clicked.connect(lambda: self.redo_action(5))
        TenRedosbtn = QPushButton("Redo x10", self)
        Redos_Layout.addWidget(TenRedosbtn)
        TenRedosbtn.clicked.connect(lambda: self.redo_action(10))
        FifteenRedosbtn = QPushButton("Redo x15", self)
        Redos_Layout.addWidget(FifteenRedosbtn)
        FifteenRedosbtn.clicked.connect(lambda: self.redo_action(15))

        main_layout.addLayout(Undos_Layout)
        main_layout.addLayout(Redos_Layout)

        self.custom_amount_input = QLineEdit(self)
        self.custom_amount_input.setPlaceholderText("Enter amount")
        self.custom_amount_input.setFixedWidth(100)
        self.custom_amount_input.setAlignment(Qt.AlignCenter)
        self.custom_amount_input.setValidator(QIntValidator(1, 999))
        main_layout.addWidget(self.custom_amount_input, alignment=Qt.AlignCenter)

        custom_buttons_layout = QHBoxLayout()
        CustomUndoBtn = QPushButton("Custom Undo", self)
        CustomUndoBtn.clicked.connect(self.custom_undo)
        custom_buttons_layout.addWidget(CustomUndoBtn)
        CustomRedoBtn = QPushButton("Custom Redo", self)
        CustomRedoBtn.clicked.connect(self.custom_redo)
        custom_buttons_layout.addWidget(CustomRedoBtn)
        main_layout.addLayout(custom_buttons_layout)

    def custom_undo(self):
        text = self.custom_amount_input.text()
        if text.isdigit():
            amount = int(text)
            for _ in range(amount):
                cmds.undo()

    def custom_redo(self):
        text = self.custom_amount_input.text()
        if text.isdigit():
            amount = int(text)
            for _ in range(amount):
                cmds.redo()

    def undo_action(self, amount):
        for _ in range(amount):
            cmds.undo()

    def redo_action(self, amount):
        for _ in range(amount):
            cmds.redo()

MayaWindow()