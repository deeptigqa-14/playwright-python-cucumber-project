Feature: Order Transaction
  Tests realted to order transaction


  Scenario Outline: Verify order success messge shown in detail page
    Given Place the item order with <username> and <password>
    And user is on login page
    When I login to portal with <username> and <password>
    And Navigated to order page
    And select orderId
    Then Verify order success message shown in detail page
    Examples:
        | username            | password      |
        | deeptigqa@gmail.com | Pr@******  |