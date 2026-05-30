import hashlib
serial = int(input("Enter Product Serial Number (numeric): "))
batch  = input("Enter Batch ID: ").strip()
owner  = input("Enter Owner Address: ").strip()

original_str = f"PRODUCT:{serial}|BATCH:{batch}|OWNER:{owner}"
print(f"Original String: '{original_str}'")
sha_orig = hashlib.sha256(original_str.encode('utf-8')).hexdigest()
print(f"Original Hash: 0x{sha_orig}")
modified_serial=serial
if serial%10 == 9:
    modified_serial-=9
else:
    modified_serial+=1
modified_str = f"PRODUCT:{modified_serial}|BATCH:{batch}|OWNER:{owner}"
print(f"Modified String: '{modified_str}'")
sha_mod = hashlib.sha256(modified_str.encode('utf-8')).hexdigest()
print(f"Modified Hash: 0x{sha_mod}")

print(f"Do the hashes match?  {sha_orig == sha_mod}")
