<h1 align="center">Pradeep Maddi</h1>
<p align="center"><b>Cloud Platform Engineering · FinOps</b><br>
Secure, cost-aware AWS platforms at 100+ account scale</p>

<p align="center">
  <a href="https://www.linkedin.com/in/pradeep-maddi"><img src="https://img.shields.io/badge/LinkedIn-in%2Fpradeep--maddi-0A66C2?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
</p>

**The problem I work on:** cloud cost recommendations rot in backlogs because nobody proves they're safe. The interesting work is the evidence layer — deterministic checks where math suffices, production metrics where it doesn't, and canary validation with automated rollback where it matters.

## Selected Work

| Project | What it shows |
|---------|---------------|
| **[cloud-finops-agent](https://github.com/prmaddi6233/cloud-finops-agent)** — flagship | Tiered validation (deterministic → statistical → production canary with SLO-gated rollback), SARIF findings in GitHub Code Scanning, fail-closed safety model. Start with the ADRs: [no sandbox benchmarks](https://github.com/prmaddi6233/cloud-finops-agent/blob/main/docs/adr/0001-why-we-dont-sandbox-benchmark.md) · [agent ≠ control plane](https://github.com/prmaddi6233/cloud-finops-agent/blob/main/docs/adr/0002-agent-is-not-the-control-plane.md) · [tiered validation](https://github.com/prmaddi6233/cloud-finops-agent/blob/main/docs/adr/0003-tiered-validation-model.md) |
| [aws-platform-control-plane](https://github.com/prmaddi6233/aws-platform-control-plane) | Policy-gated account lifecycle — Step Functions orchestration, least-privilege IAM, deterministic audit trail |
| [eks-cost-governance-toolkit](https://github.com/prmaddi6233/eks-cost-governance-toolkit) | Multi-tenant EKS guardrails — Kyverno policy-as-code, budgeted namespaces, OpenCost |

More: [AFT account vending blueprint](https://github.com/prmaddi6233/aws-aft-account-factory-blueprint) · [EKS optimization patterns](https://github.com/prmaddi6233/eks-cost-optimization)

## How I Work

- Decisions get written down — "why not X" beats "how to X"
- Guardrails live in config and policy engines, not runbooks
- A safety claim that can't fail closed isn't a safety claim

<p align="center">
  <img src="https://skillicons.dev/icons?i=aws,kubernetes,terraform,py,bash,githubactions,grafana" alt="AWS, Kubernetes, Terraform, Python, Bash, GitHub Actions, Grafana" />
</p>

<p align="center">CKA · FinOps Certified Engineer · AWS Solutions Architect</p>
