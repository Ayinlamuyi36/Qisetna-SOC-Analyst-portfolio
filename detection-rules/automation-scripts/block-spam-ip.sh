#!/bin/bash
# Script to add IPs to Cloudflare blocklist using API (example)

CLOUDFLARE_API_TOKEN="your_api_token_here"
ZONE_ID="your_zone_id_here"
IP_TO_BLOCK=$1

if [ -z "$IP_TO_BLOCK" ]; then
  echo "Usage: $0 <IP>"
  exit 1
fi

curl -X POST "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/firewall/access_rules/rules" \
     -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
     -H "Content-Type: application/json" \
     --data '{
       "mode":"block",
       "configuration":{
         "target":"ip",
         "value":"'"$IP_TO_BLOCK"'"
       },
       "notes":"Blocked by SOC Analyst script"
     }'

##How to Use
Get your Cloudflare API Token with permissions to edit firewall rules.

Get your Cloudflare Zone ID for qisetna.com from the Cloudflare dashboard.

Replace the placeholders in the script (CF_API_TOKEN, CF_ZONE_ID) with your actual values.

Add any new suspicious IP addresses to the SPAM_IPS array.

Save the script as block-spam-ip.sh.

Make it executable:

chmod +x block-spam-ip.sh
./block-spam-ip.sh
