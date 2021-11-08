Feature: Testing websites

    Scenario Outline: Scenario Outline name
        Given there is a <website>
        When we go there
        Then it returns <status code>

        Examples:
        | website                   | status code |
        | https://google.com        | 200         | 
        | https://edition.cnn.com/  | 200         | 
        | https://localhost:9999  | 200         | 