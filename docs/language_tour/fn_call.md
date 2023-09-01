# Function call

[← Language Tour](./index.md)

This document will list a handful of built-in functions, and teach how to use them.

## Built-in functions

The Vism language provides some functions. They can be immediately used in your code without importing any library.

### Operators

Operators are also functions! Here is a non-exhuastive list of them:

- `+`: addition, string concatenation
- `-`: substraction
- `*`: product
- `/`: division
- `%`: modulo

```py
>>> 3 5 +
8

>>> "Hello" "World" +
"HelloWorld"

>>> 1.0 4.0 /
0.25
```

### print

Shows the values in the terminal, separated by a space.

```py
>>> "Hello World!" print
Hello World!

>>> 19 print
19

>>> "You have", 3, "sisters?" print
You have 3 sisters?
```

### open

Opens a file given its path and one of the following modes:

- `r` (read): the file can be read but not written in
- `w` (write): the file can be read and written, replacing previous contents
- `a` (append): the file can be read and written, appending to the previous contents

```py
>>> "my_file.txt" "w" open
File (path: "my_file.txt", mode: Write)
```

### write

Writes the string in a file (or the terminal).

```py
# STDOUT is basically the terminal
>>> STDOUT "Hello World!\n" write
Hello World!

>>> @file = "my_file.txt" "w" open
>>> @file "Writing in a file!\n" write
```

### map

Applies a function to every member of a collection.

```py
>>> (2 *) [1, 2, 3, 4] map
[2, 4, 6, 8]
```

See also: [Partialization](#partialization)

### foldleft

Accumulate a collection using a function.

```py
>>> (+) [1, 2, 3, 4] foldleft
10
```

See also: [Partialization](#partialization)

### length

Returns the length of a collection or string.

```py
>>> "Hello World!" length
12

>>> [10, 9, 8, 7] length
4
```

### size

Returns the effective memory^[The memory used to store the actual data. It does NOT include the potential headers or other metadata.] size of a value as a number of bytes.

```py
>>> "Hello World! 👋" size
14

>>> 49 size
1

>>> [256, 512, 1024, 2048] size
42
```

## Calling functions

As seen in the previous examples, a function is called by being placed last in an expression.

```py
a b ... func
```

If you want to call a function inside an expression, you can use parentheses to group the function call as its own expression.

```py
a (b c func) other_func
```

`b c func` will be evaluated first, then the result will be used as the second argument of `other_func`.

### Partialization

Calling a function with less arguments than expected returns a partial function that takes the remaining arguments to finish the call.^[You can see this in action in the `map` and `foldleft` examples!]
