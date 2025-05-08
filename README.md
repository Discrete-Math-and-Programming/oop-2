# Functions 

* Read [Levin's chapter](https://discrete.openmathbooks.org/dmoi4/sec_structures-functions.html) on functions.
* Go over the exercises at the end.

Note that Levin skips over the more general notion of relation -- he comes to it
in a later stage, though. We will talk about relations a bit in class.

At this stage of the assignment, before starting the coding tasks, be clear about the
following terms and concepts:

* domain, codomain, range.
* injective (one-to-one), surjective (onto), bijective (one-to-one
    correspondence) functions.

## Tasks 

In this assignment, we will represent functions as 3-tuples (triples). The components will
be:

1. the domain (`set` type as you implemented in the previous assignment),
1. the codomain (also a `set`),
1. the mapping between the domain and the codomain (a `dict`).

You are required to implement the following functions:

* `make_func`: takes a domain and a codamain as sets (use your implementation, not
 Python's built-in `set` type), and returns a random function in the above
 format. Use the `random` module to generate the mapping. The
 `random.randint(x,y)` function generates a random integer between `x` and `y`,
 inclusive. Use this facility to randomly pick elements from collections. Once
 you do this for this assignment, you can go on by using `random.choice`
 function that picks a random element from a collection.
* `is_function`: takes a triple and returns `True` if the given 3-tuple represents a
 function, `False` otherwise.

In all the remaining functions, you can assume that the input is a function. You
do not need to check for it. Simply be careful not to test them with triples that are not
functions.

* `is_injective`: takes a function (triple) and returns `True` if it is injective, `False`
    otherwise.
* `is_surjective`: takes a function (triple) and returns `True` if it is surjective,
    `False` otherwise.
* `is_bijective`: takes a function (triple) and returns `True` if it is bijective,
    `False` otherwise.
* `compose`: takes two functions and returns their composition as a triple if it is defined,
    `None` otherwise.
* `inverse`: takes a function and returns its inverse if it has one, returns
    `None` otherwise.

When solving the problems give priority to using `lambda` functions. Revert to
named functions only when you are unable to solve the problem with a `lambda`
function.

Final remarks:

* Remember that you can define and use functions that you are not directly
asked to implment, if you think they help you in your solutions in terms of
clarity.
* If you want to use a function from a previous assignment, follow these steps:
    - copy the file that hosts your function definiton under a new name. For
        instance if you need to construct sets copy the last weeks `editme.py`
        as `mysets.py`.
    - add that file to this repository.
    - import the function you need from `mysets.py` as `from sets import
        <funcname>` or use `from sets import *` to import all functions.
