@echo off
setlocal enabledelayedexpansion

set "folderPath=D:\stark\OH_PlantNewStruscture\docdateextraction\GENERAL_OUTPUT\OH_MONTGOMERY\070723122324\01032000-01032000\PDF_FILES"
set "searchString=_1"
set "replaceString="

for %%F in ("%folderPath%\*%searchString%.pdf") do (
set "fileName=%%~nxF"
set "newFileName=!fileName:%searchString%=%replaceString%!
ren "%%F" "!newFileName!"
)

echo File names modified successfully.



