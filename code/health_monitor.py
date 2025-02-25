import subprocess
import schedule
import time
import datetime, threading
import requests
import sys
from util import node_retry
from generate_urls import make_urls, get_random_url


def periodic_healthcheck(node_count):
    urls = make_urls(node_count)
    print(urls)
    retry_nodes = []
    for i in range(node_count):
        try:
            r = requests.get(url=urls[i]+'/health')
            print(r)
            print('heathcheck success for '+urls[i])

        except:
            print('heathcheck failed for '+urls[i])
            retry_nodes.append(i)

    for i in retry_nodes:
        node_retry(3,i,node_count,)

    retry_nodes.clear()

    # threading.Timer(30,periodic_healthcheck,args=node_count).start()

if __name__ == '__main__':
        
        try:
            number_of_nodes = int(sys.argv[1])
            schedule.every(10).seconds.do(periodic_healthcheck,number_of_nodes)
            while True:
                schedule.run_pending()
                time.sleep(1)
            # periodic_healthcheck(number_of_nodes)
        except:
            print("health monitor failed")
            exit(0)




