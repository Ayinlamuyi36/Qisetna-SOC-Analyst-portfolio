# Spambot IP Analysis for qisetna.com

## 1. Introduction  
This document outlines the investigation and analysis of suspicious IP addresses linked to spam and bot activity on the qisetna.com website. The goal is to identify malicious actors and implement effective IP-based mitigation.

## 2. Data Sources  
- WP Cerber user registration and login logs  
- Cloudflare firewall event logs  
- WHOIS IP lookup data  
- Public threat intelligence feeds and blocklists

## 3. IP Addresses of Concern  
Sample suspicious IPs recorded during spam registration and brute force attempts include:  
- `91.84.96.34`  
- `50.117.101.36`  
- `77.238.235.209`  

## 4. WHOIS Lookup Summary  
Performed WHOIS lookups to gather ownership and geolocation details:

| IP Address    | Organization                | Country  | Notes                            |
|---------------|-----------------------------|----------|---------------------------------|
| 91.84.96.34   | Hetzner Online GmbH          | Germany  | Common hosting provider abused for bots |
| 50.117.101.36 | Microsoft Corporation        | USA      | Possibly Azure cloud IP          |
| 77.238.235.209| OVH SAS                     | France   | Known provider for VPS hosting  |

## 5. Analysis and Insights  
- Many spambot IPs belong to large cloud providers and VPS hosts, allowing attackers to rotate IPs easily.  
- IPs are often part of large CIDR blocks, making broad subnet blocking a potential option but with risk of blocking legitimate users.  
- Use of well-known providers like Microsoft Azure or OVH suggests attackers leverage cloud resources to scale their campaigns.

## 6. Mitigation Strategy  
- Block or challenge known bad IPs and subnets in Cloudflare firewall rules.  
- Monitor and update IP blocklists dynamically via automation scripts.  
- Rate limit requests and user registrations from suspicious IP ranges.  
- Use WP Cerber plugin to block registrations and login attempts from high-risk IPs.  
- Combine IP blocking with other controls like CAPTCHA and email verification.

## 7. Automation and Continuous Monitoring  
- Maintain a script (`block-spam-ip.sh`) to sync blocklists with Cloudflare via API.  
- Configure alerts on new suspicious IP activity in SIEM dashboards.  
- Regularly review logs for emerging IP patterns and adjust firewall rules.

## 8. References  
- WHOIS Lookup Tool: [https://arin.net](https://arin.net)  
- Cloudflare Firewall Docs: [https://developers.cloudflare.com/firewall](https://developers.cloudflare.com/firewall)  
- WP Cerber Plugin: [https://wpcerber.com/docs/](https://wpcerber.com/docs/)  
- Public Blocklists: [https://github.com/firehol/blocklist-ipsets](https://github.com/firehol/blocklist-ipsets)
