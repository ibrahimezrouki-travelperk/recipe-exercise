#!/bin/bash

docker ps > /dev/null 2>&1
[[ $? -ne 0 ]] && echo "Docker not available. Start docker daemon" && exit 0
Dockerfile=$(find . -name '*dockerfile*')
if [ -n "$Dockerfile" ]; then
  while IFS= read -r file; do
    echo "file $file exists, running Trivy"
    docker run -v "$PWD:/app" --rm aquasec/trivy config -q "/app/$file"
  done <<< "$Dockerfile"
fi