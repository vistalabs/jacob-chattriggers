# jacob-data
ChatTriggers module to collect data manually from the skyblock menu

## Setup
Create a folder in your `ChatTriggers\modules` folder (name doesn't matter) (or clone the repo in your modules folder), then download the files from github and put them there. In minecraft, make sure to reload with `/ct reload` and you're set. Make sure there is a file called `events.json` with `[]` inside it, or else it will not work.
## Collecting data
Navigate to your modules folder in a terminal window, then run `api.py`. Now go back to skyblock and go to the full calender (Nether Star -> clock -> full calender). Press H on the first page, then click the arrow on the right and press H again until you reach the end of the skyblock year. After that, type `/uploadjacobdata` and if it returns no errors you can close minecraft.

## Retrieving and moving data
In your terminal window, close the python program and open a file explorer. Copy the `events.json` file into the `jacob-bot` repository and you're all set! If you have any questions or errors, contact @WindowsVistaisCool.
