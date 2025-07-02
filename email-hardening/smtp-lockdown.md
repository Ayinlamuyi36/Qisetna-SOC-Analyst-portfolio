# SPF, DKIM, and DMARC Records Setup for qisetna.com

## 1. Introduction  
Email spoofing and phishing are common threats targeting organizations. Implementing SPF, DKIM, and DMARC email authentication standards is essential to secure the domain qisetna.com against unauthorized email use and improve email deliverability.

## 2. SPF (Sender Policy Framework)

### Purpose  
SPF specifies which mail servers are authorized to send email on behalf of your domain.

### Example SPF Record for qisetna.com  
```txt
v=spf1 include:_spf.google.com ~all
Explanation
v=spf1 indicates the SPF version.

include:_spf.google.com authorizes Google Workspace servers to send emails for the domain.

~all means soft fail for other servers (emails sent from unauthorized servers are marked but not rejected).

Deployment
Add the SPF record as a TXT record in the DNS zone for qisetna.com.

Use online tools like MXToolbox SPF checker to verify.

3. DKIM (DomainKeys Identified Mail)
Purpose
DKIM signs outgoing emails with a cryptographic signature, ensuring message integrity and authenticity.

Steps to Setup DKIM with Google Workspace
Generate DKIM keys via Google Admin Console under Apps > Google Workspace > Gmail > Authenticate Email.

Publish the public key in DNS as a TXT record under a selector subdomain, e.g., google._domainkey.qisetna.com.

Enable DKIM signing in Google Admin Console.

Example DKIM DNS TXT Record
google._domainkey.qisetna.com IN TXT "v=DKIM1; k=rsa; p=MIIBIjANBgkqh..."
Verification
Use DKIM validator tools to check if DKIM signing works correctly.

4. DMARC (Domain-based Message Authentication, Reporting & Conformance)
Purpose
DMARC builds on SPF and DKIM, instructing receiving mail servers how to handle emails failing authentication and sends reports back to the domain owner.

## v=DMARC1; p=reject; rua=mailto:dmarc-reports@qisetna.com; ruf=mailto:dmarc-reports@qisetna.com; fo=1

Explanation
v=DMARC1 specifies the DMARC version.

p=reject tells receivers to reject emails failing SPF/DKIM checks.

rua specifies the aggregate report email address.

ruf specifies the forensic report email address.

fo=1 requests failure reports.

Deployment
Publish DMARC as a TXT record under _dmarc.qisetna.com in DNS.

Monitor reports regularly to tune policies.

| Protocol | Purpose                              | DNS Record Type | Common Value Example                  |
| -------- | ------------------------------------ | --------------- | ------------------------------------- |
| SPF      | Authorizes mail servers              | TXT             | `v=spf1 include:_spf.google.com ~all` |
| DKIM     | Signs outgoing emails                | TXT             | `v=DKIM1; k=rsa; p=<public_key>`      |
| DMARC    | Defines policy for SPF/DKIM failures | TXT             | `v=DMARC1; p=reject; rua=mailto:...`  |

