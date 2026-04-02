from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By

import data
import helpers
import time
from pages import UrbanRoutesPage
from selenium.webdriver.chrome.options import (Options)


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        options = Options()
        options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(options=options)

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")


    def test_set_addresses(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)

        from_value = page.get_from_location_value()
        to_value = page.get_to_location_value()

        assert from_value == data.ADDRESS_FROM
        assert to_value == data.ADDRESS_TO


    def test_select_supportive_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)

        page.click_call_taxi()
        page.click_supportive()

        assert page.is_supportive_plan_selected()

    def test_add_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)

        page.click_call_taxi()

        time.sleep(2)

        page.click_supportive()

        page.click_phone_number()
        page.enter_phone_number(data.PHONE_NUMBER)

        page.click_next_button()

        code = helpers.retrieve_phone_code(self.driver)

        page.enter_sms_code(code)

        page.click_confirm()

        assert page.is_phone_number_displayed()


    def test_add_credit_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)

        page.click_call_taxi()
        page.click_supportive()

        page.click_payment_method()
        page.click_add_card()
        page.enter_card_number(data.CARD_NUMBER)
        page.enter_card_code(data.CARD_CODE)
        page.click_link_button()
        page.click_close_payment_method()

        payment_text = page.get_payment_method_text()
        assert "Card" in payment_text


    def test_add_comment(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)

        page.click_call_taxi()
        page.click_supportive()

        page.enter_comment(data.MESSAGE_FOR_DRIVER)

        comment_text = page.get_comment_text()
        assert comment_text == data.MESSAGE_FOR_DRIVER

    def test_add_blanket(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)

        page.click_call_taxi()
        page.click_supportive()

        page.click_blanket_toggle()

        assert page.is_blanket_selected()

    def test_order_ice_cream(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)

        page.click_call_taxi()
        page.click_supportive()

        for _ in range(2):
            page.click_ice_cream_plus()

        count_value = page.get_ice_cream_count()
        assert count_value == "2"

    def test_order_taxi(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)

        page.click_call_taxi()
        time.sleep(2)
        page.click_supportive()

        page.click_phone_number()
        page.enter_phone_number(data.PHONE_NUMBER)

        page.click_next_button()

        code = helpers.retrieve_phone_code(self.driver)

        page.enter_sms_code(code)

        page.click_confirm()

        page.click_payment_method()
        page.click_add_card()
        page.enter_card_number(data.CARD_NUMBER)
        page.enter_card_code(data.CARD_CODE)
        page.click_link_button()
        page.click_close_payment_method()

        page.click_order_button()

        assert page.is_order_modal_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


