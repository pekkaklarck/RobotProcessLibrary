*** Variables ***
${SUBJECT}        Example subject


*** Test Cases ***
Process email
    Read email
    Validate email
    Send information

*** Keywords ***
Read email
    Log    Reading information from email with subject "${SUBJECT}".

Validate email
    Log    Some strange but acceptable value found.    WARN

Send information
    No operation
