# WP Mail SMTP Setup for qisetna.com

## 1. Introduction  
WP Mail SMTP is used to improve email delivery for WordPress by configuring SMTP or API-based mail sending, avoiding the default PHP mail() which often gets blocked or marked as spam. For **qisetna.com**, we use the Gmail API via Google Workspace to securely send emails.

---

## 2. Why Use WP Mail SMTP?  
- Ensures reliable email delivery  
- Supports OAuth 2.0 authentication for Gmail (more secure than SMTP passwords)  
- Avoids emails flagged as spam by major providers  
- Provides logs and debug tools for troubleshooting

---

## 3. Prerequisites  
- Active Google Workspace or Gmail account (e.g., info@qisetna.com)  
- Admin access to Google Cloud Console  
- WordPress admin access with WP Mail SMTP plugin installed (version compatible with WP 6.8.1)

---

## 4. Step-by-Step Setup

### 4.1 Install and Activate WP Mail SMTP Plugin  
1. Go to WordPress Dashboard > Plugins > Add New.  
2. Search for "WP Mail SMTP" by WPForms.  
3. Install and activate the plugin.

### 4.2 Configure Google Cloud Project and OAuth Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com).  
2. Create a new project named `Qisetna WP Mail SMTP`.  
3. Enable the **Gmail API** under **APIs & Services > Library**.  
4. Under **APIs & Services > Credentials**, create OAuth 2.0 Client ID:  
   - Application type: Web application  
   - Authorized redirect URIs:  
     `https://connect.wpmailsmtp.com/google/`  
5. Note the **Client ID** and **Client Secret**.

### 4.3 Enter Credentials in WP Mail SMTP

1. In WordPress, navigate to **WP Mail SMTP > Settings**.  
2. Select **Google / Gmail** as the mailer.  
3. Paste the **Client ID** and **Client Secret** from Google Cloud Console.  
4. Set **From Email** as `info@qisetna.com`.  
5. Set **From Name** as your preferred sender name (e.g., "Qisetna Support").  
6. Check **Force From Email** and **Force From Name** to ensure consistency.

### 4.4 Authorize the Plugin

1. Click **Save Settings**.  
2. Click the **Allow plugin to send emails using your Google account** button.  
3. Sign in with your Google Workspace account (`info@qisetna.com`) and grant permissions.

---

## 5. Testing the Configuration

- Navigate to **WP Mail SMTP > Tools > Email Test**.  
- Send a test email to an external address (e.g., your personal email).  
- Confirm delivery and check for errors.

---

## 6. Troubleshooting Common Issues

| Issue                              | Possible Cause                      | Solution                                                      |
|-----------------------------------|-----------------------------------|---------------------------------------------------------------|
| "Client missing project ID" error | Incorrect or missing OAuth setup   | Recheck Google Cloud credentials and authorized redirect URI  |
| Emails not sending                | API authorization not completed    | Re-authorize plugin and ensure permissions are granted        |
| Emails go to spam                 | From Email not matching domain     | Use verified domain email and enforce "Force From Email"      |
| Quota exceeded                   | Gmail API limits reached            | Monitor usage or consider SMTP fallback                        |

---

## 7. Backup Mailer Configuration (Optional)

- Set up an alternative mailer (e.g., SMTP or SendGrid) as a backup connection to ensure emails are sent even if Gmail API fails.  
- This requires WP Mail SMTP Pro.

---

## 8. Summary

By configuring WP Mail SMTP with the Gmail API, **qisetna.com** achieves secure, reliable, and authenticated email delivery essential for user notifications, alerts, and support communications. This setup complements the overall SOC strategy to maintain email integrity and availability.

---

## References  
- [WP Mail SMTP Documentation](https://wpmailsmtp.com/docs/)  
- [Google Cloud Console - Create OAuth Credentials](https://console.cloud.google.com/apis/credentials)  
- [Google Workspace Gmail API Overview](https://developers.google.com/gmail/api)  

