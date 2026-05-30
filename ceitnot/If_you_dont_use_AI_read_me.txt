WaterkoofAI x Ceitnot Protocol Airdrop Script Kit

HOW TO SET UP WITHOUT AI
========================

This Kit guides Ceitnot Protocol testnet activity using Bitget Wallet to help you create Arbitrum Sepolia faucet, collateral, vault, ceitUSD, PSM, and social activity. Wallet approvals are always manual.

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
- Leave "use_quicknode_faucet" as false unless you want the script to open the backup faucet too.
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

4. ADD ARBITRUM SEPOLIA TO BITGET WALLET
----------------------------------------
Use these exact network details:

Network Name: Arbitrum Sepolia
RPC URL: https://sepolia-rollup.arbitrum.io/rpc
Chain ID: 421614
Symbol: ETH
Explorer: https://sepolia.arbiscan.io

Faucets:
Alchemy: https://www.alchemy.com/faucets/arbitrum-sepolia
QuickNode backup: https://faucet.quicknode.com/arbitrum/sepolia

Ceitnot pages:
Home: https://www.ceitnot.io/
Dashboard: https://www.ceitnot.io/dashboard
Markets: https://www.ceitnot.io/markets
Position: https://www.ceitnot.io/position
Swap / PSM: https://www.ceitnot.io/swap
Rewards: https://www.ceitnot.io/rewards

5. RUN THE SCRIPT
-----------------
Open a fresh terminal or command prompt window. Leave Chrome running.
Navigate to this folder using cd:
  cd c:\path\to\ceitnot

Then run:
  python ceitnot_auto.py

Follow the on-screen prompts.

The script will guide:
- Arbitrum Sepolia faucet claim
- Bitget Wallet connection to Ceitnot
- Test collateral mint or claim
- Vault deposit and ceitUSD borrow
- PSM / Swap activity
- Rewards and social quest review

Every Bitget Wallet approval must be reviewed and approved by you manually.

---
Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
