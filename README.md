# akqa


Steps to Execute testcases:
    Install Python3.x.
    Install chromedriver corresponding to the chrome version in the env path
    Install the requirements from the requirements.txt documents
    pip3 install -r requirements.txt
    To run the test case through pycharm,
    a. Load project in pycharm.
    b. Select Edit Configuration from Run menu.
    c. Select + option at the top of the config window.
    d. Select Python test ->> Py.test from the dropdown.
    e. Select project directory in right side of the window.
    f. Enter Keyword as validate_db and click apply and ok
    G. Select the Run optoin from the top.
    To run the command from command prompt.
    a. Navigate to the Checkout directory.
    b. Run below command.
    pytest --config config.ui_config -k validate_db
    
The above command will also be used in Jenkins job.
Additional parameter that can be used in jenkins job are "--html=index.html --self-contained-html  --cucumberjson=report.json --cucumberjson-expanded"
This will generate HTML cucumber report.
