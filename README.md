# User Agent Model â€” UAM Repository

This repository is the canonical workspace for UAM source control, artifact intake, active artifacts, archive lineage, registers, packets, evidence, tests, and handoffs.

## Directory roles

- /intake â€” raw supplied files, packets, donor material, and unsorted source drops. Files here are not active authority merely because they exist.
- /active â€” canonical active artifact locations after reconciliation and indexing.
- /registers â€” project state, artifact index, source authority register, decision log, conflict register, adoption/rollback register, component registry, assignment register, and evaluation register.
- /archive â€” immutable prior snapshots and displaced material.
- /evidence â€” evaluation records, verification outputs, run logs, and evidence packets.
- /packets â€” source-complete handoff and dispatch packets.
- /tests â€” test decks, fixtures, harnesses, and validation material.
- /handoffs â€” prepared prompts, transition notes, and operator handoff records.
- /scripts â€” repo maintenance and validation scripts.

## Authority rule

The repo may contain many files. Only indexed active artifacts are active authority. Intake files, packet exports, displaced copies, and archive material do not become governing merely by being present.
