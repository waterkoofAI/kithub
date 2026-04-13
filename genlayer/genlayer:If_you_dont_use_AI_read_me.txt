WaterkoofAI x GenLayer Airdrop Script Kit v1.5
Manual Guide — For Users Who Do Not Use AI
t.me/WaterkoofAI_Bot
================================================


RISK DISCLAIMER
---------------
- This script is open source and fully auditable
- Your private keys and seed phrases are NEVER requested or stored
- All MetaMask transaction approvals require your manual confirmation
- Airdrop eligibility is at GenLayer's sole discretion
- Use at your own risk — the authors are not responsible for any loss of funds


SUPPORTED SYSTEMS
-----------------
- Windows 10 / 11
- macOS 11 or higher
- Linux (Ubuntu, Fedora, Debian and similar)

This kit requires a desktop or laptop computer.
It cannot run on mobile phones or tablets.


FILES IN THIS KIT
-----------------
- STEP1_Drop_me_to_any_AI.md          Drop into any AI chat for guided setup
- STEP2_Fill_your_wallet_info.json    Fill in your wallet details before running
- genlayer_auto.py                    The main script
- If_you_dont_use_AI_read_me.txt      This file


WHAT YOU NEED BEFORE STARTING
------------------------------
Accounts:
  - MetaMask wallet (wallet address ready)
  - GitHub account
  - Email address for GenLayer profile

Software:
  - Google Chrome       https://www.google.com/chrome/
  - Python 3.9 or higher


HOW TO OPEN A TERMINAL
-----------------------
Windows:
  Press the Windows key, search for "Command Prompt" or "PowerShell", open it.

macOS:
  Press Cmd + Space, search for "Terminal", open it.

Linux:
  Press Ctrl + Alt + T, or search for "Terminal" in your app menu.


CHECK YOUR PYTHON VERSION
-------------------------
Windows:
  python --version

macOS / Linux:
  python3 --version

If Python is not installed or below 3.9:
  Windows / macOS: download from https://python.org
    Windows: check "Add Python to PATH" during installation
  Linux (Ubuntu/Debian): sudo apt install python3
  Linux (Fedora):        sudo dnf install python3


INSTALL DEPENDENCIES
--------------------
Windows:
  pip install playwright
  python -m playwright install chromium

macOS / Linux:
  pip3 install playwright
  python3 -m playwright install chromium

If pip gives a "not found" error on Windows, try:
  python -m pip install playwright
  python -m playwright install chromium


EDIT STEP2_Fill_your_wallet_info.json
--------------------------------------
Windows:  right-click the file → Open with → Notepad
macOS:    right-click the file → Open With → TextEdit

Replace the placeholder values:
  "address"       Your MetaMask wallet address (starts with 0x)
  "name"          A display name for your GenLayer profile
  "email"         Your email address
  "referral_code" A referral code if you have one, otherwise leave as-is

For multiple wallets, copy the wallet block and add more entries inside the [ ] brackets.
DO NOT put your private key or seed phrase in this file.


START CHROME WITH REMOTE DEBUGGING
------------------------------------
Close all regular Chrome windows first.
Then open a NEW terminal window and run the command for your system:

macOS:
  /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
    --remote-debugging-port=9222 \
    --no-first-run \
    --user-data-dir="$HOME/Library/Application Support/Google/Chrome-Debug"

Windows (Command Prompt):
  "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --no-first-run --user-data-dir="%LOCALAPPDATA%\Google\Chrome-Debug"

Windows (PowerShell):
  & "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --no-first-run --user-data-dir="$env:LOCALAPPDATA\Google\Chrome-Debug"

Linux:
  google-chrome --remote-debugging-port=9222 --no-first-run --user-data-dir="$HOME/.config/google-chrome-debug"

A Chrome window will open. Keep it open and do not close this terminal.

If Chrome is not found at the default path on Windows:
  1. Right-click the Chrome shortcut on your desktop
  2. Click Properties
  3. Copy the path in the "Target" field and use that instead


INSTALL METAMASK IN CHROME-DEBUG (FIRST TIME ONLY)
----------------------------------------------------
In the Chrome window that just opened, go to:
  https://chromewebstore.google.com/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn

Install MetaMask and import your wallet using your Secret Recovery Phrase.
You only need to do this once — Chrome-Debug will remember MetaMask next time.


RUN THE SCRIPT
--------------
Open a SEPARATE terminal window (keep the Chrome terminal open).

First navigate to the kit folder:
  Windows:        cd C:\path\to\genlayer-kit
  macOS / Linux:  cd /path/to/genlayer-kit

To find the correct path:
  Windows: open the folder in File Explorer, click the address bar, copy the path shown
  macOS:   right-click the folder, hold Option, click "Copy as Pathname"

Then run the script:
  Windows:        python genlayer_auto.py
  macOS / Linux:  python3 genlayer_auto.py

The script will pause and show ACTION NEEDED prompts at each manual step.
Read each prompt carefully and follow the instructions in the browser.

Manual steps you will need to complete:
  1.  MetaMask connect popup — switch wallet, click Connect
  2.  Profile setup form — fill name and email, click Save
  3.  GitHub authorization — authorize GenLayer in the popup
  4.  Star the Boilerplate repo on GitHub
  5.  Add GenLayer Testnet — approve in MetaMask
  6.  Get testnet tokens — complete faucet claim
  7.  Add Studio Network — approve in MetaMask
  8.  Deploy contract — in Studio, select llm_erc20.py, click Deploy, wait for success
  9.  Complete Builder Journey — click your username top right, scroll down, click the button
  10. Copy referral link — click Become a referrer, copy and save your link


TROUBLESHOOTING
---------------
"python: command not found" (macOS/Linux)
  Use "python3" instead.

"python is not recognized" (Windows)
  Python was not added to PATH. Reinstall Python from python.org and check "Add Python to PATH".

"Could not connect to Chrome"
  Make sure Chrome is still running in the other terminal.
  Close all other Chrome windows and try again.

MetaMask shows "Not installed" on the portal
  Install MetaMask in Chrome-Debug following the steps above.

Script skips a task saying "may already be done"
  The button was not found automatically.
  Complete that step manually in the browser, then press ENTER to continue.

Wallet shows "0xYourFirstWalletAddress"
  You forgot to edit STEP2_Fill_your_wallet_info.json.
  Replace the placeholder with your real wallet address.

Chrome path not found on Windows
  Right-click the Chrome desktop shortcut → Properties → copy the path in "Target" field.


FOLLOW US
---------
t.me/WaterkoofAI_Bot — for more airdrop scripts and updates
