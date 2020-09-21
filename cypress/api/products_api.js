import {CategoryAPI} from "./categories_api";
import {BaseAPI} from "./baseApi";

export class ProductApi extends BaseAPI {
    productsApiUrl = "/wp-json/wc/v3/products"

    /**
     * This method created a new product via rest API
     * name: The name of the product
     * type: The type of the product
     * regular_price: The price of the product
     * description: The description of the product
     * short_description: A short description of the product
     * category: The category of the product
     * image: The image of the product
     */
    newProduct(name, type, regular_price, description, short_description, category, image) {
        // get the id of the category
        category = new CategoryAPI(this.auth.user, this.auth.pass).getCategoryByName(category)

        if (category != null) {
            category = [{"id": category.id}]
        } else {
            category = []
        }

        // create the new product
        cy.request({
            method: 'POST',
            url: this.productsApiUrl,
            auth: this.auth,
            body: {
                "name": name,
                "type": type,
                "regular_price": regular_price,
                "description": description,
                "short_description": short_description,
                "categories": category,
                "images": [{"src": image}]
            }
        })
    }

    /**
     * This method deletes a product using API, it removes all the products that match with the given product name
     * @param product_name The product name to remove
     */
    deleteProduct(product_name) {
        // get products with name
        cy.request({
            method: "GET",
            url: this.productsApiUrl,
            auth: this.auth
        }).then((resp) => {
            resp.body.forEach(el => {
                // alert(el.name + " -- " + product_name + " == " + el.name.localeCompare(product_name))
                if (el.name.localeCompare(product_name) === 0) {
                    cy.request({
                        method: 'DELETE',
                        url: this.productsApiUrl + "/" + el.id,
                        auth: this.auth
                    })
                }
            });
        })
    }
}