#!/usr/bin/python

import sys
import binascii
import base64

from bip_utils import (
    Bip39WordsNum, Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44Changes, Bip44Coins, Bip44
)

num_args = len(sys.argv)
args = str(sys.argv)

# print('Number of arguments:', num_args, 'arguments.' )
# print('Argument List:', args )

if num_args < 3 :
    #print('Parameters are user_id, index')
    exit()

account_id = int(sys.argv[1])
index =  int(sys.argv[2])
base64_message =  sys.argv[3]

# print('Account ID: ', account_id)
# print('Account Index: ', index)

# Generate random mnemonic
#mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_24)
#print("Mnemonic string: %s" % mnemonic)


#mnemonic = VAULT.get_solana_seed( KEY )
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')

mnemonic = message
# Generate seed from mnemonic
seed_bytes = Bip39SeedGenerator(mnemonic).Generate()




# Construct from seed
bip44_mst_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.ELROND)
# Print master key
# print("Master key (bytes): %s" % bip44_mst_ctx.PrivateKey().Raw().ToHex())
# print("Master key (extended): %s" % bip44_mst_ctx.PrivateKey().ToExtended())
# print("Master key (WIF): %s" % bip44_mst_ctx.PrivateKey().ToWif())

bip44_acc_ctx = bip44_mst_ctx.Purpose().Coin().Account( account_id )
bip44_chg_ctx = bip44_acc_ctx.Change(Bip44Changes.CHAIN_EXT)
bip44_addr_ctx = bip44_chg_ctx.AddressIndex( index )
#print("%d. Address: %s %s" % (account_id, bip44_addr_ctx.PublicKey().ToAddress(), bip44_addr_ctx.PrivateKey().ToExtended()) )

priv_key_bytes = bip44_addr_ctx.PrivateKey().Raw().ToBytes()
pub_key_bytes = bip44_addr_ctx.PublicKey().RawCompressed().ToBytes()[1:]

print("{\"address\": \"%s\", \"private_key\": \"%s\"}" % (bip44_addr_ctx.PublicKey().ToAddress(), bip44_addr_ctx.PrivateKey().Raw() ) ) 

