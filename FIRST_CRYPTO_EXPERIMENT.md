# FIRST CRYPTO EXPERIMENT

SHA-256 Avalanche Behavior Under Minimal Perturbation

---

# Goal

This experiment defines a first bounded OMNIA CRYPTO case:

```text
small input perturbation
->
large cryptographic divergence
```

The goal is not cryptographic breaking.

The goal is bounded structural inspection of avalanche behavior under controlled perturbation.

---

# Scenario

We compare two nearly identical inputs.

Input A:

```text
hello
```

Input B:

```text
hellp
```

Only one character changes.

---

# Transformation

Compute:

```text
SHA-256(input A)
SHA-256(input B)
```

---

# Expected Cryptographic Behavior

A secure cryptographic hash should exhibit:

```text
high avalanche response
```

Meaning:

```text
minimal input perturbation
should produce
large output divergence
```

---

# Structural Observation Direction

The experiment does not evaluate semantic meaning.

The experiment evaluates structural response.

Possible measurements include:

```text
bit difference
normalized distance
avalanche ratio
entropy drift
residual structure
```

---

# Key Separation

```text
small input change
!=
small cryptographic output change
```

A cryptographic hash is expected to amplify minimal perturbations.

---

# Why This Matters

Cryptographic robustness depends heavily on:

```text
irreversibility
diffusion
perturbation amplification
```

A weak avalanche response may indicate structural weakness.

This experiment only defines a bounded measurement direction.

It does not validate cryptographic security formally.

---

# Boundary

This repository does NOT perform:

```text
key recovery
hash reversal
password cracking
cryptographic attacks
decryption
```

It only explores:

```text
bounded structural diagnostics
for cryptographic behavior
```

under controlled transformations.

---

# Repository Status

Current status:

```text
early bounded research direction
```

No production cryptographic claims are made.