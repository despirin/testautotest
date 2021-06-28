Scenario: Add new group
  Given a group with <name> <header> and <footer>
  And a group list
  When I add a new group to the list
  Then the new group list bi equal to the old list with the added group
#
#  Examples:
#  | name | header | footer |
#  | name1__12123123 | header1 | footer1 |
#  | name2__12123123 | header2 | footer2 |


Scenario: Delete a group
  Given a non-empty group list
  Given a random group from the list
  When I delete the group fom the list
  Then the new group is equal to the old list without the delete group

