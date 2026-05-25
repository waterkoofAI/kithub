WaterkoofAI x Tangent Airdrop Script Kit

HOW TO SET UP WITHOUT AI
========================

This Kit helps you open Tangent's predeposit page, connect Bitget Wallet on Ethereum mainnet, choose a USDC/USG or frxUSD/USG pool, review the approval/deposit flow, decide whether to hold or stake received LP tokens, and track future TAN claim steps.

Important:
- Tangent predeposit runs on Ethereum mainnet.
- You need ETH for gas if you plan to deposit.
- You need USDC or frxUSD on Ethereum mainnet if you plan to predeposit.
- Curve LP positions and stablecoins carry smart-contract, slippage, and depeg risk.
- The script never approves tokens, deposits funds, stakes LP tokens, withdraws, or claims.

1. INSTALL PYTHON & PLAYWRIGHT
-----------------------------
- Download and install Python 3.8+ from python.org (check "Add to PATH" on Windows)
- Open a terminal / command prompt and run:
  pip install playwright
  playwright install chromium

2. CONFIGURE WALLETS
-------------------
- Open STEP2_Fill_your_wallet_info.json in Notepad or any text editor
- Replace "0xYourBitgetWalletAddress" with your Bitget Wallet Ethereum address
- Keep "network" as "ethereum"
- Set "deposit_token" to "USDC" or "frxUSD"
- Set "pool_choice" to "USDC/USG" or "frxUSD/USG"
- Keep "lp_strategy" as "hold" if you want to target maximum Tangent points
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
  cd c:\dev\kithub\kits\tangent

Then run:
  python tangent_auto.py

Follow the on-screen prompts.

The script will guide you through:
- Opening Tangent predeposit
- Connecting Bitget Wallet manually
- Confirming Ethereum mainnet, ETH gas, and token readiness
- Selecting USDC/USG or frxUSD/USG
- Reviewing token approval and deposit steps
- Reviewing LP-token hold/stake strategy
- Planning retention and future TAN claim checks

---
Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
