*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  nalle
    Set Password  nalle123  nalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  n
    Set Password  nalle123  nalle123
    Submit Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Invalid Password
    Set Username  nalle
    Set Password  Jaaaaaaaa  Jaaaaaaaa
    Submit Credentials
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  nalle
    Set Password  nalle123  nalle1234
    Submit Credentials
    Register Should Fail With Message  Passwords don't match

Login After Successful Registration
    # Tiedän, että nämä turhan.. vaikeitam, mutta toimii!!
    Set Username  nalle
    Set Password  nalle123  nalle123
    Submit Credentials
    Register Should Succeed
    Click Link  Continue to main page
    Login Should Succeed
    Make Logout
    Logout Should Succeed
    Set Username  nalle
    Set Login Password  nalle123 
    Submit Login Credentials
    Login Should Succeed
    
Login After Failed Registration
    Set Username  n
    Set Password  nalle123  nalle123
    Submit Credentials
    Register Should Fail With Message  Username is too short
    Click Link  Login
    Set Username  n
    Set Login Password  nalle123 
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Logout Should Succeed
    Login Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Make Logout
    Click Button  Logout

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}  ${c_password}
    Input Password  password  ${password}
    Input Password  password_confirmation  ${c_password}

Set Login Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

