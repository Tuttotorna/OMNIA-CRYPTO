# OMNIA CRYPTO

Structural Cryptographic Diagnostics

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19882637.svg)](https://doi.org/10.5281/zenodo.19882637)

Part of the MB-X.01 / OMNIA structural measurement lineage.

---

# New Here

Start here:

1. [CRYPTO_AT_A_GLANCE.md](./CRYPTO_AT_A_GLANCE.md)
2. [FIRST_CRYPTO_EXPERIMENT.md](./FIRST_CRYPTO_EXPERIMENT.md)
3. [FIRST_CRYPTO_EXPERIMENT_RESULTS.md](./FIRST_CRYPTO_EXPERIMENT_RESULTS.md)
4. [run_first_crypto_experiment.py](./run_first_crypto_experiment.py)
5. [COLAB_FIRST_CRYPTO_RUN_V0.md](./COLAB_FIRST_CRYPTO_RUN_V0.md)

This path is currently the shortest route from first contact to the current bounded structural cryptographic direction of the repository.

---

# Quick Run

Run the first bounded crypto experiment:

```bash
python run_first_crypto_experiment.py
```

Runner:

- [run_first_crypto_experiment.py](./run_first_crypto_experiment.py)

Current experiment:

```text
SHA-256 avalanche behavior under minimal input perturbation
```

The goal is not cryptographic breaking.

The goal is bounded structural inspection under controlled transformations.

---

# What It Is

OMNIA CRYPTO is a bounded structural measurement layer for cryptographic behavior.

It focuses on:

- avalanche response
- irreversibility
- entropy drift
- residual invariants
- representation sensitivity
- controlled perturbation behavior

The framework is diagnostic.

It does not attack cryptographic systems.

---

# Core Principle

```text
cryptographic behavior can be inspected structurally
under controlled transformations
```

General OMNIA principle:

```text
structural truth = invariance under transformation
```

---

# Architectural Boundary

```text
measurement != inference != decision
```

OMNIA CRYPTO measures structural behavior.

Interpretation and operational decisions remain external.

This repository does not collapse measurement into attack, validation, or decision.

---

# What It Measures

Current directions include:

- hash avalanche behavior
- bit-distance response
- input perturbation sensitivity
- output divergence
- residual invariant patterns
- entropy drift
- irreversibility behavior

---

# First Experiment — SHA-256 Avalanche Behavior

The first experiment compares two nearly identical inputs.

Input A:

```text
hello
```

Input B:

```text
hellp
```

Only one character changes.

The experiment computes:

```text
SHA-256(input A)
SHA-256(input B)
```

and measures:

```text
bit difference
avalanche ratio
output divergence
```

Expected cryptographic behavior:

```text
small input perturbation
->
large output divergence
```

Files:

- [FIRST_CRYPTO_EXPERIMENT.md](./FIRST_CRYPTO_EXPERIMENT.md)
- [FIRST_CRYPTO_EXPERIMENT_RESULTS.md](./FIRST_CRYPTO_EXPERIMENT_RESULTS.md)
- [run_first_crypto_experiment.py](./run_first_crypto_experiment.py)
- [COLAB_FIRST_CRYPTO_RUN_V0.md](./COLAB_FIRST_CRYPTO_RUN_V0.md)

---

# Colab Verification

The first Colab verification produced:

```text
RETURN CODE: 0

Bit difference: 131/256
Avalanche ratio: 0.5117
Interpretation: strong avalanche behavior
```

Read:

- [COLAB_FIRST_CRYPTO_RUN_V0.md](./COLAB_FIRST_CRYPTO_RUN_V0.md)

---

# Key Separation

The first experiment demonstrates:

```text
small input change
!=
small cryptographic output change
```

under controlled simplified conditions.

This is consistent with expected avalanche behavior in cryptographic hash functions.

---

# What It Is NOT

OMNIA CRYPTO is NOT:

- cryptographic breaking
- key recovery
- exploit generation
- attack tooling
- password cracking
- decryption tooling
- production cryptographic validation

---

# Current Status

Current status:

```text
early bounded research direction
```

The repository currently defines:

- architectural scope
- bounded cryptographic direction
- structural measurement framing
- a first SHA-256 avalanche experiment
- runnable experiment artifact
- Colab reproducibility

No cryptographic security claims are made.

No production validation claims are made.

---

# Repository Direction

The intended direction is:

```text
bounded structural diagnostics
for cryptographic behavior
```

using OMNIA-style measurement concepts:

```text
avalanche response
irreversibility
entropy drift
residual invariants
perturbation sensitivity
divergence behavior
```

---

# Relationship To OMNIA

OMNIA CRYPTO is a verticalization of the broader OMNIA framework.

Core repository:

- [OMNIA](https://github.com/Tuttotorna/OMNIA)

Operational lineage:

- [lon-mirror](https://github.com/Tuttotorna/lon-mirror)

Related DOI:

- [Zenodo DOI](https://doi.org/10.5281/zenodo.19857066)

---

# File Landmarks

Compressed overview:

- [CRYPTO_AT_A_GLANCE.md](./CRYPTO_AT_A_GLANCE.md)

First experiment:

- [FIRST_CRYPTO_EXPERIMENT.md](./FIRST_CRYPTO_EXPERIMENT.md)

First results:

- [FIRST_CRYPTO_EXPERIMENT_RESULTS.md](./FIRST_CRYPTO_EXPERIMENT_RESULTS.md)

Runner:

- [run_first_crypto_experiment.py](./run_first_crypto_experiment.py)

Colab verification:

- [COLAB_FIRST_CRYPTO_RUN_V0.md](./COLAB_FIRST_CRYPTO_RUN_V0.md)

---

# Current Goal

The current goal is not to break cryptography.

The current goal is:

```text
bounded structural inspection
of cryptographic behavior
```

under controlled transformations.

---

# Final Boundary

OMNIA CRYPTO does not claim to validate cryptographic security.

It measures structural behavior relevant to cryptographic diagnostics.

Cryptographic interpretation and operational decisions remain external.