Feature: Parabank user-registration, user-login and account balance display
  Scenario: User creates a new account and logs in successfully
    Given the user navigates to the Parabank login page
    When the user registers a new account using dynamically generated credentials
    And the user logs in using the generated username and password
    Then the user should see the account balance on the dashboard