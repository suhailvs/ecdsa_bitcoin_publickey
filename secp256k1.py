def inverse_mod(a, m):
  """Inverse of a mod m."""
  if a < 0 or m <= a:
    a = a % m

  # From Ferguson and Schneier, roughly:
  c, d = a, m
  uc, vc, ud, vd = 1, 0, 0, 1
  while c != 0:
    q, c, d = divmod(d, c) + (c,)
    uc, vc, ud, vd = ud - q * uc, vd - q * vc, uc, vc

  # At this point, d is the GCD, and ud*a+vd*m = d.
  # If d == 1, this means that ud is a inverse.
  assert d == 1
  if ud > 0: return ud
  return ud + m

class Point(object):
  def __init__(self, x, y):    
    self.__x = x
    self.__y = y 
    # y^2 = x^3 + a*x + b (mod p)
    # p is the smallest prime that satisfies: p = 2^256 - 2^32 - t where t < 1024
    self.__curve = {"a":0,"b":7,
      "p":0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f} 

  def __str__(self):
    if self == INFINITY:return "infinity"
    return "(%d,%d)" % (self.__x, self.__y)

  def __add__(self, other):
    """Add one point to another point."""
    if other == INFINITY: return self
    if self == INFINITY: return other

    p = self.__curve['p']
    if self.__x == other.__x:
      if (self.__y + other.__y) % p == 0:
        return INFINITY
      else: return self.double()

    l = ((other.__y - self.__y) * \
         inverse_mod(other.__x - self.__x, p)) % p

    x3 = (l * l - self.__x - other.__x) % p
    y3 = (l * (self.__x - x3) - self.__y) % p

    return Point(x3, y3)

  def __mul__(self, other):
    """Multiply a point by an integer."""
    def leftmost_bit(x):
      assert x > 0
      result = 1
      while result <= x:
        result = 2 * result
      return result // 2

    e = other
    if e == 0: return INFINITY
    if self == INFINITY: return INFINITY
    assert e > 0

    e3 = 3 * e
    negative_self = Point(self.__x, -self.__y)
    i = leftmost_bit(e3) // 2
    result = self
    # print_("Multiplying %s by %d (e3 = %d):" % (self, other, e3))
    while i > 1:
      result = result.double()
      if (e3 & i) != 0 and (e & i) == 0:
        result = result + self
      if (e3 & i) == 0 and (e & i) != 0:
        result = result + negative_self
      # print_(". . . i = %d, result = %s" % ( i, result ))
      i = i // 2

    return result

  def __rmul__(self, other):
    """Multiply a point by an integer."""
    return self * other

  def double(self):
    """Return a new point that is twice the old."""
    if self == INFINITY: return INFINITY
    p = self.__curve['p']

    # (3x^2)/2y
    l = ((3 * self.__x * self.__x) * \
         inverse_mod(2 * self.__y, p)) % p

    # (l^2)-2x
    x3 = (l * l - 2 * self.__x) % p
    # l(x-x3)-y
    y3 = (l * (self.__x - x3) - self.__y) % p
    return Point(x3, y3)

  def x(self):
    return self.__x

  def y(self):
    return self.__y

# This one point is the Point At Infinity for all purposes:
INFINITY = Point(None, None)

# Generator Point: This is the same for everyone. All other points are children of this base point
G = Point(55066263022277343669578718895168534326250603453777594175500187360389116729240,
  32670510020758816978083085130507043184471273380659243275938904335757337482424)
