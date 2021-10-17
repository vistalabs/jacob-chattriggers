# jacob-data
ChatTriggers module to collect data manually from the skyblock menu

## Setup
Create a folder in your `ChatTriggers\modules` folder (name doesn't matter) (or clone the repo in your modules folder), then download the files from github and put them there. In minecraft, make sure to reload with `/ct reload` and you're set. Make sure there is a file called `events.json` with `[]` inside it, or else it will not work.

### Example directory tree:
```
jacob-data
│   api.py
│   main.js
|   run.sh
|   events.json
```
File contents of `events.json` (before API request)
```json
[]
```

## Collecting data
Navigate to your modules folder in a terminal window, then run `api.py`. Now go back to skyblock and go to the full calender (Nether Star -> clock -> full calender). Press H on the first page, then click the arrow on the right and press H again until you reach the end of the skyblock year. After that, type `/uploadjacobdata` and if it returns no errors you can close minecraft.

### Example output (minecraft chat):
```
-> Navigate to the full skyblock calender and press H for each month of the skyblock year
[JU] Done
-> /uploadjacobdata
[JU] Started upload...
[JU] Done!
=> If an error occurs:
[JU] ERROR: {error}
```
#### Example output (`api.py`):
```
root@jacob:/root/.minecraft/config/ChatTriggers/modules/jacoob$ python3 api.py
 * Serving Flask app 'api' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 [POST] 0.0.0.1 # Not exact, is just an example to show that a request has been sent from the chattriggers module
```

## Retrieving and moving data
In your terminal window, close the python program and open a file explorer. Copy the `events.json` file into the `jacob-bot` repository and you're all set! If you have any questions or errors, contact @WindowsVistaisCool. **Please note that this data is in MS, not seconds, and you will need to run `cogs.util.configure_data()` to convert this to seconds and remove 5 minutes**

### Commands (linux/debian):
```
// In your CT module
cp events.json /path/to/jacob-data
```
