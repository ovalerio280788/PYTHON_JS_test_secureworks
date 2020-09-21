// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
//
// -- This is a parent command --
// Cypress.Commands.add("login", (email, password) => { ... })
//
//
// -- This is a child command --
// Cypress.Commands.add("drag", { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add("dismiss", { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This will overwrite an existing command --
// Cypress.Commands.overwrite("visit", (originalFn, url, options) => { ... })

import {ProductApi} from "../api/products_api";

/**
 * This code creates a new Cypress command that is in charged of creating a new product
 * using the wordpress rest API
 *
 * @params
 * name: The name of the product
 * type: The type of the product
 * regular_price: The price of the product
 * description: The description of the product
 * short_description: A short description of the product
 * category: The category of the product
 * image: The image of the product
 */
Cypress.Commands.add('createProductApi', (name, type, regular_price, description, short_description, category, image) => {
    return new ProductApi(
        Cypress.env('USERNAME'),
        Cypress.env('PASSWORD')
    ).newProduct(
        name,
        type,
        regular_price,
        description,
        short_description,
        category,
        image)
});

/**
 * This code creates a new Cypress command that is in charged of removing a product
 * using the wordpress rest API. This method will remove all products with the given name
 *
 * @params
 * - product_name: The product name to be removed
 */
Cypress.Commands.add('removeProductApi', (product_name) => {
    return new ProductApi(
        Cypress.env('USERNAME'),
        Cypress.env('PASSWORD')
    ).deleteProduct(product_name)
});