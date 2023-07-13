#!/bin/bash

mkdir -p ./output/prod/ ./output/dev/

prod_req="./output/prod/requirements.txt"
dev_req="./output/dev/requirements.txt"
licenses="./output/licenses.txt"

pip-licenses --version &>/dev/null
[[ $? -ne 0 ]] && echo "pip-licenses package not found please run: pip install pip-licenses" && rm -rf ./output/ && exit 1

pip-licenses | grep 'GPL\|GPLv2\|GPLv3\|Artistic\|MPL\|ASL\|GNU\|Eclipse\|CNRI' | grep -v 'Lesser' | awk '{print tolower($0)}' > "$licenses"
[[ -f ./requirements.txt ]] && cat ./requirements.txt | grep '^[a-zA-Z].*=[^=]*$' | cut -d= -f1 > "$prod_req"
result=$(awk 'NR==FNR{words[$0]=1;next} $1 in words' "$prod_req" "$licenses")
[[ -n "$result" ]] && echo "Processing requirements.txt. The following packages are not allowed due to their licenses:\n $result"
[[ -f ./requirements.dev.txt ]] && cat ./requirements.dev.txt | grep '^[a-zA-Z].*=[^=]*$' | cut -d= -f1 > "$dev_req"
result=$(awk 'NR==FNR{words[$0]=1;next} $1 in words' "$dev_req" "$licenses")
[[ -n "$result" ]] && echo "Processing requirements-dev.txt. The following packages are not allowed due to their licenses:\n $result"
rm -rf ./output/