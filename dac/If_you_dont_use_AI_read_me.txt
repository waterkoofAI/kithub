WaterkoofAI x DAC Quantum Chain Airdrop Script Kit

HOW TO SET UP WITHOUT AI
========================

This Kit guides DAC Inception testnet activity using Bitget Wallet to help you create DAC Testnet, DACC faucet, QE mission, badge, QE Pool, Quantum Crate, and referral activity. Wallet approvals are always manual.

1. INSTALL PYTHON AND PLAYWRIGHT
-------------------------------
- Download and install Python 3.8+ from python.org. On Windows, check "Add to PATH".
- Open a terminal or command prompt and run:
  pip install playwright
  playwright install chromium

2. CONFIGURE WALLETS
--------------------
- Open STEP2_Fill_your_wallet_info.json in Notepad or any text editor.
- Replace "0xYourBitgetWalletAddress" with your actual Bitget Wallet address.
- Replace "YourDisplayName" with any local label you like.
- Set "referral_code" to your referral code or "none".
- Optional: replace "0xYourOtherTestWalletAddress" with your own spare test wallet for DACC transfers.
- The email field is not used by the script; you can leave it unchanged.
- Save the file.

Never add private keys, seed phrases, passwords, or recovery words to the JSON file.

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

4. ADD DAC TESTNET TO BITGET WALLET
-----------------------------------
Use these exact network details:

Network Name: DAC Testnet
RPC URL: https://rpctest.dachain.tech
Chain ID: 21894
Symbol: DACC
Explorer: https://exptest.dachain.tech

DAC pages:
Inception: https://inception.dachain.io/
Dashboard: https://inception.dachain.io/dashboard
Badges: https://inception.dachain.io/badges
Faucet: https://inception.dachain.io/faucet
My Activity: https://inception.dachain.io/activity
QE Pool: https://inception.dachain.io/exchange
Quantum Crate: https://inception.dachain.io/quantum-crate
Leaderboard: https://inception.dachain.io/leaderboard
Explorer: https://exptest.dachain.tech/

5. RUN THE SCRIPT
-----------------
Open a fresh terminal or command prompt window. Leave Chrome running.
Navigate to this folder using cd:
  cd c:\path\to\dac

Then run:
  python dac_auto.py

Follow the on-screen prompts.

The script will guide:
- DAC Inception sign-in
- Early Badge and Flash Badge review
- DACC faucet claim
- Home/My Activity missions
- Small transfer activity and sync
- QE Pool burn/stake
- Quantum Crate openings
- Leaderboard and referral review

Every Bitget Wallet approval must be reviewed and approved by you manually.

---
Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
