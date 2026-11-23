# RaAAR test agent execution report

Generated at: 2026-11-23T20:32:35.738952+00:00
Mode: approved declarative cases; model training: none

**Result: 17/17 passed; 0 failed/errors.**

| Case | Kind | Outcome | Expected | Observed |
|---|---|---|---|---|
| TC01-current-support | facts | PASS | {'status': 'supported', 'decision': 'resolve'} | {'status': 'supported', 'decision': 'resolve'} |
| TC02-no-evidence | facts | PASS | {'status': 'missing', 'decision': 'human_review'} | {'status': 'missing', 'decision': 'human_review'} |
| TC03-superseded-evidence | facts | PASS | {'status': 'outdated', 'decision': 'human_review'} | {'status': 'outdated', 'decision': 'human_review'} |
| TC04-conflicting-claims | facts | PASS | {'status': 'contradictory', 'decision': 'human_review'} | {'status': 'contradictory', 'decision': 'human_review'} |
| TC05-current-refutation | facts | PASS | {'status': 'refuted', 'decision': 'human_review'} | {'status': 'refuted', 'decision': 'human_review'} |
| TC06-low-score | facts | PASS | {'status': 'supported', 'decision': 'human_review'} | {'status': 'supported', 'decision': 'human_review'} |
| TC07-unknown-authority | facts | PASS | {'status': 'missing', 'decision': 'human_review'} | {'status': 'missing', 'decision': 'human_review'} |
| TC08-wrong-candidate | facts | PASS | {'status': 'missing', 'decision': 'human_review'} | {'status': 'missing', 'decision': 'human_review'} |
| TC09-old-negative-current-positive | facts | PASS | {'status': 'supported', 'decision': 'resolve'} | {'status': 'supported', 'decision': 'resolve'} |
| TC10-threshold-boundary | facts | PASS | {'status': 'supported', 'decision': 'resolve'} | {'status': 'supported', 'decision': 'resolve'} |
| TC11-extract-polarity | extract | PASS | [True, False] | [True, False] |
| TC12-extract-nonmatching | extract | PASS | [] | [] |
| TC-document-supported | manifest | PASS | {'status': 'supported', 'decision': 'resolve'} | {'status': 'supported', 'decision': 'resolve'} |
| TC-document-missing | manifest | PASS | {'status': 'missing', 'decision': 'human_review'} | {'status': 'missing', 'decision': 'human_review'} |
| TC-document-outdated | manifest | PASS | {'status': 'outdated', 'decision': 'human_review'} | {'status': 'outdated', 'decision': 'human_review'} |
| TC-document-contradictory | manifest | PASS | {'status': 'contradictory', 'decision': 'human_review'} | {'status': 'contradictory', 'decision': 'human_review'} |
| TC-document-refuted | manifest | PASS | {'status': 'refuted', 'decision': 'human_review'} | {'status': 'refuted', 'decision': 'human_review'} |

Interpretation: Controlled functional tests of the existing rules. Passing does not establish real-world anaphora accuracy, source quality, or RQ4 reliability improvement.
AI-generated expectations require human approval and are not independent gold labels.
