/// <reference types='cypress' />
import {ProductPage} from "../pages/products";

describe('Products', () => {
    let items = 7
    let item_price = 25

    beforeEach(() => {
        // create a new product via API using a custom cypress command
        cy.createProductApi(
            "OscarValerioMontes",                                                                       // name
            'simple',                                                                                   // type
            item_price.toString(),                                                                      // regular price
            "This is a product created as part of the SecureWorks technical test",                      // description
            "Product for a test.",                                                                      // short description
            "Tshirts",                                                                                  // category name
            "http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/T_2_front.jpg"   // image
        )
    });

    afterEach(() => {
        // remove the product after the test runs using a custom cypress command
        cy.removeProductApi('OscarValerioMontes')
    });

    it('Validate that a product can be added to the shopping cart', () => {
        // Navigate to the page of the product that you just created
        ProductPage.visit("OscarValerioMontes")
        cy.title().should('contain', 'OscarValerioMontes')
        ProductPage.getPrice().should('be.visible')

        // Increase the quantity number to 7
        ProductPage.getQuantity().clear().type(items, {force: true})
        ProductPage.getQuantity().should("have.value", items)

        // Click “Add to cart” button
        ProductPage.getAddToCart().click()
        ProductPage.getCartAmount().should(
            'have.text',
            `$${parseFloat((item_price * items).toString()).toFixed(2)}`)
        ProductPage.getCartCount().should('have.text', items.toString() + ' items')

        // Click on the Cart icon
        ProductPage.getCartIcon().click()
        cy.url().should('contain', '/cart/')
        cy.title().should('eq', 'Cart – QA Playground')
        ProductPage.getTableProductName().should('contain', 'OscarValerioMontes')
        ProductPage.getTableProductPrice().should('contain',
            `$${parseFloat((item_price).toString()).toFixed(2)}`)
        ProductPage.getTableProductQuantity().should('contain.value', items)
        ProductPage.getTableProductSubtotal().should('contain',
            `$${parseFloat((item_price * items).toString()).toFixed(2)}`)
    });
});