# Object Oriented Programming (Part 2) 

* Read [this](https://www.analyticsvidhya.com/blog/2021/08/explore-the-magic-methods-in-python/) to grasp the idea of magic methods. 


## Task 

Your task is to implement a class called `RSet` that stands for recursive set. The class should be able to represent a set of elements, where each element can be either a single value or another `RSet`. The `RSet` class should support the following operations:

1. **Initialization**: The class should be initialized with a single value or a list of values. If a list is provided, it should be converted into an `RSet` object.
1. **Element Addition**: (`add`) The class should allow adding elements to the set. If an element is a list, it should be converted into an `RSet` object before being added.
1. **Element Removal**: (`remove`) The class should allow removing elements from the set. If an element is a list, it should be converted into an `RSet` object before being removed.
2. **String Representation**: The class should have a string representation that shows the elements in the set. If an element is an `RSet`, it should be represented as a nested set.
4. **Membership Testing**: The class should support membership testing using the `in` keyword.
3. **Set Operations**: The class should support the following set operations:
	 - Union (`|`): Combine two sets.
	 - Intersection (`&`): Find common elements between two sets.
	 - Difference (`-`): Find elements in one set that are not in another.
	 - Symmetric Difference (`^`): Find elements that are in either set but not in both.
5. **Comparison**: The class should support equality testing using the `==` operator, proper subset with `<` and subset with `<=`, and vice versa for supersethood. 
6. **Length**: The class should support the `len()` function to return the number of unique elements in the set.
7. **Iteration**: The class should support iteration over its elements using a for loop or list comprehension. (Use `__iter__` method)

You are required to implement these functionalities by using magic methods. Here is a list of magic methods that you will need to override:


| Set Operation            | Example Syntax         | Magic Method     | Description                                |
|--------------------------|------------------------|------------------|--------------------------------------------|
| Union                    | `a | b`                | `__or__`         | Returns the union of two sets              |
| Intersection             | `a & b`                | `__and__`        | Returns the intersection of two sets       |
| Difference               | `a - b`                | `__sub__`        | Returns the difference of two sets         |
| Symmetric Difference     | `a ^ b`                | `__xor__`        | Returns the symmetric difference           |
| Membership Test          | `x in a`               | `__contains__`   | Checks whether `x` is an element of `a`    |
| Length                   | `len(a)`               | `__len__`        | Returns the number of elements in the set  |
| Equality                 | `a == b`               | `__eq__`         | Checks whether two sets are equal          |
| Inequality               | `a != b`               | `__ne__`         | Checks whether two sets are not equal      |
| Subset Test              | `a <= b`               | `__le__`         | Checks if `a` is a subset of `b`           |
| Proper Subset Test       | `a < b`                | `__lt__`         | Checks if `a` is a proper subset of `b`    |
| Superset Test            | `a >= b`               | `__ge__`         | Checks if `a` is a superset of `b`         |
| Proper Superset Test     | `a > b`                | `__gt__`         | Checks if `a` is a proper superset of `b`  |`


