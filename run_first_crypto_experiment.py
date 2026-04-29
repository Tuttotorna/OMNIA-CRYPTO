import hashlib

print("=" * 100)
print("OMNIA CRYPTO — FIRST CRYPTO EXPERIMENT")
print("=" * 100)

input_a = "hello"
input_b = "hellp"

print("\n" + "=" * 100)
print("INPUTS")
print("=" * 100)

print(f"\nInput A: {input_a}")
print(f"Input B: {input_b}")

hash_a = hashlib.sha256(input_a.encode()).hexdigest()
hash_b = hashlib.sha256(input_b.encode()).hexdigest()

print("\n" + "=" * 100)
print("SHA-256 OUTPUTS")
print("=" * 100)

print(f"\nSHA-256(Input A):\n{hash_a}")
print(f"\nSHA-256(Input B):\n{hash_b}")

bin_a = bin(int(hash_a, 16))[2:].zfill(256)
bin_b = bin(int(hash_b, 16))[2:].zfill(256)

bit_difference = sum(
    bit1 != bit2
    for bit1, bit2 in zip(bin_a, bin_b)
)

avalanche_ratio = bit_difference / 256

print("\n" + "=" * 100)
print("STRUCTURAL OBSERVATION")
print("=" * 100)

print(f"\nBit difference: {bit_difference}/256")
print(f"Avalanche ratio: {avalanche_ratio:.4f}")

if avalanche_ratio > 0.40:
    interpretation = "strong avalanche behavior"
elif avalanche_ratio > 0.20:
    interpretation = "moderate avalanche behavior"
else:
    interpretation = "weak avalanche behavior"

print(f"\nInterpretation: {interpretation}")

print("\nObserved structural direction:")

signals = [
    "minimal input perturbation",
    "large cryptographic divergence",
    "strong diffusion behavior",
    "irreversible transformation characteristics",
]

for signal in signals:
    print(f"- {signal}")

print("\n" + "=" * 100)
print("KEY SEPARATION")
print("=" * 100)

print("""
small input change
!=
small cryptographic output change
""")

print("\n" + "=" * 100)
print("BOUNDARY")
print("=" * 100)

print("""
This experiment is illustrative only.

It does NOT perform:
- cryptographic attacks
- key recovery
- hash reversal
- password cracking
- decryption

It demonstrates only:
bounded structural diagnostics
for cryptographic avalanche behavior.
""")

print("=" * 100)
print("DONE")
print("=" * 100)