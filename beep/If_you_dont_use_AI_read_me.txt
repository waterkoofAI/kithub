WaterkoofAI x BEEP Airdrop Script Kit

HOW TO SET UP WITHOUT AI
========================

This Kit helps you open BEEP through a referral link, connect Bitget Wallet on Sui, review deposit/yield setup, join or create a Squad, create an AI Trading Agent if you choose, check rewards, and complete Galxe/community tasks.

Important:
- BEEP runs primarily on Sui.
- BEEP docs say Sui-native USDC is the base stablecoin for deposits and yield.
- AI Trading and Predict features can lose money.
- The script never deposits funds, creates agents, trades, predicts, or approves wallet prompts.

1. INSTALL PYTHON & PLAYWRIGHT
-----------------------------
- Download and install Python 3.8+ from python.org (check "Add to PATH" on Windows)
- Open a terminal / command prompt and run:
  pip install playwright
  playwright install chromium

2. CONFIGURE WALLETS
-------------------
- Open STEP2_Fill_your_wallet_info.json in Notepad or any text editor
- Replace "0xYourBitgetWalletAddress" with your Bitget Wallet Sui address
- Keep "network" as "sui"
- Keep "collateral_token" as "USDC"
- Keep "referral_code" as "yy61h8u-6a" or replace it with your own BEEP referral code
- If you have a separate Squad code, replace "YOUR_SQUAD_CODE_IF_DIFFERENT"
- Save the file

Never add private keys or seed phrases to this file.

3. START CHROME IN DEBUG MODE
-----------------------------
You MUST close all regular Chrome windows before doing this.

Windows:
Press Win+R, paste this and hit Enter:
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --no-first-run --user-data-dir="%LOCALAPPDATA%\Google\Chrome-Debug"

Mac (Terminal):
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --no-first-run --user-data-dir="$HOME/Library/Application Support/Google/Chrome-Debug"

Linux (Terminal):
google-chrome --remote-debugging-port=9222 --no-first-run --user-data-dir="$HOME/.config/google-chrome-debug"

Note: In the new Chrome window, install Bitget Wallet extension if not already installed.
Bitget Wallet Download: https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak

4. RUN THE SCRIPT
-----------------
Open a fresh terminal / command prompt window (leave Chrome running).
Navigate to this folder using 'cd':
  cd c:\dev\kithub\kits\beep

Then run:
  python beep_auto.py

Follow the on-screen prompts.

The script will guide you through:
- Opening BEEP with the referral link
- Connecting Bitget Wallet manually
- Checking referral or squad code setup
- Reviewing the Sui-native USDC deposit flow
- Joining or creating a BEEP Squad
- Reviewing AI Trading Agent creation
- Checking rewards and agent activity
- Opening the BEEP Galxe/community quest page

---
Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
