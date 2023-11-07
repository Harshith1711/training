*** Settings ***

Library     SeleniumLibrary
Library    Telnet
Resource    ../resource/login.robot

*** Variables ***

${browser}   chrome
${url}       https://automationplayground.com/crm/
${dd}        https://rahulshettyacademy.com/AutomationPractice/
*** Test Cases ***

loginPage
    loginRobot
    logOut
    Close Browser

dropdown
    Open Browser  browser=${browser}
    Maximize Browser Window
    Go To    ${dd}
    Select From List By Value   //*[@id="dropdown-class-example"]   option1
    Sleep  10
    Select From List By Index    //*[@id="dropdown-class-example"]  2
    Sleep    10
    ${text}  Set Variable   1
    Log To Console  ${text}
    ${text1}    Get Text    //*[@id="dropdown-class-example"]
    Log      ${text1}