from eth_hash.auto import keccak
serial = int(input("Enter Product Serial Number (numeric): "))
batch  = input("Enter Batch ID: ").strip()
owner  = input("Enter Owner Address: ").strip()

original_str = f"PRODUCT:{serial}|BATCH:{batch}|OWNER:{owner}"
print(f"Original String: '{original_str}'")
keccak_orig = keccak(original_str.encode('utf-8')).hex()
print(f"Original Hash: 0x{keccak_orig}")
modified_serial=serial
if serial%10 == 9:
    modified_serial-=9
else:
    modified_serial+=1
modified_str = f"PRODUCT:{modified_serial}|BATCH:{batch}|OWNER:{owner}"
print(f"Modified String: '{modified_str}'")
keccak_mod = keccak(modified_str.encode('utf-8')).hex()
print(f"Modified Hash: 0x{keccak_mod}")
print(f"Hashes Match?  {keccak_orig == keccak_mod}")
