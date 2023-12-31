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
    
    mouseClick(waitForObject(names.mainWindow_background_Rectangle_2), 1280, 136, Qt.LeftButton)
    setWindowState(waitForObject(names.mainWindow_QQuickApplicationWindow), WindowState.Maximize)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle), 174, 97, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle), 68, 256, Qt.LeftButton)
    mouseClick(waitForObject(names.pediatric_Label))
    mouseClick(waitForObject(names.mainWindow_border_Rectangle), 68, 256, Qt.LeftButton)
    mouseClick(waitForObject(names.adult_Label))
    mouseClick(waitForObject(names.mainWindow_border_Rectangle), 371, 260, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 29, 27, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_Continue_StyledButton_2), 17, 17, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_decreaseButton_Button), 32, 19, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_image_IconImage_2), 11, 6, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle), 486, 325, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle), 522, 252, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 36, 25, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle), 529, 376, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_button_Button), 24, 21, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_2), 362, 58, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_2), 1030, 456, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_button_Button), 17, 25, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_2), 288, 57, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_2), 1052, 454, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle), 262, 177, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle), 1068, 463, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_2), 1063, 461, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_buttonBackground_Rectangle), 16, 21, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 30, 29, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_increaseButton_Button), 30, 29, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_increaseButton_Button), 30, 29, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_3), 1083, 466, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_buttonBackground_Rectangle_2), 42, 48, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_decreaseButton_Button), 27, 24, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_decreaseButton_Button), 27, 24, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_3), 1075, 456, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_button_Button_3), 20, 13, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_Cancel_StyledButton), 33, 18, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_button_Button_6), 12, 22, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_4), 1029, 465, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_patientInfoColumn_Rectangle), 268, 33, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_3), 55, 158, Qt.LeftButton)
    mouseDrag(waitForObject(names.mainWindow_border_Rectangle_3), 356, 200, 8, -45, Qt.NoModifier, Qt.LeftButton)
    mouseDrag(waitForObject(names.mainWindow_border_Rectangle_3), 645, 252, 0, -139, Qt.NoModifier, Qt.LeftButton)
    mouseDrag(waitForObject(names.mainWindow_border_Rectangle_3), 776, 220, -3, -113, Qt.NoModifier, Qt.LeftButton)
    mouseDrag(waitForObject(names.mainWindow_border_Rectangle_3), 930, 289, 4, 80, Qt.NoModifier, Qt.LeftButton)
    mouseDrag(waitForObject(names.mainWindow_border_Rectangle_3), 793, 288, 7, 136, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_3), 1067, 458, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_button_Button_4), 27, 19, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_3), 91, 119, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_3), 101, 158, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_3), 1072, 454, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_button_Button_2), 26, 23, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_button_Button_8), 19, 22, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_button_Button_5), 19, 19, Qt.LeftButton)
    mouseClick(waitForObject(names.shorcut_1_Label))
    mouseClick(waitForObject(names.mainWindow_button_Button_9), 12, 21, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_4), 439, 379, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_decreaseButton_Button), 31, 15, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_decreaseButton_Button), 31, 15, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_3), 1066, 451, Qt.LeftButton)
    mouseClick(waitForObject(names.flickable_18_PatientDataBlinkingLabel))
    mouseClick(waitForObject(names.flickable_buttonBackground_Rectangle_4), 53, 30, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_dismissButton_ToolButton_2), 32, 22, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_dismissButton_ToolButton), 47, 21, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_Close_StyledButton), 121, 19, Qt.LeftButton)
    snooze(2.6)
    closeWindow(names.mainWindow_QQuickApplicationWindow)
    a.kill()
