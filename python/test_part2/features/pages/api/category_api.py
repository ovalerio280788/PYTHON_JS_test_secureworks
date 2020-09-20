from pip._vendor import requests

from python.test_part2.features.pages.api.api_base import ApiBase


class Category(ApiBase):
    CATEGORY_BASE_URL = '/wp-json/wc/v3/products/categories'

    def get_category_by_name(self, name):
        """
        This method gets a category object based on a category name, to be able to get the id for example
        :param name: The category name
        :return: The category object or and empty array if not found
        """
        response = requests.get(f"{self.url}{self.CATEGORY_BASE_URL}", auth=self.auth, verify=False)
        categories = [x for x in response.json() if x['name'].lower() == name.lower()]
        return categories[0] if categories else []
