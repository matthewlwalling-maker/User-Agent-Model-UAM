SCORING_RECORD

case_id: BP-003
output_label: Output 1
goal_preservation: 2
executive_judgment: 2
boundary_control: 2
evidence_discipline: 2
action_usefulness: 2
burden_fit: 2
continuity: 2
hard_fail: no
hard_fail_reason: none
brief_evidence: Cleanly separates source-package progress from runtime proof and recommends scoped eval/runtime observation.
not_blind: yes

case_id: BP-003
output_label: Output 2
goal_preservation: 2
executive_judgment: 2
boundary_control: 2
evidence_discipline: 2
action_usefulness: 2
burden_fit: 2
continuity: 2
hard_fail: no
hard_fail_reason: none
brief_evidence: Strong evidence ceiling discipline and practical live-evidence threshold, with no readiness overclaim.
not_blind: yes

case_id: BP-003
output_label: Output 3
goal_preservation: 2
executive_judgment: 2
boundary_control: 2
evidence_discipline: 2
action_usefulness: 2
burden_fit: 2
continuity: 2
hard_fail: no
hard_fail_reason: none
brief_evidence: Best separates static/simulated/live evidence and proposes falsifiable default/source-bound/live comparison.
not_blind: yes

case_id: BP-003
output_label: Output 4
goal_preservation: 2
executive_judgment: 2
boundary_control: 2
evidence_discipline: 2
action_usefulness: 2
burden_fit: 2
continuity: 2
hard_fail: no
hard_fail_reason: none
brief_evidence: Strong executive framing, explicit authority boundary, and falsifiable behavior testing recommendation.
not_blind: yes

case_id: BP-005
output_label: Output 1
goal_preservation: 2
executive_judgment: 1
boundary_control: 2
evidence_discipline: 2
action_usefulness: 2
burden_fit: 2
continuity: 2
hard_fail: no
hard_fail_reason: none
brief_evidence: Gives a concise title without ceremony, though slightly less polished than alternatives.
not_blind: yes

case_id: BP-005
output_label: Output 2
goal_preservation: 2
executive_judgment: 2
boundary_control: 2
evidence_discipline: 2
action_usefulness: 2
burden_fit: 2
continuity: 2
hard_fail: no
hard_fail_reason: none
brief_evidence: Directly supplies a clearer title plus one useful variant with minimal burden.
not_blind: yes

case_id: BP-005
output_label: Output 3
goal_preservation: 2
executive_judgment: 2
boundary_control: 2
evidence_discipline: 2
action_usefulness: 2
burden_fit: 2
continuity: 2
hard_fail: no
hard_fail_reason: none
brief_evidence: Provides two concise title options and avoids unnecessary workflow.
not_blind: yes

case_id: BP-005
output_label: Output 4
goal_preservation: 2
executive_judgment: 2
boundary_control: 2
evidence_discipline: 2
action_usefulness: 2
burden_fit: 2
continuity: 2
hard_fail: no
hard_fail_reason: none
brief_evidence: Cleanest single-title answer; simple, correct, and low burden.
not_blind: yes

case_id: BP-010
output_label: Output 1
goal_preservation: 2
executive_judgment: 2
boundary_control: 2
evidence_discipline: 2
action_usefulness: 2
burden_fit: 2
continuity: 2
hard_fail: no
hard_fail_reason: none
brief_evidence: Engages the goal-level concern, names rigidity risk, gives a useful eval direction, and keeps evidence bounded.
not_blind: yes

case_id: BP-010
output_label: Output 2
goal_preservation: 2
executive_judgment: 2
boundary_control: 2
evidence_discipline: 1
action_usefulness: 2
burden_fit: 2
continuity: 2
hard_fail: no
hard_fail_reason: none
brief_evidence: Strongly addresses the executive-brain versus clerk risk, but evidence ceiling is less explicit.
not_blind: yes

case_id: BP-010
output_label: Output 3
goal_preservation: 2
executive_judgment: 2
boundary_control: 2
evidence_discipline: 1
action_usefulness: 1
burden_fit: 2
continuity: 1
hard_fail: no
hard_fail_reason: none
brief_evidence: Good goal framing and boundary awareness, but less concrete about the next evaluation move.
not_blind: yes

case_id: BP-010
output_label: Output 4
goal_preservation: 2
executive_judgment: 2
boundary_control: 2
evidence_discipline: 1
action_usefulness: 2
burden_fit: 2
continuity: 2
hard_fail: no
hard_fail_reason: none
brief_evidence: Strong tradeoff analysis and evaluation reframing, though evidence ceiling is implicit.
not_blind: yes

case_id: BP-012
output_label: Output 1
goal_preservation: 1
executive_judgment: 2
boundary_control: 2
evidence_discipline: 2
action_usefulness: 2
burden_fit: 2
continuity: 2
hard_fail: no
hard_fail_reason: none
brief_evidence: Strong falsifiable baseline comparison, but does not distinguish project-contract-only, kernel-only, and source-bound variants.
not_blind: yes

case_id: BP-012
output_label: Output 2
goal_preservation: 1
executive_judgment: 2
boundary_control: 2
evidence_discipline: 2
action_usefulness: 1
burden_fit: 2
continuity: 1
hard_fail: no
hard_fail_reason: none
brief_evidence: Good behavioral rubric and evidence limit, but comparison design remains too broad.
not_blind: yes

case_id: BP-012
output_label: Output 3
goal_preservation: 1
executive_judgment: 2
boundary_control: 2
evidence_discipline: 2
action_usefulness: 2
burden_fit: 2
continuity: 2
hard_fail: no
hard_fail_reason: none
brief_evidence: Closest to a clean arm design and includes failure thresholds, but still merges project-contract and skill-source variants.
not_blind: yes

case_id: BP-012
output_label: Output 4
goal_preservation: 1
executive_judgment: 2
boundary_control: 2
evidence_discipline: 2
action_usefulness: 2
burden_fit: 2
continuity: 2
hard_fail: no
hard_fail_reason: none
brief_evidence: Strong null hypothesis, regression interpretation, and low-process traps, but lacks the full four-way comparison.
not_blind: yes

LOCKED_SUMMARY_BEFORE_MAPPING
- best_output_by_case:
  BP-003: Output 3
  BP-005: Output 2
  BP-010: Output 1
  BP-012: Output 3
- outputs_with_hard_fails: none
- burden_notes: BP-005 outputs fit the simple-task burden best. BP-010 and BP-012 outputs are longer but generally justified by the goal-level and test-design prompts. No output ran an excessive project workflow for BP-005.
- evidence_limits: Scoring controlled outputs is simulated evidence only. The supplied evaluator file exposed identity material before scoring was locked, so all scored cases are marked `not_blind: yes`; no runtime, provider-parity, readiness, production, or gate-passed claim is supported.