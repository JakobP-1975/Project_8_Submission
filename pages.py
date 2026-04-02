from selenium.webdriver.common.by import By


# Defining the page class, locators and method in the class
class UrbanRoutesPage:
    # Locators as class attributes
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CALL_TAXI_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Call a taxi"]')
    SUPPORTIVE_LOCATOR = (By.XPATH,'//div[contains(@class,"tcard")][.//div[text()="Supportive"]]')
    PHONE_NUMBER_LOCATOR = (By.XPATH,'//div[@class="np-button"][.//div[text()="Phone number"]]')
    PHONE_NUMBER_INPUT_LOCATOR = (By.ID, 'phone')
    PHONE_NUMBER_DISPLAY_LOCATOR = (By.CLASS_NAME, "np-text")
    NEXT_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Next"]')
    SMS_INPUT_LOCATOR = (By.ID, 'code')
    CONFIRM_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Confirm"]')
    PAYMENT_METHOD_LOCATOR = (By.XPATH,'//div[@class="pp-button filled"][.//div[text()="Payment method"]]')
    ADD_CARD_LOCATOR = (By.XPATH, '//div[text()="Add card"]')
    CARD_NUMBER_INPUT_LOCATOR = (By.ID, 'number')
    CARD_CODE_INPUT_LOCATOR = (By.CSS_SELECTOR, 'input[placeholder="12"]')
    LINK_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Link"]')
    CLOSE_PAYMENT_MODAL_LOCATOR = (By.XPATH, "//div[contains(@class,'payment-picker') and contains(@class,'open')]//button[contains(@class,'close-button')]")
    COMMENT_LOCATOR = (By.ID, 'comment')
    ORDER_REQUIREMENTS_LOCATOR = (By.XPATH, '//div[text()="Order requirements"]')
    BLANKET_HANDKERCHIEF_LOCATOR = (By.CLASS_NAME, "switch-input")
    BLANKET_TOGGLE_LOCATOR = (By.CSS_SELECTOR, ".switch .slider.round")
    ICE_CREAM_BUCKET_LOCATOR = (By.XPATH,'//div[contains(text(),"Ice cream")]')
    ICE_CREAM_COUNT_LOCATOR = (By.CLASS_NAME, 'counter-value')
    ICE_CREAM_PLUS_LOCATOR = (By.XPATH,'//div[contains(text(),"Ice cream")]/ancestor::div[contains(@class,"r-type-counter")]//div[@class="counter-plus"]')
    ORDER_BUTTON_LOCATOR = (By.XPATH,'//button[.//span[text()="Order"]]')
    ORDER_MODAL_LOCATOR = (By.CLASS_NAME, "order-body")

    def __init__(self, driver):
        self.driver = driver

    def enter_from_location(self, from_text):
        # Enter From
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def get_from_location_value(self):
        element = self.driver.find_element(*self.FROM_LOCATOR)
        return element.get_attribute("value")

    def enter_to_location(self, to_text):
        # Enter To
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def get_to_location_value(self):
        element = self.driver.find_element(*self.TO_LOCATOR)
        return element.get_attribute("value")

    def click_call_taxi(self):
        # click call taxi
        self.driver.find_element(*self.CALL_TAXI_BUTTON_LOCATOR).click()

    def click_supportive(self):
        # click supportive
        self.driver.find_element(*self.SUPPORTIVE_LOCATOR).click()

    def is_supportive_plan_selected(self):
        element = self.driver.find_element(*self.SUPPORTIVE_LOCATOR)
        class_value = element.get_attribute("class")
        return "active" in class_value

    def click_phone_number(self):
        # Click phone number
        self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).click()

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.PHONE_NUMBER_INPUT_LOCATOR).send_keys(phone_number)

    def is_phone_number_entered(self):
        element = self.driver.find_element(*self.PHONE_NUMBER_INPUT_LOCATOR)
        return element.get_attribute("value") != ""

    def is_phone_number_displayed(self):
        element = self.driver.find_element(*self.PHONE_NUMBER_DISPLAY_LOCATOR)
        return element.is_displayed()

    def click_next_button(self):
        # Click next button
        self.driver.find_element(*self.NEXT_BUTTON_LOCATOR).click()

    def enter_sms_code(self, code):
        # Enter sms code
        self.driver.find_element(*self.SMS_INPUT_LOCATOR).send_keys(code)

    def is_sms_code_entered(self):
        element = self.driver.find_element(*self.SMS_INPUT_LOCATOR)
        return element.get_attribute("value") != ""

    def click_confirm(self):
        # Click confirm
        self.driver.find_element(*self.CONFIRM_BUTTON_LOCATOR).click()

    def click_payment_method(self):
        # Click payment method
        self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR).click()

    def get_payment_method_text(self):
        element = self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR)
        return element.text

    def click_add_card(self):
        # Click add card
        self.driver.find_element(*self.ADD_CARD_LOCATOR).click()

    def enter_card_number(self, number):
        # Enter card number
        self.driver.find_element(*self.CARD_NUMBER_INPUT_LOCATOR).send_keys(number)

    def enter_card_code(self, code):
        element = self.driver.find_element(*self.CARD_CODE_INPUT_LOCATOR)
        element.click()
        element.send_keys(code)

    def click_link_button(self):
        # Click link
        self.driver.find_element(*self.LINK_BUTTON_LOCATOR).click()

    def click_close_payment_method(self):
        self.driver.find_element(*self.CLOSE_PAYMENT_MODAL_LOCATOR).click()

    def enter_comment(self, comment):
        # Enter message
        self.driver.find_element(*self.COMMENT_LOCATOR).send_keys(comment)

    def get_comment_text(self):
        element = self.driver.find_element(*self.COMMENT_LOCATOR)
        return element.get_attribute("value")

    def click_order_requirements(self):
        # Click order requirements
        self.driver.find_element(*self.ORDER_REQUIREMENTS_LOCATOR).click()

    def click_ice_cream_bucket(self):
        # Click Ice cream bucket
        self.driver.find_element(*self.ICE_CREAM_BUCKET_LOCATOR).click()

    def click_blanket_toggle(self):
        # Click blanket toggle
        self.driver.find_element(*self.BLANKET_TOGGLE_LOCATOR).click()

    def is_blanket_selected(self):
        element = self.driver.find_element(*self.BLANKET_HANDKERCHIEF_LOCATOR)
        return element.is_selected()

    def click_ice_cream_plus(self):
        # Click ice cream twice
        self.driver.find_element(*self.ICE_CREAM_PLUS_LOCATOR).click()

    def get_ice_cream_count(self):
        element = self.driver.find_element(*self.ICE_CREAM_COUNT_LOCATOR)
        return element.text

    def click_order_button(self):
        # Click order
        self.driver.find_element(*self.ORDER_BUTTON_LOCATOR).click()

    def is_order_modal_displayed(self):
        element = self.driver.find_element(*self.ORDER_MODAL_LOCATOR)
        return element.is_displayed()

