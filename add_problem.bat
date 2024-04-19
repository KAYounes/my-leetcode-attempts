@echo off
setlocal enabledelayedexpansion

rem Check if the number of arguments is correct
if "%~1"=="" (
    echo Usage: %0 filename
    exit /b 1
)

rem Get the filename from the command line argument
set "filename=%~1"

rem Remove non-alphanumeric characters and replace spaces with underscore
set "filename_clean=%filename%"
set "filename_clean=!filename_clean: =_!"
for /f "tokens=1 delims=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_" %%A in ("%filename_clean%") do (
    set "filename_clean=!filename_clean:%%A=_!"
)

rem Replace consecutive underscores with a single underscore
set "filename_clean=!filename_clean:_=_!"
set "filename_clean=!filename_clean:__=_!"

rem Add .py extension to the filename
set "filename_py=%filename_clean%.py"

rem Create the new file with .py extension
copy nul "%filename_py%" > nul

echo File '%filename_py%' created with cleaned name.
