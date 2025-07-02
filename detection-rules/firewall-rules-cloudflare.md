# Cloudflare Firewall Rules for qisetna.com

## 1. Introduction  
This document outlines the Cloudflare firewall rules and security policies implemented to protect qisetna.com from malicious traffic, including bots, brute force attempts, and abuse targeting WordPress endpoints.

## 2. Objectives  
- Block known malicious IPs and IP ranges identified during threat hunting  
- Limit abusive or automated access to login and registration pages  
- Mitigate DDoS and brute-force attacks  
- Challenge or block suspicious user agents and bad bots  
- Ensure legitimate traffic is minimally impacted  

## 3. Firewall Rule Categories  

### 3.1 IP Address Blocking  
- Block or challenge traffic from identified malicious IPs (e.g., `91.84.96.34`, `50.117.101.36`, `77.238.235.209`)  
- Use IP reputation and threat intelligence feeds to dynamically block high-risk addresses  
- Geo-block or challenge traffic from regions with no business relevance or high spam volume

### 3.2 Rate Limiting  
- Apply rate limits on `wp-login.php` and registration endpoints  
- Example: Max 10 login attempts per IP per 10 minutes  
- Protect REST API endpoints from abuse by limiting requests per IP

### 3.3 User Agent Blocking  
- Block or challenge requests with suspicious or known bad user agents used by spambots  
- Maintain a list of malicious user agents updated from threat intelligence sources

### 3.4 URL Path Filtering  
- Block access or present CAPTCHA challenge on sensitive paths such as:  
  - `/wp-login.php`  
  - `/wp-admin/`  
  - `/xmlrpc.php` (when XML-RPC is disabled)  
  - `/wp-register.php` or other registration URLs

### 3.5 Challenge Pages and Bot Fight Mode  
- Enable Cloudflare Bot Fight Mode to automatically challenge known bots  
- Configure challenge pages for suspicious IPs detected via behavior analytics

## 4. Example Cloudflare Firewall Rules  

| Rule Name                   | Expression                                                          | Action    | Notes                                      |
|----------------------------|---------------------------------------------------------------------|-----------|--------------------------------------------|
| Block Suspicious IPs        | `(ip.src in {91.84.96.34 50.117.101.36 77.238.235.209})`          | Block     | Directly block known malicious IPs         |
| Rate Limit Login Endpoint  | `http.request.uri.path eq "/wp-login.php"`                         | Rate Limit| Max 10 requests per 10 minutes per IP      |
| Block Bad User Agents       | `http.user_agent contains "BadBot" or http.user_agent contains "Scraper"` | Challenge | Challenge or block known bad bots          |
| Block XML-RPC Access        | `http.request.uri.path eq "/xmlrpc.php"`                           | Block     | Block when XML-RPC is disabled              |
| Challenge New Registration | `http.request.uri.path contains "/wp-register.php"`                | Challenge | Challenge or CAPTCHA for registration page |

## 5. Implementation Steps  

1. Log in to the [Cloudflare Dashboard](https://dash.cloudflare.com).  
2. Navigate to the **Firewall > Firewall Rules** section.  
3. Click **Create a Firewall Rule** and enter a descriptive name.  
4. Use the **Expression Builder** to write the conditions based on the categories above.  
5. Set the **Action** (Block, Challenge, Rate Limit) as needed.  
6. Save and deploy the rule.  
7. Monitor logs under **Firewall > Overview** to fine-tune the rules and reduce false positives.

## 6. Additional Recommendations  
- Enable **Bot Fight Mode** in the Cloudflare dashboard under **Firewall > Bots** for automatic bot mitigation.  
- Use **Rate Limiting** under **Security > Rate Limiting** for granular control over specific URLs and methods.  
- Regularly review Cloudflare Analytics and Firewall logs for new suspicious trends.  
- Integrate Cloudflare logs into SIEM tools for centralized alerting and investigation.

## 7. Summary  
Cloudflare firewall rules are a critical layer in the defense-in-depth strategy for qisetna.com. By combining IP blocking, rate limiting, user agent filtering, and challenge pages, the website remains protected against automated attacks and malicious actors, while legitimate users maintain access.

---

## References  
- [Cloudflare Firewall Rules Documentation](https://developers.cloudflare.com/firewall/cf-firewall-rules/)  
- [Cloudflare Bot Management](https://www.cloudflare.com/solutions/bot-management/)  
- [Cloudflare Rate Limiting](https://developers.cloudflare.com/rate-limiting/)  
- [WordPress Security Best Practices](https://wordpress.org/support/article/hardening-wordpress/)

