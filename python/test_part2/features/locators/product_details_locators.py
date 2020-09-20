from selenium.webdriver.common.by import By


class ProductDetailsLocators:
    TITLE = By.CSS_SELECTOR, '.product_title'
    PRICE = By.CSS_SELECTOR, '.product .summary .amount'
    QUANTITY = By.CSS_SELECTOR, 'div.quantity input'
    ADD_TO_CART = By.CSS_SELECTOR, "[name='add-to-cart']"
    CART_AMOUNT = By.CSS_SELECTOR, "a.cart-contents span.amount"
    CART_COUNT = By.CSS_SELECTOR, "a.cart-contents span.count"
    CART_ICON = By.CSS_SELECTOR, "#site-header-cart a.cart-contents"
    FORM_SHOP_TABLE_ITEMS = By.CSS_SELECTOR, "form .shop_table tr.cart_item"
