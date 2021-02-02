# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\a\git\PolarBear\ui\options.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Options(object):
    def setupUi(self, Options):
        Options.setObjectName("Options")
        Options.resize(536, 267)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        Options.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Options)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_open_presets = QtWidgets.QPushButton(Options)
        self.btn_open_presets.setObjectName("btn_open_presets")
        self.gridLayout_3.addWidget(self.btn_open_presets, 1, 1, 1, 1)
        self.btn_refresh_presets = QtWidgets.QPushButton(Options)
        self.btn_refresh_presets.setObjectName("btn_refresh_presets")
        self.gridLayout_3.addWidget(self.btn_refresh_presets, 1, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(Options)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)
        self.btn_help = QtWidgets.QPushButton(Options)
        self.btn_help.setObjectName("btn_help")
        self.gridLayout_3.addWidget(self.btn_help, 1, 3, 1, 1)
        self.combo_preset = QtWidgets.QComboBox(Options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_preset.sizePolicy().hasHeightForWidth())
        self.combo_preset.setSizePolicy(sizePolicy)
        self.combo_preset.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.combo_preset.setObjectName("combo_preset")
        self.gridLayout_3.addWidget(self.combo_preset, 0, 1, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.line_3 = QtWidgets.QFrame(Options)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.label_5 = QtWidgets.QLabel(Options)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.line_edit_save_path = QtWidgets.QLineEdit(Options)
        self.line_edit_save_path.setObjectName("line_edit_save_path")
        self.gridLayout.addWidget(self.line_edit_save_path, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(Options)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(Options)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(4, 4, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.btn_open_folder = QtWidgets.QToolButton(Options)
        self.btn_open_folder.setObjectName("btn_open_folder")
        self.gridLayout.addWidget(self.btn_open_folder, 0, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(Options)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.spin_fps = QtWidgets.QSpinBox(Options)
        self.spin_fps.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spin_fps.setMinimum(1)
        self.spin_fps.setMaximum(9999)
        self.spin_fps.setProperty("value", 30)
        self.spin_fps.setObjectName("spin_fps")
        self.gridLayout.addWidget(self.spin_fps, 1, 2, 1, 2)
        self.spin_width = QtWidgets.QSpinBox(Options)
        self.spin_width.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spin_width.setMinimum(2)
        self.spin_width.setMaximum(9999)
        self.spin_width.setSingleStep(2)
        self.spin_width.setProperty("value", 800)
        self.spin_width.setObjectName("spin_width")
        self.gridLayout.addWidget(self.spin_width, 2, 2, 1, 2)
        self.spin_height = QtWidgets.QSpinBox(Options)
        self.spin_height.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spin_height.setMinimum(2)
        self.spin_height.setMaximum(9999)
        self.spin_height.setSingleStep(2)
        self.spin_height.setProperty("value", 600)
        self.spin_height.setObjectName("spin_height")
        self.gridLayout.addWidget(self.spin_height, 3, 2, 1, 2)
        self.label_9 = QtWidgets.QLabel(Options)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_reset = QtWidgets.QPushButton(Options)
        self.btn_reset.setObjectName("btn_reset")
        self.horizontalLayout_5.addWidget(self.btn_reset)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.btn_ok = QtWidgets.QPushButton(Options)
        self.btn_ok.setObjectName("btn_ok")
        self.horizontalLayout_5.addWidget(self.btn_ok)
        self.btn_cancel = QtWidgets.QPushButton(Options)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_5.addWidget(self.btn_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Options)
        QtCore.QMetaObject.connectSlotsByName(Options)

    def retranslateUi(self, Options):
        _translate = QtCore.QCoreApplication.translate
        Options.setWindowTitle(_translate("Options", "options"))
        self.btn_open_presets.setText(_translate("Options", "Open Presets Folder"))
        self.btn_refresh_presets.setText(_translate("Options", "Refresh Presets"))
        self.label_10.setText(_translate("Options", "Preset"))
        self.btn_help.setText(_translate("Options", "Presets Help"))
        self.label_5.setText(_translate("Options", "Other"))
        self.label_6.setText(_translate("Options", "Default Save Path"))
        self.label_7.setText(_translate("Options", "Default FPS"))
        self.btn_open_folder.setText(_translate("Options", "🗀"))
        self.label_8.setText(_translate("Options", "Default Width"))
        self.label_9.setText(_translate("Options", "Default Height"))
        self.btn_reset.setText(_translate("Options", "Reset"))
        self.btn_ok.setText(_translate("Options", "Ok"))
        self.btn_cancel.setText(_translate("Options", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Options = QtWidgets.QDialog()
    ui = Ui_Options()
    ui.setupUi(Options)
    Options.show()
    sys.exit(app.exec_())
