import pytest

from pytest_bdd import (
    when,
    then,
    scenarios
)
from src.pages import validate_date as vd
scenarios("../Feature/birthdate_validate.feature")


@pytest.fixture()
def validate_date(driver):
    validate_date =vd.ValidateDate(driver)
    return validate_date


@when("user enters birth month as <month>")
def select_month(validate_date,month):
    validate_date.enter_text('date_selector','month',month)


@when("user enters birth day as <day>")
def select_month(validate_date,day):
    validate_date.enter_text('date_selector','day',day)


@when("user enters birth year as <year>")
def select_month(validate_date,year):
    validate_date.enter_text('date_selector','year',year)


@when("user tries to navigate via URL")
def navigate_url(validate_date):
    validate_date.open('https://www.jagermeister.com/en-GB/product')


@then("validate action as per <expected_output>")
def validate_output(validate_date,expected_output):
    assert validate_date.get_element_present("labels",expected_output)


@then("User should be navigated back to gateway")
def validate_gateway(validate_date):
    assert validate_date.get_element_present("date_selector","month")
