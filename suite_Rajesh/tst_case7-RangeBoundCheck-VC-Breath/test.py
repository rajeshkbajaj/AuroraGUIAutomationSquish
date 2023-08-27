# -*- coding: utf-8 -*-

import names
import subprocess


def main():
    file_path = f'C:\\Users\\rajesh.bajaj\\Desktop\\QTAURORA\\QTApplicationFilesForWindowsLatest'

    # Run 980_simulator.exe
    application1_path = file_path + "\\980_simulator.exe"
    a = subprocess.Popen(application1_path)
    snooze(5)
    
    startApplication("MedtronicUI")
    setWindowState(waitForObject(names.mainWindow_QQuickApplicationWindow), WindowState.Maximize)
    snooze(2)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle), 132, 110, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle), 1059, 450, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_2), 1056, 456, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_button_Button_8), 22, 21, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_10_BlinkingLabel))
    snooze(2)
    for i in range(16):
        doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 37, 29, Qt.LeftButton)
    snooze(2)
    mouseClick(waitForObject(names.mainWindow_backgroundRectangle_Rectangle), 121, 50, Qt.LeftButton)
    snooze(2)
    mouseClick(waitForObject(names.mainWindow_Continue_StyledButton_2), 58, 15, Qt.LeftButton)
    for i in range(13):
        doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 18, 24, Qt.LeftButton)
    snooze(2)
    mouseClick(waitForObject(names.mainWindow_image_IconImage_2), 9, 7, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_3), 488, 256, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_3), 415, 172, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 29, 24, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_increaseButton_Button), 29, 24, Qt.LeftButton)
    snooze(2)
    mouseClick(waitForObject(names.mainWindow_image_IconImage_2), 7, 8, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_3), 530, 180, Qt.LeftButton)
    for i in range(54):
        doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 30, 17, Qt.LeftButton)
    snooze(2)
    mouseClick(waitForObject(names.mainWindow_image_IconImage_2), 14, 8, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_3), 298, 170, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 25, 22, Qt.LeftButton)
    for i in range(18):
        doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 24, 21, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_3), 563, 255, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_3), 403, 169, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_increaseButton_Button), 32, 24, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 32, 24, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 32, 24, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 32, 24, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 32, 24, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 32, 24, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 32, 24, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 32, 24, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 32, 24, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 32, 24, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 32, 24, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 32, 24, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 32, 24, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_Continue_StyledButton_2), 40, 19, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 27, 20, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 27, 20, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 27, 20, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 27, 20, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 27, 20, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 27, 20, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 27, 20, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 27, 20, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_increaseButton_Button), 27, 20, Qt.LeftButton)
    snooze(2)
    mouseClick(waitForObject(names.mainWindow_image_IconImage_2), 14, 7, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_3), 589, 277, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_3), 1083, 285, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_increaseButton_Button), 34, 23, Qt.LeftButton)
    for i in range(31):
        doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 34, 23, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_closePopupButton_ToolButton), 27, 14, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_3), 741, 158, Qt.LeftButton)
    for i in range(86):
        doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 35, 21, Qt.LeftButton)
    snooze(2)
    mouseClick(waitForObject(names.mainWindow_closePopupButton_ToolButton), 29, 17, Qt.LeftButton)
    snooze(2)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_3), 760, 275, Qt.LeftButton)
    for i in range(32):
        doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 32, 17, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_image_IconImage_2), 7, 13, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_3), 991, 183, Qt.LeftButton)
    for i in range(12):
        doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 33, 25, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_image_IconImage_2), 12, 3, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_3), 850, 180, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_increaseButton_Button), 21, 17, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_image_IconImage_2), 12, 8, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_3), 840, 291, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_3), 981, 285, Qt.LeftButton)
    for i in range(20):
        doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 23, 28, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_increaseButton_Button), 23, 28, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_image_IconImage_2), 9, 9, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_3), 1041, 456, Qt.LeftButton)
    snooze(3.8)
    closeWindow(names.mainWindow_QQuickApplicationWindow)
    a.kill()
    
    
    
    