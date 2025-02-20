# Copyright (c) 2021 Emanuele Bellocchia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


# Imports
import binascii
import unittest
from bip_utils import EgldAddr, Ed25519PublicKey
from .test_ecc import (
    TEST_VECT_ED25519_PUB_KEY_INVALID,
    TEST_ED25519_BLAKE2B_PUB_KEY, TEST_ED25519_MONERO_PUB_KEY,
    TEST_NIST256P1_PUB_KEY, TEST_SECP256K1_PUB_KEY, TEST_SR25519_PUB_KEY
)

# Some random public keys
TEST_VECT = [
    {
        "pub_key": b"003d39269baa6980d47007f0a30c58c3f4cf74a57230fd51ac90a10a2a6f1366f3",
        "address": "erd185ujdxa2dxqdguq87z3sckxr7n8hfftjxr74rtys5y9z5mcnvmes47zq24",
    },
    {
        "pub_key": b"003cc8a2fc750bf1f699188c17e383820dec9823bdf5f708f638289866087d11dd",
        "address": "erd18ny29lr4p0cldxgc3st78quzphkfsgaa7hms3a3c9zvxvzraz8wsp9xkpu",
    },
    {
        "pub_key": b"00d9bbd1bd99d4595fa0974e89579a9ce645a223e3d80c83010092072806b62a9b",
        "address": "erd1mxaar0ve63v4lgyhf6y40x5uuez6yglrmqxgxqgqjgrjsp4k92dspm6dx5",
    },
    {
        "pub_key": b"79338a9ab5def1305efdf0df8de1d0b9820d7939823f8a79000236c9a4d88e1b",
        "address": "erd10yec4x44mmcnqhha7r0cmcwshxpq67fesglc57gqqgmvnfxc3cdsgzsglr",
    },
    {
        "pub_key": b"e8ee6919e1969fb9ec3ad6450031ae40158f533359c00a63d55c0d70ff1b6457",
        "address": "erd1arhxjx0pj60mnmp66ezsqvdwgq2c75ent8qq5c74tsxhplcmv3tsqpw2lr",
    },
]


#
# Tests
#
class EgldAddrTests(unittest.TestCase):
    # Run all tests in test vector
    def test_to_addr(self):
        for test in TEST_VECT:
            key_bytes = binascii.unhexlify(test["pub_key"])

            # Test with bytes and public key object
            self.assertEqual(test["address"], EgldAddr.EncodeKey(key_bytes))
            self.assertEqual(test["address"], EgldAddr.EncodeKey(Ed25519PublicKey.FromBytes(key_bytes)))

    # Test invalid keys
    def test_invalid_keys(self):
        # Test with invalid key types
        self.assertRaises(TypeError, EgldAddr.EncodeKey, TEST_ED25519_BLAKE2B_PUB_KEY)
        self.assertRaises(TypeError, EgldAddr.EncodeKey, TEST_ED25519_MONERO_PUB_KEY)
        self.assertRaises(TypeError, EgldAddr.EncodeKey, TEST_NIST256P1_PUB_KEY)
        self.assertRaises(TypeError, EgldAddr.EncodeKey, TEST_SECP256K1_PUB_KEY)
        self.assertRaises(TypeError, EgldAddr.EncodeKey, TEST_SR25519_PUB_KEY)

        # Test vector
        for test in TEST_VECT_ED25519_PUB_KEY_INVALID:
            self.assertRaises(ValueError, EgldAddr.EncodeKey, binascii.unhexlify(test))
