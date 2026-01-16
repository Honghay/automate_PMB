from .aboutus import run_test as run_aboutus
from .contactus import run_test as run_contactus
from .discoveries import run_test as run_discoveries
from .faq import run_test as run_faq
from .termsNcondition import run_test as run_termsNcondition
from .logout import run_test as run_logout
from.userSetting.usersetting import run_test as run_usersetting
from .userSetting.changeLanguage import run_test as run_changeLanguage    
from .userSetting.changePin import run_test as run_changePin
from .userSetting.forgotPin import run_test as run_forgotPin
from .userSetting.forgotPassword import run_test as run_forgotPassword
from .userSetting.changePassword import run_test as run_changePassword

#Import all the test scripts under main function "Account" and put it as a list to later run in main.py, maybe have a better way to do this but idk


THREETAP_MENU = [
    # run_contactus,
    # run_faq,
    # run_termsNcondition,
    # run_discoveries,
    # run_aboutus,
    # run_usersetting,
    # run_changeLanguage
    # run_logout
    # run_changePin,
    # run_forgotPin,
    run_forgotPassword
    
]
