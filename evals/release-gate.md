# Release gate — v1.1.0 (pending execution)

**Status: NOT RUN.** This checklist is an evidence record, not a statement that the model has passed evaluation.

## Fixed comparison

Baseline: v1.0.1 tag. Candidate: exact main commit selected for v1.1.0 after docs and package pipeline are merged. Use identical model/host/settings to the extent supported, fresh conversations, and the five fictional cases.

For each case and each version, store completed `run-record-template.md` records (privately when containing output not approved for publication). Record whether the assistant asked an appropriate question before supplying additional facts. **Do not volunteer the follow-up facts unless requested**; lack of a material question may itself be a role-coverage or grounding failure.

## Results

| Case | Baseline | Candidate | Reviewer |
| --- | --- | --- | --- |
| product-manager | Not run | Not run | Pending |
| engineering-lead | Not run | Not run | Pending |
| design-lead | Not run | Not run | Pending |
| ambiguous-attribution | Not run | Not run | Pending |
| limited-evidence | Not run | Not run | Pending |

## Approval requirements

- [ ] No fabricated metric, project, effect, or attribution
- [ ] No known fixable editorial problem deferred to user
- [ ] Each evaluated dimension scores at least 2 on all five cases or exceptions are explicitly reviewed and justified
- [ ] Any regression against v1.0.1 is documented and accepted by a human reviewer
- [ ] Actual packaged ZIP tested on intended platforms, or platform limitations documented
- [ ] CI structural check passes on release candidate
- [ ] Release ZIP and version-specific bilingual notes checked
- [ ] Maintainer approval to publish

**Release approval: PENDING.** Checking a workflow input alone is not sufficient evidence.
