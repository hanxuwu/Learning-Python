# Creates a class to represent a permutation of 1, 2, ..., n for some n >= 0.
#
# An object is created by passing as argument to the class name:
# - either no argument, in which case the empty permutation is created, or
# - "length = n" for some n >= 0, in which case the identity over 1, ..., n is created, or
# - the numbers 1, 2, ..., n for some n >= 0, in some order, possibly together with "lengh = n".
#
# __len__(), __repr__() and __str__() are implemented, the latter providing the standard form
# decomposition of the permutation into cycles (see wikepedia page on permutations for details).
#
# Objects have:
# - nb_of_cycles as an attribute
# - inverse() as a method
#
# The * operator is implemented for permutation composition, for both infix and in-place uses.
#
# Written by Eric Martin for COMP9021


class PermutationError(Exception):
    def __init__(self, message):
        self.message = message

class Permutation:
    def __init__(self, *args, length = None):
        if length is not None:
            if not isinstance(length, int) or length < 0:
                raise PermutationError('Cannot generate permutation from these arguments')
            if not args:
                self._permutation = list(range(1, length + 1))
                self._cycles = [[i] for i in range(1, length + 1)]
                self.nb_of_cycles = length
                return
            if length != len(args):
                raise PermutationError('Cannot generate permutation from these arguments')
        try:
            if set(args) != set(range(1, len(args) + 1)):
                raise PermutationError('Cannot generate permutation from these arguments')
        except TypeError:
                raise PermutationError('Cannot generate permutation from these arguments')
        self._permutation = list(args)
        self._decompose_into_cycles()

    def __len__(self):
        return len(self._permutation)

    def __repr__(self):
        return f"Permutation({', '.join(str(self._permutation[i]) for i in range(len(self)))})"

    def __str__(self):
        return '(' + ')('.join(' '.join(str(e) for e in cycle) for cycle in self._cycles) + ')'

    def _decompose_into_cycles(self):
        cycles = []
        seen = set()
        for i in range(len(self) - 1, -1, -1):
            if i in seen:
                continue
            cycle = []
            while i not in seen:
                seen.add(i)
                cycle.append(i + 1)
                i = self._permutation[i] - 1
            cycles.append(cycle)
        self._cycles = list(reversed(cycles))
        self.nb_of_cycles = len(self._cycles)

    def __mul__(self, permutation):
        return Permutation(*self._multiply(permutation))

    def __imul__(self, permutation):
        self._permutation = self._multiply(permutation)
        self._decompose_into_cycles()
        return self

    def _multiply(self, permutation):
        if len(self) != len(permutation):
            raise PermutationError('Cannot compose permutations of different lengths')
        product_permutation = list(permutation._permutation[self._permutation[i] - 1]
                                                                           for i in range(len(self))
                                  )
        return product_permutation

    def inverse(self):
        L = [None] * len(self)
        for i in range(len(L)):
            L[self._permutation[i] - 1] = i + 1
        return Permutation(*L)
        



                
        
