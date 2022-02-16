#simple module for doing maths

from math import *

class DomainError(Exception):
    "Error for arc functions"

def arc_degrees(f):
    """
    allows printing result of asin, acos, atan functions in degrees instead of radians
    """
    def helper(x, dec=3, all_dec=False):
        try:
            res = degrees(f(x))
        except ValueError as e:
            raise DomainError("This function's domain is a range [-1, 1]") from e
        if all_dec is True:
            return res
        return float(f"%.{dec}f" % res)
    return helper

asin_degrees = arc_degrees(asin)
acos_degrees = arc_degrees(acos)
atan_degrees = arc_degrees(atan)

def trig_degrees(f):
    """
    allows using sin, cos, tan functions with degrees instead of radians
    """
    def helper(x, dec=3, all_dec=False):
        res = (f(radians(x)))
        if all_dec is True:
            return res
        return float(f"%.{dec}f" % res)
    return helper

sin_degrees = trig_degrees(sin)
cos_degrees = trig_degrees(cos)
tan_degrees = trig_degrees(tan)


def is_prime(initial_n):
    """
    prints out all the divisors for INITIAL_N
    """
    res = []
    def helper(n, res):
        if n == 1:
            if len(res) == 1:
                return str(initial_n) + ' is a prime number.'
            return res
        for i in range(2, n+1):
            if n % i == 0:
                res.append(i)
                return helper(n//i, res)
    return helper(initial_n, res)
