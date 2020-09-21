import requests

from python.test_part2.features.pages.api.api_base import ApiBase


class Product(ApiBase):
    PRODUCT_BASE_URL = '/wp-json/wc/v3/products'

    def create(self, name, regular_price, type, description, short_description, image=None, category=None):
        """
        This method creates a new product via API
        :param name: Product name
        :param regular_price: Product regular price
        :param type: Product type
        :param description: Product description
        :param short_description: Product short description
        :param image: Product image
        :param category: Product category
        :return: A response json object and the status code
        """
        image = [dict(src=image)] if image else []
        category = [dict(id=category['id'])] if category else []
        body = dict(name=name,
                    type=type,
                    regular_price=regular_price,
                    description=description,
                    short_description=short_description,
                    images=image,
                    categories=category)
        response = requests.post(f"{self.url}{self.PRODUCT_BASE_URL}", json=body, auth=self.auth, verify=False)
        return response.json(), response.status_code

    def delete(self, product_id):
        """
        This method deletes a product
        :param product_id: Product id to remove
        :return: The response status code
        """
        response = requests.delete(f"{self.url}{self.PRODUCT_BASE_URL}/{product_id}", auth=self.auth)
        return response.status_code
