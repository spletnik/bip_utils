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
from bip_utils import AlgoAddr, Ed25519PublicKey
from .test_ecc import (
    TEST_VECT_ED25519_PUB_KEY_INVALID,
    TEST_ED25519_BLAKE2B_PUB_KEY, TEST_ED25519_MONERO_PUB_KEY,
    TEST_NIST256P1_PUB_KEY, TEST_SECP256K1_PUB_KEY, TEST_SR25519_PUB_KEY
)

# Some random public keys
TEST_VECT = [
    {
        "pub_key": b"00999418b6fb585a05e91dc8312b15364eb1a5c5b92fef7472b9e877c44cd6486c",
        "address": "TGKBRNX3LBNAL2I5ZAYSWFJWJ2Y2LRNZF7XXI4VZ5B34ITGWJBWBQ7O4GE",
    },
    {
        "pub_key": b"009b8c7c402880a43afa68da22a6ad1aa792194e17794a509ff73f2ffe4ea42501",
        "address": "TOGHYQBIQCSDV6TI3IRKNLI2U6JBSTQXPFFFBH7XH4X74TVEEUAVQ22HNU",
    },
    {
        "pub_key": b"007de3673552c74087237a6ffa56c7ae33c85afde8bac8faf2cc9f4c494a894613",
        "address": "PXRWONKSY5AIOI32N75FNR5OGPEFV7PIXLEPV4WMT5GESSUJIYJ2ZBJRXY",
    },
    {
        "pub_key": b"fc48f2c911ddfd84c794d158f8e406195f5f16723c4747731a8aae01c1f78150",
        "address": "7REPFSIR3X6YJR4U2FMPRZAGDFPV6FTSHRDUO4Y2RKXADQPXQFIJBXUDTI",
    },
    {
        "pub_key": b"fc426991054edcb0ab81bb079df952ba4bdaa0dcfcbb3c32748cf86082950285",
        "address": "7RBGTEIFJ3OLBK4BXMDZ36KSXJF5VIG47S5TYMTURT4GBAUVAKCURE6GDQ",
    },
]


#
# Tests
#
class AlgoAddrTests(unittest.TestCase):
    # Run all tests in test vector
    def test_to_addr(self):
        for test in TEST_VECT:
            key_bytes = binascii.unhexlify(test["pub_key"])

            # Test with bytes and public key object
            self.assertEqual(test["address"], AlgoAddr.EncodeKey(key_bytes))
            self.assertEqual(test["address"], AlgoAddr.EncodeKey(Ed25519PublicKey.FromBytes(key_bytes)))

    # Test invalid keys
    def test_invalid_keys(self):
        # Test with invalid key types
        self.assertRaises(TypeError, AlgoAddr.EncodeKey, TEST_ED25519_BLAKE2B_PUB_KEY)
        self.assertRaises(TypeError, AlgoAddr.EncodeKey, TEST_ED25519_MONERO_PUB_KEY)
        self.assertRaises(TypeError, AlgoAddr.EncodeKey, TEST_NIST256P1_PUB_KEY)
        self.assertRaises(TypeError, AlgoAddr.EncodeKey, TEST_SECP256K1_PUB_KEY)
        self.assertRaises(TypeError, AlgoAddr.EncodeKey, TEST_SR25519_PUB_KEY)

        # Test vector
        for test in TEST_VECT_ED25519_PUB_KEY_INVALID:
            self.assertRaises(ValueError, AlgoAddr.EncodeKey, binascii.unhexlify(test))
