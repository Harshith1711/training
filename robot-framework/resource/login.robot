*** Settings ***

Library     SeleniumLibrary
Library    XML


*** Variables ***

${browser}   chrome
${url}       https://automationplayground.com/crm/
${password}  Harshith00

*** Keywords ***
loginRobot
    Open Browser    browser=${browser}
    Maximize Browser Window
    Go To    ${url}
    Click Element    xpath://*[@id="SignIn"]
    Press Keys       xpath://*[@id="email-id"]     harshith@gmail.com
    Press Keys       xpath://*[@id="password"]      ${password}
    Click Element    xpath://*[@id="submit-id"]
logOut
    Click Element    xpath://*[@class="nav-link"]

