# Created by milesd at 29/08/15
Feature: Parse TFL XML data feed
  # Enter feature description here

  Scenario: get XML from TFL endpoint
    Given that the TFL connections endpoint is available for "type" line
    When I make a request
    Then I should receive "XML" data
    And I should receive a "400" response
