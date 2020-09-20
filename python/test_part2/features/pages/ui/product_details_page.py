from selenium.webdriver.common.by import By

from python.test_part2.features.locators.product_details_locators import ProductDetailsLocators
from python.test_part2.features.pages.ui.base import BasePage


class ProductDetails(BasePage):

    @property
    def title(self):
        return self.driver.find_element(*ProductDetailsLocators.TITLE)

    @property
    def price(self):
        return self.driver.find_element(*ProductDetailsLocators.PRICE)

    @property
    def quantity(self):
        return self.driver.find_element(*ProductDetailsLocators.QUANTITY)

    @property
    def add_to_cart(self):
        return self.driver.find_element(*ProductDetailsLocators.ADD_TO_CART)

    @property
    def cart_amount(self):
        return self.driver.find_element(*ProductDetailsLocators.CART_AMOUNT)

    @property
    def cart_count(self):
        return self.driver.find_element(*ProductDetailsLocators.CART_COUNT)

    @property
    def cart_icon(self):
        return self.driver.find_element(*ProductDetailsLocators.CART_ICON)

    @property
    def form_shop_table_items(self):
        return self.driver.find_elements(*ProductDetailsLocators.FORM_SHOP_TABLE_ITEMS)

    def shop_table_item_cells(self, item):
        return item.find_elements(By.CSS_SELECTOR, "td")

    def shop_table_item_cell_input(self, cell):
        return cell.find_element(By.CSS_SELECTOR, "input")

    def navigate(self, product=None):
        self.driver.get(f"{self.url}/product{'/' + product if id else ''}")
