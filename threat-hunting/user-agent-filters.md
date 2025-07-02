# User-Agent Filters for Bot Mitigation on qisetna.com

## 1. Overview  
User-Agent (UA) strings sent by HTTP clients identify the browser, device, or bot making the request. Malicious bots often use distinctive or fake UA strings which can be filtered to reduce spam, scraping, and abuse.

## 2. Why Filter User-Agents?  
- Block known bad bots from crawling registration and login pages.  
- Reduce spam registrations and brute-force attacks.  
- Prevent content scraping and data theft.  
- Complement IP-based blocking with another layer of defense.

## 3. Common Malicious User-Agent Patterns  
Some example suspicious or spammy User-Agent strings identified from qisetna.com logs:

- `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/88.0.4324.96 Safari/537.36`  
- `curl/7.64.1`  
- `Python-urllib/3.7`  
- `Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)` (when spoofed)  
- `Bot/1.0 (+http://www.examplebot.com)`  

## 4. Creating User-Agent Blocklists  

### Manual Blocklist  
- Collect suspicious UA strings from server logs and Cloudflare firewall events.  
- Add them as block rules in Cloudflare Firewall or WP Cerber plugin.

### Example Cloudflare Firewall Rule  
Block requests with UA containing known bot signatures:
(http.user_agent contains "HeadlessChrome") or (http.user_agent contains "curl") or (http.user_agent contains "Python-urllib")


### WP Cerber User-Agent Blocking  
- Navigate to WP Cerber plugin → Hardening → HTTP Access → User-Agent blacklist.  
- Add UA substrings like:  
- Save changes and monitor effectiveness.

## 5. Caveats and Best Practices  
- Legitimate bots like Googlebot can be spoofed, so blocking by UA alone may block valid crawlers. Use alongside IP verification.  
- Overly aggressive UA blocking can block some real users or legitimate services. Test changes carefully.  
- Update UA blocklists regularly based on new attack patterns.

## 6. Automation  
- Use scripts to parse logs and extract frequent UA strings.  
- Feed suspicious UAs into blocklists dynamically where supported.

## 7. Summary  
User-Agent filtering is an effective additional layer of defense to reduce spam and bot traffic on qisetna.com. Combined with IP blocking, CAPTCHA, and rate limiting, it helps secure user registration and login endpoints.

---

## References  
- Cloudflare Firewall Rules: https://developers.cloudflare.com/firewall/cf-firewall-rules/  
- WP Cerber User-Agent Blacklist: https://wpcerber.com/docs/blacklist/  
- User-Agent Database: https://deviceatlas.com/blog/list-of-user-agent-strings
