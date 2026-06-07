WaterkoofAI x Pod Network Airdrop Script Kit

HOW TO SET UP WITHOUT AI
========================

This Kit guides Pod Network testnet competition activity using Bitget Wallet. It helps open the Pod testnet, handle Join the Competition, choose Login, continue with a wallet, review X verification, guide paper testnet trading, and review waitlist plus Discord follow-up. Wallet approvals, trades, social logins, and deposits are always manual.

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
- Leave "referral_code" as "none" unless you have a Pod referral code.
- Adjust "preferred_markets", "trade_size_usd", or "max_leverage" only as local reminders.
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

First time only: set up Bitget Wallet in this Chrome-Debug profile. Never paste a seed phrase, private key, or wallet password into this kit or any AI chat.

4. POD NETWORK DETAILS
----------------------
If Bitget Wallet asks to add or switch network, review these details:

Network Name: Pod Devnet / Testnet
RPC URL: https://rpc.v1.dev.pod.network
Chain ID: 1293
Symbol: pUSD
Explorer: https://explorer.v1.pod.network/

Pod pages:
Testnet: https://test.pod.network/
Main site: https://pod.network/
Main app / waitlist: https://app.pod.network/
Docs: https://docs.v2.pod.network/
Explorer: https://explorer.v1.pod.network/

5. RUN THE SCRIPT
-----------------
Open a fresh terminal or command prompt window. Leave Chrome running.
Navigate to this folder using cd:
  cd c:\path\to\pod

Then run:
  python pod_auto.py

Follow the on-screen prompts.

The script will guide:
- Join the Competition popup
- Login button
- Continue with a wallet option
- Bitget Wallet connection/signature
- X verification check
- Paper testnet market trading review
- Positions, account value, and leaderboard review
- Mainnet waitlist and Discord role follow-up

Trading orders, wallet signatures, social login, waitlist signup, and any deposit must be reviewed and completed by you manually.

---
Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
