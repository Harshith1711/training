*** Settings ***
Library               RequestsLibrary

*** Keywords ***

Get Response Status Code
    [Documentation]    Perform a GET request and check if the status code is 200 or not,if not will fail the test
    ${response}=    GET  https://jsonplaceholder.typicode.com/posts/1
    Log To Console    ${response}
    Should Be Equal As Numbers    ${response.status_code}    200

Post Response Status Code
    [Documentation]    Perform a POST request and check if the status code is 201 ,if not will fail the test
    ${response}=    POST    https://jsonplaceholder.typicode.com/posts/
    Should Be Equal As Numbers    ${response.status_code}    201

Patch Response Status Code
    [Documentation]    Perform a PATCH request, provide a payload, and check if the status code is 200,if not will fail the test
    ${payload}      Set Variable    {'body': "a new body after Patch Request", 'title': "Hello"}
    ${response}=    PATCH   https://jsonplaceholder.typicode.com/posts/1    ${payload}
    Should Be Equal As Numbers    ${response.status_code}   200

Delete Response Status Code
    [Documentation]    Perform a DELETE request and check if the status code is 200 ,if not will fail the test
    ${response}=    DELETE   https://jsonplaceholder.typicode.com/posts/1
    Should Be Equal As Numbers    ${response.status_code}   200

Delete Response JSON body is Empty
    [Documentation]    Perform a DELETE request and check if the response JSON body is empty
    ${response}=    DELETE   https://jsonplaceholder.typicode.com/posts/1
    Should Be Equal As Strings      ${response.json()}    {}


*** Test Cases ***

JSONPlaceholder API
    [Documentation]    Run a sequence of API tests
    Get Response Status Code
    Post Response Status Code
    Patch Response Status Code
    Delete Response Status Code
    Delete Response JSON body is Empty
