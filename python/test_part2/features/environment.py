import logging
import os

from selenium import webdriver

from python.test_part2.features.pages.api.product_api import Product


def before_feature(context, feature):
    # open the right browser, make sure to have the driver added as a environment variable
    if context.config.userdata.get('browser') == "firefox":
        context.driver = webdriver.Firefox()
    else:
        context.driver = webdriver.Chrome()

    try:
        context.driver.maximize_window()
    except Exception as e:
        context.logger.warning(f"Browser could not be maximized, setting the window size to 1920x1080. More info: {e}")
        context.driver.set_window_size(1920, 1080)

    context.driver.delete_all_cookies()
    context.driver.implicitly_wait(context.config.userdata.get('default_implicit_time'))
    context.driver.set_page_load_timeout(context.config.userdata.get('default_page_load_time'))


def after_feature(context, feature):
    try:
        context.driver.quit()
        context.driver = None
    except Exception as e:
        print(str(e))


def after_scenario(context, scenario):
    if "remove_product" in scenario.tags:
        # remove the product if the test case has the "remove_product" tag
        Product(context.config.userdata.get('app_url'),
                os.environ['username'],
                os.environ['password']
                ).delete(context.product_json['id'])
