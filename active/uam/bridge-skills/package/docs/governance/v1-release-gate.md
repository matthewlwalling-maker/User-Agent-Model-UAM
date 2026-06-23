# v1 Release Gate

Version: `0.1.0`  
Current decision: `blocked_until_gates_pass`

## Non-Negotiable Gates

v1 must not be released until all gates below have evidence at the required stage.

| Gate | Required Evidence | Blocking Failures |
|---|---|---|
| Routing | simulated or stronger | wrong primary command on material cases; broad implicit false positives |
| Object integrity | simulated or stronger | review mutates artifacts; handoff rewrites artifacts; compare silently merges |
| Evidence ceiling | simulated or stronger | design-time outputs claim runtime, parity, readiness, or production evidence |
| Degradation | simulated or stronger | adapter claims missing capabilities or hides fallback limits |
| Overactivation | simulated or stronger | simple reversible tasks trigger heavy process |
| Blind value proposition | simulated blind comparative or stronger | target fails to beat or tie baseline on behavioral utility; evaluator is not blind; hard-fail boundary or evidence violation |
| Cross-model parity | simulated across target providers | same command changes ownership, writes, or claim ceiling |

## Readiness Decisions

- `Green`: all required gates verified at the required stage; no critical failures.
- `Yellow`: explicit-command pilot may proceed with named limitations.
- `Red`: material gate failed; do not deploy.
- `Blocked`: required evidence, adapter, or dependency is unavailable.

## Current v0.1 Decision

`Yellow for source skeleton only`: the package may be reviewed and expanded as a source artifact. It is not approved for global installation, broad implicit routing, or v1 deployment.

## Evidence Upgrade Needed

- Run eval cases and preserve raw prompts, outputs, scoring, and environment notes.
- Run blind comparative value-proposition cases with separated suite designer, runner, evaluator, and anonymized outputs.
- Verify provider capability profiles against current official docs before adapter release.
- Test Codex adapter before any other provider priority claim.
- Record known limitations and rollback path before pilot activation.
