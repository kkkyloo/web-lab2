import rsa
from rsa import key, common
(pub_key, priv_key) = key.newkeys(256)
message = b'hello'
crypto = encrypt(message, pub_key)

(pub_key, priv_key) = rsa.newkeys(256)
crypto = encrypt(b'hello', pub_key)
decrypt(crypto, priv_key)