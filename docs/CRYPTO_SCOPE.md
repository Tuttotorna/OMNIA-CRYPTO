# OMNIA-CRYPTO Scope

## Purpose

OMNIA-CRYPTO is a bounded structural diagnostics layer for cryptographic-like behavior.

It measures structural response under controlled transformations, such as hash avalanche behavior after minimal input perturbation.

## Boundary

```text
measurement != inference != decision
diagnostic signal != cryptographic proof
hash avalanche measurement != security certification
cryptographic-like behavior != cryptographic tool
```

## What is in scope

OMNIA-CRYPTO may measure:

- hash avalanche response
- bit-distance behavior
- output divergence
- entropy drift
- irreversibility
- perturbation sensitivity
- residual invariant patterns
- structural fragility under minimal input changes

## What is out of scope

OMNIA-CRYPTO does not perform:

- cracking
- key recovery
- password recovery
- wallet recovery
- decryption
- encryption breaking
- exploit generation
- vulnerability scanning
- production cryptographic validation
- cryptographic security certification

## Correct interpretation

```text
signal = bounded structural diagnostic evidence
evidence = input to external review
external review = outside this repository
decision remains external
```
