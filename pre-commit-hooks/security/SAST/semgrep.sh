#!/bin/bash

docker ps > /dev/null 2>&1
pip install -q semgrep
[[ $? -ne 0 ]] && echo "Docker not available. Start docker daemon" && exit 1
semgrep scan --config auto -q