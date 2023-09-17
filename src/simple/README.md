<a id="py1st-src-simple"></a>
# Python First — Simple Examples

These scripts are mostly designed to illustrate one Python feature. They are not necessarily *useful* outside of an educational context.

### [argslist.py](./argslist.py) — List Command-Line Arguments

This scripts shows how we can obtain [command-line arguments][w-cli-arg] passed to a script. From the [standard library][p-stdlib]'s [**sys**][p-m-sys] module, the script uses [**sys.argv**][p-m-sys-argv], which is a [**list**][p-t-list] type.

[w-cli-arg]:
   https://en.wikipedia.org/wiki/Command-line_interface#Arguments
   "Wikipedia — Command-Line Interface / Arguments"
[p-m-sys]:
   https://docs.python.org/3/library/sys.html
   "Python Docs — Library / sys module"
[p-m-sys-argv]:
   https://docs.python.org/3/library/sys.html#sys.argv
   "Python Docs — Library / sys.argv list"
[p-t-list]:
   https://docs.python.org/3/library/stdtypes.html#list
   "Python Docs — Built-In Types / list"
[p-stdlib]:
   https://docs.python.org/3/library/index.html
   "Python Docs — Standard Library Index"

### [exitcode.py](./exitcode.py) — Return Exit Code

An exit code, is also called an [exit status][w-exit-sts], and is an integer value returned by terminating processes (in this case, a Python script). This value can be obtained by parent [processes][w-process] (like your [command-line][w-cli] [shell][w-shell]).

It makes use of the [**sys.exit()**][p-m-sys-exit] function from the [**sys**][p-m-sys] module in the [standard library][p-stdlib].

[w-exit-sts]:
   https://en.wikipedia.org/wiki/Exit_status
   "Wikipedia — Exit Status / Code"
[w-shell]:
   https://en.wikipedia.org/wiki/Shell_(computing)
   "Wikipedia — Shell (computing)"
[w-process]:
   https://en.wikipedia.org/wiki/Process_(computing)
   "Wikipedia — Process (computing)"
[w-cli]:
   https://en.wikipedia.org/wiki/Command-line_interface
   "Wikipedia — Command-Line Interface (CLI)"
[p-m-sys-exit]:
   https://docs.python.org/3/library/sys.html?highlight=sys%20exit#sys.exit
   "Python Docs — Library / sys.exit() function"

### [hiby.py](./hyby.py) — Hello and Goodbye

Stupid little example used to illustrate typographical conventions. Many like to add **y** in programs that are for, or written in, Python — so we comply.
