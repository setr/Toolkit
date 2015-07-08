# Tree Generator
##Python script to pretty-print an outline.

`./textParser.py infile outfile` to parse the infile, and print to outfile. An absent outfile will print to screen instead. 

Now comes with proper argsparse support! [See!](#argsparse)

Now comes with a GUI! [See!](#GUI) Written with wxPython

Automagically copies the output to clipboard

####MISSION OF INTENT:
- [x] Display tree properly
- [x] Parse text and display tree
- [x] Useful CLI
- [x] Useful GUI
- [ ] Working C executables so no one has to bother with installing python
- [ ] OSX, Windows and Linux distribution build scripts
- [ ] Possibly, convert backwards as well. 
- Otherwise, maybe just save the last 30 or so converted outlines, and buttons to flip through them





Note: Requires a monospace font to print properly

Note: Are you serious github fuck your font

#### EXAMPLES: 
```
*Header1
**data1
***data11
****data111
****data112
****data113
***data12
****data121
****data122
***data13
****data131
***data14
**data2
***data21
***data22
**data3
***data31
GARBAGE
****data311
*****data3111
******data31111
**data4
*Header2
**data1
GARBAGE
***data11
****data111
****data112
****data113
GARBAGE
*Header3
*Header4 
```
BECOMES 
```
┌─ Header1
│  ├─ data1
│  │  ├─ data11
│  │  │  ├─ data111
│  │  │  ├─ data112
│  │  │  └─ data113
│  │  ├─ data12
│  │  │  ├─ data121
│  │  │  └─ data122
│  │  ├─ data13
│  │  │  └─ data131
│  │  └─ data14
│  ├─ data2
│  │  ├─ data21
│  │  └─ data22
│  ├─ data3
│  │  └─ data31
│  │     └─ data311
│  │        └─ data3111
│  │           └─ data31111
│  └─ data4
├─ Header2
│  └─ data1
│     └─ data11
│        ├─ data111
│        ├─ data112
│        └─ data113
├─ Header3
└─ Header4


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
Note: The blank textbox is the header designator. If left blank, it uses * as the default header identifier. If changed to #, then # will be the identifier. If ##, then a header level is only identified on every pair of #.
####GUI:
```


```
