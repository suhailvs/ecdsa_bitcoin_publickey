# To Hack
# pubKey = 108885535526593411662006730550522905195475559108777682412292337598664109614708
# pubKey_hex= "02f0bb0774f61a63a610719f73c63f0019c0db62bdfc3682bc55f911538c766674"
# address='16rCmCmbuWDhPjWTrpQGaU3EPdZF7MTdUk'

from secp256k1 import G
"""
# Generator Point
Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424
G = Point(Gx,Gy)
"""

# RoyalForkblog ECDSA
priKey = 23695310554196047209792918797392416191148132060917476866274911959533140016553
pubKey = priKey*G
print (pubKey)

# Public key for SHA256("brettonwoods_7_1_1944")
priKey =0x9DF5A907FF17ED6A4E02C00C2C119049A045F52A4E817B06B2EC54EB68F70079
pubKey = priKey*G
print ('X:',hex(pubKey.x()))