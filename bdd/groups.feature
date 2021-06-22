Scenario Outline: Add new group
  Given a group list
  Given a group with <name> <header> and <footer>
  When I add a new group to the list
  Then the new group list bi equal to the old list with the added group

  Examples:
  | name | header | footer |
  | name1 | header1 | footer1 |
  | name2 | header2 | footer2 |