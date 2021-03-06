#!/usr/bin/env python3
# coding=utf-8
from random import getrandbits


def fact(x):
    """Factorial"""
    return x * fact(x - 1) if x else 1


def permutation_to_variable_positions(perm):
    """Position of an element counting only the available positions"""
    assert isinstance(perm, list)
    cpy = perm[:]
    positions = []
    for i in range(len(cpy)-1):
        pos = cpy.index(i)
        positions.append(pos)
        del cpy[pos]
    return positions


def permutation_to_integer(perm):
    """Permutation (0÷n-1) to integer"""
    # Set the correct order
    assert isinstance(perm, list)

    def f(_perm):
        """perm -> integer"""
        positions = permutation_to_variable_positions(_perm)
        base = 1
        weight = 1
        integer = 0
        for p in positions[::-1]:
            integer += p * weight
            base += 1
            weight *= base
        return integer

    integer = f(perm)
    if integer < fact(len(perm)) // 2:
        return integer
    integer = f(list(reversed(perm)))
    assert integer < fact(len(perm)) // 2
    return integer


def integer_to_variable_positions(integer, n):
    """Permutation (0÷n-1) to variable positions"""
    base = 2
    positions = []
    for _ in range(n-1):
        positions.append(integer % base)
        integer //= base
        base += 1
    return reversed(positions)


def variable_to_absolute_positions(var):
    """Variable positions to absolute positions"""
    absolute = [None] * len(var)
    pointers = list(range(len(var)))
    for e, p in enumerate(var):
        absolute[pointers[p]] = e
        del pointers[p]
    return absolute


def integer_to_permutation(integer, n):
    """Integer (0÷n-1) to permutation"""
    if integer >= fact(n) // 2:
        raise ValueError('integer %d is too big to be represented'
                         ' as permutation of %d elements. fact(n) / 2'
                         ' = %d' % (integer, n, fact(n) // 2))
    var_pos = list(integer_to_variable_positions(integer, n))
    var_pos.append(0)
    abs_pos = variable_to_absolute_positions(var_pos)
    # randomize the reverse
    if getrandbits(1):
        abs_pos = list(reversed(abs_pos))
    return abs_pos


__all__ = [
    'permutation_to_integer',
    'integer_to_permutation',
]
