# Vault Condition

## Decision Tree

Just a simple BST that pulls in data from a text file. It's meant to take in a values text file, of the form
`methane: 10
 CO2: 20`
 etc. Then you have a conditionals text file, of the form
 `A
  if CO2 < 20 go B
  if methane > 20 go C else go B

  B
  if methane < 10 go C

  C`
and it just prints out the node it ended at. Conditionals can't nest, and the parser is extremely naive (space-delimited, the 'go' keyword means absolutely nothing except that it produces spaces around it). I redid the conditional parser better in conditional_parser, though it's still not very intelligent.

Main reason I'm keeping this around is because it can read the tree and format an output to be fed into graphviz for an image of the tree.
