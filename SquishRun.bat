REM add Squish to PATH
set SQUISH_PREFIX=C:\Squish for Qt 7.1.1
set PATH=%SQUISH_PREFIX%\bin;%PATH%


REM The Log Directory does not (but perhaps should) have today's date in it:
set LOGDIRECTORY=%USERPROFILE%\squish-results

REM Execute the test suite with a --local squishserver:
squishrunner --testsuite %USERPROFILE%\suite_Rajesh --local --reportgen "xml3.5,%LOGDIRECTORY%"

testcentercmd --url=http://localhost:8800 --token=2Qiu0-_hADyqmaYlhN1nkBYOHvM4aeUnqg302ZVDOow upload Aurora %USERPROFILE%\squish-results --label=OS-WINDOWS --batch=2.0
    