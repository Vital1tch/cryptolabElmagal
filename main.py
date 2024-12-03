from ecpy.curves import WeierstrassCurve, Point
from codetable import code

p = 65521
ec = WeierstrassCurve({'name': 'custom','type': 'WEIERSTRASS', 'size': 16, 'a':65520,'b': 16,'field': p,'generator': (0, 4),'order':65993,'cofactor':1})

pubKey = Point(42254, 59491,ec)

gen = Point(0, 4, ec)

prKey = 0

a = gen

for i in range(2, p):
    a = a + gen
    if a == pubKey:
        prKey = i
        break

print(prKey)

data = open('encrypted/28-EC.ec', 'rb').read()
out = open('decrypted/28-EC.png', 'wb')

print(len(data))


for i in range(0, len(data), 8):

    x1, y1, x2, y2 = data[i:i+2], data[i+2:i+4], data[i+4:i+6], data[i+6:i+8]
    x1 = int.from_bytes(x1, "big")
    y1 = int.from_bytes(y1, "big")
    x2 = int.from_bytes(x2, "big")
    y2 = int.from_bytes(y2, "big")

    C1, C2 = Point(x1,y1,ec), Point(x2, y2, ec)

    M = C2 - prKey * C1 # (12845, 27801)
    b = code[(M.x, M.y)]
    #print(hex())
    out.write(b.to_bytes(2, 'big'))


out.close()
