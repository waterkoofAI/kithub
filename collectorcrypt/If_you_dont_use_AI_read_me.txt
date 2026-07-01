WaterkoofAI x Collector Crypt Airdrop Script Kit

HOW TO SET UP WITHOUT AI
=========================

This Kit guides Collector Crypt activity using Bitget Wallet to help you build Gacha
points toward the quarterly $CARDS distribution (15,000,000 $CARDS per quarter) and the
separate monthly holder airdrop.

Caution: Use a burner wallet for this airdrop and secure your seed phrase. Never paste a
seed phrase into this script or any website.

Important: Collector Crypt runs on Solana. Opening Gacha packs costs real USDC or $CARDS.
Only enable the real-money prompts if you accept that cost and risk.

1. INSTALL PYTHON & PLAYWRIGHT
-----------------------------
- Download and install Python 3.8+ from python.org (check "Add to PATH" on Windows)
- Open a terminal / command prompt and run:
  pip install playwright
  playwright install chromium

2. CONFIGURE WALLETS
-------------------
- Open STEP2_Fill_your_wallet_info.json in Notepad or any text editor
- Replace "YourSolanaWalletAddress" with your actual Bitget Wallet Solana address
- Keep "network" as "solana"
- Set "default_pack_spend_usdc" to the amount you may choose to spend per session
- Set "i_understand_gacha_costs_real_money" to true only after you understand this
- Set "enable_real_money_tasks" to true only if you want guided pack-opening / $CARDS
  buying prompts (leave false to just be guided through sign-in, referrals, and claiming)
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

Note: In the new Chrome window, install Bitget Wallet extension if not already installed,
and make sure it's set to a Solana account.
Bitget Wallet Download: https://web3.bitget.com/share/2kwRSC?inviteCode=waterkoof
Bitget Wallet Chrome Web Store: https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak

4. RUN THE SCRIPT
-----------------
Open a fresh terminal / command prompt window (leave Chrome running).
Navigate to this folder using 'cd':
  cd c:\path\to\collectorcrypt

Then run:
  python collectorcrypt_auto.py

Follow the on-screen prompts. Every Bitget Wallet approval, every Gacha pack purchase,
and every $CARDS swap must be reviewed and confirmed manually by you. Always double-check
the $CARDS contract address before swapping:
CARDSccUMFKoPRZxt5vt3ksUbxEFEcnZ3H2pd3dKxYjp

---
Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
