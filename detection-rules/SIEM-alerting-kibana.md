# SIEM Alerting with Kibana for qisetna.com

## 1. Introduction
This document describes how Security Information and Event Management (SIEM) alerting is configured using Kibana for the qisetna.com WordPress environment. It focuses on detecting suspicious activities, brute-force attacks, and malicious registrations through log analysis and alerting rules.

## 2. Objective
- Proactively detect security incidents by monitoring logs from WordPress, Cloudflare, and plugins like WP Cerber.
- Configure Kibana alerting rules to notify SOC analysts of anomalous events.
- Automate response workflows for rapid incident mitigation.

## 3. Data Sources
- **WordPress logs:** Login attempts, user registrations, plugin logs (e.g., WP Cerber)
- **Cloudflare logs:** Firewall events, rate limiting, bot detection
- **System logs:** Web server access/error logs, authentication logs

## 4. Kibana Setup Overview
- Use the **Elastic Stack (ELK)**: Elasticsearch stores logs, Logstash ingests and parses, and Kibana visualizes and alerts.
- Ingest logs into Elasticsearch from WordPress (via plugins or syslog), Cloudflare (via logpush), and system sources.
- Create saved searches and visualizations to identify key security events.

## 5. Key Alerting Rules in Kibana

### 5.1 Brute Force Login Attempts
- **Trigger:** More than 5 failed login attempts from the same IP within 10 minutes.
- **Query:** Filter WordPress logs where `event.type = "login_failure"` grouped by IP.
- **Action:** Send email or Slack alert to SOC team with IP details and timestamps.

### 5.2 Suspicious User Registrations
- **Trigger:** New user registrations with disposable or suspicious email domains (e.g., `delhinightqueen.com`).
- **Query:** Filter logs for `event.type = "user_registration"` where `email_domain` matches known spam domains.
- **Action:** Alert for manual review or automated block via firewall.

### 5.3 XML-RPC Abuse Attempts
- **Trigger:** Access attempts to `/xmlrpc.php` endpoint exceeding threshold (e.g., 10 requests per 5 minutes).
- **Query:** Filter web server or Cloudflare logs for `request.uri = "/xmlrpc.php"` and count by IP.
- **Action:** Alert and auto-block offending IPs using Cloudflare API or WP Cerber.

### 5.4 Firewall Rule Triggers
- **Trigger:** Firewall blocks or challenges (e.g., IP blocked, captcha triggered).
- **Query:** Cloudflare logs where `action` equals `block` or `challenge`.
- **Action:** SOC team notification and review in Kibana dashboard.

## 6. Sample Kibana Query DSL Example

```json
{
  "query": {
    "bool": {
      "must": [
        {"match": {"event.type": "login_failure"}},
        {
          "range": {
            "@timestamp": {
              "gte": "now-10m",
              "lte": "now"
            }
          }
        }
      ]
    }
  },
  "aggs": {
    "by_ip": {
      "terms": {
        "field": "source.ip",
        "min_doc_count": 5
      }
    }
  }
}
This query detects IPs with 5 or more failed login attempts in the last 10 minutes.

7. Alerts Configuration
Use Kibana Alerting UI to create alerts based on saved searches or custom queries.

Configure alert actions such as email, Slack, or webhook to notify the SOC team.

Tune thresholds and filters regularly to reduce false positives.

8. Integration with Incident Response
Alerts trigger automated scripts to block IPs (e.g., using Cloudflare API).

Create tickets in tracking systems like Jira or ServiceNow for analyst follow-up.

Maintain a dashboard for real-time monitoring of security events.

9. Summary
By leveraging Kibana for log visualization and alerting, the SOC team at Qisetna gains critical visibility into web attacks and suspicious behavior, enabling rapid response and ongoing threat hunting.

References
Elastic SIEM Documentation

Kibana Alerting

WP Cerber Logging & Alerts

Cloudflare Logpush

Incident Response Best Practices