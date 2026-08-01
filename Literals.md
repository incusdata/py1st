[Literals][p-ref-literals] are constant values with clear and apparent values. You surely have no doubt about the value of **123**? It is clearly not a variable… its value cannot vary, it is fixed, or *constant* (which is the reason some use the term ‘constant’ instead of the more appropriate ‘[literal][w-literal]’).

In Python terminology, **123** is a literal having the *value* **123** with [type][idgh-wiki-types] of [**int**][p-fn-int]. There are several other types of literals, each having their on syntax to distinguish them from other literals.

[p-ref-literals]:
   https://docs.python.org/3/reference/expressions.html#literals
   "Python Reference — Expressions # 6.2.2 Literals"
[idgh-wiki-types]:
   Simple-Types.md
   "GitHub — Incus Data / Python First / Wiki / Simple Types"
[p-fn-int]:
   https://docs.python.org/3/library/functions.html#int 
   "Python Built-in Functions — int()"
[w-literal]:
   https://en.wikipedia.org/wiki/Literal_(computer_programming)
   "Wikipedia — Literal (computer programming)"

# None

A lone, but special literal, is [**None**][p-lit-none], which is the only value that has [type]{.stx}: [**NoneType**](##). If you are familiar with [SQL][w-sql], you can think of [**None**][p-lit-none] as roughly equivalent to NULL.

Some functions will return [**None**][p-lit-none] under certain conditions. We cannot test if an [expr]{.stx}ession is equal to [**None**][p-lit-none] with the equality or inequality operators. Instead, we must use the [identity comparison][p-expr-ident] operators [**is**][p-expr-ident] and [**is not**][p-expr-ident].

#### **py** — *None value and inspection*
```py
>> x = None
>> print(x is None)          #→ True
>> x = ""
>> print(x is not None)      #→ True
```

Some functions also has a default argument of [**None**][p-lit-none] for a parameter. Such a parameter is then *optional* — you can pass an argument, or omit the argument (in which case [**None**][p-lit-none] will be used automatically).

[p-lit-none]:
   https://docs.python.org/3/library/constants.html#None
   "Python Constants — None"
[w-sql]:
   https://en.wikipedia.org/wiki/SQL
   "Wikipedia — SQL (Structured Query Language)"
[p-expr-ident]:
   https://docs.python.org/3/reference/expressions.html#is-not
   "Python Expressions — 6.10.3 Identity Comparisons"
[w-null-sql]:
   https://en.wikipedia.org/wiki/Null_(SQL)
   "Wikipedia — NULL (SQL)"

# Boolean Literals

Not much to say here… there are only two boolean literals: [**False**][p-lit-false] and [**True**][p-lit-true], and they have type [**bool**][p-fn-bool] (boolean). When you convert these literals to [**int**][p-fn-int]egers, [**False**][p-lit-false] will become **0**, and [**True**][p-lit-true] will become **1**.

#### **py** — *Boolean literals True and False*
```py
>> print(True)                         #→ True
>> print(False)                        #→ False
>> print(int(False), int(True))        #→ 0 1
```

Because of [implicit boolean][idgh-wiki-types-implicit-bool] conversion, we seldom have need for these literals.

#### **py** — *Boolean expressions in if statements*
```py
>> a = True
>> if a == True: print("a is TRUE")    #→ a is TRUE
>> if a: print("a is TRUE")            #→ a is TRUE
```

The second statement unnecessarily used ‘**if a == True:**’, whereas ‘**if a:**’ worked just as well. The last version is more pythonic<sup>[1]</sup>, if you care.

> <sup>[1]</sup> From Wikipedia: “A common neologism in the Python community is pythonic, which has a wide range of meanings related to program style. "Pythonic" code may use Python idioms well, be natural or show fluency in the language, or conform with Python's minimalist philosophy and emphasis on readability. Code that is difficult to understand or reads like a rough transcription from another programming language is called unpythonic.”

[p-lit-false]:
   https://docs.python.org/3/library/constants.html#False 
   "Python Literals — False (bool)"
[p-lit-true]:
   https://docs.python.org/3/library/constants.html#True 
   "Python Literals — True (bool)"
[p-fn-bool]:
   https://docs.python.org/3/library/functions.html#bool
   "Python Built-in Functions — bool(x=False)"
[idgh-wiki-types-implicit-bool]:
   Simple-Types.md#implicit-conversion
   "GitHub — Incus Data / Python First / Wiki / Types # Implicit Conversion"

# Integer Literals

Numeric literal values without a decimal point are given the type [**int**][p-fn-int]. The default numeric base is 10 (decimal 0…9), so ‘**123**’ means ‘one hundred and twenty three’. Python allows us to represent them in [binary][w-binary], [octal][w-octal], [decimal][w-decimal] (default) or [hexadecimal][w-hexadecimal]. We can make literals more readable with embedded underscores.

[w-decimal]:
   https://en.wikipedia.org/wiki/Decimal
   "Wikipedia — Decimal"
[w-binary]:
   https://en.wikipedia.org/wiki/Binary_number
   "Wikipedia — Binary Number"
[w-octal]:
   https://en.wikipedia.org/wiki/Octal
   "Wikipedia — Octal"
[w-hexadecimal]:
   https://en.wikipedia.org/wiki/Hexadecimal
   "Wikipedia — Hexadecimal"

## Literal Syntax & Size

When we write literals, Python allows us to separate groups of digits with underscores (**_**). This is simply so that large numbers can be easier to read — they add no additional meaning. Python can handle *huge* integers, because Python supports [arbitrary-precision][w-aprec-arith] arithmetic.

#### **py** — *Integer literals*
```py
>> print(123**22)                 #→ 123 to the power 22
#→ 9504131829385633475328037226727697567232041929
>> print(123456789)               #→ 123456789
>> print(123_456_789)             #→ 123456789
>> print(1_2_3_4_5_6_7_8_9)       #→ 123456789
```

The last example is just obnoxious; there is never a good reason to put an underscore between every single digit — but Python does not care, it still sees it as the value **12345689**. Readers of your code might just be annoyed if you overdo it. Line two, on the other hand, is a good example to follow.

## Binary Literals

Integer literals can use base 2 ([binary][w-binary]). For the digits to be treated as binary, the literal has to start with **0b**. The decimal value **123**, in binary, can thus be written as **0b1111011**, or **0b_0111_1011** (leading zeros are allowed). To learn that **123** can be written in this binary value, you can use the built-in [**bin** function][p-fn-bin].

#### **py** — *Binary integer literals*
```py
>> print(bin(123))                #→ 0b1111011
>> print(0b1111011)               #→ 123
>> print(0b_0111_1011)            #→ 123
```

Not everybody needs to work with binary, so you could probably safely ignore binary. But understanding binary numbers can be an advantage.

[w-aprec-arith]:
   https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic
   "Wikipedia — Arbitrary-Precision Mathematics"
[p-fn-bin]:
   https://docs.python.org/3/library/functions.html#bin
   "Python Built-In Functions — bin()"

## Octal Literals

There are some applications and codes that are documented in [octal][w-octal] (base 8), like the [permissions][w-fs-perms] of files and directories on Unix-like file systems. It is convenient because every octal digit (0-7) represents exactly three bits.

```
 0₈ ≡ 000₂   1₈ ≡ 001₂   2₈ ≡ 010₂   3₈ ≡ 011₂
 4₈ ≡ 100₂   5₈ ≡ 101₂   6₈ ≡ 110₂   7₈ ≡ 111₂
```

By memorising the above relationships, it becomes easy to convert from octal to binary, or from binary to octal — for those who care. Like binary, not everybody *needs* octal.

To write an literal integer in octal, you must start it with **0o**. Like the other literals, you can separate digits with underscores. You can get the octal representation of any number using the [**oct** function][p-fn-oct].

#### **py** — *Octal an binary conversions*
```py
>> oct(123)                     #→ 0o173 ≡ 1×8²+7×8¹+3×8⁰ = 123
>> bin(0o_173)                  #→ 0b1111011
>> oct(0b_1_111_011)            #→ 0o173
```

[p-fn-oct]:
   https://docs.python.org/3/library/functions.html#oct
   "Python Built-In Functions — oct()"
[w-fs-perms]:
   https://en.wikipedia.org/wiki/File-system_permissions
   "Wikipedia — File-System Permissions"

## Hexadecimal Literals

For base 16 ([hexadecimal][w-hexadecimal]) literals, the prefix **0x** is used. In hexadecimal, every one of the sixteen digits (0…9 A…F), represents exactly four bits when converted to binary. This again makes it easy to convert from hexadecimal to binary and vice versa.

```
 0₁₆ ≡ 0000₂   1₁₆ ≡ 0001₂   2₁₆ ≡ 0010₂   3₁₆ ≡ 0011₂
 4₁₆ ≡ 0100₂   5₁₆ ≡ 0101₂   6₁₆ ≡ 0110₂   7₁₆ ≡ 0111₂
 8₁₆ ≡ 1000₂   9₁₆ ≡ 1001₂   A₁₆ ≡ 1010₂   B₁₆ ≡ 1011₂
 C₁₆ ≡ 1100₂   D₁₆ ≡ 1101₂   E₁₆ ≡ 1110₂   F₁₆ ≡ 1111₂
```

The [**hex** function][p-fn-hex] can show the hexadecimal representation of an integer value.

#### **py** — *Hexadecimal and binary conversions*
```py
>> hex(123)             #→ 0x7b
>> 0x0000_007B          #→ 123
>> bin(0x7B)            #→ 0b1111011
```

And yes, not everybody might need to know or use hexadecimal values; but Unicode and other encoding values are often document with hexadecimal, to it may become more useful than you think — generally more useful than binary or octal, at least.

[p-fn-hex]:
   https://docs.python.org/3/library/functions.html#hex
   "Python Built-In Functions — hex()"

# Floating-Point Literals

Sometimes integers do not fit the data we want to represent. For this purpose Python supplies the standard [**float** type][p-fn-float] to represent numbers that can represents fractions in decimal notation (digits following a decimal point).

If a numeric literal contains a decimal point, and/or an **e**/**E** (for *exponent*), its type will be [**float**][p-fn-float], and not [**int**][p-fn-int] or anything else. For those familiar with C, this maps to **double**, which is an [IEEE-754][w-ieee754] [double-precision][w-double], 64-bit floating-point value.

#### **py** — *Types of floating point literals*
```py
>> type(.0)             #→ float
>> type(0.)             #→ float
>> type(0.0)            #→ float
>> type(1_234.456_7)    #→ float
>> type(1e234567)       #→ float
>> type(1_E_234_567)    #→ ERROR
>> type(1E234_567)      #→ float
```

## Float Notation

Python supports two notations for floating point literals. The **e**xponent is case-insensitive, so **E** will also work:

 * Fixed point notation: **1234.56789**
 * Exponential notation: **1.2345689e3**

Underscores for digit grouping are allowed, but never before or after the **e**/**E**.

When a [**float**][p-fn-float] is converted to [**str**][p-fn-str], implicitly or explicitly, Python will try to create as few significant digits as possible for the value to remain unambiguous. Because of [IEEE-754][w-ieee754], it can only display a maximum of 17 significant digits.

#### **py** — *Floating point and fixed point notation*
```py
>> a = 123.456_789_012_345_678_900
>> b = 0.123_456_789_012_345_678_900
>> print(str(a))                     #→ 123.45678901234568
>> print(str(b))                     #→ 0.12345678901234568
>> print(a)                          #→ 123.45678901234568
>> print(b)                          #→ 0.12345678901234568
```

Whether explicitly converted with [**str**][p-fn-str], or implicitly by [**print**][p-fn-print], the result is the same.

[w-ieee754]:
   https://en.wikipedia.org/wiki/IEEE_754
   "Wikipedia — IEEE 754"
[p-fn-print]:
   https://docs.python.org/3/library/functions.html#print
   "Python Built-In Functions — print()"
[p-fn-str]:
   https://docs.python.org/3/library/functions.html#func-str
   "Python Built-In Functions — str()"

## Float Conversions 

You cannot represent a floating point literal in hexadecimal notation in Python. You can convert it to hexadecimal with the [**hex** function][p-fn-hex], or the [**float.hex()** method][p-float.hex]. We can convert from a hexadecimal string back to [**float**][p-fn-float] with [**float.fromhex()**][p-float.fromhex].

#### **py** — *Float conversions*
```py
>> float.hex(1.23)
#→ '0x1.3ae147ae147aep+0'
>> float.fromhex('0x1.3ae147ae147aep+0')
#→ 1.23
```

We sometimes have need to convert a floating point value to an [**int**][p-fn-int]eger value. This will *truncate* any decimals. If you want to *round* a decimal to a certain number of places, you can use the built-in [**round** function][p-fn-round]. 

The Python Standard Library's [**math**][p-lib-math] module provide many mathematical functions that operate on [**float**][p-fn-float] values, and many return [**float**][p-fn-float] values as results. It also provides the [**floor**][p-lib-math-floor], [**ceil**][p-lib-math-ceil] and [**trunc**][p-lib-math-trunc] functions for other ways to convert to integers. 

#### **py** — *Rounding and other float operations*
```py
>> import math          #← necessary.
>> num = 12.3456789
>> math.floor(num)      #→ 12
>> math.ceil(num)       #→ 13
>> math.int(num)        #→ 12
>> int(num)             #→ 12
>> round(num)           #→ 12
>> round(num, 2)        #→ 12.35
>> num = 12345.6789
>> round(num, -1)       #→ 12350.0
>> round(num, -2)       #→ 12300.0
```

As you can see, [**round**][p-fn-round] takes an optional argument. If positive, it will round to the indicated number of decimals. When negative, it will round to the left; so **-1**, will round to the nearest unit of 10, and **-2** to the nearest 100, and so on.

## Float Formatting

Since it is something that may quickly bother your when you start experimenting with floating pointer numbers, is the number of decimal digits displayed. We can control that with *formatting*, which is quite a large topic, but here are a few examples:

#### **py** — *Formatting floats*
```py
>> num = 1234.567890
>> print("num: |%.4f|" % num)               #→ |1234.5679|
>> print("num: |%10.4f|" % num)             #→ |  1234.5679|
>> print("num: |%-10.4f|" % num)            #→ |1234.5679  |
>> print("num: |{N:4f}|".format(N=num)      #→ |1234.5679|
>> print("num: |{N:10.4f}|".format(N=num))  #→ |  1234.5679|
>> print("num: |{N:<10.4f}|".format(N=num)) #→ |1234.5679  |
>> print("num: |{N:^10.4f}|".format(N=num)) #→ | 1234.5679 |
>> print(f"num: |{num:10.4f}|")             #→ |  1234.5679|
>> print(f"num: |{num:<10.4f}|")            #→ |1234.5679  |
>> print(f"num: |{num:^10.4f}|")            #→ | 1234.5679 |
```

The basic [formatting syntax][p-strfmt-stx] for floating point uses the **f** specifier for *fixed point*, and the **e** specifier for *exponential* notation.

&nbsp;&nbsp;&nbsp;&nbsp; [[[align]{.stx}](## "< left&#10;> right&#10;^ centre")][[[width]{.stx}](## "Total output width")][[**.**](## "Required")[[digits]{.stx}](## "Number of significant digits")][**f**](## "Fixed point formatting specifier") &nbsp;&nbsp; ← &nbsp;&nbsp; fixed point.<br/>
&nbsp;&nbsp;&nbsp;&nbsp; [[[align]{.stx}](## "< left&#10;> right&#10;^ centre")][[[width]{.stx}](## "Total output width")][[**.**](## "Required")[[digits]{.stx}](## "Number of significant digits")][**e**](## "Exponential notation formatting specifier") &nbsp;&nbsp; ← &nbsp;&nbsp; exponential notation.

The last three statements utilised *f-strings*, which is only available from Python 3.6 and later. It the version you probably should be using, since it is the most concise, flexible and less error-prone than the other more older formatting options.

The **10** in the formatting specifications above means that the total output width should be 10 characters wide, and if the value is smaller, to pad it with spaces on the left or right. The very last line also show how to *centre* output within a given output width.

[p-fn-float]:
   https://docs.python.org/3/library/functions.html#float
   "Python Built-in Functions — float()"
[w-double]:
   https://en.wikipedia.org/wiki/Double-precision_floating-point_format
   "Wikipedia — IEEE-754 Double-Precision Floating-Point Format"
[p-float.hex]:
   https://docs.python.org/3/library/stdtypes.html#float.hex
   "Python Library — Standard Types # float.hex() method"
[p-float.fromhex]:
   https://docs.python.org/3/library/stdtypes.html#float.fromhex
   "Python Library — Standard Types # float.fromhex() method"
[p-fn-round]:
   https://docs.python.org/3/library/functions.html#round
   "Python Built-In Functions — round()"
[p-lib-math]:
   https://docs.python.org/3/library/math.html
   "Python Library — math Module"
[p-lib-math-floor]:
   https://docs.python.org/3/library/math.html#math.floor
   "Python Library — math # floor()"
[p-lib-math-ceil]:
   https://docs.python.org/3/library/math.html#math.ceil
   "Python Library — math # ceil()"
[p-lib-math-trunc]:
   https://docs.python.org/3/library/math.html#math.trunc
   "Python Library — math # trunc()"
[p-strfmt-stx]:
   https://docs.python.org/3/library/string.html#format-string-syntax
   "Python Library — Format String Syntax"

# String Literals

A sequence of characters stored in memory for the purpose of being a collective *unit*, is called a [string][idgh-wiki-types-str], having type [**str**][p-fn-str]. It would be strange for a programming language not to support string literals. Python has *several* ways to represent them.

[idgh-wiki-types-str]:
   Simple-Types.md#string-type
   "GitHub — Incus Data / Python First / Types # String Type"

## Delimiters

String literals can use either ‘straight’ single quotes (**'**), or ‘straight’ double quotes (**"**) as *delimiters* for sequences of characters. They have no difference in meaning, so which is used, is often a matter of preference. The quotes are not stored. A string can be empty: **''**, or **""**.

#### **py** — *String literal forms*
```py
>> print("ABCDEF")             #→ ABCDEF
>> print('ABCDEF')             #→ ABCDEF
>> print(type("ABCDEF"))       #→ str
>> print(type('ABCDEF'))       #→ str
>> name = ''                   #← empty string.
>> name = ""                   #← empty string.
```

Strings delimited by these quotes cannot span lines — they must start and stop on the same line. You can use explicit statement [continuation][idgh-wiki-inter-cont] (backslash as last character on a line) inside a string literal.

#### **py** — *Invalid string literals*
```py
>> print('                     #← ERROR
··    ABC')
>> print('\
·· ABC\
·· DEF')                       #→ ABCDEF
```

The trailing backslash and newline following it, is effectively deleted, so Python treats the last statement as:

#### **py** — *Result of continuation*
```py
>> print('ABCDEF')
```

If we had leading spaces (indentation) before the `ABC` or `DEF`, that would become part of the string.

#### **py** — *Effect of leading spaces*
```py
>> print('\
··    ABC\
··    DEF')                       #→    ABC   DEF
```

Not a very useful feature, so this will not be seen or used often, if at all.

[idgh-wiki-inter-cont]:
   Interactive-Python.md#statement-continuation
   "GitHub — Incus Data / Python First / Interactive Python # Statement Continuation"

## Long Strings

Python also allows for [long strings][p-lex-lit-longstr], which are sequence of characters delimited by three (triple) single quotes, or three double quotes. **'''**…**'''**, or **"""**…**"""**. They are sometimes also called *triple-quoted strings*.

Long strings may contain embedded newlines (can span lines), but don't *have* to. Leading spaces (indentation) is significant.

#### **py** — *Long/Tripple-quoted string literals*
```py
>> print("""ABCDEF""")           #→ ABCDEF
>> print('''ABCDEF''')           #→ ABCDEF
>> print('''ABC
··    DEF''')
#→ ABC
#→    DEF
>> print('''
·· ABC
·· DEF''')
#→
#→ ABC
#→ DEF
>> print('''\
·· ABC
·· DEF''')
#→ ABC
#→ DEF
```

The most common use for triple-quoted/long strings are as [docstrings][pep257] or *documentation strings*, as the first non-comment [expression statement][p-st-expr] in a file (module), and as the very first statement inside classes and functions. These docstrings can be extracted with the standard [**pydoc** module][p-lib-pydoc]. It is also used by the built-in [**help**][p-fn-help] function, and popup help in editors like VSCode.

#### **py** — *Docstrings in functions*
```py
>> def myfunc1 ():
··     "Documentation for myfunc1"
··     return
>> def myfunc2 ():
··     """Documentation for myfunc2"""
··     return
>> def myfunc3 ():
··     """
··     Documentation for myfunc3
··     """
··     return
>> help(myfunc1)
```

The output of the last statement will be something like this:

```
Help on function myfunc1 in module __main__

myfunc1()
    Documentation for myfunc1
```

In our examples, only as a matter of consistency, we only use triple-quoted strings for docstrings; and in the form used with `myfunc3`.

[p-st-expr]:
   https://docs.python.org/3/reference/simple_stmts.html#expression-statements
   "Python Simple Statements — 7.1 Expression Statements"
[w-string]:
   https://en.wikipedia.org/wiki/String_(computer_science)
   "Wikipedia — String (computer science)"
[p-lex-lit-longstr]:
   https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-longstring
   "Python Reference — Lexical Analysis # longstring"
[pep257]:
   https://peps.python.org/pep-0257/
   "PEP 257 — Docstring Conventions"
[p-lib-pydoc]:
   https://docs.python.org/3/library/pydoc.html
   "Python Library — pydoc"
[p-fn-help]:
   https://docs.python.org/3/library/functions.html#help
   "Python Reference — Built-In Functions # help()"

## Implicit Concatenation

String literals use any delimiters, can be *implicitly concatenated* if they are separated by only whitespace characters (tabs, newlines, spaces).

#### **py** — *Implicit string literal concatenation*
```py
>> print("ABC"  'DEF')   #→ ABCDEF    ← concatenated.
>> print("ABC", 'DEF')   #→ ABC DEF   ← not concatenated.
>> print(
··    "ABC"
··    "DEF")             #→ ABCDEF    ← concatenated.
```

This rule applies to all string literals, even triple-quoted string literals.

#### **py** — *More implicit string literal concatenation*
```py
>> print("""ABC"""
··    '''DEF'''  "GHI")  #→ ABCDEFGHI
```

This implicit concatenation takes place during the initial phases of parsing statements. Following this phase, *meaning* is applied to the result, and will ‘see’ only one string literal.

## Escape Sequences

Sometimes you may want to represent special characters inside a string that has no representation on you keyboard, or that your editor interprets (like [TAB]{.stx} or [CR]{.stx}).

### Escape Character

Inside string literals, the backslash character (**\\**) has special meaning. One consequence of this, is that you must write two backlashes to get *one* backslash stored. Following the backslash, can be one of several predefined characters, or an [ASCII code][w-ascii] code (compatible with corresponding Unicode codes).

#### Table: Escape Sequences
| esc        | description                                      |
|:-----------|:-------------------------------------------------|
| **\\**[NL]{.stx} | Line continuation |
| **\\\\**   | Single backslash |
| **\\'**    | Useful inside '…' |
| **\\"**    | Useful inside "…" |
| **\a**     | [BEL]{.stx} bell character (code 7)
| **\b**     | [BS]{.stx} backspace character (code 8)
| **\f**     | [FF]{.stx} form feed character (code 12)
| **\n**     | [NL]{.stx}/[LF]{.stx} (newline/linefeed) character (code 10) |
| **\r**     | [CR]{.stx} carriage return character (code 13) |
| **\t**     | [TAB]{.stx}/[HT]{.stx} horizontal tab character (code 9) |
| **\v**     | [VT]{.stx} vertical tab character (code 11) |
| <strong>\\</strong>ooo  | ooo ← octal character code |
| **\x**hh   | hh ← hexadecimal character code |
| **\u**hhhh | hhhh ← hexadecimal 2-byte Unicode code |
| **\U**hhhhhhhh | hhhhhhhh hexadecimal 4-byte Unicode code |
| **\N\{**[name]{.stx}**}** | Unicode character [name]{.stx} |

The escape sequences using character codes, must have leading zeros so that the value is either 2 digits (**\x**), 4 digits (**\u**) or 8 digits (**\U**).

#### **py** — *Character code escapes*
```py
>> print("\101 \x41 \u0041 \U00000041")  #→ A A A A
```

### Unicode Escapes

Other times, you may want to place [Unicode][w-unicode] characters in a string. If your Python file encoding is [UTF-8][w-utf8], you can just paste Unicode characters from a Web page, for example. Or you can use the Unicode [name]{.stx}: **\N\{**[name]{.stx}**}**.

An alternative to **\N\{**…**}**, is ‘**\u**hhhh’, where hhhh is a 4 digit hexadecimal value if the Unicode code is between 0000 and FFFF. For longer codes, you can use ‘**\U**hhhhhhhh’, which is long enough for any Unicode code.

#### **py** — *Unicode characters*
```py
>> print("🐈 \N{CAT} \U0001F408")     #→ 🐈 🐈 🐈
>> print("🐍 \N{SNAKE} \U0001F40D")   #→ 🐍 🐍 🐍
```

Whether a Unicode character will *display*, depends on your terminal or other output device, and fonts. Sometimes font rendering systems will substitute characters for you, if the main font does not contain them. Browsers do that often.

[w-unicode]:
   https://en.wikipedia.org/wiki/Unicode
   "Wikipedia — Unicode"
[w-utf8]:
   https://en.wikipedia.org/wiki/UTF-8
   "Wikipedia — UTF-8"
[w-ascii]:
   https://en.wikipedia.org/wiki/ASCII
   "Wikipedia — ASCII (American Standard Code for Information Interchange)"

## Raw Strings

Sometimes it is inconvenient to deal with backslashes in strings. A good example is Windows path names:

#### **py** — *Need for raw strings*
```py
>> print( "C:\\Users\\me\\Documents\\filename.txt" )
```

Python allows a **r**/**R** prefix to string literals, which we then call *raw* string literals. The effect of the **r**/**R**, is that the backslash escape character will not be interpreted:

#### **py** — *Raw string solution*
```py
>> print( r"C:\Users\me\Documents\filename.txt" )
```

Another situation where raw string literals are useful, is in the representation of [regular expressions][w-regex], by way of Python's standard [**re** module][p-lib-re]. Regular expression syntax also use backslash as an escape character, but is first interpreted by the Python parses. So, to pass two backslashes (**\\\\**) to the regular expression code, you must type *four* (**\\\\\\\\**)… unless you use a raw string literal.

#### **py** — *Raw strings for regular expressions*
```py
>> import re
>> pattern1 =  "\\d+\\s*\\w+"        #← without raw string.
>> pattern2 = r"\d+\s*\w+"           #← with raw string.
>> text = "Box of 12 apples."
>> print(re.findall(pattern1,text))  #→ ['12 apples']
>> print(re.findall(pattern2,text))  #→ ['12 apples']
```

There is one problem though… the last character in a raw string cannot be a backslash. That will cause a syntax error. We can use [implicit concatenation](#implicit-concatenation) in that case:

#### **py** — *Backslash as last character solution*
```py
>> print( r"ABC\" )                  #← ERROR
>> print( r"ABC" "\\" )              #→ ABC\
```

The raw string literals prefix can also be applied to [long strings](#long-strings).

[w-regex]:
   https://en.wikipedia.org/wiki/Regular_expression
   "Wikipedia — Regular Expression"
[p-lib-re]:
   https://docs.python.org/3/library/re.html
   "Python Library — re (Regular Expression) Module"

## Formatted Literals

Starting with Python 3.6, string literals may have an **f**/**F** prefix, in which case they are called *formatted string literals*, or just *f-strings*. The [formatting syntax][p-strfmt-stx] is the same ‘[mini language][p-strfmt-lang]’ employed by [**str.format()**][p-tp-str-fmt].

Placeholders in a formatted string literal consists of paired curly braces (**{**…**}**). Any [expr]{.stx}ession may appear inside the curly braces, as long as the expression does not contain the same string delimiters, or any backslash.

#### **py** — *Basic formatted string literals*
```py
>> print( f"--{"ABC"}--" )          #← ERROR
>> print( f"--{"ABC\n"}--" )        #← ERROR
>> print( f"--{'ABC'}--" )          #→ --ABC--
>> print( f'--{"ABC"}--' )          #→ --ABC--
>> text = "ABC"
>> print( f"--{text}--" )           #→ --ABC--
```

To prevent curly braces from being treated as placeholders in an f-string, they must appear twice. They do not have to be paired. The backslash escape character will not work: **\\{** or **\\}**.

#### **py** — *Curly braces in formatted string literals*
```py
>> print( f"{{2 * 3}}={2 * 3}" )    #→ {2 * 3}=6
>> print( f"{{2 * 3 ={2 * 3}" )     #→ {2 * 3 =6
>> print( f"2 * 3}} ={2 * 3}" )     #→ 2 * 3} =6
```

Note that the expression **2 \* 3** was calculated and the *result* placed in the f-string, minus the placeholder curly braces. The expansion of an [expr]{.stx}ession inside a string literal is often called [string interpolation][w-str-inter].

The basic syntax only requires an [expr]{.stx}ession between the curly braces. Spaces around the [expr]{.stx} part is ignored. A second variant allows a [format]{.stx} *specification* following a colon (**:**).

&nbsp;&nbsp;&nbsp;&nbsp; **{**[[expr]{.stx}](##)**}**<br/>
&nbsp;&nbsp;&nbsp;&nbsp; **{**[[expr]{.stx}](##)**:**[[format]{.stx}](#fmt-fmt)**}**

 * [[expr]{.stx}](##) &nbsp; — &nbsp; any expression not containing backslashes.
 * [[format]{.stx}](#fmt-fmt) &nbsp; — &nbsp; formatting specification.

What kind of formatting specifications are available, depends on the [type]{.stx} of the [expr]{.stx}ession. The *result* of the [expr]{.stx}ession, is what gets formatted. The [format]{.stx} can have an [align]{.stx}ment prefix, but is only useful if the [format]{.stx} includes an output [width]{.stx}.

&nbsp;&nbsp;&nbsp;&nbsp; <a id="fmt-fmt"></a>[[format]{.stx}](##) &nbsp; ⇒ &nbsp; [[[fill]{.stx}](#fmt-fill)][[[align]{.stx}](#fmt-aln)][[[sign]{.stx}](#fmt-sign)][[**#**](#fmt-hash)][[**0**](#fmt-zero)][[[width]{.stx}](#fmt-width)][[**,**](#fmt-comma)][[**_**](#fmt-uscore)][**.**[[prec]{.stx}](#fmt-prec)][[[type-spec]{.stx}](#fmt-spec)]

* <a id="fmt-fill"></a>[[fill]{.stx}](##) &nbsp; — &nbsp; An optional character that specifies the padding character to fill the available space. If omitted, the padding character defaults to space. Only useful if [width]{.stx} is present.

* <a id="fmt-aln"></a>[[align]{.stx}](##) &nbsp; — &nbsp; An optional alignment option: [**\<**](##) (left-align), [**\>**](##) (right-align), [**^**](##) (center), or [**=**](##) (padding after the sign for numbers).

* <a id="fmt-sign"></a>[[sign]{.stx}](##) &nbsp; — &nbsp; An optional sign option: [**+**](##) (sign for both positive and negative numbers); [**-**](##) (sign only for negative numbers); or [SP]{.stx} (space for positive numbers, sign for negative numbers).

* <a id="fmt-hash"></a>[__#__](##) &nbsp; — &nbsp; An optional flag that indicates the inclusion of an alternate form for certain types: **0b** prefix for binary, **0o** prefix for octal, and **0x** prefix for hexadecimal.

* <a id="fmt-zero"></a>[**0**](##) &nbsp; — &nbsp; An optional flag that indicates zero-padding; it's equivalent to using fill character [**0**](##) with align option [**=**](##).

* <a id="fmt-width"></a>[[width]{.stx}](##) &nbsp; — &nbsp; An optional integer specifying the minimum width of the formatted value.

* <a id="fmt-comma"></a>[**,**](##) &nbsp; — &nbsp; An optional flag that indicates the use of a comma as a thousands separator for numbers.

* <a id="fmt-uscore"></a>[**_**](##) &nbsp; — &nbsp; An optional flag that indicates the use of an underscore as a thousands separator for numbers.

* <a id="fmt-prec"></a>**.**[[prec]{.stx}](##) &nbsp; — &nbsp; An optional precision specifier consisting of a period ([**.**](##)) followed by an integer, specifying the number of digits after the decimal point for floating-point numbers; or the maximum length of the output for strings.

* <a id="fmt-spec"></a>[[type-spec]{.stx}](##) &nbsp; — &nbsp; An optional type specifier for formatting the value: [**b**](##) for binary; [**d**](##) for decimal; [**f**](##) for fixed-point notation; [**e**](##) for exponential/scientific notation.

Reminder: The available formatting options depend on the [type]{.stx} of [expr]{.stx}ession being formatted.

The [type-spec]{.stx} part may be omitted, in which case the formatting will use the default specifier, depending on the actual [type]{.stx} of the [expr]{.stx}ession. Good convention suggests that you never omit the [type-spec]{.stx}ifier.

#### **py** — *More formatting string literals*
```py
## Only ‹expr›ession part.
>> print(f"|{'Python'}|")        #→ Python
>> print(f"|{42}|")              #→ 42

## With alignment and width, without type-spec.
>> print(f"|{'Python':<10}|")    #→ |Python    |
>> print(f"|{42:>10}|")          #→ |        42|

## With precision for a float, without type-spec.
>> print(f"|{3.14159265:.3}|")   #→ |3.14|

## With type
>> print(f"|{42:b}|")            #→ |101010|
>> print(f"|{42:#b}|")           #→ |0b101010|
>> print(f"|{3.14159265:.3e}|")  #→ |3.142e+00|
```

The f-string string literals prefix can also be applied to [long strings](#long-strings).

One can combined f-strings with [raw strings](#raw-strings), using any of the literal string prefixes **fr** or **rf**, in any combination of upper case or lower case.

[p-strfmt-lang]:
   https://docs.python.org/3/library/string.html#format-specification-mini-language
   "Python Library — Strings # Format Specification Mini-Language"
[p-tp-str-fmt]:
   https://docs.python.org/3/library/stdtypes.html#str.format
   "Python Types — ‹str›.format()"
[w-str-inter]:
   https://en.wikipedia.org/wiki/String_interpolation
   "Wikipedia — String Interpolation"

# Characters

Python does not have a type that represents a single character. A string containing one character, *is* a character. Some functions expects ‘a character’, which means they will only accept strings containing a single character.

You can get the *ordinal value* (Unicode code point) of a string containing one character, with the built-in [**ord**][p-fn-ord] function. It will not accept strings containing more than one character.

#### **py** — *Ordinal values of some characters*
```py
print(ord("0"))                   #→ 48
print(ord("A"))                   #→ 65
print(ord("a"))                   #→ 97
print(ord("\N{SNAKE}"))           #→ 128013
print(hex(ord("\N{SNAKE}")))      #→ 0x1f40d
```

Given an ordinal value (Unicode code point), we can get a string containing one character from the built-in [**chr**][p-fn-chr] function.

#### **py** — *Characters from ordinal values*
```py
print(chr(48))                    #→ 0
print(chr(65))                    #→ A 
print(chr(97))                    #→ a
print(chr(128013))                #→ 🐍
print(chr(0x1f40d))               #→ 🐍
```

[p-fn-ord]:
   https://docs.python.org/3/library/functions.html#ord
   "Python Reference — Built-In Functions # ord()"
[p-fn-chr]:
   https://docs.python.org/3/library/functions.html#chr
   "Python Reference — Built-In Functions # chr()"


