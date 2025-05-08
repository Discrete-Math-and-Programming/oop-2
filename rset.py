# class RSet:

def test_rset():
    a = RSet([1, 2, 3])
    b = RSet([3, 4])
    c = RSet([a, 5])  # nested set

    try:
        assert a | b == RSet([1, 2, 3, 4]), "Union"
        assert a & b == RSet([3]), "Intersection"
        assert a - b == RSet([1, 2]) , "Difference"
        assert b - a == RSet([4]), "Difference"
        assert a ^ b == RSet([1, 2, 4]) , "Symmetric Difference"

        assert 2 in a, "Contains"
        assert 4 not in a, "Does not contain"
        assert len(a) == 3, "Length"
        assert a == RSet([3, 2, 1]), "Equality"
        assert a != b, "Inequality"

        assert RSet([1, 2]) < a, "Proper subset"
        assert RSet([1, 2, 3]) <= a, "Subset"
        assert a > RSet([1]), "Proper superset"
        assert a >= RSet([1, 2]), "Superset"

        # Recursive containment
        assert a in c
        assert 5 in c
        assert RSet([5, a]) == c
    except AssertionError as e:
        print("Test failed:", str(e))
        return

    print("All tests passed.")

test_rset()
