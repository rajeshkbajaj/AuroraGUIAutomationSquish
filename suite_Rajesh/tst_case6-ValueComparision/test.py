# -*- coding: utf-8 -*-
import names
import subprocess
import builtins

lower_limit = 15
upper_limit = 20

def is_within_range(data, lower_limit, upper_limit):
    return lower_limit <= data <= upper_limit

def main():
    file_path = f'C:\\Users\\rajesh.bajaj\\Desktop\\QTAURORA\\QTApplicationFilesForWindowsLatest'

    # Run 980_simulator.exe
    application1_path = file_path + "\\980_simulator.exe"
    a=subprocess.Popen(application1_path)
    snooze(5)
    startApplication("MedtronicUI")
    setWindowState(waitForObject(names.mainWindow_QQuickApplicationWindow), WindowState.Maximize)
    snooze(5)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle), 163, 98, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle), 1078, 459, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_2), 1081, 453, Qt.LeftButton)
    snooze(1)
    test.vp("VP1")
    test.compare(str(waitForObjectExists(names.flickable_18_PatientDataBlinkingLabel).text), "18")
    Ppeak = builtins.int(str(waitForObjectExists(names.flickable_18_PatientDataBlinkingLabel).text))
    
    if is_within_range(Ppeak, lower_limit, upper_limit):
        print(f"{Ppeak} is within the range [{lower_limit}, {upper_limit}]")
    else:
        print(f"{Ppeak} is NOT within the range [{lower_limit}, {upper_limit}]")
    
    snooze(1)
    test.vp("VP2")
    test.compare(str(waitForObjectExists(names.flickable_31_PatientDataBlinkingLabel).text), "31")
    snooze(1)
    test.vp("VP3")
    test.compare(str(waitForObjectExists(names.flickable_10_PatientDataBlinkingLabel).text), "10")
    snooze(1)
    test.vp("VP4")
    test.compare(str(waitForObjectExists(names.flickable_1_5_0_PatientDataBlinkingLabel).text), "1:5.0")
    snooze(1)
    test.vp("VP5")
    test.compare(str(waitForObjectExists(names.flickable_6_2_PatientDataBlinkingLabel).text), "6.2")
    snooze(1)
    test.vp("VP6")
    test.compare(str(waitForObjectExists(names.flickable_7_1_PatientDataBlinkingLabel).text), "7.1")
    test.compare(str(waitForObjectExists(names.flickable_7_1_PatientDataBlinkingLabel).text), "7.0")
    snooze(2.6)
    closeWindow(names.mainWindow_QQuickApplicationWindow)
    a.kill()
    
