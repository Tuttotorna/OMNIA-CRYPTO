# OMNIA-CRYPTO Results Index

## Purpose

This file gives a public entrypoint into current OMNIA-CRYPTO experiment and result notes.

## Experiment 01 — SHA-256 avalanche behavior

Files:

- `FIRST_CRYPTO_EXPERIMENT.md`
- `FIRST_CRYPTO_EXPERIMENT_RESULTS.md`
- `COLAB_FIRST_CRYPTO_RUN_V0.md`
- `run_first_crypto_experiment.py`

Core distinction:

```text
small input change != small cryptographic output change
```

Purpose:

- compare SHA-256 outputs for two minimally different inputs
- measure bit difference
- measure avalanche ratio
- represent hash avalanche behavior as bounded structural diagnostics

## Colab verification

File:

- `COLAB_FIRST_CRYPTO_RUN_V0.md`

Recorded result:

```text
Bit difference: 131/256
Avalanche ratio: 0.5117
Interpretation: strong avalanche behavior
```

## Reading rule

```text
experiment result = bounded structural diagnostic output
bounded structural diagnostic output != cryptographic proof
bounded structural diagnostic output != security certification
bounded structural diagnostic output != key recovery
```
