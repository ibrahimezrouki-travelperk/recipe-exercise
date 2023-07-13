#!/bin/bash

docker ps > /dev/null 2>&1
[[ $? -ne 0 ]] && echo "Docker not available. Start docker daemon" && exit 0
docker run --rm -v "$PWD:/path" zricethezav/gitleaks:latest protect --source="/path" --verbose --redact --staged
