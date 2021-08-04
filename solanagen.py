#!/usr/bin/python

import sys
import binascii

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

# print('Account ID: ', account_id)
# print('Account Index: ', index)

# Generate random mnemonic
#mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_24)
#print("Mnemonic string: %s" % mnemonic)


#mnemonic = VAULT.get_solana_seed( KEY )

mnemonic = "gallery hospital reflect tray strike pyramid scrap two proud cute trend sunny bulk almost surface trap license drastic fiber tumble rare purity dentist dice"
# Generate seed from mnemonic
seed_bytes = Bip39SeedGenerator(mnemonic).Generate()




# Construct from seed
bip44_mst_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.SOLANA)
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
key_pair = priv_key_bytes + pub_key_bytes

print("{\"address\": \"%s\", \"private_key\": \"%s\"}" % (bip44_addr_ctx.PublicKey().ToAddress(), key_pair.hex() ) ) 

