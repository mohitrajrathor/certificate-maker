@echo off
rem Check if a filename is provided as an argument
if "%1" == "" (
    echo Usage: %0 filename
    exit /b 1
)

rem Execute the file
"%1"
