# OMNIA-CRYPTO

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19882637.svg)](https://doi.org/10.5281/zenodo.19882637)

**OMNIA-CRYPTO** is a bounded structural diagnostics repository for cryptographic-like behavior.

It is not cryptography.

It is not a cryptographic tool.

It is not cryptographic proof.

It is not cracking.

It is not key recovery.

It does not break encryption.

It does not validate production cryptographic security.

Its role is narrower:

```text
measure structural behavior under controlled cryptographic-like transformations
```

Core boundary:

```text
measurement != inference != decision
```

Decision remains external.

---

## Current role

OMNIA-CRYPTO applies the OMNIA measurement lineage to bounded cryptographic-like cases.

It focuses on post-hoc structural diagnostics:

- hash avalanche behavior
- bit-distance response
- output divergence
- entropy drift
- irreversibility
- perturbation sensitivity
- residual invariant inspection
- structural fragility under minimal input change

The repository currently contains a small controlled SHA-256 avalanche experiment.

---

## What it measures

OMNIA-CRYPTO measures structural behavior such as:

- how strongly a hash output changes after minimal input perturbation
- whether output divergence behaves as expected under a bounded test
- whether structural distance increases under input variation
- how bit-level response can be represented as structural measurement

These are structural diagnostics.

They are not cryptographic security proofs.

---

## What it is not

OMNIA-CRYPTO is not:

- cryptographic implementation
- cryptographic proof system
- key recovery tool
- password cracking tool
- wallet recovery tool
- decryption tool
- exploit generator
- attack automation
- vulnerability scanner
- production cryptographic validation
- security certification
- final decision engine

It does not crack.

It does not recover keys.

It does not break encryption.

It does not certify that a primitive is secure.

---

## Existing bounded experiment

### Experiment 01 — SHA-256 avalanche behavior

The first experiment compares two nearly identical inputs:

```text
Input A: hello
Input B: hellp
```

Only one character changes.

The experiment computes SHA-256 for both inputs and measures:

- bit difference
- avalanche ratio
- output divergence
- structural response to minimal input perturbation

Core distinction:

```text
small input change != small cryptographic output change
```

Relevant files:
- [`FIRST_CRYPTO_EXPERIMENT.md`](FIRST_CRYPTO_EXPERIMENT.md)
- [`FIRST_CRYPTO_EXPERIMENT_RESULTS.md`](FIRST_CRYPTO_EXPERIMENT_RESULTS.md)
- [`COLAB_FIRST_CRYPTO_RUN_V0.md`](COLAB_FIRST_CRYPTO_RUN_V0.md)
- [`run_first_crypto_experiment.py`](run_first_crypto_experiment.py)

---

## Run

Run the bounded experiment:

```bash
python run_first_crypto_experiment.py
```

Run repository checks:

```bash
python -m pip install -e .
python -m pytest
```

---

## Public entrypoints

- [`CRYPTO_AT_A_GLANCE.md`](CRYPTO_AT_A_GLANCE.md)
- [`docs/CRYPTO_SCOPE.md`](docs/CRYPTO_SCOPE.md)
- [`docs/RESULTS_INDEX.md`](docs/RESULTS_INDEX.md)
- [`docs/REPOSITORY_STATUS.md`](docs/REPOSITORY_STATUS.md)

---

## Methodological boundary

Correct reading:

```text
avalanche measurement = bounded structural diagnostic evidence
bounded diagnostic evidence != cryptographic proof
cryptographic proof != operational decision
measurement != inference != decision
```

Incorrect reading:

```text
OMNIA-CRYPTO proves SHA-256 is secure
OMNIA-CRYPTO breaks encryption
OMNIA-CRYPTO performs key recovery
OMNIA-CRYPTO replaces cryptographic review
```

---

## Relationship to OMNIA

OMNIA-CRYPTO is a verticalization of the broader OMNIA framework.

```text
OMNIA           = structural measurement core
OMNIA-CRYPTO    = bounded structural diagnostics for cryptographic-like behavior
OMNIA-VALIDATION = evidence / reproducibility layer
OMNIA-LIMIT     = terminal boundary layer
Decision         = external layer
```

The separation remains strict:

```text
measurement != inference != decision
```

---

## Related repositories

- lon-mirror: https://github.com/Tuttotorna/lon-mirror
- OMNIA: https://github.com/Tuttotorna/OMNIA
- OMNIA-VALIDATION: https://github.com/Tuttotorna/OMNIA-VALIDATION
- OMNIA-SECURITY: https://github.com/Tuttotorna/OMNIA-SECURITY
- omnia-limit: https://github.com/Tuttotorna/omnia-limit

---

## Citation

If you reference this repository, use the archived Zenodo record:

```text
DOI: 10.5281/zenodo.19882637
https://doi.org/10.5281/zenodo.19882637
```

Citation metadata is available in:

- [`CITATION.cff`](CITATION.cff)

---

## Summary

OMNIA-CRYPTO is a bounded structural diagnostics repository.

It is not cryptography.

It is not a cryptographic tool.

It is not cracking.

It is not key recovery.

It does not break encryption.

It measures structural behavior in controlled cryptographic-like cases.

Its central boundary is:

```text
measurement != inference != decision
```

---

## OMNIA-CRYPTO — Public Boundary

- OMNIA-CRYPTO is a bounded structural diagnostics layer for cryptographic behavior.
- OMNIA-CRYPTO is not cryptography.
- OMNIA-CRYPTO is not a cryptographic tool.
- OMNIA-CRYPTO is not cryptographic proof.
- OMNIA-CRYPTO is not key recovery.
- OMNIA-CRYPTO is not cracking.
- OMNIA-CRYPTO does not break encryption.
- OMNIA-CRYPTO is not a truth oracle.
- OMNIA-CRYPTO is not a semantic judge.
- OMNIA-CRYPTO is not a decision engine.
- measurement != inference != decision
- decision remains external

This section is a public boundary clarification. It does not change the repository core logic.
