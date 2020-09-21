Feature: Tests for products

  @remove_product
  Scenario: Validate that a product can be added to the shopping cart
    Given Via API, the user creates a new product with data
      | name               | regular_price | type   | description                    | short_description | category | image                                                                                   |
      | OscarValerioMontes | 25            | simple | Product descriptions for Oscar | Oscar's product   | TShirts  | http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/T_2_front.jpg |
    When The user goes to product OscarValerioMontes in the UI
    Then The product page loads properly
    When The user increase the quantity to 7
    Then The quantity should be 7 in the page
    When The user clicks on the Add to cart button
    Then Count of cart icon gets updated
    When The user clicks on the Cart icon
    Then The product is added to the Cart
