# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/grossmj/PycharmProjects/gns3-gui/gns3/ui/appliance_wizard.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ApplianceWizard(object):
    def setupUi(self, ApplianceWizard):
        ApplianceWizard.setObjectName("ApplianceWizard")
        ApplianceWizard.resize(726, 428)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ApplianceWizard.sizePolicy().hasHeightForWidth())
        ApplianceWizard.setSizePolicy(sizePolicy)
        ApplianceWizard.setMaximumSize(QtCore.QSize(2000, 2000))
        ApplianceWizard.setModal(True)
        ApplianceWizard.setWizardStyle(QtWidgets.QWizard.ClassicStyle)
        ApplianceWizard.setOptions(QtWidgets.QWizard.NoBackButtonOnStartPage)
        self.uiServerWizardPage = QtWidgets.QWizardPage()
        self.uiServerWizardPage.setObjectName("uiServerWizardPage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.uiServerWizardPage)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.uiServerTypeGroupBox = QtWidgets.QGroupBox(self.uiServerWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiServerTypeGroupBox.sizePolicy().hasHeightForWidth())
        self.uiServerTypeGroupBox.setSizePolicy(sizePolicy)
        self.uiServerTypeGroupBox.setMinimumSize(QtCore.QSize(0, 161))
        self.uiServerTypeGroupBox.setObjectName("uiServerTypeGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.uiServerTypeGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uiRemoteRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteRadioButton.sizePolicy().hasHeightForWidth())
        self.uiRemoteRadioButton.setSizePolicy(sizePolicy)
        self.uiRemoteRadioButton.setMinimumSize(QtCore.QSize(0, 20))
        self.uiRemoteRadioButton.setChecked(True)
        self.uiRemoteRadioButton.setObjectName("uiRemoteRadioButton")
        self.verticalLayout_2.addWidget(self.uiRemoteRadioButton)
        self.uiLocalRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiLocalRadioButton.sizePolicy().hasHeightForWidth())
        self.uiLocalRadioButton.setSizePolicy(sizePolicy)
        self.uiLocalRadioButton.setMinimumSize(QtCore.QSize(0, 20))
        self.uiLocalRadioButton.setObjectName("uiLocalRadioButton")
        self.verticalLayout_2.addWidget(self.uiLocalRadioButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_4.addWidget(self.uiServerTypeGroupBox)
        self.uiRemoteServersGroupBox = QtWidgets.QGroupBox(self.uiServerWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServersGroupBox.sizePolicy().hasHeightForWidth())
        self.uiRemoteServersGroupBox.setSizePolicy(sizePolicy)
        self.uiRemoteServersGroupBox.setObjectName("uiRemoteServersGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.uiRemoteServersGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.uiRemoteServersLabel = QtWidgets.QLabel(self.uiRemoteServersGroupBox)
        self.uiRemoteServersLabel.setObjectName("uiRemoteServersLabel")
        self.gridLayout.addWidget(self.uiRemoteServersLabel, 0, 0, 1, 1)
        self.uiRemoteServersComboBox = QtWidgets.QComboBox(self.uiRemoteServersGroupBox)
        self.uiRemoteServersComboBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServersComboBox.sizePolicy().hasHeightForWidth())
        self.uiRemoteServersComboBox.setSizePolicy(sizePolicy)
        self.uiRemoteServersComboBox.setObjectName("uiRemoteServersComboBox")
        self.gridLayout.addWidget(self.uiRemoteServersComboBox, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.uiRemoteServersGroupBox)
        ApplianceWizard.addPage(self.uiServerWizardPage)
        self.uiQemuWizardPage = QtWidgets.QWizardPage()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiQemuWizardPage.sizePolicy().hasHeightForWidth())
        self.uiQemuWizardPage.setSizePolicy(sizePolicy)
        self.uiQemuWizardPage.setObjectName("uiQemuWizardPage")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.uiQemuWizardPage)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.uiQemuListLabel = QtWidgets.QLabel(self.uiQemuWizardPage)
        self.uiQemuListLabel.setObjectName("uiQemuListLabel")
        self.horizontalLayout_2.addWidget(self.uiQemuListLabel)
        self.uiQemuListComboBox = QtWidgets.QComboBox(self.uiQemuWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiQemuListComboBox.sizePolicy().hasHeightForWidth())
        self.uiQemuListComboBox.setSizePolicy(sizePolicy)
        self.uiQemuListComboBox.setObjectName("uiQemuListComboBox")
        self.horizontalLayout_2.addWidget(self.uiQemuListComboBox)
        ApplianceWizard.addPage(self.uiQemuWizardPage)
        self.uiInstructionsPage = QtWidgets.QWizardPage()
        self.uiInstructionsPage.setObjectName("uiInstructionsPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.uiInstructionsPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.uiInstructionsTextEdit = QtWidgets.QTextEdit(self.uiInstructionsPage)
        self.uiInstructionsTextEdit.setObjectName("uiInstructionsTextEdit")
        self.verticalLayout_3.addWidget(self.uiInstructionsTextEdit)
        ApplianceWizard.addPage(self.uiInstructionsPage)
        self.uiFilesWizardPage = QtWidgets.QWizardPage()
        self.uiFilesWizardPage.setObjectName("uiFilesWizardPage")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.uiFilesWizardPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiApplianceVersionTreeWidget = QtWidgets.QTreeWidget(self.uiFilesWizardPage)
        self.uiApplianceVersionTreeWidget.setIndentation(20)
        self.uiApplianceVersionTreeWidget.setObjectName("uiApplianceVersionTreeWidget")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.uiApplianceVersionTreeWidget.headerItem().setFont(0, font)
        self.uiApplianceVersionTreeWidget.header().setDefaultSectionSize(120)
        self.uiApplianceVersionTreeWidget.header().setMinimumSectionSize(20)
        self.verticalLayout.addWidget(self.uiApplianceVersionTreeWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiImportPushButton = QtWidgets.QPushButton(self.uiFilesWizardPage)
        self.uiImportPushButton.setObjectName("uiImportPushButton")
        self.horizontalLayout.addWidget(self.uiImportPushButton)
        self.uiDownloadPushButton = QtWidgets.QPushButton(self.uiFilesWizardPage)
        self.uiDownloadPushButton.setObjectName("uiDownloadPushButton")
        self.horizontalLayout.addWidget(self.uiDownloadPushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.allowCustomFiles = QtWidgets.QCheckBox(self.uiFilesWizardPage)
        self.allowCustomFiles.setToolTip("")
        self.allowCustomFiles.setObjectName("allowCustomFiles")
        self.horizontalLayout.addWidget(self.allowCustomFiles)
        self.uiCreateVersionPushButton = QtWidgets.QPushButton(self.uiFilesWizardPage)
        self.uiCreateVersionPushButton.setObjectName("uiCreateVersionPushButton")
        self.horizontalLayout.addWidget(self.uiCreateVersionPushButton)
        self.uiRefreshPushButton = QtWidgets.QPushButton(self.uiFilesWizardPage)
        self.uiRefreshPushButton.setObjectName("uiRefreshPushButton")
        self.horizontalLayout.addWidget(self.uiRefreshPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        ApplianceWizard.addPage(self.uiFilesWizardPage)
        self.uiUsageWizardPage = QtWidgets.QWizardPage()
        self.uiUsageWizardPage.setObjectName("uiUsageWizardPage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.uiUsageWizardPage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.uiUsageTextEdit = QtWidgets.QTextEdit(self.uiUsageWizardPage)
        self.uiUsageTextEdit.setObjectName("uiUsageTextEdit")
        self.gridLayout_3.addWidget(self.uiUsageTextEdit, 0, 0, 1, 1)
        ApplianceWizard.addPage(self.uiUsageWizardPage)

        self.retranslateUi(ApplianceWizard)
        QtCore.QMetaObject.connectSlotsByName(ApplianceWizard)

    def retranslateUi(self, ApplianceWizard):
        _translate = QtCore.QCoreApplication.translate
        ApplianceWizard.setWindowTitle(_translate("ApplianceWizard", "Install appliance"))
        self.uiServerWizardPage.setTitle(_translate("ApplianceWizard", "Server"))
        self.uiServerWizardPage.setSubTitle(_translate("ApplianceWizard", "Please choose a server type to install the appliance. The grayed out server types are not supported or configured."))
        self.uiServerTypeGroupBox.setTitle(_translate("ApplianceWizard", "Server type"))
        self.uiRemoteRadioButton.setText(_translate("ApplianceWizard", "Install the appliance on a remote server"))
        self.uiLocalRadioButton.setText(_translate("ApplianceWizard", "Install the appliance on the main server"))
        self.uiRemoteServersGroupBox.setTitle(_translate("ApplianceWizard", "Remote server"))
        self.uiRemoteServersLabel.setText(_translate("ApplianceWizard", "Run on:"))
        self.uiQemuWizardPage.setTitle(_translate("ApplianceWizard", "Qemu settings"))
        self.uiQemuWizardPage.setSubTitle(_translate("ApplianceWizard", "Please choose the qemu binary that will be used to run this appliance."))
        self.uiQemuListLabel.setText(_translate("ApplianceWizard", "Qemu binary:"))
        self.uiInstructionsPage.setTitle(_translate("ApplianceWizard", "Installation instructions"))
        self.uiInstructionsPage.setSubTitle(_translate("ApplianceWizard", "Please read the following instructions in order to install your new appliance."))
        self.uiInstructionsTextEdit.setHtml(_translate("ApplianceWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.uiFilesWizardPage.setTitle(_translate("ApplianceWizard", "Required files"))
        self.uiFilesWizardPage.setSubTitle(_translate("ApplianceWizard", "The following files are required to install the appliance"))
        self.uiApplianceVersionTreeWidget.headerItem().setText(0, _translate("ApplianceWizard", "Appliance version and files"))
        self.uiApplianceVersionTreeWidget.headerItem().setText(1, _translate("ApplianceWizard", "Size"))
        self.uiApplianceVersionTreeWidget.headerItem().setText(2, _translate("ApplianceWizard", "Status"))
        self.uiImportPushButton.setText(_translate("ApplianceWizard", "&Import"))
        self.uiDownloadPushButton.setText(_translate("ApplianceWizard", "&Download"))
        self.allowCustomFiles.setText(_translate("ApplianceWizard", "Allow custom files"))
        self.uiCreateVersionPushButton.setText(_translate("ApplianceWizard", "&Create a new version"))
        self.uiRefreshPushButton.setText(_translate("ApplianceWizard", "&Refresh"))
        self.uiUsageWizardPage.setTitle(_translate("ApplianceWizard", "Usage"))
        self.uiUsageWizardPage.setSubTitle(_translate("ApplianceWizard", "Please read the following instructions in order to use your new appliance."))
        self.uiUsageTextEdit.setHtml(_translate("ApplianceWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The default username/password is admin/admin. A default configuration is present.</p></body></html>"))
from . import resources_rc
