*** Settings ***
Library             RobotProcessLibrary.py

*** Test Cases ***
Example
    Run Robot Process    tasks.robot
    Run Robot Process    tasks.robot    variable=SUBJECT:Custom subject
