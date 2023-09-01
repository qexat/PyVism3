# Basic data types

[← Language Tour](./index.md)

This document will present to you the data types that enjoy literal
representations, i.e. they are built in the language.

## Integers

The Integer type represents "full", round numbers (e.g. in counting).

```py
3
-69
```

**Note:** `-69` is syntax sugar for `0 69 -`.

See also: [Technical details :: Integer](../tech_details/basic_dt.md#integer)

## Reals

The Real type represents decimal numbers (e.g. length, duration, temperature...). It is often called `float` in other programming languages.

```py
3.14
19.0
.5  # same as 0.5
-42.7
```

**Note:** `-42.7` is syntax sugar for `.0 42.7 -`.

See also: [Technical details :: Real](../tech_details/basic_dt.md#real)

## Character strings

The String type represents text. They support escape sequences.

It is written as text surrounded by double-quotes:

```py
"Hello World!"
"This string has an escape sequence: \n"
"Connor \"Pat\" O'Milley" 
```

To write a double-quote inside a string, escape it by prepending a backslash `\`:

```py
>>> "The following text will be double-quoted: \"I'm double-quoted!\"" print
The following text will be double-quoted: "I'm double-quoted!"
```

See also: [Technical details :: String](../tech_details/basic_dt.md#string)

## Byte strings

The Bytestring type represents a sequence of raw bytes. It supports escape sequences.

It is written as text surrounded by single-quotes:

```py
'Hello World!'
'\x04\x02\x00'
```

See also: [Technical details :: Bytestring](../tech_details/basic_dt.md#bytestring)

## Tuples

The Tuple type represents an ordered immutable^[A tuple cannot be changed after its creation.] collection of elements. It is also called [product type](https://en.wikipedia.org/wiki/Product_type).

It is written as a sequence of elements separated by commas and surrounded by parentheses^[Contrary to some other languages, the parentheses are mandatory!]:

```py
(1, 2, 3, 4)
("Python", "Rust", "Java")
("one", 2, ("the third", "element is", "a tuple!"))
()  # empty tuple
```

:x: A tuple CANNOT contain only one element!

See also: [Technical details :: Tuple](../tech_details/basic_dt.md#tuple)

## Lists

The List type represents an ordered mutable collection of elements. Some other languages call it `Vector`.

It is written as a sequence of elements separated by commas and surrounded by square brackets:

```py
[1, 2, 3, 4]
["Hello"]  # list of one element
[[1, 2, 3], [4, 5, 6]]  # list of nested lists
[]  # empty list
```

Contrary to [tuples](#tuples), a list can contain only one element.

:x: A list CANNOT contain elements of different types^[Be aware: a list of integers and a list of reals are NOT considered of the same type, despite being both lists.]!

See also: [Technical details :: List](../tech_details/basic_dt.md#list)

## Sets

The Set type represents an unordered mutable collection of elements. It is similar to the [set in mathematics](https://en.wikipedia.org/wiki/Set_(mathematics)).

It is written as a sequence of elements separated by commas and surrounded by braces:

```py
{1, 2, 3, 4}
{"Hello"}  # set with one element
{}  # empty set (also called null set)
```

See also: [Technical details :: Set](../tech_details/basic_dt.md#set)

## Mappings

The Mapping type represents an ordered mutable collection of key/value pairs.

It is written as a sequence of key-value pairs, separated by commas and surrounded by vertical bars ; a arrow (`=>`) splits a key and a value.

```py
|
    "name" => "Alice",
    "age" => 31,
|
```

See also: [Technical details :: Mapping](../tech_details/basic_dt.md#mapping)
