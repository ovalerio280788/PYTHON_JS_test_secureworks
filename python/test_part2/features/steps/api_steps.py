import os

from behave import step

from python.test_part2.features.pages.api.category_api import Category
from python.test_part2.features.pages.api.product_api import Product


@step('Via API, the user creates a new product with data')
def via_api_the_user_creates_a_new_product_with_data(context):
    """
    This step definition can create as many users as rows in the table
    :param context: The context variable for behave (it is a behave's feature)
    :return: NA
    """
    api_base_parameters = (context.config.userdata.get('app_url'),
                           os.environ['username'],
                           os.environ['password'])
    category = Category(*api_base_parameters)
    product = Product(*api_base_parameters)

    for row in context.table:
        resp_json, status_code = product.create(name=row['name'],
                                                regular_price=row['regular_price'],
                                                type=row['type'],
                                                description=row['description'],
                                                short_description=row['short_description'],
                                                image=row['image'],
                                                category=category.get_category_by_name(row['category']))
        context.product_json = resp_json if status_code == 201 else None
