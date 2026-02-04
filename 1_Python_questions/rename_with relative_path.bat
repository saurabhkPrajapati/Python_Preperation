@echo off

color A
setlocal enabledelayedexpansion
set "folder_path=D:\stark\OH_PlantNewStruscture\docdateextraction\GENERAL_OUTPUT"

for /r "%folder_path%" %%A in (*.pdf) do (
set "filename=%%~nA"
set "new_filename=!filename:_1=!"
ren "%%A" "!new_filename!%%~xA"
)


echo File names modified successfully.
pause