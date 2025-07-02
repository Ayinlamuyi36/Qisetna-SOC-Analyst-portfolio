# Fake User Registration Spam on qisetna.com

## 1. Overview  
Qisetna.com’s WordPress site experienced a surge in fake user registrations, primarily from disposable and spammy email domains. This compromised user data quality, increased admin workload, and posed a potential security risk.

## 2. Symptoms and Indicators  
- Sudden increase in new user signups with suspicious usernames (e.g., darwin47q6085).  
- Email addresses from known disposable or spammy domains, such as `delhinightqueen.com`, `discard.email`, and similar.  
- Registrations occurring in rapid bursts, sometimes dozens per hour.  
- User accounts with no activity after creation, indicating bot or spam registrations.

## 3. Investigation Approach  
- Enabled WP Cerber’s user registration logging to capture detailed registration events.  
- Extracted user registration logs to identify common IPs and email domains involved.  
- Cross-checked suspicious IPs using WHOIS to identify bot hosting providers.  
- Analyzed user agent strings to spot automated scripts or bot signatures.

## 4. Mitigation Actions  
- Enabled reCAPTCHA (v2 or v3) on the registration form to block automated submissions.  
- Configured WP Cerber to block registrations from disposable email domains.  
- Added Cloudflare firewall rules to challenge or block IPs with suspicious registration behavior.  
- Disabled or restricted anonymous REST API access to reduce bot entry points.  
- Set up email verification for new user registrations to ensure valid email ownership.

## 5. Ongoing Monitoring and Improvements  
- Regularly updated blocklists with new spammy domains and IPs.  
- Monitored registration logs weekly to detect new spam patterns.  
- Educated site admins on manual user review and removal of fake accounts.  
- Considered using third-party anti-spam services specialized for WordPress registrations.

## 6. Lessons Learned  
- Combining WordPress plugin settings with Cloudflare firewall rules offers strong protection.  
- CAPTCHA is a critical barrier against automated bots.  
- Continuous log analysis is necessary to adapt to evolving spam tactics.

## 7. References  
- WP Cerber Security Plugin Documentation: [https://wpcerber.com/docs/](https://wpcerber.com/docs/)  
- Cloudflare Firewall Rules: [https://developers.cloudflare.com/firewall/](https://developers.cloudflare.com/firewall/)  
- Disposable Email Domains List: [https://github.com/disposable-email-domains/disposable-email-domains](https://github.com/disposable-email-domains/disposable-email-domains)  
- WordPress User Registration Best Practices: [https://wordpress.org/support/article/user-roles-and-capabilities/](https://wordpress.org/support/article/user-roles-and-capabilities/)
