#!/usr/bin/env bash
docker build -t suzu2 .
docker run -it --rm -p 8000:80 -p 5432 --network="host" --name suzu2 suzu2