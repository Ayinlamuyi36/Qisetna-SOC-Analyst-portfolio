# SPF, DKIM, and DMARC Records Setup for qisetna.com

## 1. Introduction  
Email security is critical to protect **qisetna.com** from phishing, spoofing, and spam. Implementing SPF, DKIM, and DMARC DNS records helps verify legitimate email senders and improve email deliverability.

---

## 2. What Are SPF, DKIM, and DMARC?

- **SPF (Sender Policy Framework):**  
  A DNS TXT record that specifies which mail servers are authorized to send email on behalf of the domain. It helps prevent unauthorized sources from sending spoofed emails.

- **DKIM (DomainKeys Identified Mail):**  
  Uses cryptographic signatures added to emails that allow recipients to verify that the email was indeed sent from the domain owner and that the content was not altered in transit.

- **DMARC (Domain-based Message Authentication, Reporting & Conformance):**  
  Builds on SPF and DKIM to specify policies for handling emails that fail authentication checks and provides reporting to monitor abuse.

---

## 3. SPF Record Setup for qisetna.com

### Purpose  
Authorize only designated mail servers (e.g., Google Workspace, your SMTP server) to send emails on behalf of qisetna.com.

### Example SPF TXT record
v=spf1 ip4:37.27.56.228 include:_spf.google.com ~all
- `ip4:37.27.56.228` — Your authorized mail server IP  
- `include:_spf.google.com` — Includes Google Workspace servers  
- `~all` — Soft fail for unauthorized senders (can change to `-all` for stricter enforcement)

### How to add SPF record  
1. Log in to your DNS provider or Cloudflare dashboard.  
2. Add a new TXT record for the root domain (`qisetna.com`).  
3. Paste the SPF record value.  
4. Save and allow DNS propagation.

---

## 4. DKIM Record Setup for qisetna.com

### Purpose  
Cryptographically sign outbound emails to verify authenticity and integrity.

### Steps to generate DKIM keys  
- If using Google Workspace, DKIM keys can be generated from the Admin Console under **Apps > Google Workspace > Gmail > Authenticate email**.  
- For other mail providers, generate keys using their recommended tools.

### Example DKIM TXT record  
- Name: `default._domainkey.qisetna.com`  
- Value:  

### How to add DKIM record  
1. Add a TXT record with the selector name (e.g., `default._domainkey`).  
2. Paste the public key value.  
3. Save and wait for DNS propagation.  
4. Enable DKIM signing on your mail server or Google Workspace.

---

## 5. DMARC Record Setup for qisetna.com

### Purpose  
Define the policy for handling emails that fail SPF or DKIM checks and receive reports of authentication failures.

### Example DMARC TXT record  
- Name: `_dmarc.qisetna.com`  
- Value:  
v=DMARC1; p=quarantine; rua=mailto:dmarc-reports@qisetna.com; ruf=mailto:dmarc-failures@qisetna.com; pct=100; sp=none; aspf=r;
- `p=quarantine`: Emails failing checks will be marked as suspicious.  
- `rua`: Aggregate reports email address.  
- `ruf`: Forensic failure reports email address.  
- `pct=100`: Applies policy to 100% of emails.  
- `sp=none`: Subdomain policy (none means no specific action).  
- `aspf=r`: Relaxed SPF alignment.

### How to add DMARC record  
1. Add a TXT record with the name `_dmarc`.  
2. Paste your DMARC policy string.  
3. Save and allow DNS propagation.  
4. Monitor reports sent to your specified emails.

---

## 6. Verification and Testing

- Use tools like [MXToolbox SPF Lookup](https://mxtoolbox.com/spf.aspx), [DKIM Validator](https://dkimvalidator.com/), and [DMARC Analyzer](https://dmarcian.com/dmarc-inspector/) to verify correct setup.  
- Send test emails to verify DKIM signatures and SPF passing.  
- Monitor DMARC reports regularly to identify unauthorized senders or misconfigurations.

---

## 7. Summary

Implementing SPF, DKIM, and DMARC is crucial to securing the email channel of **qisetna.com**. This hardening reduces phishing risks, prevents domain spoofing, and improves email deliverability, aligning with best practices for SOC-level email security.

---

## References  
- [SPF Record Overview](https://www.spf-record.com/)  
- [DKIM.org](https://dkim.org/)  
- [DMARC.org](https://dmarc.org/)  
- [Google Workspace Email Authentication](https://support.google.com/a/answer/174124)

