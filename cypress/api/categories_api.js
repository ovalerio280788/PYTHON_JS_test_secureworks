import {BaseAPI} from "./baseApi";

export class CategoryAPI extends BaseAPI {
    categoriesApiUrl = "/wp-json/wc/v3/products/categories"

    /**
     * This method get a category based on a name, and return an object with all the information
     * about the given category
     * @param name The category name
     */
    getCategoryByName(name) {
        // get the id of the category
        var options = {
            url: this.categoriesApiUrl,
            method: "GET",
            auth: this.auth
        }

        cy.request(options).then(async (resp) => {
            resp.body.forEach(el => {
                // alert(el.name + " -- " + name + " == " + el.name.localeCompare(name))
                if (el.name.localeCompare(name) === 0) {
                    return el;
                }
            });
        })
    }
}