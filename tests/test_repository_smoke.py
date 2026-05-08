
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_public_entrypoints_exist():
    required = [
        "README.md",
        "LICENSE",
        "CITATION.cff",
        "pyproject.toml",
        "pytest.ini",
        "CRYPTO_AT_A_GLANCE.md",
        "docs/CRYPTO_SCOPE.md",
        "docs/RESULTS_INDEX.md",
        "docs/REPOSITORY_STATUS.md",
    ]
    for rel in required:
        assert (ROOT / rel).exists(), rel

def test_current_experiment_files_exist():
    required = [
        "FIRST_CRYPTO_EXPERIMENT.md",
        "FIRST_CRYPTO_EXPERIMENT_RESULTS.md",
        "COLAB_FIRST_CRYPTO_RUN_V0.md",
        "run_first_crypto_experiment.py",
    ]
    for rel in required:
        assert (ROOT / rel).exists(), rel

def test_readme_boundary_terms():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    required_phrases = [
        "measurement != inference != decision",
        "not a cryptographic tool",
        "not cryptographic proof",
        "not cracking",
        "not key recovery",
        "does not break encryption",
        "Decision remains external",
    ]
    for phrase in required_phrases:
        assert phrase in text

def test_scope_boundary_terms():
    text = (ROOT / "docs" / "CRYPTO_SCOPE.md").read_text(encoding="utf-8")
    required_phrases = [
        "diagnostic signal != cryptographic proof",
        "hash avalanche measurement != security certification",
        "cryptographic-like behavior != cryptographic tool",
        "decision remains external",
    ]
    for phrase in required_phrases:
        assert phrase in text

def test_citation_contains_doi():
    text = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    assert "10.5281/zenodo.19882637" in text
