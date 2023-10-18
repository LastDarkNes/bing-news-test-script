# Bing news test script
This is a script for tests with bing news api.
## Usage
* Activate venv.
* Install dependencies.
* Adjust settings.json
* Run!

## Activate venv
To activate venv go to the project root and use this command:
```
source venv/bin/activate
```

## Install dependencies
To install dependencies go to the project root and use this command:
```
pip install -r requirements.txt
```

## Adjust settings.json
settings.json is a config file to setup script, you need to provide:
* API key to use - An Azure service API key.
* URL - URL of api provider.
* Endpoint - search endpoint to use.
* Query params - Params to perform search.

## Run!
Use this command to run script:
```
python3 main.py
```
