from lib2to3.pgen2 import driver
from math import fabs
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import re

class Login_Test(unittest.TestCase):

    def Launch_Application(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.driver.get("https://m.snappfood.ir/login")
        cls.driver.implicitly_wait(10)

    def Check_Invalid_Mobile(self):
        self.PhoneNumber = self.driver.find_element_by_id("phoneNumber-input")
        self.PhoneNumber.send_keys("09378008")
        self.driver.implicitly_wait(4)
        self.submitPhoneNumber = driver.find_element_by_id("submitPhoneNumber")
        if (self.submitPhoneNumber.is_enabled == True):
            print("Validation of the number of characters was not checked")
            self.driver.close()
            self.driver.quit()
        elif (self.submitPhoneNumber.is_enabled == False):
            print("Validation of the number of characters was checked")
        self.PhoneNumber.clear()
        self.driver.implicitly_wait(4)
        self.PhoneNumber.send_keys("0937800820900")
        self.MessagePhoneNumber = driver.find_element_by_id("input-error")
        if (self.submitPhoneNumber.is_enabled == True and self.MessagePhoneNumber != "لطفاً شماره موبایل خود را بصورت درست وارد کنید."):
            print("Validation of the number of characters was not checked")
            self.driver.close()
            self.driver.quit()
        elif (self.submitPhoneNumber.is_enabled == True and self.MessagePhoneNumber == "لطفاً شماره موبایل خود را بصورت درست وارد کنید."):
            print("Validation of the number of characters was checked")
        self.PhoneNumber.clear()
        self.driver.implicitly_wait(4)
        self.PhoneNumber.send_keys("beheshti")   
        phone_regex = re.compile(r"^([0-9])([0-9]*)") 
        if (phone_regex.match(self.PhoneNumber) and self.MessagePhoneNumber != "لطفاً شماره موبایل خود را بصورت درست وارد کنید."):
            print("Input type validation not checked")
            self.driver.close()
            self.driver.quit()
        elif (phone_regex.match(self.PhoneNumber) and self.MessagePhoneNumber == "لطفاً شماره موبایل خود را بصورت درست وارد کنید."):
            print("Input type validation was checked")
        self.PhoneNumber.clear()
        self.driver.implicitly_wait(4)
        self.PhoneNumber.send_keys("09378008209")    
        if (self.submitPhoneNumber.is_enabled == True):
            self.submitPhoneNumber.click()
        elif (self.submitPhoneNumber.is_enabled == False):
            print("The mobile information is correct but the confirmation button is disabled")
            self.driver.close()
            self.driver.quit()

    def Check_Invalid_VerificationCode(self):   
        self.password = self.driver.find_element_by_id("password")
        self.submitPassword = self.driver.find_element_by_id("submitPassword")
        self.invalidpassworderror = self.driver.find_element_by_id("invalid-password-error")
        self.btnreturn = self.driver.find_element_by_id("back-navBar")
        self.password.send_keys("12345")
        self.driver.implicitly_wait(4)
        self.submitPassword.click()
        self.driver.implicitly_wait(4)
        if (self.invalidpassworderror == "رمز عبور اشتباه است"):
            print("Verification code validation verified")
            self.btnreturn.click()
            self.driver.implicitly_wait(4)
        elif (self.invalidpassworderror != "رمز عبور اشتباه است"):
            print("Verification code validation not verified")
            self.driver.close()
            self.driver.quit()

    def Check_Valid_Mobile_and_valid_VerificationCode(self): 
        self.PhoneNumber.clear()
        self.driver.implicitly_wait(4)
        self.PhoneNumber.send_keys("09301941972")
        self.submitPhoneNumber.click()
        self.driver.implicitly_wait(4)
        self.inputOTP = self.driver.find_element_by_id("input-OTP")
        self.submitPasswordOTP = self.driver.find_element_by_id("submitPasswordOTP")
        self.inputOTP.send_keys("12345")
        self.driver.implicitly_wait(4)
        if (self.submitPasswordOTP.is_enabled != True):
            print("The information was entered correctly but the confirmation button is disabled")
            self.driver.close()
            self.driver.quit()
        elif (self.submitPasswordOTP.is_enabled == True):
            self.name = self.driver.find_element_by_id("firstname-input")
            self.family = self.driver.find_element_by_id("lastname-input")
            if (self.name.is_displayed == True and self.family.is_displayed == True):
                print("The correct information was entered and the first and last name information was displayed")
            elif (self.name.is_displayed != True and self.family.is_displayed != True):
                print("The correct information was entered and the first and last name information was not displayed")
                self.driver.close()
                self.driver.quit()



    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")       












