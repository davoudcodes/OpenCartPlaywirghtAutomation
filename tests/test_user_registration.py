"""
Test Case: User Registration Functionality

===========================================
Test Steps
===========================================

1. Open the application in the browser.
2. Navigate to the "My Account" menu and click on "Register".
3. Enter user details:
   - First Name
   - Last Name
   - Email
   - Telephone Number
   - Password and Confirm Password
4. Accept the Privacy Policy checkbox.
5. Click on the "Continue" button.
6. Verify that the account creation confirmation message is displayed.

Expected Result:
----------------
After submitting valid details, the system should display the message:
"Your Account Has Been Created!"
"""
from playwright.sync_api import expect

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from config import Config
from utils.random_data_util import RandomDataUtil


def test_registration(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    registration_page = RegistrationPage(page)
    random_data = RandomDataUtil()
    home_page.click_my_account()
    home_page.click_register()
    registration_page.set_first_name(random_data.get_full_name())
    registration_page.set_last_name(random_data.get_last_name())
    registration_page.set_email(random_data.get_email())
    registration_page.set_telephone(random_data.get_phone_number())
    registration_page.set_password('test@123')
    registration_page.set_confirm_password('test@123')
    registration_page.set_privacy_policy()
    registration_page.click_continue()
    expect(registration_page.get_confirmation_msg()).to_have_text('Your Account Has Been Created!')



