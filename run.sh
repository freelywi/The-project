#!/bin/bash
docker build . -t fastapi_app
docker run -d -p 7654:8000 fastapi_app