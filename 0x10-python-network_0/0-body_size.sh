#!/bin/bash
# CURL body size
curl -s $1 | grep 'Content-Length:' | awk '{print$2}'
