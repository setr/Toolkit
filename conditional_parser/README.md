## Conditional Parser

The main file is parser.py, which reads input.txt and vals.txt. 

Input.txt contains a decision tree of the given node format, intended to be easily modified. Written line by line.
```
  line_1: node_name
  line_2: node_description
  line_n..+: conditionals declaring which node_name to goto next
  line_n..+1: line break
```
and then the next node can begin, with the same format.

Conditionals are in the form: `if [cond] [(and|or) (cond)] go node_name` with infinite recursive depth for the conditionals. 

Reads left to right, so `A and B or C or F` becomes `(((A and B) or C) or F)`

vals.txt is a simple dict of the form `[key] : [value]`
which serves as the input for the decision tree. 

and of course, parser.py does all the work. Reads, parses, understands, and decides. Spits out the final node.


I highly doubt this is the most intelligent manner in which to write a language parser. A proper tokenizer probably would have made this a lot simpler, especially in regards to (unavailable) handling of () precedence
