import pytest
from pages.product_page import ProductPage


@pytest.mark.parametrize('link',
                         ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer" + str(i)
                          for i in range(10) if i != 7] +
                         [pytest.param(
                             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                             marks=pytest.mark.xfail)])
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_add_to_basket()
    page.should_be_message_basket_cost()
    page.message_add_to_basket_has_correct_product_name()
    page.message_basket_cost_has_correct_price()
