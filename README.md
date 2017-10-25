# Bitcoin Publickey creator

This will generate bitcoin public key from a private key.
PublicKeyPoint = PrivateKey * GeneratorPoint

## Bitcoin Numbers

To ground all this in reality, here are some real numbers taken directly from bitcoin itself (bitcoin uses the sicp256k1 curve, which has it’s own paramers and generator point).

**Generator Point:** Remember, this is the same for everyone. All other points are children of this base point.
```
x: 55066263022277343669578718895168534326250603453777594175500187360389116729240
y: 32670510020758816978083085130507043184471273380659243275938904335757337482424
```

## Example

```
>>> from secp256k1 import G
>>> priKey = 23695310554196047209792918797392416191148132060917476866274911959533140016553
>>> pubKey = priKey*G
>>> print (pubKey)
```
will return Public Key:
```
x: 39874617776630327813190058413816560767734954098998567043224950074533143699292
y: 83115399533222200534442050051826386603242609920409430626876080623730665355556
```