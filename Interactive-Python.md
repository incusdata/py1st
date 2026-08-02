---
title: Interactive Python
abstract: |
   A quick way to start with Python, is to use it interactively. This means, using it in some form of [REPL][w-repl] (Read Eval Print Loop). In such an environment, the values of expressions are printed automatically, making it useful as a calculator. The main downside is that your input and results are lost when you exit this environment. 
---

[w-repl]:
   https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop
   "Wikipedia — Read-Eval-Print-Loop (REPL)"

# Start Stop

First choice to make, is which of many Python [REPL][w-repl]s to use. You can start a command-line REPL in a [terminal emulator][w-term-emu]; start a command-line REPL as a GUI; start a [Docker][w-docker] [container][idgh-py1st-wiki-venv-docker] with a command-line REPL; navigate in your browser to an [online REPL][idgh-py1st-wiki-intro-res-online]… the choices are legion.

To keep things simple, we shall [first](#cpython-repl) consider the ‘stock’ standard CPython command-line REPL running in a [terminal emulator][w-term-emu] or the [Windows Console][w-conhost], though the stock [IDLE][w-idle] graphical console has a ‘nicer’ interface, but is not always installed. And [later](#ipython-repl), the [IPython][w-ipython] REPL, which is a more productive and friendlier REPL. It too, has a GUI console counterpart, called [[qtconsole]{.cc}][pypi-qtconsole].

From this point, we assume that the **python** and/or **python3** executable is on [your PATH][idgh-py1st-wiki-path] by your own actions, or that you have activated a [virtual environment][idgh-py1st-wiki-venv], which will ensure [python]{.cc} is on your PATH.

[idgh-py1st-wiki-path]:
   Your-PATH.md
   "GitHub — Incus Data / Python First / Wiki / Your PATH"
[idgh-py1st-wiki-venv]:
   Virtual-Environments.md
   "GitHub — Incus Data / Python First / Wiki / Virtual Environments"
[w-docker]:
   https://en.wikipedia.org/wiki/Docker_(software)
   "Wikipedia — Docker (software)"
[w-idle]:
   https://en.wikipedia.org/wiki/IDLE
   "Wikipedia — IDLE (Python IDE)"
[idgh-py1st-wiki-intro-res-online]:
   Introduction.md#online-interpreters
   "GitHub — Incus Data / Python First / Introduction # Resources ## Online Interpreters"
[idgh-py1st-wiki-venv-docker]:
   Virtual-Environments.md#docker-podman
   "GitHub — Incus Data / Python First / Virtual Environments # Docker & Podman"
[pypi-qtconsole]:
   https://pypi.org/project/qtconsole/
   "PyPI — qtconsole"
[w-term-emu]:
   https://en.wikipedia.org/wiki/Terminal_emulator
   "Wikipedia — Terminal Emulator"
[w-conhost]:
   https://en.wikipedia.org/wiki/Windows_Console
   "Wikipedia — Windows Console"

## CPython REPL

If you have Python installed, and it is [on your PATH][idgh-py1st-wiki-path], or you have a [virtual environment][idgh-py1st-wiki-venv] enabled, simply running [python]{.cc} or [python3]{.cc} on the command-line, will ‘drop’ you into the standard Python interactive environment. You will be presented with something like this:

```
Python 3.14.6 ···
Type "help", "copyright", "credits" or "license" for more information.
>>> ▄
```

The first line will give you some information about the version of Python installed, and for which operating system it has been compiled. That can vary, so focus on the `3.14.…` part, which is the most important and says we are running Python 3.14. If yours says `3.15.…`, that is fine as well; if older that `3.10`, you have a problem.

The `>>>` part is called a *prompt*, which indicates that Python is ready for the ‘read’ part of REPL. The `▄` shows the position of your cursor. Whatever you type now, must be legal Python syntax, but it is good to see what Python will do if you type something like `hello` (which is not valid):

:::{.cmdline prompt='>>'}
 * hello
   * Traceback (most recent call last):
   *   File "<stdin>", line 1, in <module>
   * NameError: name 'hello' is not defined. Did you mean: 'help'?
 * ▄
:::

Python interprets your input when you press the [Enter]{.kbd} or [CR]{.kbd} (carriage return) key. Some call it the newline or linefeed key ([NL]{.chr} or [LF]{.chr}), which is unnecessarily confusing, but more on that later. This represents the ‘eval’ part in REPL.

The output depends on what you entered; in the above example, we entered garbage as far as Python is concerned, and it tells us that in no uncertain terms with an *error message*. The important parts in the message are the line number `line 1`, and the type of error [[NameError]{.cc}][p-e-namerror], which says clearly that [hello]{.cc} is not a defined (valid) [ident]{.stx}ifier.

Now we are *back* at the prompt, which means Python performed the ‘loop’ part in REPL. We can enter expressions, which the REPL will evaluate, and print the result of automatically. 

:::{.cmdline prompt='>>'}
###### `repl` — Automatic printing of expression statements
 * ``2 + 3 * 5``{.py}
   * 17
 * ▄
:::

The result of the expression is automatically (R)ead, (E)valuated, the result (P)rinted on the next line, and the prompt displayed for the next (L)oop.

:::{.admon .important}
&#x2757; This will not work in a script. When a *script* is interpreted, a [statement][p-simple-stmts] that consists only of an expression like above, will be *legal*, but will have *no effect*. We will have to use `print(2 + 3 * 5)` to get the same effect (which will work in a REPL as well).
:::

You can now type [exit()]{.cc}[CR]{.kbd} to terminate the Python REPL — we have established that it works. In Python 3.14, the parentheses are not necessary. In Unix-like shells, pressing [Ctrl-D]{.kbd} will also exit the REPL. In Windows, you can press [Ctrl+Z]{.kbd}[CR]{.kbd} to exit the REPL.

[p-e-namerror]:
   https://docs.python.org/3/library/exceptions.html#NameError
   "Python Standard Library — Exceptions # NameError"
[p-simple-stmts]:
   https://docs.python.org/3/reference/simple_stmts.html
   "Python Reference — 7. Simple Statements"

## IPython REPL

A much friendlier Python REPL can be found by way of [IPython][w-ipython]. This requires the [[ipython]{.cc} package][pypi-ipython] to be installed with [[pip]{.cc}][pypi-pip], preferably in a [virtual environment][idgh-py1st-wiki-venv]. Assuming you have a virtual enviroment called [py314]{.cc} in [~/work/py314]{.cc}, first *activate* the environment, if you have not already.

:::{.cmdline}
 * ``. ~/work/py314/activate            # Non-Windows``{.sh .ws}
 * ``~/work/py314/Scripts/Activate.ps1  # PowerShell``{.ps1 .ws}
 * **``pip``** ``install ipython``{.sh .ws}
 * **``ipython``{.sh .ws}**
:::

If you have [uv]{.cc} installed, and created your virtual environment with [uv venv ~/work/py314]{.cc}, you activate it the same way, but install with:

:::{.cmdline}
 * **``uv``** pip ``install ipython``{.sh .ws}
:::

This will provide you with an [ipython]{.cc} executable [command]{.stx}, which should be [on your `PATH`][idgh-py1st-wiki-path]. Running the [ipython]{.cc} command, will result in something like this:

```
Python 3.14.6 ···
Type 'copyright', 'credits' or 'license' for more information
IPython 9.16.0 -- An enhanced Interactive Python. Type '?' for help

In [1]: ▄
```

The number in the IPython prompt will increase with each line executed when you pressed [CR]{.kbd}. The output will also be numbered in relation to the input number:

```
In [1]: 2 + 3 * 5
Out[1]: 17

In [2]: ▄
```

You can refer to previous output with [_N]{.cc} where [N]{.cc} is the number in [Out\[N\]]{.cc}. So, if we continue from above:

```
In [2]: _1 * 3
Out[2]: 51 

In [3]: ▄
```

The [_1]{.cc} is replaced with the result of [Out\[1\]]{.cc}, which was [17]{.cc}, and multiplied by [3]{.cc}, gives [51]{.cc} (which later can be referred to as [_2]{.cc}).

To exit the IPython REPL, you can press [Ctrl+D]{.kbd} on both Unix-like and Windows environments; or you can type [exit]{.cc}[CR]{.kbd} — no need for parentheses to follow [exit]{.cc} as in versions of Python REPLs prior to 3.14.

IPython has many [magic commands][ipy-magics] or just ‘magics’, all starting with [%]{.cc}, designed to make your interactive use more productive; here a are a few useful ones:

 * [%ls]{.cc} — list files in current directory.
 * [%reset]{.cc} — delete all names (variables, functions, etc.)
 * [%clear]{.cc} — clear the screen (or [%cls]{.cc} on Windows).
 * [%cd]{.cc} — change working directory.
 * [%pwd]{.cc} — print working directory.
 * [%run]{.cc} `script.py` — run a `script.py` Python file in the current directory.
 * [%edit]{.cc} `script.py` — edit a file in your default system editor, or your configured editor (set in the EDITOR environment variable).
 * [%edit]{.cc} — edit command-line in a temporary file, execute when leaving editor.

[pypi-pip]:
   https://pypi.org/project/pip/
   "PyPI — pip — Package Installer for Python (Package Manager)"
[w-ipython]:
   https://en.wikipedia.org/wiki/IPython
   "Wikipedia — IPython"
[pypi-ipython]:
   https://pypi.org/project/ipython/
   "PyPI — ipython"
[ipy-magics]:
   https://ipython.readthedocs.io/en/stable/interactive/magics.html
   "IAPython Docs — Built-in Magic Commands"

# Interaction

Python REPLs allow you to enter Python [statements][p-simple-stmts] and [expressions][p-ref-expr], which the interpreters evaluate. In the case of expressions, they will print the results automatically. But there is more…

[p-ref-expr]:
   https://docs.python.org/3/reference/expressions.html
   "Python Reference — 6. Expressions"

## Command-Line Editing

You can edit a command-line by moving the cursor with the arrow keys ([Left]{.kbd}/[Right]{.kbd}). You can delete characters to the left with backspace ([BS]{.kbd}). Pressing [Ctrl-C]{.kbd} will abandon the current line.

Depending on your terminal emulator, you should be able to mark visible characters by dragging your mouse while pressing [Left-Click]{.kbd}. Once marked, you can copy the marked text to your clipboard. Many terminal emulators, including Windows Terminal, allow you to press [Shift-Ctrl-C]{.kbd} to perform the copy. Windows Console and Windows Terminal, also will copy the marked text to the clipboard with a [Right-Click]{.kbd} mouse button.

You can paste text in many terminal emulators, commonly with [Shift-Ctrl-V]{.kbd}. Windows Console and Terminal will also paste with a mouse [Right-Click]{.kbd} (as long as nothing is marked).

## Command-Line History

When you press the cursor [Up]{.kbd} key, you will have an opportunity to edit and re-evaluate a previous statement. The more you press [Up]{.kbd}, the older the statements in your command-line history will appear. You can edit any. The cursor [Down]{.kbd} key, will show more recent statements. Pressing [CR]{.kbd} on any historical statement, even after editing it, will cause Python to re-evaluate that statement.

IPython will persist your history in a file; so when you load IPython tomorrow, you can still access old statements. The number of line of history saved, is [configurable][ipy-config].

[ipy-config]:
   https://ipython.readthedocs.io/en/stable/config/intro.html
   "IPython — Introduction to IPython Configuration"

## Completion

In most REPLs, you seldom have to type out complete keywords or function names. You only need to type a few starting characters, and the press the [Tab]{.kbd} key, which will either complete it for you if there is only one possible completion; or it will show you a list of possibilities (you have to press [Tab]{.kbd} twice in the CPython REPL).

If more than one completion is possible, IPython will show a list of matching possibilities. You can select an appropriate completion by pressing [Tab]{.kbd} to select successive options. [Shift-Tab]{.kbd} will select backwards. Press [CR]{.kbd} to accept a completion.

## IPython Edit

If you are using IPython, you can use the **%edit** ‘[magic command][ipy-magics]’ to edit a new statement. This will open your default editor, which depends on your operating system and configuration. You can set an `EDITOR` environment variable to control which editor is used.

After editing a statement in the editor opened with **%edit**, once the temporary file has been saved and you exited the editor, IPython will load the content, and immediately interpret it.

IPython also allows you to use: ‘[%edit]{.cc} [file]{.stx}.py’ to edit a Python source file. It will automatically run the source file after you exited from the editor. You can explicitly use ‘[%run]{.cc} [file]{.stx}’ or ‘[%run]{.cc} [file]{.stx}.py’ to run any Python script in the current directory.

You can run external shell [command]{.stx}s in IPython with ‘**!**[command]{.stx}’. You can even pass arguments to the [command]{.stx}.

# Basic Statements

A statement in Python is generally terminated by a newline ([NL]{.chr}), but there are exceptions as a matter of convenience. Statements are not automatically assumed to be complete under the following conditions:

 * Between paired delimiters like [\[]{.cc}…[\]]{.cc}, [(]{.cc}…[)]{.cc} and [\{]{.cc}…[\}]{.cc}
 * Between the delimiters of a *long*, or *tripple-quoted*, string: ["&hairsp;"&hairsp;"]{.cc} … ["&hairsp;"&hairsp;"]{.cc}, or ['&thinsp;'&thinsp;']{.cc} … ['&thinsp;'&thinsp;']{.cc}.
 * After a backslash + newline sequence ([\\]{.cc}[NL]{.chr}).
 * After a colon ([:]{.cc}) as part of statement syntax.

A statement must be complete and error-free before it will be successfully evaluated.

You can explicitly continue a statement on the following line by ending a line with [\\]{.cc}[NL]{.chr} (backslash + newline). The REPL will change the prompt to a *continuation prompt*, in order to show you that the statement is not yet complete. There cannot be spaces or comments after the [\\]{.cc}.

:::{.cmdline prompt='>>'}
###### `repl` — Explicit statement continuation
 * `print("ABC`{.py}\
   `DEF`{.py}\
   `GHI")`{.py}
   * ABCDEFGHI
:::

Between paired delimiters, excluding single and double quotes, you can continue a statement without an explicit continuation backslash. The following statement is split across three lines, producing the same output as the example above. We can even add comments:

:::{.cmdline prompt='>>'}
###### `repl` — Delimiter statement continuation
 * ``print(                    #← first line of statement.``{.py .ws}\
   ``"ABCDEFGHI"               #← second line of statement.``{.py .ws}\
   ``)                         #← last line of statement.``{.py .ws}
   * ABCDEFGHI
:::

One can break lines between other paired delimiters like `{}` and `[]`.

::: {.cmdline prompt=">>"}
###### `repl` — More implicit statement continuations
* ``L = [ 12,``{.py .ws}\
  ``       34,``{.py .ws}\
  ``       56 ]``{.py .ws}
* `print(L)`{.py}
* ``D = {``{.py .ws}\
  ``   'A':12,``{.py .ws}\
  ``   'B':23,``{.py .ws}\
  ``   'C':34,``{.py .ws}\
  ``   }``{.py .ws}
* ``print(D)``{.py .ws}
:::

The leading spaces have no syntactic meaning (*semantics*) in the above examples, but in other places they are significant. We call such places *blocks*.

## Expression Statements

Python has several categories of statements, but a very common one, is the *expression statement*. It consists of any legal expression. For an expression statement to be useful, it should call a function, or modify program state.

:::{.cmdline prompt='>>'}
###### `repl` — Expression statement examples
 * ``123 + 654            #← no call, no state change.``{.py .ws}
   * 777``                  #← REPL will print result.``{.py .ws}
 * ``print(a)             #← function call.``{.py .ws}
:::

‘Useless’ expression statements are allowed. Only in a REPL, will the results of such expressions be printed automatically — in a script, they will just be ignored.

Technically, a function call does not involve an operator, but you can think of it as an operator: it performs a *task* and returns a *result*, just like an operator. A statement consisting of a single function call, is thus an expression statement (not a function call statement).

## Assignment Statements

Unlike some C-like languages, where the equal sign (**=**) is an *operator* that copies values and return results, in Python the equal sign is part of an [assignment statement][p-st-assign]. There are several assignment statements.

### Simple Assignment

The most basic and common assignment statement syntax, pairs an [ident]{.stx}ifier on the left, of an equal sign ([=]{.cc}), with an [expr]{.stx}ression on the right. Effectively, the [ident]{.stx}ifier *labels* the result of the [expr]{.stx}ression.

`     `{.ws}[ident]{.stx} [=]{.cc} [expr]{.stx}

This is the most common form of assignment. It will create the [ident]{.stx}ifier if it does not exist. A referenced to the [expr]{.stx}ression will be allocated to the [ident]{.stx}ifier. In Python, the [expr]{.stx}ression, will always be an *object* automatically allocated memory.

### Chained Assignment

Python supports *chained assignment*, which means a single statement syntax that assigns the value of an [expr]{.stx}ession to more than [ident]{.stx}ifier. These names will be created if necessary.

`     `{.ws}[ident~1~]{.stx} [=]{.cc} [ident~2~]{.stx} [=]{.cc} [ident~3~]{.stx} … [ident~n~]{.stx} [=]{.cc} [expr]{.stx}

Any number of names can appear on the left, separated by equal signs ([=]{.cc}).

:::{.cmdline prompt='>>'}
###### `repl` — Chained assigments
 * ``a = b = c = 123             #← a, b, and c reference `123`.``{.py .ws}
:::

The variables [a]{.cc}, [b]{.cc} and [c]{.cc}, will all ‘label’ the same object.

### Iterable Unpacking

It is possible to have several names on the left of a single assignment, as long as there is an *iterable* [expr]{.stx}ession on the right. Abstractly, an iterable is a collection of values that can be ‘visited’ one-by-one. The number of items in the iterable must match the number of names on the left. This syntax is called *iterable unpacking* (though some call it *tuple unpacking*).

`     `{.ws}[ident~1~]{.stx}[,]{.cc} [ident~2~]{.stx}[,]{.cc} … [ident~n~]{.stx} [=]{.cc} [iterable]{.stx}

The result of the right hand [expr]{.stx}ession can be of any [type]{.stx}, as long as the type supports iteration. This is true for functions like [[range]{.cc}][p-fn-range]. Types like [[list]{.cc}][p-fn-list] and [[tuple]{.cc}][p-fn-tuple], including their literals are also iterable.

:::{.cmdline prompt='>>'}
###### `repl` — Tuple unpacking
 * ``a, b, c = 11, 22, 33         #← (tuple) a=11, b=22, c=33.``{.py .ws}
 * ``a, b, c = [ 11, 22, 33 ]     #← (list)  a=11, b=22, c=33.``{.py .ws}
 * ``a, b, c = range(3)           #← (range) a=0,  b=1,  c=2.``{.py .ws}
 * ``T = 11, 22, 33``{.py .ws}
 * ``a, c, c = T                  #← (tuple) a=11, b=22, c=33.``{.py .ws}
 * ``a, b, c = 11, 22, 33, 44     #← ERROR (too many on right).``{.py .ws}
 * ``a, b, c = 11, 22             #← ERROR (too few on right).``{.py .ws}
:::

As long as the [expr]{.stx}ession on the right is an *iterable* of three values, the unpacking will work as expected. It does not matter if the [expr]{.stx}ession is a literal tuple, a literal list, the result of a function call, or a sequence variable (like [L]{.cc} above).

### Extended Iterable Unpacking

A special syntax allows *one* of the names on the left, to be prefixed with an asterisk ([\*]{.cc}). This name will always be a [[list]{.cc}][p-fn-list], and will ‘consume’ all the items on the right, that was not allocated to other names. It is possible for such a variable to be an empty list. This syntax is called *extended iterable unpacking*.

:::{.cmdline prompt='>>'}
###### `repl` — Extended iterable unpacking
 * ``*a,  b,  c = 11, 22, 33, 44  #← a=[11,22], b=33, c=44.``{.py .ws}
 * `` a, *b,  c = 11, 22, 33, 44  #← a=11, b=[22,33], c=44.``{.py .ws}
 * `` a,  b, *c = 11, 22, 33, 44  #← a=11, b=22, c=[33,44].``{.py .ws}
:::

### Augmented Assignments

As a convenient shorthand, Python allows for the assignment's equal sign to be prefixed with a *binary operator*, e.g.: [+=]{.cc}, [\*=]{.cc}, [%=]{.cc}, etc. The [op]{.stx} in the syntax below can be any binary [op]{.stx}erator:

`     `{.ws}[ident]{.stx} \ [op]{.stx}[=]{.cc} \ [expr]{.stx} \ \ \ \ []{.eqv} \ \ \ \ [ident]{.stx} [=]{.cc} [ident]{.stx} [op]{.stx} [expr]{.stx}

:::{.cmdline prompt='>>'}
###### `repl` — Augmented assignments
 * ``expr = 12 ``{.py .ws}
 * ``ident1 = ident2 = 34``{.py .ws}
 * ``ident1 = ident1 + expr         #← long way.``{.py .ws}
 * ``ident2 += expr                 #← augmented assignment.``{.py .ws}
 * ``print(ident1, ident2)          #▷ 46 46 ``{.py .ws}
:::

We strongly recommend you use these augmented assignment statements, since they reduce repetition of names, which in turn leaves fewer opportunities for errors.

[p-st-assign]:
   https://docs.python.org/3/reference/simple_stmts.html#assignment-statements
   "Python Reference — Simple Statements # 7.2 Assignment Statements"
[p-fn-list]:
   https://docs.python.org/3/library/functions.html#func-list
   "Python Reference — Built-In Functions # list()"
[p-fn-tuple]:
   https://docs.python.org/3/library/functions.html#func-tuple
   "Python Reference — Built-In Functions # tuple()"
[p-fn-range]:
   https://docs.python.org/3/library/functions.html#func-range
   "Python Reference — Built-In Functions # range()"


# Identifiers

Formally, we call the names of ‘things’, [identifiers][w-ident]. Anything with a name, must follow identifier [naming rules][p-ref-ident]. Simplified: an [iden]{.stx}ifier must start with an alphabetic character, after which, more alphabetic characters, decimal digits, and underscores can follow, to arbitrary length. There are special situations where we start indentifiers with one or two underscores (&hairsp;[_]{.cc}&hairsp;), but that is only in advanced situations.

<!--TODO: Once implemented, enable this, and remove the alternative below
`     `{.ws}[ident]{.stx} []{.dra} [alpha-char]{.stx}[ [alpha-char]{.stx}[]{.alt}[digit]{.stx}[] ]{.opt}{.zom}
-->

`     `{.ws}[ident]{.stx} []{.dra} [alpha-char]{.stx}[ [alpha-char]{.stx}[]{.alt}[digit]{.stx} ]~*~

The above means: An *identifier* is defined in terms of an alphabetic character, followed by zero or more of either another alphabetic character, or a decimal digit. It cannot start with a digit.

An additional identifier naming rule states that it cannot be a [keyword](#keywords). See below.

<!--TODO: Remove this experiment:-->
`     `{.ws}[ [extern]{.cc .def} []{.alt} [void]{.cc} ]{.opt} [ident]{.stx} [(]{.cc} [ [parm-list]{.stx} []{.alt} [void]{.cc} ]{.opt} [)]{.cc}

`     `{.ws}[ [extern]{.cc .def} []{.alt} [void]{.cc} ] [ident]{.stx} [(]{.cc} [ [parm-list]{.stx} []{.alt} [void]{.cc} ] [)]{.cc}

## Keywords

Keywords, also called [reserved words][w-keyword] cannot be used as identifiers. They can only be used for their intend purpose. Python does not have too many keywords

:::{.admon .warning}
***Renaming Built-In Functions***

Unlike keywords, you *can* change the meaning of built-in function names. Even though it is syntactically legal, you should **never**, **ever**, do that. Linters like [pylint]{.cc} will warn you when you do, so pay attention.
:::

For completeness, here is a list of the Python 3.14 keywords, as produced by the output of [help('keywords')]{.cc} in the Python REPL:

```{.output}
False    class      from       or
None     continue   global     pass
True     def        if         raise
and      del        import     return
as       elif       in         try
assert   else       is         while
async    except     lambda     with
await    finally    nonlocal   yield
break    for        not
```

[w-keyword]:
   https://en.wikipedia.org/wiki/Reserved_word
   "Wikipedia — Reserved Word (keyword)"

## Dictionaries

All identifiers are stored in *dictionaries*. Some identifiers, like those of the built-in functions, are stored in the ‘global’ dictionary. We can inspect dictionaries with the built-in [[dir]{.cc} function][p-fn-dir].

:::{.cmdline prompt='>>'}
###### `repl` — Built-ins name dictionary
 * ``import builtins``{.py .ws}
 * ``print( dir(builtins) )``{.py .ws}
:::

Calling [[dir()]{.cc}][p-fn-dir] without arguments in a REPL, will show names in the current module's dictionary. You can get a reference to this dictionary *object*, using the [[global]{.cc} function][p-fn-globals].

In the short term, ignore all names starting with double underscores that may be present in dictionaries. In the output of the following examples, we omitted those names for clarity.

:::{.cmdline prompt='>>'}
###### `repl` — Dictionary inspections
 * ``dir()                     #←only `__*` names.``{.py .ws}
 * ``X = 123                   #←add `X` to dictionary.``{.py .ws}
 * ``dir()                     #▷ ['X']``{.py .ws}
 * ``print( X )                #▷ 123``{.py .ws}
 * ``print( globals()['X'] )   #▷ 123``{.py .ws}
 * ``list(globals())           #▷ ['X']``{.py .ws}
:::

The last statement tries to emphasise the fact that all names are stored in a dictionary. Python just provide some automatic name lookups, that is why ‘[print( X )]{.cc}’ produces the same result as the more inconvenient: ‘[print( globals()['X'] )]{.cc}’.

:::{.admon .note}
**Namespaces & Scopes**

In Python, a dictionary is often used to represent a [namespace][w-namespace]. A dictionary is a mapping from keys (like names), to corresponding values (objects). Different dictionaries can represent different namespaces and since dictionaries can contain other dictionaries as values, it is possible to represent nested namespaces. This is how all [scopes][w-scope] work in Python.
:::

[w-ident]:
   https://en.wikipedia.org/wiki/Identifier_(computer_languages)
   "Wikipedia — Identifier (computer language)"
[p-ref-ident]:
   https://docs.python.org/3/reference/lexical_analysis.html#identifiers
   "Python Reference — 2.3 Identifiers and Keywords"
[p-fn-dir]:
   https://docs.python.org/3/library/functions.html#dir
   "Python Built-In Functions — dir()"
[p-fn-globals]:
   https://docs.python.org/3/library/functions.html#globals
   "Python Built-In Functions — globals()"
[w-namespace]:
   https://en.wikipedia.org/wiki/Namespace
   "Wikipedia — Namespace"
[w-scope]:
   https://en.wikipedia.org/wiki/Scope_(computer_science)
   "Wikipedia — Scope (computer science)"

## Named Values

In Python, each entry in a dictionary not only contains an identifier, but also a [reference][w-reference] to a [value]{.stx}, also known as an [object]{.stx}. And that is all. This rule has no exceptions.

An identifier is effectively just a label for an [object]{.stx}. The identifier itself has no type, and is only a *temporary* label for some value. The label can later refer to any other value. This is very unlike many other programming languages.

The term *variable* is thus a bit of a misnomer in Python. It is a convenient term, but can be misinterpreted. A *variable*, i.e., some [ident]{.stx}ifier, as we have seen, is just an entry in a dictionary; all it ‘stores’, is a *reference* to some [object]{.stx}. We can change the reference, but that is all that can ‘vary’.

A ‘variable’ (i.e., a dictionary entry), has no [type]{.stx}. The object it currently references, *does* have a [type]{.stx}. This name is only temporarily associated with or ‘has a reference to’, a value — it can be changed at any time.

:::{.cmdline prompt='>>'}
###### `repl` — Named values (identifiers) as variables
 * ``x = 123               #← associate `x` with `123`.``{.py .ws}
 * ``print( type(x) )      #▷ int``{.py .ws}
 * ``x = 1.23              #← change reference in `x`.``{.py .ws}
 * ``print( type(x) )      #▷ float``{.py .ws}
 * ``x = "ABC"             #← change reference in `x`.``{.py .ws}
 * ``print( type(x) )      #▷ str``{.py .ws}
 * ``p = print             #← associate `p` with `print`.``{.py .ws}
 * ``p("Hello")            #▷ Hello``{.py .ws}
 * ``print = bin           #← associate `print` with `bin`.``{.py .ws}
 * ``p( print(123) )       #▷ 0b1111011``{.py .ws}
:::

Changing the references of built-in names like the names of built-in functions, is never a good idea. We only want to emphasise the important points:

 * all names (identifiers) are entries in dictionaries;
 * all names have a temporary associations to values via references.

You are welcome to call ‘names’ ‘*variables*’, when you know the name references some value, but do misunderstand how names AKA identifiers actually work.

## Deleting Names

Names can be only be removed from dictionaries with the [[del]{.cc} statement][p-st-del]. The [[del]{.cc}][p-st-del] is not a built-in function. It has no return result, unlike a function, which always have a return result.

:::{.cmdline prompt='>>'}
###### `repl` — Delete names
 * ``x = 123 ; print( x )  #▷ 123``{.py .ws}
 * ``del x``{.py .ws}
 * ``print( x )            #← ERROR (`x` does not exist)``{.py .ws}
:::

The last statement tries to look up the name [x]{.cc} in the current dictionary, but fails, since we [[del]{.cc}][p-st-del]eted it in the previous statement.

[w-reference]:
   https://en.wikipedia.org/wiki/Reference_(computer_science)
   "Wikipedia — Reference (computer science)"
[p-st-del]:
   https://docs.python.org/3/reference/simple_stmts.html#the-del-statement
   "Python Simple Statements — 7.5 The del Statement"

# Help

Inside a Python REPL, you can request help for any [built-in][p-fn] function, [standard library][p-lib] module, or [keyword][p-kwds] by default. If you have extra modules installed, or even your own, you can still request help, but you must first import the module.

[p-lib]:
   https://docs.python.org/3/library/index.html
   "Python Standard Library"

## Topical Help 

Python has a built-in function called [[help]{.cc}][p-fn-help]. To call this function you must append the function call operator: `()` or `('‹arg›')`. For an [arg]{.stx}ument, you can enter an standard library module name, a built-in function name, or even a keyword.

:::{.cmdline prompt=">>"}
###### `repl` — Topical help
 * `help('keywords')      #← show list of keywords.`{.py .ws}
 * `help('modules')       #← show list of standard modules.`{.py .ws}
 * `help('topics')        #← specific topics help understands.`{.py .ws}
 * `help('PRECEDENCE')    #← show operator precedence table.`{.py .ws}
 * ``help('import')        #← help for the `import` statement.``{.py .ws}
 * ``help('while')         #← help for the `while` statement.``{.py .ws}
 * ``help('print')         #← help for `print` built-in function.``{.py .ws}
:::

There seems to be no simple way to get a list of [built-in functions][p-fn], but these two statements will show a list of them.

:::{.cmdline prompt=">>"}
###### `repl` — List built-in function names
* `import builtins as bi, inspect as it`{.py .ws}
* `[f for f in dir(bi) if it.isbuiltin(getattr(bi, f))] #(1)`{.py .ws}
:::
 
 1) The above does not output the names of *type functions*, for some reason.

[p-fn]:
   https://docs.python.org/3/library/functions.html
   "Python — Built-In Functions"

## Interactive Help
 
When calling [[help()]{.cc}][p-fn-help] without an [arg]{.stx}ument, you will enter interactive help, which will display a message with some suggestions. The prompt will change to indicate that your are now inside an interactive help REPL. Type [quit]{.cc} to exit the interactive help, or press [Ctrl-D]{.kbd}.

:::{.cmdline prompt=">>"}
###### `repl` — Start interactive help REPL
* help()
:::

This will enter a help REPL, with a different prompt. This indicates that normal Python statements and expressions are not allow; only help-specific keywords can be typed. You can, for example, get a list of [keywords][p-kwds] by entering [keywords]{.cc}[CR]{.kbd}. Any of the example above you can enter as: ‘[command]{.stx}[CR]{.kbd}’:


:::{.cmdline prompt="help>"}
###### `help` — Interactive help REPL
 * keywords
 * modules
 * topics
 * PRECEDENCE
 * quit
 * ▄
:::

Notice how the prompt changes when you are inside the interactive help REPL.

[p-kwds]:
   https://docs.python.org/3/reference/lexical_analysis.html#keywords
   "Python — Syntax # 2.3.1 Keywords"

To inspect the documentation for the any [module]{.stx}, we must first [[import]{.cc}][p-st-import] the module. In general terms, the process is:

`     `{.ws}[[import]{.cc}][p-st-import] \ [module]{.stx}\
`     `{.ws}[[help]{.cc}][p-fn-help][(]{.cc} [module]{.stx} [)]{.cc}

To display documentation for the [[math]{.cc} module][p-m-math], as an example:

:::{.cmdline prompt=">>"}
###### `repl` — Show math module documentation
 * `import math`{.py .ws}
 * `help(math)       #←module documentation.`{.py .ws}
 * `help(math.sqrt)  #←function documentation.`{.py .ws}
:::

[p-m-math]:
   https://docs.python.org/3/library/math.html?highlight=math%20module#module-math
   "Python — math — Mathematical Functions"
[p-st-import]:
   https://docs.python.org/3/reference/simple_stmts.html#import
   "Python — Reference / 7.11 The import Statement"
[p-fn-help]:
   https://docs.python.org/3/library/functions.html#help
   "Python — Built-In Functions # help"

# Text IO

As we have seen Python REPLs will automatically print the results of [expr]{.stx}ession statements. This is not always ideal, since we have no control over *how* it outputs the results. Plus, this REPL-only feature does not work in scripts.


## Text Output

The premier ‘tool’ for writing output, is the [[print]{.cc} function][p-fn-print]. It is documented as follows:

`     `{.ws}[[print]{.cc}][p-fn-print][(]{.cc} \**objects*, [sep]{.cc}='\ \ ', [end]{.cc}='\\n', [file]{.cc}=[None]{.cc}, [flush]{.cc}=[False]{.cc} [)]{.cc}

The ‘\**objects*’ part means that you can pass [[print]{.cc}][p-fn-print] *any* number of arguments. It will print each of those arguments separated by the value of the [sep]{.cc} parameter, which by default is space ([SP]{.chr} or &thinsp;␣&thinsp;). After all arguments have been send to output, the value of [end]{.cc} (by default [NL]{.chr} or ['\\n']{.cc}) is added.

The other parameters have default values as indicated, which means they are optional. To pass them however, we must use *keyword-argument syntax*, which means me must specify the name of the parameter: [parm]{.stx}**=**[arg]{.stx}.

:::{.cmdline prompt='>>'}
###### `repl` — Print function examples
 * `print("ABC", "DEF", 123)       #▷ ABC␣DEF␣123`{.py .ws}
 * `print("ABC", 'DEF' sep='!')    #▷ ABC!DEF`{.py .ws}
 * `print("ABC", end='#'))         #← ABC     ← with no newline.`{.py .ws}
 * `print("DEF")                   #▷ ABCDEF  ← result of last two.`{.py .ws}
:::

By default, the output ‘[file]{.cc}’ is *standard output*. Practically, this will mean your terminal screen… unless you have changed the default using your shell's [redirection][w-redirect] or [piping][w-piping] features. This works in PowerShell on Windows as well.

The standard output file is represented by [[sys.stdout]{.cc}][p-sys.stdout]. You can change the default output ‘file’ of [[print]{.cc}][p-fn-print] by passing the ‘[file]{.cc}=[expr]{.stx}’ keyword argument. The most immediate use of this, is to write error messages your program produces to *standard error*, or [[sys.stderr]{.cc}][p-sys.stderr].

:::{.cmdline prompt='>>'}
###### `repl` — Set output for print
 * `import sys`{.py .ws}
 * `print("Hello")                    #← write to sys.stdout.`{.py .ws}
 * `print("Hello", file=sys.stdout)   #← write to sys.stdout.`{.py .ws}
 * `print("Error", file=sys.stderr)   #← write to sys.stderr.`{.py .ws}
:::

You would rarely, if ever, need to the pass the [flush]{.cc} keyword argument. The only viable option is [True]{.cc} (since the default is [False]{.cc}). Output is normally automatically flushed at the end of a line at the latest, or before any input.

:::{.cmdline prompt='>>'}
###### `repl` — Flush keyword argument
 * `print("Hello", flush=True)`{.py}
:::

The keyword arguments you pass to [[print]{.cc}][p-fn-print] can appear in any order.

[p-fn-print]:
   https://docs.python.org/3/library/functions.html#print
   "Python Functions — print()"
[w-redirect]:
   https://en.wikipedia.org/wiki/Redirect_(computing)
   "Wikipedia — Redirect (computing)"
[w-piping]:
   https://en.wikipedia.org/wiki/Pipeline_(Unix)
   "Wikipedia — Unix Pipeline"
[p-sys.stdout]:
   https://docs.python.org/3/library/sys.html#sys.stdout
   "Python Library — sys.stdout"
[p-sys.stderr]:
   https://docs.python.org/3/library/sys.html#sys.stderr
   "Python Library — sys.stderr"

## Text Input

We can also perform text input using the [[input]{.cc} function][p-fn-input]. It allows for an optional *prompt* to be displayed before waiting for input. The [[input]{.cc}][p-fn-input] function returns a [[str]{.cc}][p-fn-str] result, minus a trailing newline.

It is possible for [[input]{.cc}][p-fn-input] to return an empty string. When [Ctrl-D]{.kbd} is pressed (or [Ctrl-Z]{.kbd}[CR]{.kbd} on Windows), it signals end-of-file ([EOF]{.chr}), and an [[EOFError]{.cc}][p-e-eof] exception will be raised.

:::{.cmdline prompt='>>'}
###### `repl` — Text input
 * `print("Name?: ", end='')         #← prompt user.`{.py .ws}
 * `name = input()                   #← wait for input.`{.py .ws}
 * `print(f"You entered: {name}")    #← use input.`{.py .ws}
 * `name = input("Name?: ")          #← prompt & wait for input.`{.py .ws}
 * `print(f"You entered: {name}")    #← use input.`{.py .ws}
:::

You do not always need text input; sometimes you want the user to enter, for example, an [[int]{.cc}][p-fn-int]eger value. So, if the user enters [123]{.cc}, [[input]{.cc}][p-fn-input] will return a [[str]{.cc}][p-fn-str] value: ["123"]{.cc}. It *looks* like a number, but in the computer, it is just a sequence of characters — we cannot perform general arithmetic on strings.

Strings that ‘look like’ integers can be converted to strings using [[int]{.cc}][p-fn-int]. When the string does *not* ‘look like’ an integer, [[int]{.cc}][p-fn-int] will raise a [ValueError]{.cc} exception. Which means you have to ‘handle’ the exception, otherwise your program will crash immediately.

Until we have discussed exceptions in more depth, you can either ignore the possibility, or use the following pattern:

:::{.cmdline prompt='>>'}
###### `repl` — Input error handling pattern
 * `import sys`{.py}
 * `try:`{.py}\
   `   height = input("Height?: ") #← input height.`{.py .ws}\
   `   print(f"Height: {height}")  #← use height.`{.py .ws}\
   `except:                        #← handle any exception.`{.py .ws}\
   `   print("Bad input", file=sys.stderr)`{.py .ws}
:::

The first [[print]{.cc}][p-fn-print] line will not execute if an exception was raised — execution will continue on the line after [except:]{.cc}&thinsp;. If no exception was raised, statements after [except]{.cc}, will not execute.

The [file=sys.stderr]{.cc} part, is just a *good convention*: error messages should be written to standard error, which in Python, means: [sys.stderr]{.cc}.

If you need to input a floating point value, substitute [[int]{.cc}][p-fn-int] above, with [[float]{.cc}][p-fn-float].

[p-fn-input]:
   https://docs.python.org/3/library/functions.html#input
   "Python Built-In Functions — input()"
[p-fn-str]:
   https://docs.python.org/3/library/stdtypes.html#str
   "Python Built-In Functions — str()"
[p-fn-int]:
   https://docs.python.org/3/library/stdtypes.html#int
   "Python Built-In Functions — int()"
[p-fn-float]:
   https://docs.python.org/3/library/stdtypes.html#float
   "Python Built-In Functions — float()"
[p-e-eof]:
   https://docs.python.org/3/library/exceptions.html#EOFError
   "Python Built-In Exceptions — EOFError"
