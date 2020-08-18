#!/bin/bash
#jason files whit post
curl -s -d @"$2" 0.0.0.0:5000/route_json
