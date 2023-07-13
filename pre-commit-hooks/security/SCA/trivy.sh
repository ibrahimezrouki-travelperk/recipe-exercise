#!/bin/bash

[[ -f ./requirements.txt  ]] && echo "requirements.txt exists, running trivy" && docker run --rm -v "$PWD":/myapp aquasec/trivy fs myapp/requirements.txt --ignore-unfixed -q --scanners vuln || exit 0
[[ -f ./requirements-dev.txt  ]] && echo "requirements-dev.txt exists, running trivy" && docker run --rm -v "$PWD":/myapp aquasec/trivy fs myapp/requirements-dev.txt --ignore-unfixed -q --scanners vuln || exit 0