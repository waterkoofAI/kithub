======================================================
WaterkoofAI x Isometric Automation Kit - Manual Setup
======================================================

If you are not using an AI assistant to guide you, follow these steps exactly to run the Isometric automation script:

PREREQUISITES:
1. Install Python (https://www.python.org/downloads/)
2. Install the Bitget Wallet Chrome Extension:
   https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak

STEP 1: INSTALL DEPENDENCIES
Open your terminal or command prompt and run:
pip install playwright
playwright install chromium

STEP 2: CONFIGURE YOUR WALLETS
1. Open the file `STEP2_Fill_your_wallet_info.json` in a text editor.
2. Replace "YourSolanaWalletAddress1Here" with your actual Solana wallet address.
3. Add or remove wallet blocks as needed. Do NOT put your private keys in this file.

STEP 3: START CHROME WITH REMOTE DEBUGGING
The script needs to attach to an open Chrome browser. You must start Chrome from the terminal with a specific flag.

On Windows (Command Prompt):
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --no-first-run --user-data-dir="%LOCALAPPDATA%\Google\Chrome-Debug"

On Mac (Terminal):
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --no-first-run --user-data-dir="$HOME/Library/Application Support/Google/Chrome-Debug"

STEP 4: RUN THE SCRIPT
Leave the Chrome browser open. In a NEW terminal window, navigate to the folder containing the script and run:
python isometric_auto.py

SAFETY REMINDERS:
- Never give your private key to any script.
- Review every transaction in the Bitget Wallet popup before clicking approve.
- This script does NOT click "Approve" for you. You must do it manually.
