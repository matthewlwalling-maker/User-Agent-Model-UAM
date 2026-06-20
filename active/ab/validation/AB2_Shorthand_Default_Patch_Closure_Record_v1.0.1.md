# AB2 Shorthand Default Patch Closure Record

**Patch:** Agent Builder PM Framework v1.0.1  
**Date:** 2026-06-18  
**Evidence stage:** `.design-time` / deterministic parser regression  
**Decision:** Fixed

## Defect

`07_Agent_Builder_Deployment_Quickstart_v1.0.md` showed:

```text
AB2.adversarial.test the router
-> AB2.adversarial.behavior.test the router.design-time.retest
```

That conflicted with `01_Agent_Builder_Core_Router_v1.0.md` section 4, which owns default resolution and states that an omitted action defaults to `.assess-only`.

## Correction

The Quickstart example now resolves to:

```text
AB2.adversarial.test the router
-> AB2.adversarial.behavior.test the router.design-time.assess-only
```

Actual test execution remains explicit:

```text
AB2.adversarial.test the router.simulated.retest
```

## Boundary Preservation

No PM schema change was made. No AB2-specific `.retest` default was introduced. Skill names, Skill boundaries, E1-E12 scoring, automatic chaining policy, and experimental O1-O4 status remain unchanged.

## Regression Results

| Case | Expected | Result |
|---|---|---|
| `AB2.adversarial.test the router` | `AB2.adversarial.behavior.test the router.design-time.assess-only` | PASS |
| `AB2.adversarial.test the router.simulated.retest` | Valid; maps to `adversarial-evaluation` | PASS |
| `AB2.adversarial.test the router.retest` | Reject V4, missing evidence before explicit action | PASS |
| Other AB shorthand defaults | Unchanged (`mode=holistic`, mode default lens, `design-time`, `assess-only`) | PASS |
| `+open-architecture` compatibility | Unchanged; valid only with registered generative actions | PASS |

## Status

E001 is closed in v1.0.1. Historical v1.0 records are preserved and superseded by this closure record.
