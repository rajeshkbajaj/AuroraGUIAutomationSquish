@echo off

set TEST_SUITE="C:\Users\rajesh.bajaj\suite_Rajesh"
set TEST_CASE1="tst_case1-SanityGUICheck"
set TEST_CASE2="tst_case6-ValueComparision"

:: Squish
set SQUISH_PATH="C:\Squish for Qt 7.1.1"

%SQUISH_PATH%\bin\squishrunner.exe ^
    --testsuite %TEST_SUITE% ^
    --testcase %TEST_CASE1% ^
    --testcase %TEST_CASE2% ^
    --local
    
	
