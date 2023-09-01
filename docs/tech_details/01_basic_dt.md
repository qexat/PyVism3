# Basic data types

[← Implementation details](./index.md)

## Integer

### Bounds

The Integer type should theoretically not have bounds ; but in practice, they have some since no computer has infinite memory.
It is an **implementation detail**, with one restriction though: the lower
bound should be at most -2,147,483,648 and the upper bound at least 2,147,483,647.

### Overflow and underflow behavior

⚠️ When overflowing or underflowing, integers should **NOT** wrap: for example, the lower bound minus one should not equal the upper bound.

➡️ Instead, it should raise a runtime error if it was not possible to catch during compilation.

## Real

The Real type is defined as specified in the [IEEE standard for floating-point arithmetic](https://en.wikipedia.org/wiki/IEEE_754).

**Overflow and underflow behavior:** see [`Integer::overflow_and_underflow_behavior`](#overflow-and-underflow-behavior).

## String

Character strings are encoded in UTF-8, and support escape sequences and emojis.

The character size is not necessarily one byte: to get the number of characters in a string, use the `length` function ; for the string effective size in memory (number of bytes), use `size`.

```py
>>> "👩‍👩‍👦‍👦" length
1
>>> "👩‍👩‍👦‍👦" size
7
```

## ByteString

Byte strings, contrary to character strings, will always have `length` and `size` return the same value.

```py
>>> '👩‍👩‍👦‍👦' length
7
>>> '👩‍👩‍👦‍👦' size
7
```

## Tuple

The Tuple type generic arity is variadic.

```py
Tuple<Real, Real>  # a pair of real numbers (e.g. a 2D point)
Tuple<Integer, ...> # this tuple contains any number of integers 
Tuple<()>  # empty tuple
```

Similarly to Swift, singles are intentionally not allowed. They have virtually no world use, and add complexity to the literal as well as to the typing syntax.

## List

The List type generic arity is one.

```py
List<Integer>
```

A list gets re-allocated if its length must be bigger than its current capacity.

**Growth factor:** `3 / 2` (1.5)

## Set

The Set type generic arity is one.

```py
Set<Integer>
```

Set values are NEVER guaranteed to be stored in order. They are not required to be hashable: you might be looking for [`HashSet`](#hashset).

**Growth factor:** `3 / 2` (1.5)

## HashSet

The HashSet type generic arity is one.

```py
HashSet<Integer>
```

It has the same properties as the [`Set`](#set) type, with the exception of requiring elements to be hashable.

**Growth factor:** `3 / 2` (1.5)

## Mapping

The Mapping type generic arity is two.

```py
Mapping<String, Integer>
```
