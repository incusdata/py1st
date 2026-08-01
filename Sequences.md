[Data structures][p-tp-seqs] that other languages call *collections* or *containers*, Python calls *sequences*, and provides several built-in sequences like [**list**][p-fn-list], which is a [mutable][p-tp-seqs-mutable] sequence; [**tuple**][p-fn-tuple], which is an [immutable][w-immutable] sequence; [**dict**][p-fn-dict], which is a key-value pair mapping; [**str**][p-fn-str], which is a sequence of characters; and [**set**][p-fn-set]s of unique keys.

All sequences are [iterable][w-iterator], i.e., they support the [**iter**][p-fn-iter] and [**next**][p-fn-next] build-in functions. This means their items can be accessed one-by-one. Many standard sequences support some [common][p-tp-seqs-common] operations, while [mutable][p-tp-seqs-mutable] supports more, and can perform operations directly on the items (in-place).

[p-tp-seqs]:
   https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
   "Python Reference — Sequence Types — list, tuple, range"
[p-fn-list]:
   https://docs.python.org/3/library/functions.html#func-list
   "Python Reference — Built-In Functions # list()"
[p-fn-tuple]:
   https://docs.python.org/3/library/functions.html#func-tuple
   "Python Reference — Built-In Functions # tuple()"
[p-fn-dict]:
   https://docs.python.org/3/library/functions.html#func-dict
   "Python Reference — Built-In Functions # dict()"
[p-fn-str]:
   https://docs.python.org/3/library/functions.html#func-str
   "Python Reference — Built-In Functions # str()"
[w-immutable]:
   https://en.wikipedia.org/wiki/Immutable_object
   "Wikipedia — Immutable Object"
[p-tp-seqs-common]:
   https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
   "Python Reference — Standard Types # Common Sequence Operations"
[p-tp-seqs-mutable]:
   https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types
   "Python Reference — Standard Types # Mutable Sequence Types"
[p-fn-set]:
   https://docs.python.org/3/library/functions.html#func-set
   "Python Reference — Built-In Functions # set()"
[w-iterator]:
   https://en.wikipedia.org/wiki/Iterator
   "Wikipedia — Iterator"
[p-fn-iter]:
   https://docs.python.org/3/library/functions.html#iter
   "Python Reference — Built-In Functions # iter()"
[p-fn-next]:
   https://docs.python.org/3/library/functions.html#next
   "Python Reference — Built-In Functions # next()"

# List

The [**list**][p-fn-list] [type]{.stx} represents a flexible and mutable sequence. An object of [type]{.stx} [**list**][p-fn-list] can be created in several ways, and each item is a reference to any object, including other [**list**][p-fn-list]s.

## List Creation

Objects of [type]{.stx} [**list**][p-fn-list] can be created by function call, or by using list literals.

### List Type Function

Like all type functions, [**list**][p-fn-list] can create a list object from any *iterable* [expr]{.stx}ession ([iter-expr]{.stx}). When passed no arguments, it returns an *empty* sequence.

&nbsp;&nbsp;&nbsp;&nbsp; [**list**][p-fn-list]**(** [ [iter-expr]{.stx} ] **)**

#### **py** — *Create lists with the list function*
```py
L1 = list()                    #← empty list.
L2 = list("ABC")               #← L2 = ['A', 'B', 'C']
L3 = list(range(5))            #← L3 = [0, 1, 2, 3, 4]
print(type(L1))                #→ class list
```

### List Literals

We can also create a [**list**][p-fn-list] object using a *list literal*, which is a set of square brackets delimiting zero or more items ([expr]{.stx}essions), separated by a comma (**,**). A trailing comma is allowed. The [type]{.stx}s of the items do not have to be the same, since each item is a *reference* to an object.

#### **py** — *Create lists with list literals*
```py
L1 = []                        #← empty list.
L2 = ["A", "B", "C"]
L3 = [11, 22.33, "STRING"]     #← `int`, `float` and `str`.
print(L1, L2, L3)
```
```
[] ['A', 'B', 'C'] [11, 22.33, 'STRING']
```

As with all [type]{.stx}s, [**list**][p-fn-list] objects are convertible to [**str**][p-fn-str]ing, implicitly, or explicitly. When converted to a string, the representation will surround the items with square brackets, with the items separated by commas.

List items can reference any [type]{.stx} of object, even other [**list**][p-fn-list]s.

#### **py** — *Lists of lists*
```py
L1 = [11, 22]
L2 = [33, 44, 55]
L3 = [L1, L2, [66, 77], "ABC", ] 
print(f"L3={L3}")
```
```
L3=[[11, 22], [33, 44, 55], [66, 77], 'ABC']
```

As can be seen with **L3**, a trailing comma is a allowed as a matter of convenience. This is especially useful when the [**list**][p-fn-list] literal spans several lines.

#### **py** — *List literals spanning lines*
```py
L1 = [
   "First item",
   "Second item",
   "Third item",
   ]
```

Leading spaces are not relevant, and the trailing comma makes it easy to add more items. The indentation level of the closing square bracket delimiter, is also not significant. The following example is entirely legal, but not recommended:

#### **py** — *Legal but ‘ugly’ indentation*
```py
if True:
   L1 = [
   "First item",
"Second item",
                  "Third item",
]
   print(L1)
```

Syntax-wise, it is only important for **L1** and [**print**][p-fn-print] to be consistently indented. But, the code above is difficult for humans to read and understand.

### Empty Lists

An empty [**list**][p-fn-list] when converted to [**bool**][p-fn-bool]ean, will return [**False**][p-lit-false]. Any other value, will produce [**True**][p-lit-true]. This is useful with the [**if**][p-st-if] statement, where ‘**if** [list-expr]{.stx}**:**’ becomes an abstraction for ‘if the [list-expr]{.stx} is non-empty…’.

#### **py** — *Empty list abstraction*
```py
print(bool([]))             #→ False
print(bool(list()))         #→ False

L1 = []
if L1:
   print("List is not empty")
else
   print("List is empty")

print(bool(L1))             #→ False
```

This is more *idiomatic* than: ‘**[if][p-st-if]** [**len**][p-fn-len]**(**[list-obj]{.stx}**)** **==** **0:**’.

[p-fn-bool]:
   https://docs.python.org/3/library/functions.html#bool
   "Python Reference — Built-In Functions # bool()"
[p-lit-false]:
   https://docs.python.org/3/library/constants.html#False 
   "Python Literals — False (bool)"
[p-lit-true]:
   https://docs.python.org/3/library/constants.html#True 
   "Python Literals — True (bool)"
[p-st-if]:
   https://docs.python.org/3/reference/compound_stmts.html#the-if-statement
   "Python Reference — Compound Statements # 8.1 If Statement"
[p-fn-print]:
   https://docs.python.org/3/library/functions.html#print
   "Python Reference — Built-In Functions # print()"

# Tuple

The [**tuple**][p-fn-tuple] built-in function creates immutable sequences — once created, they cannot be modified. Operations on [**tuple**][p-fn-tuple]s, create *copies*. Objects of type [**tuple**][p-fn-tuple] can also be created with literals.

## Tuple Creation

We can create objects of type [**tuple**][p-fn-tuple] using the function, or using a tuple literal.

### Tuple Function

Calling the [**tuple**][p-fn-tuple] function without arguments, will create an *emtpy* [**tuple**][p-fn-tuple] ([**len**][p-fn-len] is **0**). Alternatively, it will accept any *iterable* expression as argument. For a literal with one item, a trailing comma is required.

#### **py** — *Create tuple with tuple function*
```py
T1 = tuple()                     #← empty tuple.
T2 = tuple("ABC")                #← T2=('A','B','C')
T3 = tuple(range(6))             #← T3=(0,1,2,3,4,5)
```

When a [**tuple**][p-fn-tuple] is converted to a string, the items are separated with a comma, and they will all be surrounded by parentheses.

### Tuple Literals

A literal [**tuple**][p-fn-tuple] *can* be surrounded by parentheses, but because parentheses are also used for arithmetic grouping, and function calls, Python uses other heuristics to determine if a literal is a [**tuple**][p-fn-tuple]. Here, the comma separating items, becomes important.

#### **py** — *Create tuples with tuple literals*
```py
T1 = ()                          #← empty tuple literal.
T2 = (11, 22, 33)                #← parentheses optional.
T3 =  11, 22, 33                 #← equivalent to above.
T4 = (11, 22, 33,)               #← trailing comma OK.
T4 =  11, 22, 33,                #← trailing comma also OK.
T5 = (11)                        #← NOT A TUPLE.
T6 = (11,)                       #← tuple with one item.
T7 =  11,                        #← tuple with one item.
T8 = (11,                        #← parentheses required.
      22,                        #
      33,)                       #
```

In the last statement the parentheses are required; the trailing comma is still optional. Passing a [**tuple**][p-fn-tuple] literal as an argument also requires the parentheses:

#### **py** — *Pass tuple literal as argument*
```py
def func (param): print(f"param={param})

func(11, 22, 33)                 #← ERROR
func((11, 22, 33))               #→ param=(11, 22, 33)
```

As with [Lists](#list), the items in a [**tuple**][p-fn-tuple], can be any [type]{.stx}, including other [**tuple**][p-fn-tuple]s, [**list**][p-fn-list]s, other sequences (whose items can reference other sequences, …, and so on).

#### **py** — *Complex tuple literals*
```py
T1 = 11, 22
T2 = 55,
T3 = (T1, [33, 44], (T2, 66)) 
print("T3 =", T3)
```
```
T3 = ((11, 22), [33, 44], ((55,), 66))
```

A [**tuple**][p-fn-tuple] supports all the [common][p-tp-seqs-common] sequence operations, but not the [mutable][p-tp-seqs-mutable] operations. New [**tuple**][p-fn-tuple]s can be created with the overloaded **+** (concatenation) and **\*** (repetition) operators, both can be used in augmented assignments: **+=** and **\*=**.

# Sequence Operations

As [**list**][p-fn-list], [**tuple**][p-fn-tuple] supports similar operations, we focus on these operations applied to the sequences in general.

### Sequence Length

The built-in [**len**][p-fn-len] indirectly calls a special **\_\_len\_\_** method, which is implemented in [**list**][p-fn-list] and other sequence objects to return the *number of items* in the sequence. An empty sequence will have a [**len**][p-fn-len]gth of **0**.

#### **py** — *Number of items in sequences*
```py
L1 = [ 11, [ 22, 33, ], 44, [ 55, 66, ], ]
print("L1 #items =", len(L1))             #→ L1 #items = 4
print(len([11, 22, 33, 44, 55, 66]))      #→ 6
print(len([]))                            #→ 0
L2 = []
print(len(L2))                            #→ 0
T1 = ( 11, [ 22, 33, ], 44, [ 55, 66, ], )
print("T1 #items =", len(T1))             #→ T1 #items = 4
T2 = tuple()                              #← empty tuple. 
print(len(T2))                            #→ 0
```

Note that **L1** and **T1** both contain only **4** items, not **6**. Two of the four items are [**list**][p-fn-list]s. Each item is just a reference to some [type]{.stx} of object.

[p-fn-len]:
   https://docs.python.org/3/library/functions.html#len
   "Python Reference — Built-In Functions # len()"

### Sequence Subscript

Individual items in any sequence can be accessed with the postfix subscript operator applied to a [seq-obj]{.stx}ect: [seq-obj]{.stx}**\[** [expr]{.stx} **\]**. The [expr]{.stx}ession between the square brackets, is the *index* of the item to access; which ranges from **0** (first item) to ‘[**len**][p-fn-len]**(**[seq-obj]{.stx}**)** **-** **1**’ (last item). An out of range [index]{.stx} will result in raising a **IndexError** exception.

#### **py** — *Sequence subscript index range*
```py
L = [11, 22, 33, 44]
print(L[0], L[1], L[2], L[3], L[len(L)-1]) #→ 11 22 33 44 44 
T = (11, 22, 33, 44)
print(T[0], T[1], T[2], T[3], T[len(L)-1]) #→ 11 22 33 44 44 
```

Note that **L[3]** and **T[3]** results in **44**, which is the last item. The same result can be obtained with: **L[**\[**len**][p-fn-len]**(L1)-1]**, for example. The number of items in **L** and **T**, is **4**.

Negative indexes on a sequence: ‘**\[** **-**[index]{.stx} **\]**’, are allowed as a convenient shorthand for: ‘**\[** [**len**][p-fn-len]**(**[list-obj]{.stx}) **-** [index]{.stx} **\]**’.

#### **py** — *Negative sequence subscript indexes*
```py
S = [11, 22, 33, 44]                #→ or: `S = ( ··· )`
print(S[ 0], S[ 1], S[ 2], S[ 3])   #→ 11 22 33 44
print(S[-4], S[-3], S[-2], S[-1])   #→ 11 22 33 44 
print(S[-1], S[-2], S[-3], S[-4])   #→ 44 33 22 11
print(S[len(S)-1], end=" ")         #→ 44
print(S[len(S)-2], end=" ")         #→ 33
print(S[len(S)-3], end=" ")         #→ 22
print(S[len(S)-4])                  #→ 11
```

It should be apparent that any item in a sequence can be referenced using either a positive, or a negative, [index]{.stx}.

The subscript operator is convenient shorthand for calling the special **\_\_setitem\_\_** and **\_\_getitem\_\_** methods present in all sequences.

### List Modification

Since [**list**][p-fn-list]s are mutable, we can modify the values in such an object. We can overwrite existing references, add new items, or even [**del**][p-st-del]ete items. This is not possible for [**tuple**][p-fn-tuple]s.

#### **py** — *Modifying lists items*
```py
L = [ 11, 22, 33, 44, 55 ]
print(L)                            #→ [11, 22, 33, 44, 55]
L[2] = 99                           #← assignment statement.
print(L)                            #→ [11, 22, 99, 44, 55]
del L[2]                            #← delete statement.
print(L)                            #→ [11, 22, 44, 55]
```

Note that [**del**][p-st-del] is a *statement*, not a built-in function.

In order to add more items to a list, we can use ‘[list-obj]{.stx}**.append(**[item]{.stx}**)**’ to append a single item; or ‘[list-obj]{.stx}**.extend(**[iterable]{.stx}**)**’ to append multiple items. Both add items at the *end* of the [**list**][p-fn-list]. Think of **append** as ‘pushing’ items onto the list; the corresponding ‘[list-obj]{.stx}**.pop()**’, will *remove* the last item.

#### **py** — *Appending and removing list items*
```py
L1 = [ 1, 2, 3, 4, 5, 6, 7 ]        #← L1=[1,2,3,4,5,6,7]
L1.pop() ; L1.pop() ; L1.pop()      #← L1=[1,2,3,4]
L1.append(5)                        #← L1=[1,2,3,4,5]
L1.extend(L2)                       #← L1=[1,2,3,4,5,6,7]
```

## Sequence Concatenation

The plus operator (**+**) applies to all sequences. It will concatenate two sequences of the same [type]{.stx}, resulting in a new sequence. It also works with augmented assignment (**+=**).

#### **py** — *Sequence concatenation*
```py
S1 = [ 11, 22 ]
S1 = S1 + S1 + S1
print(S1)                           #→ [11,22, 11,22, 11, 22]
S1 = [ 11, 22 ]
S1 += [ 33, 44, 55 ]
print(S1)                           #→ [11,22,33,44,55]
S1 = ( 11, 22 )
S1 += S1 + S1
print(S1)                           #→ (11,22, 11,22, 11,22)
```

## Sequence Repetition

Any sequence can be repeated [count]{.stx} times using the asterisk (**\***) operator, where [count]{.stx} is an [**int**][p-fn-int]eger expression that can appear on the left or right of the asterisk. The other operand must be a sequence.

#### **py** — *Sequence repetition*
```py
L = [11, 22]
print(L * 3)                     #→ [11,22, 11,22, 11,22]
print(3 * L)                     #→ [11,22, 11,22, 11,22]
N = 3 ; L *= N
print(L)                         #→ [11,22, 11,22, 11,22]
print((11, 22) * N)              #→ (11,22, 11,22, 11,22)
print(N * (11, 22))              #→ (11,22, 11,22, 11,22)
print("ABC" * N)                 #→ ABCABCABC
print(N * "ABC")                 #→ ABCABCABC
```

## Other Operations

The [list-obj]{.stx}**.clear** method will empty the [**list**][p-fn-list], and the [list-obj]{.stx}**.copy** method will make a shallow copy. The [list-obj]{.stx}**.insert** method can insert an new item at a given [index]{.stx}.

The [list-obj]{.stx}**.index**, [list-obj]{.stx}**.count** and [list-obj]{.stx}**.remove**, all accept item *values*; where **index** will return the first [index]{.stx} where a *value* is found; **count** will count the number of items equal to a *value*; and **remove** will delete the first item with that *value*.

The [list-obj]{.stx}**.sort** method will perform an in-place ordering of the items based on their values. The [list-obj]{.stx}**.reverse** method will reverse all the items in-place. The [**sorted**][p-fn-sorted] and [**reverse**][p-fn-reversed] built-ins will make *copies* of a [**list**][p-fn-list] object, unlike the corresponding methods.

Other built-in functions also accept iterables, like [**sum**][p-fn-sum], [**min**][p-fn-min] and [**max**][p-fn-max]. The **sum** method will only work in numeric types, while the other two will only work with object types that implement special **\_\_min\_\_** and **\_\_max\_\_** methods.

The overloaded asterisk (**\***) will *repeat* a list [count]{.stx} number of times, where [count]{.stx} must be an [**int**][p-fn-int]eger [expr]{.stx}ession. The [count]{.stx} can be on the left hand side, or right hand side, of the asterisk: ‘[list-obj]{.stx} **\*** [count]{.stx}’ ‖ ‘[count]{.stx} **\*** [list-obj]{.stx}’.

[p-st-del]:
   https://docs.python.org/3/reference/simple_stmts.html#the-del-statement
   "Python Reference — Simple Statements # 7.5 The del Statement"
[p-fn-sum]:
   https://docs.python.org/3/library/functions.html#sum
   "Python Reference — Built-In Functions # sum()"
[p-fn-min]:
   https://docs.python.org/3/library/functions.html#min
   "Python Reference — Built-In Functions # min()"
[p-fn-max]:
   https://docs.python.org/3/library/functions.html#max
   "Python Reference — Built-In Functions # max()"
[p-fn-sorted]:
   https://docs.python.org/3/library/functions.html#sorted
   "Python Reference — Built-In Functions # sorted()"
[p-fn-reversed]:
   https://docs.python.org/3/library/functions.html#reversed
   "Python Reference — Built-In Functions # reversed()"
[p-fn-int]:
   https://docs.python.org/3/library/functions.html#int
   "Python Reference — Built-In Functions # int()"
