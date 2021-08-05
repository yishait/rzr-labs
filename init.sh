#!/bin/bash

# Creating Virtualenv
if [ -d "venv" ]
then
    echo "Virtualenv already exists." 
else
    echo "Virtualenv does not exist."
    virtualenv -p python3 venv
fi
sleep 1
source venv/bin/activate
echo $pwd

echo "installing requirements"
pip install -r requirements.txt

# create remote state
echo "generating remote state"
cd remote_state 
terraform init && terraform apply -auto-approve
cd ..

cd rzrlabs_cluster
logname="logs/myLogFile$(date +"%s").log"

# create cluster and VPC configuration
echo "generating cluster and VPC configuration"
terraform init && terraform apply -auto-approve | tee ../$logname
cd ..

# ship logs to S3
python tf_logger.py $logname

# deploy the helm chart whats my ip from public registry created in aws project
cd whats-my-ip-chart
python ../deploy_wmip.py
