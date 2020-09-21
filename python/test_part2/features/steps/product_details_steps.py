from behave import step, use_step_matcher, then

from python.test_part2.features.pages.ui.product_details_page import ProductDetails

use_step_matcher('re')


@step('The user goes to product (.*) in the UI')
def the_user_goes_to_product_in_the_ui(context, product):
    page = ProductDetails(context)
    page.navigate(product)
    context.product = product


@then('The product page loads properly')
def the_product_page_loads_properly(context):
    page = ProductDetails(context)
    assert page.get_title == f"{context.product} – QA Playground", "The title of the page is not the expected!!"
    assert context.product in page.get_current_url, "The current url of the page is not the expected!!"
    assert page.title.is_displayed(), "The title of the product is not displayed!!"
    assert page.price.is_displayed(), "The price of the product is not displayed!!"


@step('The user increase the quantity to (\\d+)')
def the_user_increase_the_quantity_to(context, quantity):
    page = ProductDetails(context)
    page.quantity.clear()
    page.quantity.send_keys(quantity)


@step('The quantity should be (\\d+) in the page')
def the_user_increase_the_quantity_to(context, quantity):
    page = ProductDetails(context)
    assert page.quantity.get_attribute('value') == quantity, 'The quantity in the page was not set correctly!!'
    context.quantity = quantity


@step('The user clicks on the Add to cart button')
def the_user_clicks_on_the_add_to_cart_button(context):
    page = ProductDetails(context)
    page.add_to_cart.click()


@step('Count of cart icon gets updated')
def count_of_cart_icon_gets_updated(context):
    page = ProductDetails(context)
    assert page.cart_count.text.split()[0] == page.quantity.get_attribute('value'), "The quantity and the cart amount are different!!"
    assert float(page.cart_amount.text.replace("$", "")) == int(page.quantity.get_attribute('value')) * float(page.price.text.replace("$", "")), \
        "The quantity and the cart amount are different!!"


@step('The user clicks on the Cart icon')
def the_user_clicks_on_the_cart_icon(context):
    page = ProductDetails(context)
    page.cart_icon.click()


@step('The product is added to the Cart')
def the_product_is_added_to_the_cart(context):
    page = ProductDetails(context)
    items = page.form_shop_table_items
    assert "cart" in page.get_current_url, "The user was not taken to the cart page!!"
    assert len(items) == 1, "The are more than 1 product in the cart"
    assert float(page.shop_table_item_cells(items[0])[3].text.replace('$', "")) == float(context.product_json['price']), \
        "The are more than 1 product in the cart"
    assert page.shop_table_item_cell_input(page.shop_table_item_cells(items[0])[4]).get_attribute('value') == context.quantity, \
        "The are more than 1 product in the cart"
    assert float(page.shop_table_item_cells(items[0])[5].text.replace('$', "")) == int(context.quantity) * float(context.product_json['price']), \
        "The are more than 1 product in the cart"
