#!/bin/bash
python webserver.py &

sleep 1
curl -X POST http://localhost:8080/ -d "installing openquake"

sudo add-apt-repository ppa:openquake/ppa -y
sudo apt-get update
sudo apt-get install python-oq-engine -y

oq-engine --upgrade-db -y

sleep 1
curl -X POST http://localhost:8080/ -d "running openquake"

oq-engine --run-hazard=/usr/share/openquake/risklib/demos/hazard/SimpleFaultSourceClassicalPSHA/job.ini

sleep 1
curl -X POST http://localhost:8080/done -d "finished"