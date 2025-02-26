#!/bin/bash

set -e
echo "Implement your tests here"

# Define API URL (Update this to match your deployment)
API_URL="http://team${TEAM_NUMBER}.northeurope.azurecontainer.io"

# Wait for the API to be available (max 60s)
echo "Waiting for API to be live..."
for i in {1..30}; do
    if curl -s --head --request GET "$API_URL/version" | grep "200 OK" > /dev/null; then
        echo "API is live!"
        break
    fi
    echo "Waiting..."
    sleep 2
done