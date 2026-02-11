# Adlyna

1. **Context**
    - Client name: Adlyna
    - Project name: Adlyna
    - Date: 01-02-2025
    - People involved: Backend/API (Fahri, Sahrul,Irfan) Devops (Deddy) and Lewi (QA)
2. **Trigger**
- **What triggered the start of the Infrastructure ?**

• Client requested new infrastructure setup for Adlyna application.

- New project requires infrastructure setup (servers, database, network).
- Infrastructure setup needed for production / staging environment.
- **Who initiated it?**
    - Client Adlyna
    - Project Manager
    - Tech Lead
    - Director (Megandi)
- **Tool used:**

AWS Console, EC2, RDS Postgres, S3, CloudFront, Lambda; SSH (e.g. Termius), 	GitHub Actions, VS Code. [Adjust.]

1. **Chronological Steps (what actually happened)**

**Output produced:**

- **Action performed:**
    - VPC: vpc-0b57aba5df067ee69 (172.31.0.0/16), 3 availability zones:
- subnet-08ba88ad0199ebb25 (eu-west-3a, 172.31.0.0/20)
- subnet-0bc622320f298c2e7 (eu-west-3a, 172.31.49.0/25)
- subnet-0890cb9b09adadbf9 (eu-west-3b, 172.31.16.0/20)

**Database**

• RDS Postgres:

- adlyna-postgresql: adlyna-postgresql.ca0srojefpsr.eu-west-				         3.rds.amazonaws.com (available)

**EC2 instances:**

• Adlyna Api: i-0ccaba1c65ca2932c (t3.large)

**• Lightsail:**

- Instance: Windows_Server_2022-2 (running, blueprint 				              	     windows_server_2022, bundle xlarge_win_3_0)

- Public IP: 35.180.122.154; Private IP: 172.26.14.72; Created: 2024-12-21

- Static IPs (unattached): StaticIp-1 (15.237.20.200), StaticIp-2 (13.39.146.194)

- **Who did it:**
    - DevOps Team (Deddy)
    - Backend Developer (Sahrun, Irfan, Fahri)
    - QA (Lewi)
- **Tools:**
    - AWS Console
    - Github Actions
    - SSH (Termius)
    - VsCode
    - RDP Remote
1. **Blockers & Frictions**
- What slowed down the process?
- Lightsail Windows issues – insufficient specification capacity for Excel Application
- Resource limitations – AWS or instance-level resource limits (CPU, memory, I/O) affecting performance.
- High load on the Lightsail Windows server when app hit were running white same time
- Where did it block?
- At the Lightasil server – high CPU because Excel Application access from API
- If Windows Excel not response, can make API service down
- Why?
- Limitation Server Lightsail Specification for Windows running Excel application
1. **Founder Intervention**
- Did the Director (Megandi) intervene?
    - Yes, but only for final approval about cost usage
- When?
    - Before live apps
- For what reason?
    - Approval budget
    - Resolve blocker from client
1. **Final Deliverables**
- What was delivered to the client?

Complete production / staging infrastructure setup for [Adlyna] (AWS account 		093018225583, region eu-west-3) with the following components:

**Infrastructure components**

- AWS VPC (vpc-0b57aba5df067ee69) with 3 subnets across eu-west-3a, eu- west-3b, eu-west-3c.
- RDS Postgres: adlyna-postgresql (adlyna-postgresql.ca0srojefpsr.eu-west 3.rds.amazonaws.com).
- EC2 instances: Adlyna Api Server (i-0ccaba1c65ca2932c, t3.large)
- Lightsail: Windows_Server_2022-2 (running, windows_server_2022, xlarge_win_3_0); Public IP 35.180.122.154; Static IPs: StaticIp-1 (15.237.20.200), StaticIp-2 (13.39.146.194, unattached).
- Backup: RDS automated snapshots; EBS/AMI snapshots.

**In what format?**

- Live infrastructure on AWS (profile Adlyna, eu-west-3).
- Configuration files: GitHub repository
- --

**When?**

- Infrastructure start: February 2025
1. **Project Closure**
- What marked the end of the Infrastructure setup?

Transition to BAU (Business as Usual) – setup phase ended when the team moved from “build/deploy” to “maintain and operate”; no explicit “project closed” statement.

- Was it explicit or implicit?

Implicit. there was no formal “project closed” meeting or signed handover document; the setup was considered complete when infrastructure was live, deliverables were handed over, and the team shifted to maintenance. Director approval (cost) was the last formal milestone before go-live.