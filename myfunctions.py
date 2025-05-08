#
# Assingment on mathematical functions
#

#
# Note on set types for the functions
# 
# In this assignment use the set implementation of the Sets assignment,
# rather than the built-in Python set type. 
# Whenever a type is indicated as set, this will mean your implmentation.
#
# To be able to use your previous solution, save a copy of it under the name
# myset.py and import all the functions from it by the following line:

# from myset import *

# Note that myset.py must be in the same directory as this file for this to
# work. And don't forget to add the file to the repository and push it to
# GitHub.


## Here are some utility functions to make your code more readable.
## Functions are triples of the form (domain, codomain, mapping) and the
## following suite of functions will help you extract the components of the
## function.

fdomain = lambda func: func[0]
fcodomain = lambda func: func[1]
fmapping = lambda func: func[2]
frange = lambda func: set_from_list(fmapping(func).values())

# Implement the following functions:

# make_func
# Input: domain (set), codomain (set)
# Output: triple (<set,set,dict>) 

# is_function
# Input: triple (<set,set,dict>) 
# Output: boolean

# is_injective
# Input: triple (<set,set,dict>) 
# Output: boolean

# is_surjective
# Input: triple (<set,set,dict>) 
# Output: boolean

# is_bijective
# Input: triple (<set,set,dict>) 
# Output: boolean

# compose
# Input: f (triple), g (triple)
# Output: triple that represents the composition of f and g or None if not defined.

# inverse
# Input: triple (<set,set,dict>) 
# Output: triple or None if the inverse is not defined. 

# Testing

def test():

    domain = {1: None, 2: None, 3: None, 4: None}
    codomain = {'a': None, 'b': None, 'c': None, 'd': None}

    results = {}
    test_cases =\
            {'is_function': [
                ([(domain, codomain, {1: 'c', 2: 'c', 3: 'b', 4: 'a'})],True),
                ([(domain, codomain, {1: 'c', 2: 'c', 3: 'b', 4: 'e'})],False),
                ([(domain, codomain, {2: 'c', 3: 'b', 4: 'c'})],False)],
             'is_injective': [
                 ([(domain, codomain |{'e':None,'f':None}, {1: 'c', 2: 'd', 3: 'a', 4:'b'})],True),
                 ([(domain, codomain, {1: 'c', 2: 'a', 3: 'c'})],False)],
             'is_surjective': [
                 ([(domain, codomain, {1: 'd', 2: 'b', 3: 'c', 4: 'a'})],True),
                 ([(domain, codomain, {1: 'b', 2: 'c', 3: 'c', 4: 'd'})],False)],
             'is_bijective': [
                 ([(domain, codomain, {1: 'b', 2: 'd', 3: 'a', 4: 'c'})],True),
                 ([(domain, codomain, {1: 'c', 2: 'a', 3: 'a', 4: 'c'})],False),
                 ([(domain, codomain|{'e':None}, {1: 'a', 2: 'b', 3: 'c', 4: 'd'})],False)
             ],
             'compose': [
                    ([(domain,codomain,{1: 'c', 2: 'd', 3: 'c', 4: 'd'}), (remove(codomain,'c'),domain,{'a': 1, 'b': 1, 'c': 2, 'd': 3} )], None)
             ],
             'inverse': [
                 ([(domain,codomain, {1: 'd', 2: 'b', 3: 'c', 4: 'a'})], ({'d': None, 'b': None, 'c': None, 'a': None}, {1: None, 2: None, 3: None, 4: None}, {'d': 1, 'b': 2, 'c': 3, 'a': 4})),
                 ([(domain,codomain, {1: 'c', 2: 'd', 3: 'd', 4: 'b'})], None)
                    ]
            } 


    for funcname, cases  in test_cases.items():
        try:
            results[funcname] =  "OK" if all([eval(funcname)(*case[0]) == case[1] for case in cases]) else "Not OK"
        except NameError:
            results[funcname] = "Not Implemented"
        except Exception as e:
            results[funcname] = "Error -- " + str(e)

    print("Function Name            | Status")
    print("-------------------------|--------")
    for key, value in results.items():
        print(f"{key:<24} | {value}")

