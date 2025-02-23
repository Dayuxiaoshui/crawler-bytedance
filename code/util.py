import subprocess
import datetime, threading
import requests
from generate_urls import make_urls, get_random_url


MAX_PORTS = 6


def start_all_nodes(n):
    for i in range(n):
        port = 5000+i
        subprocess.Popen(['gnome-terminal', '-x',"python3", "code/node.py",str(port),str(n)])

def start_a_nodes(n,num_nodes):
    port = 5000+n
    subprocess.Popen(["python3", "code/node.py",str(port),str(num_nodes)])

def start_health_monitor(num_nodes):
    subprocess.Popen(['gnome-terminal', '-x',"python3", "code/health_monitor.py",str(num_nodes)])


def node_retry(tries,node,num_nodes):
    
    if tries == 0:
        return
    
    try:
        port = 5000+node
        subprocess.Popen(['gnome-terminal', '-x',"python3", "code/node.py",str(port),str(num_nodes)]) 

    except Exception as e: 
        print(e)

        return node_retry(tries-1,node,num_nodes) 
    



    

    
            

