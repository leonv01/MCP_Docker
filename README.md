# FastMCP Docker

## Prerequisites
- docker-compose
- uvicorn
- FastMCP
- python3

## Run Server
The repository contains in the root project directory a shell script `run.sh` which automatically starts the docker-compose process. 

## Run Client
The `test/` directory contains a shell script which automatically sets up the virtual environment and install all needed dependencies. The `test_client.py` script executes the mcp tools from the server and asserts them with expected values.