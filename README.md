<div align="center">

<img src="assets/hero.svg" width="100%" alt="Pradeep Maddi — the control plane at the centre of a cloud platform topology" />

<br />

[![Portfolio](https://img.shields.io/badge/Portfolio-prmaddi6233.github.io-22d3ee?style=for-the-badge&logo=googlechrome&logoColor=white&labelColor=0a0e1a)](https://prmaddi6233.github.io)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-a78bfa?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0a0e1a)](https://www.linkedin.com/in/pradeep-maddi)
[![Email](https://img.shields.io/badge/Email-Say%20hello-2dd4bf?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0a0e1a)](mailto:maddipradeep201@gmail.com)

</div>

<img src="assets/h-about.svg" width="100%" alt="01 · WHOAMI" />

I run cloud platforms at organization scale and make cost, security, and reliability
**enforceable** — not aspirational. My work sits where platform engineering, FinOps,
and governance meet: guardrails that fail closed, evidence that survives an audit, and
automation that takes humans out of the critical path.

<div align="center">

<img src="assets/manifest.svg" width="100%" alt="Operator manifest — role: Cloud Platform Engineer & FinOps · org: 150+ account AWS Organization · building cloud-finops-agent · thesis: I build the evidence layer that proves cost & security changes are safe to apply" />

</div>

Principles I build by:

| Principle | Why it holds |
|---|---|
| Policy engines over runbooks | SCPs and Kyverno *enforce*; documents get forgotten |
| Fail closed or it isn't safety | If the system can't verify, it stops — no silent pass |
| Document *why-not*, not just *how* | Rejected options are what stop repeated mistakes |
| Evidence over assertion | A claim without a check is a hope, not a control |

<img src="assets/h-impact.svg" width="100%" alt="02 · SCOPE & IMPACT" />

- **150+ AWS accounts** governed through Control Tower + AFT — policy-gated vending with cost attribution baked in from account zero.
- **Kubernetes at scale** — multi-tenant EKS with Karpenter, Kyverno guardrails, and per-namespace budgets so no tenant outspends its envelope.
- **Evidence-based FinOps** — surfaced **$500K+/yr** in defensible savings (RI/SP coverage, Graviton, gp2→gp3, storage lifecycle), each with a proof step before it ships.
- **Org-wide security posture** — own the preventive→detective→audit stack: SCPs and IAM/OIDC guardrails, centralized GuardDuty + Security Hub + AWS Config across ~115 accounts, KMS/encryption and WAF baselines — all Terraform-managed and drift-free.
- **Fail-closed automation** — SARIF findings, OIDC-scoped access, and production canaries instead of sandbox benchmarks that lie.

<img src="assets/h-projects.svg" width="100%" alt="03 · SELECTED WORK" />

<table>
<tr>
<td width="50%" valign="top">

**🛰️ [cloud-finops-agent](https://github.com/prmaddi6233/cloud-finops-agent)**

Tiered validation engine — math, metrics, then a production canary. SARIF findings, fail-closed, OIDC.

`Python` · `SARIF` · `GitHub Actions` · `OIDC`

[Blog](https://github.com/prmaddi6233/cloud-finops-agent/blob/main/docs/blog-why-sandbox-benchmarks-fail.md) · [ADRs](https://github.com/prmaddi6233/cloud-finops-agent/tree/main/docs/adr)

</td>
<td width="50%" valign="top">

**☁️ [aws-platform-control-plane](https://github.com/prmaddi6233/aws-platform-control-plane)**

Self-service account lifecycle — policy-gated provisioning, Step Functions, full audit trail.

`Python` · `Step Functions` · `DynamoDB`

</td>
</tr>
<tr>
<td width="50%" valign="top">

**🏭 [aws-aft-account-factory-blueprint](https://github.com/prmaddi6233/aws-aft-account-factory-blueprint)**

Secure, cost-attributed account vending on Control Tower + AFT.

`Terraform` · `Control Tower` · `AFT`

</td>
<td width="50%" valign="top">

**☸️ [eks-cost-governance-toolkit](https://github.com/prmaddi6233/eks-cost-governance-toolkit)**

Kyverno guardrails + budgeted namespaces for multi-tenant EKS.

`Kubernetes` · `Kyverno` · `Helm` · `OpenCost`

</td>
</tr>
</table>

<img src="assets/h-stack.svg" width="100%" alt="04 · TECH STACK" />

| Domain | Tools |
|---|---|
| **Cloud** | AWS (Organizations · Control Tower · IAM · EKS · Lambda) · Azure · GCP |
| **Containers** | Kubernetes · EKS · Karpenter · Kyverno · Helm · ArgoCD · OpenCost |
| **IaC** | Terraform · OpenTofu · Terragrunt · CloudFormation · Spacelift · Ansible |
| **CI/CD** | GitHub Actions · CodePipeline · Step Functions · EventBridge |
| **FinOps** | FOCUS 1.2 · CUR 2.0 · Athena · QuickSight · Cost Explorer · Savings Plans · Graviton |
| **Security** | SCPs · IAM · OIDC · GuardDuty · Security Hub · AWS Config · KMS · WAF · SARIF |
| **Observability** | Grafana · Prometheus · CloudWatch · Datadog |
| **Languages** | Python · Bash · Go · SQL · HCL |

<div align="center">

<img src="https://skillicons.dev/icons?i=aws,kubernetes,terraform,docker,python,go,bash,githubactions,grafana,prometheus,linux,git&perline=12" alt="Core toolchain" />

</div>

<img src="assets/h-certs.svg" width="100%" alt="05 · CREDENTIALS" />

<div align="center">

[![CKA](https://img.shields.io/badge/CKA-Certified%20Kubernetes%20Administrator-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white&labelColor=0a0e1a)](https://www.credly.com/badges/5150b9c4-aa9b-4946-8fc0-c2c2fa3bfbb9/linked_in_profile)
[![FinOps](https://img.shields.io/badge/FinOps-Certified%20Engineer-2dd4bf?style=for-the-badge&labelColor=0a0e1a)](https://verify.skilljar.com/c/kaqtuub8ax3j)
[![AWS SAA](https://img.shields.io/badge/AWS-Solutions%20Architect%20Associate-ff9900?style=for-the-badge&logo=amazonwebservices&logoColor=white&labelColor=0a0e1a)](https://www.credly.com/badges/5150b9c4-aa9b-4946-8fc0-c2c2fa3bfbb9/linked_in_profile)

</div>

<img src="assets/h-writing.svg" width="100%" alt="06 · FIELD NOTES" />

| | Piece | Theme |
|---|---|---|
| 📡 | [Why Sandbox Benchmarks Don't Validate What They Claim](https://github.com/prmaddi6233/cloud-finops-agent/blob/main/docs/blog-why-sandbox-benchmarks-fail.md) | FinOps · Validation |
| 📐 | [The Agent Is Not the Control Plane](https://github.com/prmaddi6233/cloud-finops-agent/blob/main/docs/adr/0002-agent-is-not-the-control-plane.md) | Security · Architecture |
| 📐 | [Tiered Validation Model](https://github.com/prmaddi6233/cloud-finops-agent/blob/main/docs/adr/0003-tiered-validation-model.md) | Systems Design |

<img src="assets/h-contact.svg" width="100%" alt="07 · ESTABLISH LINK" />

<div align="center">

*Open to **Principal / Senior Cloud Platform Engineering**, **AWS Architecture**, and **FinOps** roles.*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Let's%20connect-a78bfa?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0a0e1a)](https://www.linkedin.com/in/pradeep-maddi)
[![Portfolio](https://img.shields.io/badge/Portfolio-prmaddi6233.github.io-22d3ee?style=for-the-badge&logo=googlechrome&logoColor=white&labelColor=0a0e1a)](https://prmaddi6233.github.io)
[![Email](https://img.shields.io/badge/Email-maddipradeep201-2dd4bf?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0a0e1a)](mailto:maddipradeep201@gmail.com)

<br />

<img src="assets/footer.svg" width="100%" alt="Open to Principal / Senior Cloud Platform Engineering · AWS · FinOps" />

</div>
