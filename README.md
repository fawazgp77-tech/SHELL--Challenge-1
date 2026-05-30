# Title: Challenge 1 - Hashing & The Avalanche Effect
## My Approach: 
For part A, I've used hashlib as it provides the SHA-256 algorithim used for hashing. For part B I've used eth-hash library as it provides keccak256 which is also used by Ethereuem and Solidity.

I've taken input for serial number of product, batch and owner's address and combined them to get an identity string. 

To change one character of the string to test the avalanche effect, I've assumed serial number is numeric and taken the last digit of the string and added 1, if it's 9 then it becomes 0. Then using the respective algorithims, I hashed them and compared. 
## Step by Step approach: 
### Part A
#### 1. Import haslib
```python
import hashlib
```
#### 2. Take input and construct the original identity string
```python
serial = int(input("Enter Product Serial Number (numeric): "))
batch  = input("Enter Batch ID: ").strip()
owner  = input("Enter Owner Ethereum Address: ").strip()

original_str = f"PRODUCT:{serial}|BATCH:{batch}|OWNER:{owner}"
print(f"Original String: '{original_str}'")
```
Sample Data Used: 
```
Serial: 1001  
Batch: 29
Owner's Address: 0x981B34766E1D8E7D17e1bDE1Db9C9FEEFF1F232B
Identity String: PRODUCT:1001|BATCH:29|OWNER:0x981B34766E1D8E7D17e1bDE1Db9C9FEEFF1F232B
```
#### 3. Hash the original identity string
```python
sha_orig = hashlib.sha256(original_str.encode('utf-8')).hexdigest()
print(f"Original Hash: 0x{sha_orig}")
```
Output
```
Original Hash: 0x6174e859f01f4976e37f1609b24c1866d7e73b8ebea499985b1159aad3763437
```
#### 4. Change the original string
```python
modified_serial=serial
if serial%10 == 9:
    modified_serial-=9
else:
    modified_serial+=1
modified_str = f"PRODUCT:{modified_serial}|BATCH:{batch}|OWNER:{owner}"
print(f"Modified String: '{modified_str}'")
```
Output
```
Modified String: 'PRODUCT:1002|BATCH:29|OWNER:0x981B34766E1D8E7D17e1bDE1Db9C9FEEFF1F232B'
```
#### 5. Hash the changed string
```python
sha_mod = hashlib.sha256(modified_str.encode('utf-8')).hexdigest()
print(f"Modified Hash: 0x{sha_mod}")

print(f"Do the hashes match?  {sha_orig == sha_mod}")
```
Output
```
Modified Hash: 0x40ae84f812363d8886b631305b2c3a9bfd4fdd839cff3115defac23cca0f7e73
Hashes Match?  False
```

### Part B
#### 1. Import the eth-hash library
```python
from eth_hash.auto import keccak
```
#### 2. Take input and construct the original identity string
```python
serial = int(input("Enter Product Serial Number (numeric): "))
batch  = input("Enter Batch ID: ").strip()
owner  = input("Enter Owner Address: ").strip()

original_str = f"PRODUCT:{serial}|BATCH:{batch}|OWNER:{owner}"
print(f"Original String: '{original_str}'")
```
Sample Data Used: 
```
Serial: 1001  
Batch: 29
Owner's Address: 0x981B34766E1D8E7D17e1bDE1Db9C9FEEFF1F232B
Identity String: PRODUCT:1001|BATCH:29|OWNER:0x981B34766E1D8E7D17e1bDE1Db9C9FEEFF1F232B
```
#### 3. Hash the original identity string
```python
keccak_orig = keccak(original_str.encode('utf-8')).hex()
print(f"Original Hash: 0x{keccak_orig}")
```
Output
```
Original Hash: 0xb478295b673ba353cb44786e9404a352c35b7139b183bea8e524c4b8c11ab947
```
#### 4. Change the original string
```python
modified_serial=serial
if serial%10 == 9:
    modified_serial-=9
else:
    modified_serial+=1
modified_str = f"PRODUCT:{modified_serial}|BATCH:{batch}|OWNER:{owner}"
print(f"Modified String: '{modified_str}'")
```
Output
```
Modified String: 'PRODUCT:1002|BATCH:29|OWNER:0x981B34766E1D8E7D17e1bDE1Db9C9FEEFF1F232B'
```
#### 5. Hash the changed string
```python
keccak_mod = keccak(modified_str.encode('utf-8')).hex()
print(f"Modified Hash: 0x{keccak_mod}")
print(f"Hashes Match?  {keccak_orig == keccak_mod}")
```
Output
```
Modified Hash: 0x6692289cda80cd60715097b0f7ddadb05bfa13fc9494aee8ab494244d5d85217
Hashes Match?  False
```
## Outputs
### Part A
![Keccak-256 Output](screenshots/your_screenshot_name.png)

![Keccak-256 Output](screenshots/your_screenshot_name.png)

![Keccak-256 Output](screenshots/your_screenshot_name.png)

### Part B
![Keccak-256 Output](screenshots/your_screenshot_name.png)

![Keccak-256 Output](screenshots/your_screenshot_name.png)

![Keccak-256 Output](screenshots/your_screenshot_name.png)
