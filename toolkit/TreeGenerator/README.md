# Tree Generator
##Python script to pretty-print an outline.

`./textParser.py infile outfile` to parse the infile, and print to outfile. An absent outfile will print to screen instead. 

Now comes with proper argsparse support! [See!](#argsparse)
Next step is to write the outline parser, and after that, a simple GUI for easy use.

Possibly, convert backwards too.

Note: Requires a monospace font to print properly

Note: Are you serious github fuck your font

#### EXAMPLES: 
```
┌─ H1
│  ├─ data11
│  │  ├─ data111
│  │  │  └─ data1111
│  │  │     └─ data11111
│  │  └─ data112
│  └─ data12
├─ H2
│  └─ data21
│     ├─ data211
│     └─ data212
├─ H3
│  └─ data31
│     └─ data311
└─ H4
   └─ data41


Tree Generator
   └─ Python script to pretty-print an outline.
      ├─ EXAMPLE OUTPUT:
      └─ ARGSPARSE:
```

#### ARGSPARSE:
```
usage: Tree-Generator [-h] [-d] [-t] [-H HEADER] [-v] [infile] [outfile]

Generates a tree representation of a hierarchy from the specified file

positional arguments:
  infile                File to be parsed. Necessary unless -t is used
  outfile               specify output file. Ifot specified, prints tree to
                        screen

optional arguments:
  -h, --help            show this help message and exit
  -d, --default         sets outfile to infile_OUT
  -t, --test            runs test outline
  -H HEADER, --header HEADER
                        Header identifier used in the infile
  -v, --verbose         increase verbosity
```
