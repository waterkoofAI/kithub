WaterkoofAI x Brighter Airdrop Script Kit

HOW TO SET UP WITHOUT AI
========================

This Kit guides Brighter's points-reservation campaign using Bitget Wallet:
connecting your wallet, linking X, entering a referral code, and sharing your
own referral link. Brighter has no token yet and no airdrop is officially
confirmed — this only builds points toward a possible future reward.

Caution: Use a burner wallet for this airdrop and secure your seed phrase.
Never paste a seed phrase into this script or any website.

1. INSTALL PYTHON & PLAYWRIGHT
-----------------------------
- Download and install Python 3.8+ from python.org (check "Add to PATH" on Windows)
- Open a terminal / command prompt and run:
  pip install playwright
  playwright install chromium

2. CONFIGURE WALLETS
-------------------
- Open STEP2_Fill_your_wallet_info.json in Notepad or any text editor
- Replace "0xYourBitgetWalletAddress" with your actual Bitget Wallet Ethereum address
- Keep "network" as "ethereum"
- Change "referral_code_to_enter" if you want to use a different code
- Save the file
- Never add private key or seed phrase fields

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
  cd c:\path\to\brighter

Then run:
  python brighter_auto.py

Follow the on-screen prompts. Every Bitget Wallet approval must be reviewed
and confirmed manually. Following/linking X, the Lit Hub upvote + screenshot,
and joining Telegram also require your own manual actions.

---
Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
