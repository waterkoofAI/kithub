WaterkoofAI x SolPump Airdrop Script Kit

HOW TO SET UP WITHOUT AI
========================

This Kit guides SolPump activity using Bitget Wallet to help you participate in possible SOLPUMP and hourly airdrop eligibility paths.

Caution: Use a burner wallet for this airdrop and secure your seed phrase. Never paste a seed phrase into this script or any website.

Important: SolPump involves real SOL wagering/trading and may be restricted in some jurisdictions. Do not use it unless it is legal for your location and you accept the risk.

1. INSTALL PYTHON & PLAYWRIGHT
-----------------------------
- Download and install Python 3.8+ from python.org (check "Add to PATH" on Windows)
- Open a terminal / command prompt and run:
  pip install playwright
  playwright install chromium

2. CONFIGURE WALLETS
-------------------
- Open STEP2_Fill_your_wallet_info.json in Notepad or any text editor
- Replace "0xYourBitgetWalletAddress" with your actual Bitget Wallet address
- Keep "network" as "solana"
- Keep "minimum_bet_sol" as "0.001" unless SolPump changes the requirement
- Set "i_confirm_solpump_is_legal_for_me" to true only after checking local rules
- Set "enable_real_money_tasks" to true only if you want guided SOL wagering/trading prompts
- Save the file
- Never add private keys or seed phrases

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
Bitget Wallet Download: https://web3.bitget.com/share/2kwRSC?inviteCode=waterkoof
Bitget Wallet Chrome Web Store: https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak

4. RUN THE SCRIPT
-----------------
Open a fresh terminal / command prompt window (leave Chrome running).
Navigate to this folder using 'cd':
  cd c:\path\to\SolPump

Then run:
  python solpump_auto.py

Follow the on-screen prompts. Every wallet approval must be reviewed and confirmed manually in Bitget Wallet.

---
Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
