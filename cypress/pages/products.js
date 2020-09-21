export class ProductPage {

    static visit(product_name) {
        cy.visit("/product/" + product_name)
        return this
    }

    // code to generate webelements to be reusable
    static getPrice() { return cy.get('.product .summary .amount') }
    static getQuantity() { return cy.get('div.quantity input') }
    static getAddToCart() { return cy.get('[name="add-to-cart"]') }
    static getCartAmount() { return cy.get('a.cart-contents span.amount') }
    static getCartCount() { return cy.get('a.cart-contents span.count') }
    static getCartIcon() { return cy.get('#site-header-cart a.cart-contents') }
    static getTableProductName() { return cy.get('.product-name') }
    static getTableProductPrice() { return cy.get('.product-price') }
    static getTableProductQuantity() { return cy.get('.product-quantity input[type="number"]') }
    static getTableProductSubtotal() { return cy.get('.product-subtotal') }
}