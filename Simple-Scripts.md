Once you've outgrown the limited features of the Python REPL, you maybe want to graduate to writing scripts. Scripts are sometimes called *modules*. Scripts are just Python statements… the same statements you use in a REPL. Running the script, effectively ‘replays’ the statements in the script.

:::{.admon .important}
**Script Naming**

Naming of scripts are important: they should be named like [ident]{.stx}ifiers. In other words, only use alphabetic characters and underscores. Using characters like hyphens (**-**), dollar signs (**\$**), or other ‘weird’ characters, will create problems.
:::

# Most Basic

The simplest script you can write, contains at least one statement. As a matter of convention, we save scripts with the **.py** extension. Save the following in file called **hello.py** in a convenient location. 

##### `hello.py` — Simplest Python Script {#hello.py .file}
```py
print("Hello.")
```

To run the script, you must pass its name to the **python** (or **python3**) interpreter:

###### `sh/pwsh` — Run hello.py {#run-hello .snip}
```sh
$> python hello.py
```

If **hello.py** is not in the current directory, you must either change your current working directory, specify the full path, or provide a path relative to the current directory.

This way of running scripts will always work on all supported operating systems and shells. 

# Unix-Like Executable

In a Unix-like OS, you can set the executable permissions bit. However, that alone is not enough. You must also add a [shebang][w-shebang] (or hash-bang) line to specify the interpreter to use for the script:

##### `hello_exe.py` — Hello Script as Executable {#hello_exe.py .file}
```py
#!/usr/bin/env python3
print("Hello.")
```

Now, you can run your script as a [command]{.stx}. Assuming **hello_exe.py** is in the current directory:

```sh
$> chmod a+x hello_exe.py
$> ./hello_exe.py
```

Like any executable, it is most useful when on your **PATH**. A common convention is to have a **\$HOME/.local/bin** directory, which is first in your **PATH**. You can either copy your executable Python scripts to this directory, or you can create a symbolic link.

&nbsp;&nbsp;&nbsp;&nbsp; **cd &nbsp; $HOME/.local/bin**<br/>
&nbsp;&nbsp;&nbsp;&nbsp; **ln &nbsp; -s** &nbsp; [path-to]{.stx}**/**[script]{.stx}**.py** &nbsp; [script]{.stx}

Now, regardless of your current working directory location, you can run the script with [script]{.stx}. Here is an example series of command-lines based on the above pattern:

###### `sh/pwsh` — Create link to executable script {.snip}
```sh
$> cd $HOME/.local/bin
$> ln -s $HOME/work/learn/hello_exe.py hello_exe
$> hello_exe                  #→ Hello.
$> cd $HOME/work/learn
$> hello_exe                  #→ Hello.
```

The name of the symbolic link do not have to exactly match the name of the script. You could have make the link **hello**, instead of **hello_exe**, for example.

On Windows, you may create ‘launchers’ which are batch files or actual dedicated executables, that will automatically run the **python.exe** executable with the script name as argument. Any arguments passed to the ‘launcher’ will be forwarded to the script.

[w-shebang]:
   https://en.wikipedia.org/wiki/Shebang_(Unix)
   "Wikipedia — Shebang"

# Script Docstring

If the first non-comment statement in your script is an [expression statement][p-st-expr] having type **str**, Python will store it in the [documentation][w-docstr] for your script or *module*. Take this simple script:

##### `docstring.py` — Simple Script with Docstring {#docstring.py .file}
```py
#!/usr/bin/env python3
"""
Documentation for my script (also called a module).
It can span several lines, which is why we used a
‘long string’ or ‘triple-quoted string’.
"""
```

Now, assuming **docstring.py** is in the current directory, you can ‘load’ it into a REPL session using **import**. You must not add the **.py** extension:

##### `py` — Inspecting docstring attribute {.snip}
```py
>> import docstring
>> print(docstring.__doc__)
#→ Documentation for my script (also called a module).
#→ It can span several lines, which is why we used a
#→ ‘long string’ or ‘tripple-quoted string’.
>> help(docstring)
```

Here is the output for the last statement using the **help** function:

```{.output}
Help on module docstring:

NAME
    docstring

DESCRIPTION
    Documentation for my script (also called a module).
    It can span several lines, which is why we used a
    ‘long string’ or ‘tripple-quoted string’.

FILE
    ···/work/learn/docstring.py
```

You can obtain that same output from the **pydoc** module on the shell command-line:

###### `sh/pwsh` — View documenation with pydoc module {.snip}
```sh
$> python -m pydoc docstring
```

Again, notice the absence of the **.py** extension.

Your scripts should always have a docstring. It is simply the ‘right thing to do’. And if you followed advice to always encode your scripts as UTF-8, you can use ‘raw’ Unicode characters in your docstrings.

:::{.admon .note}
 **Other Docstrings**

 [Docstrings][w-docstr] can also appear as the first expression statement inside the blocks of [**class**][p-ref-class]es and [functions][p-st-funcdef]. Like a module, each of these constructs also have a **\_\_doc\_\_** attribute, where these docstrings are stored and retrieved by functions like [**help**][p-fn-help] and modules like [**pydoc**][p-lib-pydoc].
:::

[w-docstr]:
   https://en.wikipedia.org/wiki/Docstring
   "Wikipedia — Docstring"
[p-st-expr]:
   https://docs.python.org/3/reference/simple_stmts.html#expression-statements
   "Python Simple Statements — 7.1 Expression Statements"
[p-ref-class]:
   https://docs.python.org/3/tutorial/classes.html#classes
   "Python Reference — 9. Classes"
[p-st-funcdef]:
   https://docs.python.org/3/reference/compound_stmts.html#function-definitions
   "Python Reference — 8.7. Function Definitions"
[p-fn-help]:
   https://docs.python.org/3/library/functions.html#help
   "Python — Built-in Functions # help()"

# Comments

Comments are not to be confused with [docstrings](#script-docstring). Comments start with a hash character (**#**) and extends to the end of the line. Python will ignore the hash, as well as everything that follows it, until the end of the line.

We use comments to explain implementation detail that could be useful to yourself, or maintainers of the code. Comments should be brief. They should not take the place of [docstrings](#script-docstring).

A hash character in a string literal, will not be treated as the beginning of a comment.

###### `py` — Python comments example {.snip}
```py
# This is a comment. Ignored up to here↓
print("Hello!")             ## This is a comment too.
print("#Hello#")
```

The `"#Hello…` does not start a comment, because the `#` is inside a string literal.

The number of hash characters is not significant, only the first.

[w-comment]:
   https://en.wikipedia.org/wiki/Comment_(computer_programming)
   "Wikipedia — Comment (computer programming)"

# Command-Line Arguments

For scripts that want to process [command-line arguments][w-cli-args], you can use the [**sys.argv**][p-sys.argv] list. Python populates that list with command-line arguments, before interpreting any code in your script. It will contain a list of strings, the first being the script name, the rest (if any), will contain the arguments.

Here is a simple script that simply prints out the command-line arguments passed to it:

##### [`minargslist.py`](src/simple/minargslist.py) — List Command-Line Arguments {#src_simple_argslist.py .snip}
```{.py include=src/simple/minargslist.py}
```

The purpose of the above script uses several features you may not yet be familiar with, but that is not the point — we wanted the simplest script you can use to experiment with command-line arguments. A more pythonic version can be found: [**src/simple/argslist.py**][idgh-py1st-simple-argslist_py].

```sh
$> python argslist.py
#→ Script: argslist.py
$> python argslist.py ABC 'DEF GHI'
#→ Script: argslist.py
#→ Arg #1: ABC
#→ Arg #2: DEF GHI
```

To tell your *shell* to treat an argument containing special characters like spaces, you must *quote* the argument. Unix-like shells and PowerShell allow you to quote arguments using single or double quotes. The script will not get those quotes.

[w-cli-args]:
   https://en.wikipedia.org/wiki/Command-line_interface#Arguments
   "Wikipedia — Command-Line Interface # Arguments"
[idgh-py1st-simple-argslist_py]:
   src/simple/argslist.py
   "GitHub — Incus Data / Python First / Source / Simple / argslist.py"

# Exit Codes

If your script terminates normally, it will return an [exit code][w-exitcode] of **0**, which is a common operating system convention for a ‘successful termination’ code. You can explicitly set this code using [**sys.exit**][p-sys.exit]**(**&nbsp;[exit-code]{.stx}&nbsp;**)**. Be aware that only [exit-code]{.stx} values 0…255 are useful on Unix-like operating systems.

You can call [**sys.exit**][p-sys.exit] anywhere in your script… and your script will immediately terminate. The exit code can be obtains in shells or processes that launched your script. In a Unix-like shell, the exit code will be in a special variable: **\$?**, which contains the exit code of the last command. In PowerShell, you can use **\$LastExitcode**, and in Command Prompt, **%ERRORLEVEL%**.

When your script terminates for any reason other than ‘normal termination’, you should exit with a non-zero exit code. This is good practice, and allows users to take different actions depending on the exit status of your program.

###### `sh` — View exit codes in different shells {.snip}
```sh
#= sh
$> ‹command›
$> echo $?
#= pwsh
$> ‹command›
$> echo $LastExitcode
#= cmd
$> ‹command›
$> echo %ERRORLEVEL%
```

Here is a Python script called **exitcode.py** that you can experiment with. It will return a random exit code in the range [0…255], if no command-line argument was passed. Otherwise, if the command-line argument is an integer in this range, it will return that instead.

##### [`exitcode.py`](src/simple/exitcode.py) — Different Exit Codes to Test {#exitcode.py .file}
```py
#!/usr/bin/env python3

import sys, random                    #← required modules.

exit_code = None
if len(sys.argv) > 1:                 #← if command-line args…
    exit_code = int(sys.argv[1])      #← convert 1st argument.
else:
    exit_code = random.randrange(256) #← random int in [0…255].

sys.exit(exit_code)                   #← terminate & set code.
```

The above script is deliberately simplistic, avoids error handling, and does not follow the [main pattern](#main-pattern), but is sufficient for our purpose. See [**src/simple/exitcode.py**][idgh-py1st-simple-exitcode_py] in the repository for a ‘proper’ version.

###### `sh` — Experiments viewing exit codes {.snip}
```sh
#= sh
$> python3 exitcode.py 123
$> echo $?                            #→ 123
$> python3 exitcode.py 1234
$> echo $?                            #→ 210
#= pwsh (windows)
$> python exitcode.py 123
$> echo $LastExitcode                 #→ 123
$> python exitcode.py 1234
$> echo $LastExitcode                 #→ 1234
#= cmd
$> python exitcode.py 123
$> echo %ERRORLEVEL%                  #→ 123
$> python exitcode.py 1234
$> echo %ERRORLEVEL%                  #→ 1234
```

Even if you have not considered exit codes before, users of your scripts may care. In production scripts, return **0** for normal termination and a value less than 256 (1 is common) for abnormal termination. Document any potential exit codes your script may return.

[w-exitcode]:
   https://en.wikipedia.org/wiki/Exit_status
   "Wikipedia — Exit Status/Code"
[p-sys.exit]:
   https://docs.python.org/3/library/sys.html#sys.exit
   "Python Library — sys # sys.exit"
[idgh-py1st-simple-exitcode_py]:
   src/simple/exitcode.py
   "GitHub — Incus Data / Python First / Source / Simple / exitcode.py"

# Main Pattern

The ‘main pattern’ is a common pattern (not a syntax) for creating executable scripts. The convention has several advantages:

 * as an executable, the script will run normally;
 * or, it can be [**import**][p-ref-import] ed as a module; and
 * the [**pydoc**][p-lib-pydoc] module can show its documentation.

The advantages are compelling enough, that you should always try to follow this pattern.

The **hello_main.py** script below, has a shebang line and a docstring as before. But the ‘work’ of the script (the [**print**][p-fn-print]), has been moved to a **main** function. The name is just part of the convention, and nothing special.

The important part is always at the end of scripts following this pattern:

###### `py` — Simple ‘main’ pattern {.snip}
```py
if __name__ == '__main__':
   main()
```

Here is the **hello_exe.py** script reorganised to follow the ‘main pattern’, and we renamed it to **hello_main.py**. We also added a [docstring](#script-docstring) for the **main** function.


##### `hello_main.py` — Hello World with Main Pattern {#hello_main.py .file}
```py
#!/usr/bin/env python3
"""
Documentation for my script (also called a module).
It can span several lines, which is why we used a
‘long string’ or ‘triple-quoted string’.
"""

def main ():
    """
    Print a greeting to standard output.
    """
    print("Hello.")

if __name__ == '__main__':
    main()
```

If you were to run ‘**python**&nbsp;**-m**&nbsp;**pydoc**&nbsp;**hello_main**’, the output will be something like this:

```{.output}
Help on module hello_main:

NAME
    hello_main

DESCRIPTION
    Documentation for my script (also called a module).
    It can span several lines, which is why we used a
    ‘long string’ or ‘triple-quoted string’.

FUNCTIONS
    main()
        Print a greeting to standard output.

FILE
    ···/work/learn/hello_main.py
```

And, you can make it an executable like **hello_exe.py**, and place it on your **PATH**, or make a symbolic link to it, that is on your **PATH**. The best of all worlds.

You can also **import** **hello_main.py** inside a REPL or other script. Since not running as a script, the **if** part will not call **main**. You have to explicitly call **main** in this case.

###### `py` — Import and run script with main {.snip}
```py
>> import hello_main
>> hello_main.main()           #← call main function.
```

For now, focus on the *pattern*, which is why we showed you the transformation of the *same program* to eventually become the more pythonic version. You do not have to concern yourself right now, with **if** statements, or the point of the **def** keyword, for example. Here is a **template1.py** you can copy to new scripts:

##### `template1.py` — Simple Template {#template1.py .file}
```py
#!/usr/bin/env python3
"""
‹script documentation›
"""

def main ():
    """
    ‹function documentation›
    """
    ‹code›

if __name__ == '__main__':
    main()
```

All you have to do, is replace the parts in angle brackets (guillemets, actually), the most import part being: `‹code›` could become: `print("Hello.")`.

For scripts dealing with [command-line arguments](#command-line-arguments), and you are writing scripts that wants to process said arguments, you could use this template:

##### `template2.py` — Template for Command-Line Arguments {#template2.py .file}
```py
#!/usr/bin/env python3
"""
‹script documentation›
"""
import sys

def main (args):
    """
    ‹function documentation›
    """
    <code>

if __name__ == '__main__':
    main(sys.argv)
```

Python automatically stores command-line arguments in a [**sys.argv**][p-sys.argv] list.

Here is **template3.py** for scripts that deal not only with [command-line arguments](#command-line-arguments), but also are aware of [exit codes](#exit-codes).

##### `template3.py` — Template for Arguments and Exit Codes {#template3.py .file}
```py
#!/usr/bin/env python3
"""
‹script documentation›
"""
import sys

def main (args):
    """
    ‹function documentation›
    """
    ‹code›
    return ‹exit-code› 

if __name__ == '__main__':
    sys.exit(main(sys.argv))
```

[p-sys.argv]:
   https://docs.python.org/3/library/sys.html#sys.argv
   "Python Library — sys # sys.argv"

| &#x2139;&#xFE0F; **ADVICE** — **Editor Settings** |
|:--------------------------------------------------|
| And a final reminder: set your file encoding to UTF-8 in your editor, and even on Windows, use ‘Unix line endings’ ([LF]{.stx}) not ‘Windows line endings’ ([CR]{.stx}[LF]{.stx}). Indentation width should be 4 spaces (not hard [TAB]{.stx} characters — set tab expansion on).|

[p-lib-pydoc]:
   https://docs.python.org/3/library/pydoc.html?highlight=docstr
   "Python Library — pydoc"
[p-ref-import]:
   https://docs.python.org/3/reference/import.html#the-import-system
   "Python Reference — 5. Import System"
[p-fn-print]:
   https://docs.python.org/3/library/functions.html#print
   "Python Functions — print()"

# External Tools 

Several tools are available, not only to check your code for correctness, but also against style guides like [PEP-8][pep8]. Editors and IDEs can format your code to also conform, but external tools are available.

[pep8]:
   https://peps.python.org/pep-0008/
   "PEP 8 — Style Guide for Python Code"

## Style Checks

Three tools are available to check your code for conformance to [PEP-8][pep8]. The oldest is [**pylint**][gh-pylint] and has extensive [documentation][pylint-doc]. It is available as package [**pylint**][pypi-pylint], as is [another][gh-flake8] tool called [**flake8**][pypi-flake8], also with good [documentation][flake8-docs].

###### `sh` — *Installing Linters* {.snip}
```sh
$> pip install pylint flake8
$> flake8 ‹script-name›
$> pylint ‹script-name›
```

These tools will not show exactly the same ‘problems’, and both can be configured. This is why it is a good idea to run your code through both, and read their documentation to see how to configure them for your requirements.

The VSCode editor can be configured to use either.

[gh-pylint]:
   https://github.com/pylint-dev/pylint
   "GitHub — pylint"
[pylint-doc]:
   https://pylint.readthedocs.io/en/latest/
   "Pylint — Documenation"
[pypi-pylint]:
   https://pypi.org/project/pylint/
   "PyPI — pylint"
[pypi-flake8]:
   https://pypi.org/project/flake8/
   "PyPI — flake8"
[gh-flake8]:
   https://github.com/pycqa/flake8
   "GitHub — flake8"
[flake8-docs]:
   https://flake8.pycqa.org/en/latest/index.html#
   "Flake8 — Your Tool for Style Guide Enforcement"

## Code Formatting

The [**black**][pypi-black] ([GitHub][gh-black]) and [**yapf**][pypi-yapf] ([GitHub][gh-yapf]) tools are popular code formatters, both based on the recommendations in [PEP-8][pep8]. Editors like VSCode can be configured to use either. If you have no preference, we recommend [**black**][gh-black]; it has fewer options and is simple to use.

###### `sh` — Installing Code Formatters {.snip}
```sh
$> pip install black yapf
$> black ‹script-name›
$> yapf ‹script-name›
```

Both can be configured (though [**black**][gh-black] less so) to better fit your personal style.

[pypi-black]:
   https://pypi.org/project/black/
   "PyPI — black — Uncompromising Code Formatter"
[gh-black]:
   https://github.com/psf/black
   "GitHub — psf/black"
[pypi-yapf]:
   https://pypi.org/project/yapf/
   "PyPI — yapf"
[gh-yapf]:
   https://github.com/google/yapf
   "GitHub — google/yapf"

# Structure Summary

All scripts can have a basic structure. For scripts that are supposed to be executable (or optionally executable), we use the [main pattern](#main-pattern):

 * Shebang/hash-bang line — Even in Python scripts intended mainly for Windows.
 * Script docstring — Keep a consistent form.
 * Imports — Any modules to be used in the script. Static analysis tools expect one [**import**][p-ref-import] statement per module.
 * Global variables — Variables that are global to the script. Static analysis tools will expect them to be in all capital letters.
 * Definitions
   * Class definitions — For creating new user-defined types. Should have a docstring.
   * Function definitions, e.g., **main**, and all should have a docstring.
 * **if __name__ == '__main__:'** … — Always at the end of the script.

If a script has multiple function in addition to **main**, the **main** function should be first, followed by the functions it calls, followed by the functions they calls, etc. This allows the program to be more easily read from the top down. Lower down, will be more implementation detail, while higher up, more abstractions.

# Experiments

The normal GitHub alert syntax is supported by a Pandoc extension. It is enabled and styled:

> [!NOTE]
> Highlights information a reader should notice even while skimming.
> Use for clarifications, definitions, and cross-references.

> [!TIP]
> Optional advice that helps the reader do something better or faster.
> Use for shortcuts, best practices, and recommendations.

> [!IMPORTANT]
> Crucial information required to avoid a problem.
> Use when omitting the note would lead to broken behaviour.

> [!WARNING]
> Potentially harmful content. Use when an action risks data loss,
> security issues, or other hard-to-reverse consequences.

> [!CAUTION]
> Describes negative consequences of an action that has already been taken
> or is about to be taken. Use for irreversible or destructive operations.

Admonitions can contain rich content:

> [!TIP]
> **Data Validation**
> 
>  Validate all external input, but also output, at the system boundary:
>
> - Never trust user-supplied data.
> - Use parameterised queries for SQL.
> - Escape output for its target context (HTML, shell, JSON).
>
> ```python
> name = escape_html(request.form["name"])
> ```

Admonitions can also be created using Pandoc's attributes on fenced divs:

::: {.admon .tip}
**Data Validation**

 Validate all external input, but also output, at the system boundary:

- Never trust user-supplied data.
- Use parameterised queries for SQL.
- Escape output for its target context (HTML, shell, JSON).

```python
name = escape_html(request.form["name"])
```
:::

## ASCII Art

By adding a `{.ascart}` attribute to a fenced code block, the line spacing
will be greatly reduced. Example:

```{.ascart}
 ┌───────┬──────────────────────────────┐
 │ SASKI │ Catus                        │     |\      _,,,---,,_
 ├───────┼──────────────────────────────┤     /,`.-'`'    -.  ;-;;,_
 │ Felis │ Prefered state of being, and │    |,4-  ) )-,_. ,\ (  `'-'
 │       │ with no care in the world.   │   '---''(_/--'  `-'\_)
 ├───────┴──────────────────────────────┤    __
 │ https://www.asciiart.eu/animals/cats │  ▓▓▒▒░░░ Felis Catus ░░░▒▒▓▓
 └──────────────────────────────────────┘
```

## Command-Lines

:::{.cmdline}
###### `sh` — Individual vs collapsed options
 * [**ls**][m7-ls1] -l -a -t -r `  # individual short options`{.sh .ws}
   * `-rw-r--r--    1 brx brx   907 May 25 15:16 LICENSE`
   * `-rw-r--r--    1 brx brx  4583 May 27 13:11 GCC Options.md`
 * [**ls**][m7-ls1] -latr `        # collapsed short options`{.sh .ws}
   * `-rw-r--r--    1 brx brx   907 May 25 15:16 LICENSE`
   * `-rw-r--r--    1 brx brx  4583 May 27 13:11 GCC Options.md`
 * **python3** -m pydoc hello.py
 * **python3** --version
 * **gcc** --version
:::

[m7-ls1]:
   https://www.man7.org/linux/man-pages/man1/ls.1.html
   "Man7 — ls(1) — List directory contents"
