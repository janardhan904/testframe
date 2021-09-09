@Smoke
  Feature: verify data from Orange HRM and Excel
    Scenario: verify the candidate details in the Excel match with user details in OrangeHRMDemo application
      Given User is on OrangeHRM Login Page
      Then Verify the Login Page displayed
      When User login using username and password
      Then User should be successfully navigated to dashboard page
      And User clicks on recruitment and candidates link
      Then User should be navigated to candidate's page
      Then Verify the test data on candidates details page from Excel sheet
