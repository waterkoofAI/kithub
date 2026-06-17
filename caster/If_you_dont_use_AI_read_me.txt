WaterkoofAI x Caster Airdrop Script Kit

HOW TO SET UP WITHOUT AI
========================

This Kit automates Caster activity using Bitget Wallet to help you qualify for the airdrop.

1. INSTALL PYTHON & PLAYWRIGHT
-----------------------------
- Download and install Python 3.8+ from python.org (Check "Add to PATH" on Windows)
- Open a terminal / command prompt and run:
  pip install playwright
  playwright install chromium

2. CONFIGURE WALLETS
-------------------
- Open STEP2_Fill_your_wallet_info.json in Notepad or any text editor
- Replace "0xYourBitgetWalletAddress" with your actual Bitget Wallet address
- Save the file

3. START CHROME IN DEBUG MODE
-----------------------------
You MUST close all regular Chrome windows before doing this.

Windows:
Press Win+R, paste this and hit Enter:
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --no-first-run --user-data-dir="%LOCALAPPDATA%\Google\Chrome-Debug"

Mac (Terminal):
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --no-first-run --user-data-dir="$HOME/Library/Application Support/Google/Chrome-Debug"

Note: In the new Chrome window, install Bitget Wallet extension if not already installed.
Bitget Wallet Download: https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak

4. RUN THE SCRIPT
-----------------
Open a fresh terminal / command prompt window (leave Chrome running).
Navigate to this folder using 'cd':
  cd c:\dev\kithub\kits\caster
Then run:
  python caster_auto.py

Follow the on-screen prompts!

---
Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
