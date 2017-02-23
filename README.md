xls2csv from https://github.com/dilshod/xlsx2csv/

if you fork/use, please credit: matthew berland

license is gpg v3

this is not supported, don't email me please!
it is totally hacked up & broken - feel free to submit a pull req to fix it
it is public because someone might find it useful, but that is it

python 2 only because i am lazy

how to use:
`brew install drake` (on a mac) 
put XLSX files (as many as you like!) into data/
they should have one column per tag per line and the first column should be "Name"
all cells should either be 0 or 1

so like this:
```
| Name | TAG1 | TAG2 | ... | TAGN |
| Bill | 1    | 0    | ... | 1    |
| Alice| 0    | 0    | ... | 1    |
```

then just run "drake" in the top level directory

see what pops out in `out.txt`
