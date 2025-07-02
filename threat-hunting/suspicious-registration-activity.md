# Suspicious Registration Activity on qisetna.com

## 1. Overview  
This document analyzes patterns and indicators of suspicious or automated user registrations observed on the qisetna.com WordPress site. It covers techniques used by spambots, detection methods, and mitigation strategies.

## 2. Indicators of Suspicious Registrations

### Common Signs:
- Use of disposable or temporary email domains (e.g., `@discard.email`, `@delhinightqueen.com`)  
- Rapid bursts of multiple registrations from the same IP or IP range  
- Usernames with random or nonsensical character strings (e.g., `darwin47q6085`)  
- Registrations occurring at unusual times or in patterns suggesting automation

### Sample Data Extracted:  
| Username        | Email                          | Registration Time       | IP Address     | Notes                 |
|-----------------|--------------------------------|------------------------|----------------|-----------------------|
| darwin47q6085   | margerymccullers@discard.email | 2025-06-26 20:39 BST   | 91.84.96.34    | Disposable email used |
| tammara-skeyhill27 | tammara-skeyhill27@delhinightqueen.com | 2025-06-25 14:10 BST | 50.117.101.36  | Spam domain email     |
| joel_vanish33   | joel_vanish33@5091.delhinightqueen.com | 2025-06-25 14:12 BST | 77.238.235.209 | Spam domain email     |

## 3. Data Collection & Monitoring  
- Logs collected from WordPress registration hooks and WP Cerber live traffic  
- Cloudflare firewall logs for suspicious IPs hitting registration endpoints  
- Email patterns identified through DNS SPF/DKIM failure reports and bounce notifications

## 4. Detection Techniques  
- Email domain blacklist using known disposable and spammy providers  
- IP reputation lookups using WHOIS and threat intelligence feeds  
- User-Agent filtering on registration form submissions  
- Rate limiting and CAPTCHA enforcement on registration page  

## 5. Mitigation Measures Implemented  
- Blocklisted high-risk IP addresses at Cloudflare and WP Cerber  
- Disabled XML-RPC to reduce automated bot attacks  
- Enabled CAPTCHA and limited registration attempts per IP  
- Configured WP Cerber to deny registrations from disposable email domains  
- Set up email verification before account activation  

## 6. Recommendations for Ongoing Protection  
- Regularly update disposable email domain blacklists  
- Monitor registration traffic spikes and unusual patterns  
- Integrate third-party anti-spam services like Akismet or reCAPTCHA v3  
- Review and tighten firewall rules on the registration URL  
- Consider temporary manual approval for new accounts if attacks escalate

## 7. Summary  
Suspicious registrations on qisetna.com are primarily driven by spambots using disposable email addresses and botnets originating from specific IP ranges. Combining multi-layered detection and mitigation strategies significantly reduces spam user registrations and protects site integrity.

---

## References  
- Disposable Email Domains: https://github.com/disposable-email-domains  
- WP Cerber Anti-Spam: https://wpcerber.com/docs/anti-spam/  
- Cloudflare Firewall Rules: https://developers.cloudflare.com/firewall/cf-firewall-rules/  
- WordPress Registration Hooks: https://developer.wordpress.org/reference/hooks/user_register/
