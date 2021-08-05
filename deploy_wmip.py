import boto3
import subprocess
import os
cwd = os.getcwd()

client = boto3.client('eks')
cluster = client.list_clusters()['clusters'][0]

subprocess.run(['aws','eks','update-kubeconfig','--name',cluster])
subprocess.run(['kubectl','create','namespace','yishai-whats-my-ip'])

subprocess.run(['helm','install','yishai-wmip','-n', 'yishai-whats-my-ip', '.'])