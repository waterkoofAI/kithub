WaterkoofAI x GIWA Airdrop Script Kit

HOW TO SET UP WITHOUT AI
========================

This Kit guides GIWA Sepolia testnet activity using Bitget Wallet to help you create faucet, playground, transfer, and contract deployment activity. Wallet approvals are always manual.

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
- The email field is not used by the script; you can leave it unchanged.
- Leave "use_backup_faucet" as false unless you want the script to open the backup faucet too.
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

4. ADD GIWA SEPOLIA TO BITGET WALLET
------------------------------------
Use these exact network details:

Network Name: GIWA Sepolia
RPC URL: https://sepolia-rpc.giwa.io
Chain ID: 91342
Symbol: ETH
Explorer: https://sepolia-explorer.giwa.io

Official faucet: https://faucet.giwa.io/
Backup faucet: https://faucet.lambda256.io/giwa-sepolia
Playground: https://sepolia-playground.giwa.io/

5. RUN THE SCRIPT
-----------------
Open a fresh terminal or command prompt window. Leave Chrome running.
Navigate to this folder using cd:
  cd c:\path\to\giwa

Then run:
  python giwa_auto.py

Follow the on-screen prompts.

The script will guide:
- GIWA Sepolia network setup
- Official faucet claim
- Optional backup faucet
- GIWA Playground tasks
- Small manual test transfers
- Owlto simple contract deployment

Every Bitget Wallet approval must be reviewed and approved by you manually.

---
Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
