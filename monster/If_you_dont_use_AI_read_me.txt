WaterkoofAI x Monster Strategy (mnstr.xyz) Airdrop Script Kit — Manual Setup Guide
=====================================================================================
t.me/WaterkoofAI_Bot

This guide is for users who prefer not to use an AI assistant.
Follow each step exactly as written.


WHAT THIS KIT DOES
-------------------
This Kit automates Monster Strategy (mnstr.xyz) activity to help you
earn weekly leaderboard points and build on-chain history for a
potential future airdrop. It is designed for a fresh burner wallet only.

Tasks covered:
  1. Connect Bitget Wallet to mnstr.xyz
  2. Navigate to Packs and review pack details (Starter / Monster / Ultra)
  3. Browse the Marketplace
  4. Check your Vault for collected graded cards
  5. Monitor the weekly Leaderboard for points ranking
  6. Additional pack strategy review

Wallet used: Bitget Wallet (Chrome extension)
Wallet safety: use a fresh burner wallet only. Do NOT use or import a main wallet.
Paid pack purchases: disabled by default and optional.

COVERAGE:
  - Total tasks: 6
  - Automated by this Kit: 6 / 6 guided browser steps
  - Manual tasks: fresh burner wallet setup, wallet approvals, optional pack purchases, optional marketplace trades
  - Wallet used: Bitget Wallet
    Download: https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak


ABOUT MONSTER STRATEGY (mnstr.xyz)
-------------------------------------
Monster Strategy is an on-chain trading card platform:
  - Open packs to pull real, professionally graded Pokemon cards
  - Cards are graded by PSA, CGC, or BGS
  - Ship physical cards to your door or sell back at 85% FMV
  - Earn weekly leaderboard points through activity
  - Points reset every Sunday

Pack tiers:
  Starter  — $50 per pack  (best for points-per-dollar)
  Monster  — $250 per pack (better card value odds)
  Ultra    — $1,250 per pack (highest mythic chance)

Accepted payments: USDC, ETH, USDm


SOFTWARE REQUIREMENTS
----------------------
You need all of the following installed before running the script:

  - Google Chrome browser
    https://www.google.com/chrome/

  - Bitget Wallet Chrome extension
    Download: https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak

  - Python 3.8 or newer
    https://www.python.org/downloads/
    IMPORTANT (Windows): Check "Add Python to PATH" during installation

  - Playwright Python package
    Open a terminal and run:
      pip install playwright
      playwright install chromium


STEP 1: START CHROME WITH REMOTE DEBUGGING
--------------------------------------------
IMPORTANT: Close ALL Chrome windows first.

Then open a terminal and run ONE of these commands:

WINDOWS (Command Prompt):
  "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --no-first-run --user-data-dir="%LOCALAPPDATA%\Google\Chrome-Debug"

WINDOWS (PowerShell):
  & "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --no-first-run --user-data-dir="$env:LOCALAPPDATA\Google\Chrome-Debug"

macOS:
  /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --no-first-run --user-data-dir="$HOME/Library/Application Support/Google/Chrome-Debug"

LINUX:
  google-chrome --remote-debugging-port=9222 --no-first-run --user-data-dir="$HOME/.config/google-chrome-debug"

Keep this Chrome window open.


STEP 2: INSTALL BITGET WALLET AND CREATE A BURNER
---------------------------------------------------
Use the Chrome-Debug window from Step 1.

1. Go to: https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak
2. Click "Add to Chrome"
3. Create a NEW burner wallet for this kit
4. Do NOT import an existing wallet and do NOT use your main wallet
5. Keep any wallet backup details private and offline; never paste them into this script or the config file
6. Copy only the burner wallet public address (starts with 0x)
7. Pin the extension to your Chrome toolbar (click puzzle icon > pin)


STEP 3: FILL IN YOUR WALLET INFO
----------------------------------
Open STEP2_Fill_your_wallet_info.json in a text editor (Notepad, VS Code, etc.).
Fill in the following fields:

  "address"         Your fresh burner Bitget Wallet address from Chrome-Debug (starts with 0x)
  "name"            Your display name (optional)
  "email"           Your email address (optional)
  "referral_code"   Referral code if you have one
  "burner_wallet_required"  Keep this true
  "pack_purchase_enabled"   Keep this false for the default safe review-only run
  "max_pack_budget_usd"     Spending limit if you intentionally enable paid purchases later
  "pack_tier"       Which pack page to review: starter, monster, or ultra
  "payment_token"   Payment token to use only if paid purchases are enabled

Save the file after editing.


STEP 4: RUN THE SCRIPT
------------------------
Open a NEW terminal (keep Chrome running in the other one).
Navigate to the monster folder containing this Kit and run:

WINDOWS:
  cd C:\path\to\your\kit\monster\folder
  python mnstr_auto.py

macOS / Linux:
  cd /path/to/your/kit/monster/folder
  python3 mnstr_auto.py

The script will guide you through each task step by step.
Follow the on-screen instructions.


WHAT HAPPENS DURING THE SCRIPT
---------------------------------
The script will:

  1. Open mnstr.xyz in Chrome
  2. Click "Connect Wallet" and try to select Bitget Wallet
     -> You confirm it is the fresh burner wallet and manually approve the connection in the Bitget popup
  3. Navigate to your chosen Pack tier (Starter/Monster/Ultra)
     -> Paid purchases are disabled by default
     -> You review odds, cost, and payment options without buying
     -> If you intentionally enabled paid purchases, you click and approve manually from the burner wallet only
  4. Navigate to the Marketplace
     -> You browse marketplace pages
     -> Any buy/list action is optional, manual, and burner-wallet-only
  5. Navigate to your Vault
     -> You review your collected graded cards
     -> Shipping, sale, or buyback actions are optional and manual
  6. Open the Leaderboard
     -> You check your weekly points and ranking
     -> Top players win bonus cards and free spins

At each step, the script will pause and tell you exactly what to do.
Press ENTER in the terminal after completing each action.


TIPS FOR MAXIMIZING POINTS & POTENTIAL AIRDROP
-------------------------------------------------
  - Never use or import your main wallet for this kit
  - Use a fresh burner wallet with only the funds you are willing to risk
  - If you intentionally buy packs, spread pack openings throughout the week instead of all at once
  - Stay ACTIVE on the marketplace safely; any buy/list action is manual
  - Points RESET every Sunday — plan your biggest activity mid-week
  - Watch for DOUBLE POINTS events — fastest way to climb rankings
  - STARTER packs ($50) give the best points-per-dollar ratio
  - MONSTER/ULTRA packs have better odds for rare graded cards
  - KEEP valuable cards in your vault for long-term potential
  - Consider the points-per-dollar value when choosing pack tiers


TROUBLESHOOTING
-----------------

"Could not connect to Chrome"
  -> Make sure Chrome is running with --remote-debugging-port=9222
  -> Close all other Chrome windows and try again

"Bitget Wallet not found"
  -> Install the extension in the debug Chrome profile:
     https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak
  -> Create a fresh burner wallet in that profile
  -> Do NOT import or use a main wallet

"Transaction failed"
  -> Paid transactions are optional and disabled by default
  -> If you intentionally enabled them, check that the burner wallet has enough USDC, ETH, or USDm for the pack
  -> Check that the burner wallet has enough gas tokens for the transaction

"Can I use my main wallet?"
  -> No. Use a fresh burner wallet only.
  -> Do not import a main wallet into the Chrome-Debug profile.

"Chrome path not found" (Windows)
  -> Right-click Chrome shortcut > Properties > copy the Target path
  -> Replace the path in the command above

"pip not found" or "python not found"
  -> Windows: Reinstall Python and CHECK "Add Python to PATH"
  -> macOS: Use python3 and pip3 instead
  -> Linux: sudo apt install python3 python3-pip


SECURITY NOTICE
-----------------
  - Use a fresh burner wallet only
  - Do NOT use or import your main wallet in the Chrome-Debug profile
  - This script NEVER asks for your private key or seed phrase
  - Paid pack purchases are disabled by default
  - All transactions require YOUR manual approval in Bitget Wallet
  - The script only reads your public wallet address from the config file
  - Pack purchases require YOUR explicit confirmation
  - The code is open source — you can read every line before running it


================================================================
Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
