#!/bin/bash
python webserver.py &
echo "hello it worked ok" > /tmp/yes

sleep 1
curl -X POST http://localhost:8080/done -d "finished"