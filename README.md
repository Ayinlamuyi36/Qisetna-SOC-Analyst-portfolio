<<<<<<< HEAD
# 🛡️ Qisetna SOC Analyst Portfolio

### 🔍 Objective
This portfolio showcases my work in proactively securing **qisetna.com**, including:
- Incident analysis
- Plugin and firewall configuration
- Bot mitigation
- Email authentication setup

---

## 📁 Repository Structure

```
qisetna-soc-portfolio/
├── README.md
├── incident-reports/
│   ├── brute-force-detection.md
│   ├── xmlrpc-exploit-attempt.md
│   └── fake-user-registration-spam.md
├── threat-hunting/
│   ├── suspicious-registration-activity.md
│   ├── spambot-ip-analysis.md
│   └── user-agent-filters.md
├── detection-rules/
│   ├── firewall-rules-cloudflare.md
│   ├── wp-cerber-config.md
│   ├── SIEM-alerting-kibana.md
│   └── xmlrpc-blocking-strategy.md
├── email-hardening/
│   ├── spf-dkim-dmarc-records.md
│   ├── smtp-lockdown.md
│   └── wp-mail-smtp-setup.md
├── automation-scripts/
│   ├── block-spam-ip.sh
│   ├── backup-alert-script.py
│   └── email-log-monitor.py
└── assets/
    └── screenshots-and-diagrams.png

    
### 🔐 Key Technologies Used
- **Cloudflare**: DNS, WAF rules, bot protection, rate limiting
- **WordPress**: Core hardening (v6.8.1), plugin management
- **WP Cerber Security**: Anti-spam, brute force blocking, IP control
- **WP Mail SMTP + Gmail API**: Secure transactional email delivery
- **Linux Tools**: WHOIS, Dig, Curl, IPTables, Fail2Ban
- **SIEM Stack**: Simulated ELK (Elasticsearch, Logstash, Kibana) for event logging

## 📌 Highlights

### 1. 🔎 Threat Detection & Hunting
**Folder:** `threat-hunting/`
- `suspicious-registration-activity.md`: Logs of fake or disposable email attempts
- `spambot-ip-analysis.md`: WHOIS investigation of high-risk IPs
- `user-agent-filters.md`: Blocklists for malicious bots and scrapers

### 2. 📤 Email Security & Hardening
**Folder:** `email-hardening/`
- `spf-dkim-dmarc-records.md`: Setup for SPF, DKIM, DMARC to stop spoofing
- `smtp-lockdown.md`: Restricting unauthorized email relay
- `wp-mail-smtp-setup.md`: Gmail OAuth config and fix for SMTP errors

### 3. 🔐 WordPress Security Configuration
**Folder:** `detection-rules/`
- `wp-cerber-config.md`: CAPTCHA, rate limits, and login restrictions
- `xmlrpc-blocking-strategy.md`: Strategies to stop XML-RPC abuse
- `SIEM-alerting-kibana.md`: Sample alert rules for WordPress logs

### 4. 🌐 Cloudflare Firewall & DNS
- `firewall-rules-cloudflare.md`: Blocking bad bots, IPs, and API abuse
- Includes rate limiting, Bot Fight Mode, and challenge pages

### 5. ⚙️ Automation & Scripting
**Folder:** `automation-scripts/`
- `block-spam-ip.sh`: Cloudflare API IP block script
- `email-log-monitor.py`: Monitor failed email deliveries
- `backup-alert-script.py`: Alerts when backups fail

### 6. 🔔 Incident Reports
**Folder:** `incident-reports/`
- `brute-force-detection.md`: Failed login trends and IP actions
- `xmlrpc-exploit-attempt.md`: Log of XML-RPC abuse and mitigations
- `fake-user-registration-spam.md`: Analysis of spam registrations

## Appendix

For detailed raw logs and examples of attack patterns, see the [Appendix folder](appendix/).

- [Example Attack Log 1 - Brute Force](appendix/example-attack-log-1.md)
- [Example Attack Log 2 - XML-RPC Exploit](appendix/example-attack-log-2.md)

=======
# Qisetna-SOC-Analyst-portfolio
A GitHub portfolio documenting my SOC Analyst work for Qisetna
>>>>>>> 256287f1cc991c991ee384c621432fa9b5523943
