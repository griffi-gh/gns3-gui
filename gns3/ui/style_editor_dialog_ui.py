# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/grossmj/PycharmProjects/gns3-gui/gns3/ui/style_editor_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StyleEditorDialog(object):
    def setupUi(self, StyleEditorDialog):
        StyleEditorDialog.setObjectName("StyleEditorDialog")
        StyleEditorDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(StyleEditorDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiStyleSettingsGroupBox = QtWidgets.QGroupBox(StyleEditorDialog)
        self.uiStyleSettingsGroupBox.setObjectName("uiStyleSettingsGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.uiStyleSettingsGroupBox)
        self.formLayout.setObjectName("formLayout")
        self.uiColorLabel = QtWidgets.QLabel(self.uiStyleSettingsGroupBox)
        self.uiColorLabel.setObjectName("uiColorLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.uiColorLabel)
        self.uiColorPushButton = QtWidgets.QPushButton(self.uiStyleSettingsGroupBox)
        self.uiColorPushButton.setText("")
        self.uiColorPushButton.setObjectName("uiColorPushButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.uiColorPushButton)
        self.uiBorderColorLabel = QtWidgets.QLabel(self.uiStyleSettingsGroupBox)
        self.uiBorderColorLabel.setObjectName("uiBorderColorLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.uiBorderColorLabel)
        self.uiBorderColorPushButton = QtWidgets.QPushButton(self.uiStyleSettingsGroupBox)
        self.uiBorderColorPushButton.setText("")
        self.uiBorderColorPushButton.setObjectName("uiBorderColorPushButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.uiBorderColorPushButton)
        self.uiBorderWidthLabel = QtWidgets.QLabel(self.uiStyleSettingsGroupBox)
        self.uiBorderWidthLabel.setObjectName("uiBorderWidthLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.uiBorderWidthLabel)
        self.uiBorderWidthSpinBox = QtWidgets.QSpinBox(self.uiStyleSettingsGroupBox)
        self.uiBorderWidthSpinBox.setMinimum(1)
        self.uiBorderWidthSpinBox.setMaximum(100)
        self.uiBorderWidthSpinBox.setProperty("value", 2)
        self.uiBorderWidthSpinBox.setObjectName("uiBorderWidthSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.uiBorderWidthSpinBox)
        self.uiBorderStyleLabel = QtWidgets.QLabel(self.uiStyleSettingsGroupBox)
        self.uiBorderStyleLabel.setObjectName("uiBorderStyleLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.uiBorderStyleLabel)
        self.uiBorderStyleComboBox = QtWidgets.QComboBox(self.uiStyleSettingsGroupBox)
        self.uiBorderStyleComboBox.setObjectName("uiBorderStyleComboBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.uiBorderStyleComboBox)
        #
        self.uiBorderRadiusLabel = QtWidgets.QLabel(self.uiStyleSettingsGroupBox)
        self.uiBorderRadiusLabel.setObjectName("uiBorderRadiusLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.uiBorderRadiusLabel)
        self.uiBorderRadiusSpinBox = QtWidgets.QSpinBox(self.uiStyleSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiBorderRadiusSpinBox.sizePolicy().hasHeightForWidth())
        self.uiBorderRadiusSpinBox.setSizePolicy(sizePolicy)
        self.uiBorderRadiusSpinBox.setMinimum(0)
        self.uiBorderRadiusSpinBox.setMaximum(100)
        self.uiBorderRadiusSpinBox.setObjectName("uiBorderRadiusSpinBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.uiBorderRadiusSpinBox)
        #
        self.uiRotationLabel = QtWidgets.QLabel(self.uiStyleSettingsGroupBox)
        self.uiRotationLabel.setObjectName("uiRotationLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.uiRotationLabel)
        self.uiRotationSpinBox = QtWidgets.QSpinBox(self.uiStyleSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRotationSpinBox.sizePolicy().hasHeightForWidth())
        self.uiRotationSpinBox.setSizePolicy(sizePolicy)
        self.uiRotationSpinBox.setMinimum(-360)
        self.uiRotationSpinBox.setMaximum(360)
        self.uiRotationSpinBox.setObjectName("uiRotationSpinBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.uiRotationSpinBox)
        self.verticalLayout.addWidget(self.uiStyleSettingsGroupBox)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(StyleEditorDialog)
        self.uiButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.verticalLayout.addWidget(self.uiButtonBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(StyleEditorDialog)
        self.uiButtonBox.accepted.connect(StyleEditorDialog.accept)
        self.uiButtonBox.rejected.connect(StyleEditorDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(StyleEditorDialog)

    def retranslateUi(self, StyleEditorDialog):
        _translate = QtCore.QCoreApplication.translate
        StyleEditorDialog.setWindowTitle(_translate("StyleEditorDialog", "Style editor"))
        self.uiStyleSettingsGroupBox.setTitle(_translate("StyleEditorDialog", "Style settings"))
        self.uiColorLabel.setText(_translate("StyleEditorDialog", "Fill color:"))
        self.uiBorderColorLabel.setText(_translate("StyleEditorDialog", "Border color:"))
        self.uiBorderWidthLabel.setText(_translate("StyleEditorDialog", "Border width:"))
        self.uiBorderWidthSpinBox.setSuffix(_translate("StyleEditorDialog", " px"))
        self.uiBorderStyleLabel.setText(_translate("StyleEditorDialog", "Border style:"))
        self.uiBorderRadiusLabel.setText(_translate("StyleEditorDialog", "Border Radius:"))
        self.uiRotationLabel.setText(_translate("StyleEditorDialog", "Rotation:"))
        self.uiRotationSpinBox.setToolTip(_translate("StyleEditorDialog", "Rotation can be ajusted on the scene for a selected item while\n"
"editing (notes only) with ALT and \'+\' (or P) / ALT and \'-\' (or M)"))
        self.uiRotationSpinBox.setSuffix(_translate("StyleEditorDialog", "°"))
from . import resources_rc
