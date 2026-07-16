# Pradeep Maddi

## Cloud Platform Engineer | AWS | Kubernetes | Terraform | FinOps

Cloud Platform Engineer building secure, scalable, automated, and cost-efficient AWS platforms.

[GitHub](https://github.com/prmaddi6233) | [LinkedIn](https://www.linkedin.com/in/pradeep-maddi)

Based in Calgary, Alberta, Canada.

## Professional Summary

I specialize in AWS platform engineering, Kubernetes, Infrastructure as Code,
cloud governance, security automation, and FinOps. My work focuses on building
enterprise cloud platforms that are repeatable, policy-aligned, observable, and
cost-aware from the start.

Day to day, I help operate an enterprise AWS Organization of 100+ accounts with
centralized governance, security, and cost management. My experience spans
automated account lifecycle (provisioning through decommissioning), reusable
Terraform and OpenTofu patterns, EKS operations, org-wide security baselines, and
engineering-led FinOps analytics. I am especially interested in platform
capabilities that make the secure, cost-aware path the easiest path for product
teams without slowing delivery.

## Current Focus

- Automating the full AWS account lifecycle with Account Factory for Terraform (AFT), Control Tower, and Step Functions across the organization
- Engineering-led FinOps: CUR and FOCUS data layers, CID/CUDOS dashboards, and cost analytics on Athena, QuickSight, and Grafana
- Hardening org-wide security and governance with CIS Benchmark 3.0 baselines, AWS Config, GuardDuty, and least-privilege IAM
- Reusable Terraform and OpenTofu platform modules delivered through Spacelift, GitHub Actions, and Jenkins
- Kubernetes and Amazon EKS platform reliability, workload governance, and cost optimization
- AI-assisted cloud operations (Amazon Bedrock, MCP-based agents) for cost investigation, governance, and documentation

## Core Capabilities

- AWS multi-account architecture and governance with Organizations, Control Tower, and IAM Identity Center
- Automated account lifecycle: vending, baseline customization, renaming, and decommissioning (AFT, Step Functions, CodePipeline, CodeBuild)
- Infrastructure as Code module and platform design with Terraform and OpenTofu, delivered via Spacelift and GitHub Actions
- Kubernetes platform engineering with EKS, Helm, Docker, and GitOps-oriented delivery
- Cloud security and governance automation: CIS 3.0 baselines, AWS Config, GuardDuty, least-privilege IAM, and policy-as-code
- Centralized logging, detective controls, and threat-finding pipelines into downstream SIEM
- Engineering-led FinOps: cost allocation, tagging governance, and showback enablement
- Cloud cost analytics using CUR, FOCUS, Athena, QuickSight, and Grafana
- Cost optimization through commitment strategy (Reserved Instances, Savings Plans), Graviton adoption, and non-production sprawl detection
- Platform scripting and automation with Python, Bash, and PowerShell

## Selected Engineering Outcomes

- Operate and govern an enterprise AWS Organization of 100+ accounts with
  standardized OUs, centralized logging, and policy-based guardrails.
- Automate the end-to-end account lifecycle — vending, baseline customization,
  renaming, and decommissioning — using AWS Account Factory for Terraform (AFT),
  Step Functions, and CodePipeline/CodeBuild.
- Standardize account provisioning with a ticket-keyed, allowlist-validated request
  flow and enforced naming conventions, reducing manual steps and configuration drift.
- Run organization-wide threat detection with centrally delegated Amazon GuardDuty
  across multiple regions and 100+ member accounts, exporting findings through a
  Terraform-managed pipeline into downstream SIEM.
- Enforce a CIS Benchmark 3.0 security baseline org-wide via AWS Config, with
  role-based cross-account trust and least-privilege access (no long-lived IAM users
  for automation).
- Build engineering-led FinOps analytics on AWS CUR and FOCUS data using Athena,
  QuickSight (CID/CUDOS), and Grafana for queryable cost visibility and showback.
- Drive cost optimization through commitment strategy (Reserved Instances and Savings
  Plans), Graviton adoption, storage tiering, and non-production sprawl detection.
- Design reusable Terraform and OpenTofu modules with Spacelift and GitHub Actions
  delivery — branch guardrails, remote state, and review-based promotion.

## Technology Stack

### Cloud and Platform

![AWS](https://img.shields.io/badge/AWS-232F3E?logo=amazonwebservices&logoColor=white)
![Amazon EKS](https://img.shields.io/badge/Amazon%20EKS-FF9900?logo=amazoneks&logoColor=white)

AWS Organizations, Control Tower, Account Factory for Terraform (AFT), IAM Identity Center, IAM, VPC, Step Functions, CodePipeline, CodeBuild,
GuardDuty, CloudWatch, CloudTrail, AWS Config, KMS

### Infrastructure as Code

![Terraform](https://img.shields.io/badge/Terraform-844FBA?logo=terraform&logoColor=white)
![OpenTofu](https://img.shields.io/badge/OpenTofu-FFDA18?logo=opentofu&logoColor=black)

Reusable modules, policy-aligned platform patterns, remote state, review-based infrastructure delivery

### Containers

![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?logo=kubernetes&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![Helm](https://img.shields.io/badge/Helm-0F1689?logo=helm&logoColor=white)

Amazon EKS, workload governance, deployment standards, cluster operations, cost-aware platform practices

### Delivery and Automation

![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?logo=jenkins&logoColor=white)

Spacelift, CI/CD pipelines, infrastructure promotion workflows, automation runbooks

### Observability and Governance

CloudWatch, CloudTrail, AWS Config, IAM Access Analyzer, centralized logging, policy controls, operational dashboards

### FinOps and Analytics

AWS CUR, FOCUS, Athena, QuickSight (CID/CUDOS), Grafana, cost allocation, tagging governance, showback, commitment strategy (RI/Savings Plans),
optimization workflows

### Programming and Scripting

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?logo=gnubash&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?logo=powershell&logoColor=white)

Automation, reporting, platform tooling, operational scripts

## Certifications

- Certified Kubernetes Administrator - CKA
- FinOps Certified Engineer
- AWS Certified Solutions Architect - Associate

## Featured Projects

### FinOps Analytics Platform

Problem: Cost data is hard to operationalize when billing exports, dashboards, and engineering ownership signals are disconnected.

Key technologies: AWS CUR 2.0, FOCUS, S3, Athena, QuickSight, Grafana, Terraform

Expected engineering value: Serverless cost analytics with queryable billing data, reusable views, and dashboards for engineering-led FinOps.

Repository: Coming soon - summary only; source code not published here.

### Cost Optimization Automation

Problem: Optimization recommendations need repeatable analysis, verification, and governance loops to move from reports to action.

Key technologies: Python, AWS Cost Optimization Hub, AWS APIs, Athena, Terraform

Expected engineering value: Automated cost opportunity analysis for storage, reservations, savings plans, tagging, and governance reviews.

Repository: Coming soon - summary only; source code not published here.

### AWS Account Factory and Landing Zone Automation

Problem: Multi-account AWS adoption requires standardized account vending, baseline controls, and repeatable delivery workflows.

Key technologies: AWS Control Tower, AWS Account Factory for Terraform, AWS Organizations, Terraform, CodePipeline, CodeBuild

Expected engineering value: Repeatable account provisioning with centralized platform guardrails, logging, and customization pipelines.

Repository: Coming soon - summary only; source code not published here.

### Cloud Governance Baseline

Problem: New AWS accounts need security and compliance controls applied consistently before workloads are deployed.

Key technologies: Terraform, AWS Config, CloudTrail, GuardDuty, IAM Access Analyzer, S3 Block Public Access, EBS encryption

Expected engineering value: Standardized account baselines for encryption, access analysis, detective controls, and policy-aligned governance.

Repository: Coming soon - summary only; source code not published here.

### Centralized Security Findings Pipeline

Problem: Security findings need centralized, encrypted, and reliable routing into downstream operational systems.

Key technologies: Amazon GuardDuty, S3, SQS, KMS, Terraform, SIEM integration patterns

Expected engineering value: Centralized threat finding delivery with repeatable infrastructure, encrypted storage, and operational integration.

Repository: Coming soon - summary only; source code not published here.

### AI-Assisted FinOps Operations

Problem: Cloud cost investigations are slow when engineers must manually connect Cost Explorer, CUR, pricing, and account context.

Key technologies: AWS Bedrock, MCP servers, Athena, Cost Explorer, DynamoDB, S3, Python, Terraform

Expected engineering value: Grounded natural-language cost analysis with cached answers, cited data sources, and reusable operational knowledge.

Repository: Coming soon - summary only; source code not published here.

## Engineering Principles

- Build platforms that make the secure path the easiest path.
- Prefer automation, reusable patterns, and policy-as-code over manual control gates.
- Treat cost, security, reliability, and operability as engineering requirements.
- Design cloud platforms for product team autonomy with clear guardrails.
- Keep infrastructure changes reviewable, auditable, and reproducible.
- Use AI assistance to accelerate operations while keeping human review and engineering judgment in the loop.

## GitHub Activity

GitHub repositories and contribution activity are available at [github.com/prmaddi6233](https://github.com/prmaddi6233).

## Contact

- GitHub: [github.com/prmaddi6233](https://github.com/prmaddi6233)
- LinkedIn: [linkedin.com/in/pradeep-maddi](https://www.linkedin.com/in/pradeep-maddi)
