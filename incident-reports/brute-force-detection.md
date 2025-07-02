# Brute Force Login Detection and Mitigation on qisetna.com

## 1. Overview  
Brute force attacks involve attackers attempting many username/password combinations to gain unauthorized access. Qisetna.com, running WordPress 6.8.1, has been targeted by such attacks frequently, necessitating robust detection and response strategies.

## 2. Detection Methods Used  
- **WP Cerber Security Plugin:** Configured to log failed login attempts and trigger alerts on suspicious activity.  
- **Cloudflare Firewall:** Rate limiting login endpoints to reduce automated login attempts.  
- **Live Traffic Monitoring:** Enabled in WP Cerber to analyze login traffic patterns in real time.  
- **Log Analysis:** Manually reviewed WordPress and server logs for repeated failed login IPs and suspicious user agents.

## 3. Data Collected  
- IP addresses with multiple failed login attempts (e.g., 91.84.96.34, 50.117.101.36)  
- Targeted usernames (often admin, root, or randomly generated)  
- Attempt frequency spikes during specific periods (e.g., 60+ attempts within 10 minutes)

## 4. Incident Example  
On June 25th, 2025, an IP (77.238.235.209) attempted over 100 failed logins within 1 hour targeting admin and generic usernames. WP Cerber logged these attempts and automatically blocked the IP after 5 failed attempts in 15 minutes.

## 5. Mitigation Steps  
- Added offending IPs to Cloudflare IP Access Rules to block at the network edge.  
- Configured WP Cerber for aggressive login rate limiting and CAPTCHA challenges after 3 failed attempts.  
- Disabled XML-RPC to prevent credential stuffing via this API.  
- Enforced two-factor authentication (2FA) for all administrative users.  
- Enabled Bot Fight Mode on Cloudflare to challenge suspected bots.

## 6. Lessons Learned  
- Early detection with WP Cerber’s live logging helped block attacks before damage occurred.  
- Cloudflare’s firewall rules effectively reduce attack surface.  
- 2FA is essential for admin account security.

## 7. References  
- WP Cerber Documentation: [https://wpcerber.com/docs/](https://wpcerber.com/docs/)  
- Cloudflare Rate Limiting: [https://developers.cloudflare.com/firewall/cf-rulesets/rate-limiting/](https://developers.cloudflare.com/firewall/cf-rulesets/rate-limiting/)  
- WordPress Security Best Practices: [https://wordpress.org/support/article/hardening-wordpress/](https://wordpress.org/support/article/hardening-wordpress/)
