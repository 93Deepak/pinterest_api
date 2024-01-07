This APP Posts data/Creates pin on Pinterest
Steps to install and run

install python3.9
install python3.9 virtual environment

create a virtual environment
python3.9 -m venv <env name>

activate the environment
. <env name>/bin/activate

clone this repository
git clone <repo url>

checkout to branch - pinterest

install all dependencies
pip install -r requrements.txt

run the server with essential environment variables
PINTEREST_ACCESS_TOKEN="your access token" BOARD_ID="your board id" uvicorn main:app --reload


you can run 127.0.0.1:8000/docs in the browser to view swagger ui of the api or
you can hit POST 127.0.0.1:8000 with json payload {'id':0, 'media_url':'your media url','caption':'your caption'}

to run tests
run pytest in console

