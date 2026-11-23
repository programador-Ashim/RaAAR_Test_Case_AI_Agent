import pytest
from raaar_evidence import Fact, analyze_evidence, gate


CANDIDATE = "sensor"
CAPABILITY = "measure_temperature"
VERSION = "2.0"


def make_fact(polarity=True, versions=None, superseded_by=None):
    return Fact(
        source_id="test_source",
        candidate=CANDIDATE,
        capability=CAPABILITY,
        polarity=polarity,
        valid_versions=versions if versions is not None else ["2.0"],
        superseded_by=superseded_by,
    )


# Test 1: Current supporting evidence
def test_supported_evidence():
    result = analyze_evidence(
        CANDIDATE, CAPABILITY, VERSION,
        [make_fact(True)]
    )
    assert result["status"] == "supported"


# Test 2: No matching evidence
def test_missing_evidence():
    result = analyze_evidence(
        CANDIDATE, CAPABILITY, VERSION, []
    )
    assert result["status"] == "missing"


# Test 3: Superseded historical evidence
def test_outdated_evidence():
    result = analyze_evidence(
        CANDIDATE, CAPABILITY, VERSION,
        [make_fact(True, ["1.0"], "new_source")]
    )
    assert result["status"] == "outdated"


# Test 4: Conflicting current claims
def test_contradictory_evidence():
    result = analyze_evidence(
        CANDIDATE, CAPABILITY, VERSION,
        [make_fact(True), make_fact(False)]
    )
    assert result["status"] == "contradictory"


# Test 5: Current evidence refutes claim
def test_refuted_evidence():
    result = analyze_evidence(
        CANDIDATE, CAPABILITY, VERSION,
        [make_fact(False)]
    )
    assert result["status"] == "refuted"


# Test 6: Strong score + supporting evidence
def test_accept_supported_candidate():
    result = gate(
        CANDIDATE, CAPABILITY, VERSION,
        0.90, [make_fact(True)], 0.65
    )
    assert result["decision"] == "resolve"


# Test 7: Low score should trigger review
def test_abstain_on_low_score():
    result = gate(
        CANDIDATE, CAPABILITY, VERSION,
        0.40, [make_fact(True)], 0.65
    )
    assert result["decision"] == "human_review"


# Test 8: Contradictory evidence should trigger review
def test_abstain_on_contradiction():
    result = gate(
        CANDIDATE, CAPABILITY, VERSION,
        0.95, [make_fact(True), make_fact(False)], 0.65
    )
    assert result["decision"] == "human_review"


# Test 9: Outdated evidence should trigger review
def test_abstain_on_outdated():
    result = gate(
        CANDIDATE, CAPABILITY, VERSION,
        0.95, [make_fact(True, ["1.0"], "new_source")], 0.65
    )
    assert result["decision"] == "human_review"


# Test 10: Missing evidence should trigger review
def test_abstain_on_missing():
    result = gate(
        CANDIDATE, CAPABILITY, VERSION,
        0.95, [], 0.65
    )
    assert result["decision"] == "human_review"
