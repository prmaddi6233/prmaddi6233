<div align="center">

<img src="assets/hero.svg" width="100%" alt="Operator Dossier — Pradeep Maddi · Platform Engineer & FinOps" />

<br />

[![Portfolio](https://img.shields.io/badge/PORTFOLIO-prmaddi6233.github.io-ff8c1a?style=for-the-badge&logo=googlechrome&logoColor=white&labelColor=0a0f0a)](https://prmaddi6233.github.io)
[![LinkedIn](https://img.shields.io/badge/COMMS-LINKEDIN-7CFC00?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0a0f0a)](https://www.linkedin.com/in/pradeep-maddi)
[![Email](https://img.shields.io/badge/RADIO-EMAIL-ff8c1a?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0a0f0a)](mailto:maddipradeep201@gmail.com)

</div>

<img src="assets/h-about.svg" width="100%" alt="01 // MISSION BRIEFING" />

I run cloud platforms at organization scale and make cost, security, and reliability
**enforceable** — not aspirational. My lane is where platform engineering, FinOps, and
governance converge: guardrails that fail closed, evidence that survives an audit, and
automation that pulls humans out of the critical path.

```yaml
# // INTEL PACKET — do not distribute
operator:   Pradeep "CloudOps" Maddi
role:       Cloud Platform Engineer · FinOps
theater:    150+ account AWS Organization
specialty:  [ platform engineering, FinOps, Kubernetes at scale, governance ]
active_op:  cloud-finops-agent   # tiered, fail-closed cost validation (open source)
doctrine: >
  Cost and security recommendations rot in backlogs because nobody
  proves they are safe to apply. I build the evidence layer that does.
```

Rules of engagement:

| Rule | Why it holds the line |
|---|---|
| Policy engines over runbooks | SCPs and Kyverno *enforce*; documents get forgotten |
| Fail closed or it isn't safety | If the system can't verify, it stops — no silent pass |
| Document *why-not*, not just *how* | Rejected options are what stop repeated mistakes |
| Evidence over assertion | A claim without a check is a hope, not a control |

<img src="assets/h-impact.svg" width="100%" alt="02 // THEATER OF OPS" />

- **150+ AWS accounts** governed via Control Tower + AFT — policy-gated vending with cost attribution baked in from account zero.
- **Kubernetes at scale** — multi-tenant EKS with Karpenter, Kyverno guardrails, and per-namespace budgets so no tenant outspends its envelope.
- **Evidence-based FinOps** — surfaced **$500K+/yr** in defensible savings (RI/SP coverage, Graviton, gp2→gp3, storage lifecycle), each with a proof step before it ships.
- **Org-wide security posture** — centralized GuardDuty across ~115 member accounts on a drift-free, Terraform-managed export pipeline.
- **Fail-closed automation** — SARIF findings, OIDC-scoped access, and production canaries instead of sandbox benchmarks that lie.

<img src="assets/h-projects.svg" width="100%" alt="03 // OPERATIONS LOG" />

<table>
<tr>
<td width="50%" valign="top">

**`OP. FAIL-CLOSED` 🎯 [cloud-finops-agent](https://github.com/prmaddi6233/cloud-finops-agent)**

Tiered validation engine — math, metrics, then a production canary. SARIF findings, fail-closed, OIDC.

`Python` · `SARIF` · `GitHub Actions` · `OIDC`

[Debrief](https://github.com/prmaddi6233/cloud-finops-agent/blob/main/docs/blog-why-sandbox-benchmarks-fail.md) · [ADRs](https://github.com/prmaddi6233/cloud-finops-agent/tree/main/docs/adr)

</td>
<td width="50%" valign="top">

**`OP. GATEKEEPER` 🛰️ [aws-platform-control-plane](https://github.com/prmaddi6233/aws-platform-control-plane)**

Self-service account lifecycle — policy-gated provisioning, Step Functions, full audit trail.

`Python` · `Step Functions` · `DynamoDB`

</td>
</tr>
<tr>
<td width="50%" valign="top">

**`OP. FOUNDRY` 🏭 [aws-aft-account-factory-blueprint](https://github.com/prmaddi6233/aws-aft-account-factory-blueprint)**

Secure, cost-attributed account vending on Control Tower + AFT.

`Terraform` · `Control Tower` · `AFT`

</td>
<td width="50%" valign="top">

**`OP. WARDEN` ☸️ [eks-cost-governance-toolkit](https://github.com/prmaddi6233/eks-cost-governance-toolkit)**

Kyverno guardrails + budgeted namespaces for multi-tenant EKS.

`Kubernetes` · `Kyverno` · `Helm` · `OpenCost`

</td>
</tr>
</table>

<img src="assets/h-stack.svg" width="100%" alt="04 // LOADOUT" />

| Class | Equipped |
|---|---|
| **PRIMARY** | AWS (Organizations · Control Tower · IAM · EKS · Lambda) · Kubernetes · Terraform |
| **SECONDARY** | Python · Go · Bash · SQL · HCL |
| **TACTICAL** | Karpenter · Kyverno · Helm · ArgoCD · OpenCost · Docker |
| **LETHAL** | SCPs · OIDC · GuardDuty · Security Hub · AWS Config · SARIF |
| **PERKS** | FOCUS 1.2 · CUR 2.0 · Athena · QuickSight · Cost Explorer · Savings Plans · Graviton |
| **FIELD KIT** | Grafana · Prometheus · CloudWatch · Datadog · OpenTofu · Spacelift · GitHub Actions |

<div align="center">

<img src="https://skillicons.dev/icons?i=aws,kubernetes,terraform,docker,python,go,bash,githubactions,grafana,prometheus,linux,git&perline=12" alt="Core toolchain" />

</div>

<img src="assets/h-certs.svg" width="100%" alt="05 // DOG TAGS" />

<div align="center">

[![CKA](https://img.shields.io/badge/CKA-CERTIFIED%20KUBERNETES%20ADMIN-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white&labelColor=0a0f0a)](https://www.credly.com/badges/5150b9c4-aa9b-4946-8fc0-c2c2fa3bfbb9/linked_in_profile)
[![FinOps](https://img.shields.io/badge/FINOPS-CERTIFIED%20ENGINEER-7CFC00?style=for-the-badge&labelColor=0a0f0a)](https://verify.skilljar.com/c/kaqtuub8ax3j)
[![AWS SAA](https://img.shields.io/badge/AWS-SOLUTIONS%20ARCHITECT%20ASSOCIATE-ff8c1a?style=for-the-badge&logo=amazonwebservices&logoColor=white&labelColor=0a0f0a)](https://www.credly.com/badges/5150b9c4-aa9b-4946-8fc0-c2c2fa3bfbb9/linked_in_profile)

</div>

<img src="assets/h-writing.svg" width="100%" alt="06 // INTEL" />

| | Dispatch | Sector |
|---|---|---|
| 📡 | [Why Sandbox Benchmarks Don't Validate What They Claim](https://github.com/prmaddi6233/cloud-finops-agent/blob/main/docs/blog-why-sandbox-benchmarks-fail.md) | FinOps · Validation |
| 📐 | [The Agent Is Not the Control Plane](https://github.com/prmaddi6233/cloud-finops-agent/blob/main/docs/adr/0002-agent-is-not-the-control-plane.md) | Security · Architecture |
| 📐 | [Tiered Validation Model](https://github.com/prmaddi6233/cloud-finops-agent/blob/main/docs/adr/0003-tiered-validation-model.md) | Systems Design |

<img src="assets/h-contact.svg" width="100%" alt="07 // EXFIL" />

<div align="center">

*Accepting missions: **Principal / Senior Cloud Platform Engineering**, **AWS Architecture**, **FinOps**.*

[![LinkedIn](https://img.shields.io/badge/ESTABLISH%20COMMS-LINKEDIN-7CFC00?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0a0f0a)](https://www.linkedin.com/in/pradeep-maddi)
[![Portfolio](https://img.shields.io/badge/RECON-PORTFOLIO-ff8c1a?style=for-the-badge&logo=googlechrome&logoColor=white&labelColor=0a0f0a)](https://prmaddi6233.github.io)
[![Email](https://img.shields.io/badge/RADIO-maddipradeep201-7CFC00?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0a0f0a)](mailto:maddipradeep201@gmail.com)

<br />

<img src="assets/footer.svg" width="100%" alt="Signal out — open to Principal / Senior Cloud Platform roles · AWS · FinOps" />

</div>
