# OMR Evidence Capture Protocol v0.1

Status: active shared procedure
Applies to: future Agent Builder / OMR pilots, eval suites, reruns, architecture comparisons, and corrected evidence packages
Evidence ceiling of this protocol: design-time procedural standard until validated by a future run

## Purpose

This protocol makes evidence capture a first-class package requirement. A run can be behaviorally correct and still fail validation when required selector, packet, state, context, or scoring artifacts are missing.

It does not relabel, repair, or pool prior flawed evidence. Flawed evidence versions remain closed with their limitations. Corrected packages must receive new versions and report old and new results separately.

## Required Evidence Artifacts

Every future OMR or comparable Agent Builder evaluation run must retain these artifacts as auditable records:

- exact selector record for every attempted transition;
- rejected-selection log for every illegal, stale, contaminated, or out-of-order attempted transition;
- exact ExecutionPacket manifest for every operator or legacy-equivalent execution;
- exact operator input packet, including permitted and forbidden reads;
- O2 packet contents and O2 packet hash;
- forbidden-input record for O2 or any equivalent independence-critical step;
- full state snapshot for every governed state object;
- object ID, object kind, schema version, revision, branch, parent refs, content hash, freshness, status, producer, evidence refs, conflict refs, and projection for every state object;
- invalid, stale, superseded, contested, or rejected objects retained as records, not overwritten;
- raw prompts, raw outputs, manual interventions, repairs, token/latency/handoff metrics when available, and first-pass failure records.

For OMR, the governed state objects are exactly `GoalContract`, `CapabilityModel`, `EvidenceLedger`, `CoverageMap`, and `ChangeDecision`. The metadata envelope is embedded in those objects and is not a sixth state object.

## State and Packet Capture

Every required state object must be reconstructable without conversation history. A downstream object is valid only when it cites exact parent refs by object ID, revision, branch, and content hash.

An ExecutionPacket manifest must include:

- run ID, row ID, case ID, variant ID, replicate ID, source profile, model/provider/config when available, timestamp, and evidence stage;
- operator or legacy-equivalent target;
- context condition label and actual context ID;
- selector decision and selector record ID;
- input object refs and snapshot hashes;
- ledger projection metadata;
- permitted reads and forbidden reads;
- expected schema or output contract;
- packet content hash.

Referenced-subset EvidenceLedger projections remain auditable only when they retain stable ledger ID, ledger revision, projection digest, included entry IDs, omitted count, append-delta rule, and the rule forbidding inference from omitted entries.

Validation must fail when a conclusion is correct but required state or packet artifacts are missing.

## Selector Capture

Every transition must produce a selector record with:

- prior state refs and freshness;
- attempted operator or legacy-equivalent step;
- eligibility rule evaluated;
- accepted/rejected outcome;
- rejection code when rejected;
- selected next step;
- reason basis;
- record hash.

Rejected selections are evidence. They must remain in the run archive and must not be rewritten into successful transitions.

## Independence and Context Labels

`separate-context` may be used only when the execution context is actually isolated from prior asset exposure. The row must record context ID or equivalent isolation proof, isolation method, contamination checks, and the limitation note.

Parent-thread or same-conversation execution must be labeled `parent-thread-single-context` or `packet-boundary`, not `separate-context`.

Every run row must record intended context condition, actual context condition, context ID(s), isolation method, asset-exposure status, and limitation note.

Packet-boundary, parent-thread-single-context, and true separate-context results must be stratified. They must never be pooled unless the manifest explicitly marks the pooled result non-comparable and excludes isolation credit.

## O2 Independence Requirements

Material O2 or equivalent capability derivation packets must prohibit asset text, asset decomposition, component names, section labels, coverage judgments, and proposed edits unless the case is explicitly testing contamination handling.

O2 evidence must include:

- exact input GoalContract snapshot;
- exact O2 packet content and hash;
- forbidden input list;
- forbidden-input inspection record;
- CapabilityModel snapshot;
- bidirectional GoalContract to CapabilityModel trace;
- derivation boundary with context label and asset exposure status.

If an O2 trace is narrative prose without packet and state artifacts, validation fails.

## Compact Trace Minimums

Compact variants must preserve the minimum fields required to reconstruct the governed decision:

- requiredness class and basis;
- bidirectional obligation/capability trace;
- capability refs;
- evidence ceiling;
- parent object refs and hashes;
- branch/conflict state;
- coverage/gap refs when applicable;
- impact readiness and reach basis when applicable;
- terminal decision and stop basis.

Compact output cannot pass trace completeness if it is behaviorally correct but not reconstructable.

## Scoring Observability

All future scorecards must separate these dimensions:

- behavior correctness;
- trace completeness;
- state/packet completeness;
- isolation validity;
- evidence ceiling compliance;
- burden/compactness;
- terminal decision correctness;
- evaluator confidence;
- limitations.

Executor terminal decisions are raw outputs. They are not pass/fail labels, evaluator scores, architecture verdicts, or promotion evidence.

## Versioning and Archive Rules

Flawed evidence must be closed with limitations, not retroactively relabeled.

Corrected packages receive a new version. Results from flawed and corrected packages are reported separately. Cross-version results must not be pooled unless a manifest explicitly stratifies them and marks the pooled view non-comparable for claims affected by the defect.

Sealed old evidence may be referenced as a limitation source, but not repaired in place.

## Validation Gates

Package validation must fail if:

- required selector, state, packet, O2, or ledger-projection artifacts are missing;
- `separate-context` is claimed without isolation proof;
- parent-thread or same-conversation runs are credited as separate-context;
- compact traces omit required reconstruction fields;
- scorecards collapse behavior pass and evidence completeness into one score;
- executor raw decisions are treated as pass/fail labels;
- old evidence is relabeled, repaired, or pooled into new package results;
- invalid, stale, superseded, contested, or rejected objects are overwritten instead of retained.

## Migration Requirement

Future eval packages must reference this protocol by path and version, include a package-local capture addendum only for case-specific rules, and include a manifest entry proving the protocol file hash used at freeze time.
