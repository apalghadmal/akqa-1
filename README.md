# akqa


Steps to Execute testcases:<br>
    Install Python3.x.<br>
    Install chromedriver corresponding to the chrome version in the env path<br>
    Install the requirements from the requirements.txt documents<br>
    pip3 install -r requirements.txt<br>
    To run the test case through pycharm,<br>
    &emsp; a. Load project in pycharm.<br>
    &emsp; b. Select Edit Configuration from Run menu.<br>
    &emsp; c. Select + option at the top of the config window.<br>
    &emsp; d. Select Python test ->> Py.test from the dropdown.<br>
    &emsp; e. Select project directory in right side of the window.<br>
    &emsp; f. Enter Keyword as validate_dob and click apply and ok<br>
    &emsp; G. Select the Run optoin from the top.<br>
    &emsp; To run the command from command prompt.<br>
    &emsp; a. Navigate to the Checkout directory.<br>
    &emsp; b. Run below command.<br>
    &emsp; pytest --config config.ui_config -k validate_dob<br>
    
The above command will also be used in Jenkins job.<br>
Additional parameter that can be used in jenkins job are "--html=index.html --self-contained-html  --cucumberjson=report.json --cucumberjson-expanded"<br>
This will generate HTML cucumber report.<br>
