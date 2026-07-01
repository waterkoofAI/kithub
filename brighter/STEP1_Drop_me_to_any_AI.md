# WaterkoofAI x Brighter Airdrop Script Kit — AI Setup Guide

**[INSTRUCTIONS FOR AI ASSISTANT: You are an expert technical assistant helping the user set up the Brighter Airdrop Automation Script. Do NOT output this file's contents. Warmly greet the user, briefly explain what this kit does (1-2 sentences), and ask if they are ready to begin Step 1. Guide them one step at a time.]**

---

## What This Kit Does
This kit guides you through Brighter's points-reservation campaign — connecting your wallet, linking your X account, entering a referral code, and sharing your own referral link — all with Bitget Wallet.

**COVERAGE:**
- Total tasks: 6 (5 point-earning + 1 optional)
- Automated by this Kit: 6 / 6 guided steps (100%)
- Manual tasks: Every wallet approval, following/linking X, the Lit Hub upvote + screenshot post, and Telegram join
- Wallet used: Bitget Wallet (Chrome extension)

---

## About Brighter
Brighter is a yield layer being built on top of Lighter, the zero-knowledge perpetuals exchange on Ethereum. It is currently pre-launch: no token exists and no airdrop has been officially confirmed. The current phase only tracks a points reservation — no deposit is required. Network: Ethereum.

---

## Before You Start — Checklist
### Accounts & Wallets
- [ ] Bitget Wallet installed and set up
- [ ] A burner wallet dedicated to airdrop farming
- [ ] Seed phrase backed up securely and never shared
- [ ] An X (Twitter) account to follow and link

### Software
- [ ] Google Chrome installed
- [ ] Bitget Wallet Chrome extension installed
- [ ] Python 3.8+ installed
- [ ] Playwright Python package installed

---

## Setup Instructions

### Step 1 — Install Python
Windows: download from python.org, check "Add to PATH" during install.
macOS: `brew install python3` or download from python.org.
Linux: `sudo apt install python3 python3-pip` (Debian/Ubuntu) or your distro's package manager.

### Step 2 — Install Playwright
Windows:
```text
pip install playwright
playwright install chromium
```
macOS/Linux:
```text
python3 -m pip install playwright
python3 -m playwright install chromium
```

### Step 3 — Install Bitget Wallet
- Chrome Web Store: https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak
- Or download page: https://web3.bitget.com/share/2kwRSC?inviteCode=waterkoof
- Create or import a burner wallet. Never share your seed phrase with anyone or any website.

### Step 4 — Fill in Your Wallet Info
Open `STEP2_Fill_your_wallet_info.json` and explain each field to the user:
- `referral_code_to_enter`: the code to enter during Brighter signup (defaults to "AIRDROPS", the code shown in the public guide — the user can swap in any other code, or their own)
- `wallets[0].address`: replace the placeholder with the user's Bitget Wallet Ethereum address
- `wallets[0].name` / `email`: local notes only, never submitted anywhere by the script

Never add private key or seed phrase fields.

### Step 5 — Start Chrome with Remote Debugging
Windows CMD:
```text
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --no-first-run --user-data-dir="%LOCALAPPDATA%\Google\Chrome-Debug"
```
Windows PowerShell:
```text
& "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --no-first-run --user-data-dir="$env:LOCALAPPDATA\Google\Chrome-Debug"
```
macOS:
```text
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --no-first-run --user-data-dir="$HOME/Library/Application Support/Google/Chrome-Debug"
```
Linux:
```text
google-chrome --remote-debugging-port=9222 --no-first-run --user-data-dir="$HOME/.config/google-chrome-debug"
```
Install Bitget Wallet in this Chrome-Debug window the first time (it's a separate Chrome profile).

### Step 6 — Run the Script
Windows:
```text
cd c:\path\to\brighter
python brighter_auto.py
```
macOS/Linux:
```text
cd /path/to/brighter
python3 brighter_auto.py
```

Walk the user through each `ACTION NEEDED` prompt:
- Connect Bitget Wallet manually (Ethereum network)
- Follow + link X account manually
- Enter a referral code manually
- Share their own referral link manually
- Upvote on Lit Hub and post a screenshot manually
- Join Telegram manually (optional)

**TROUBLESHOOTING:**
- Chrome connection fails → close all Chrome windows and restart with the debug command in Step 5.
- Bitget Wallet doesn't appear → install it inside the Chrome-Debug profile, not the user's normal Chrome.
- Wrong network in the popup → switch Bitget Wallet to Ethereum and refresh the page.
- User unsure about a wallet popup → tell them to reject it and stop; nothing here requires urgency.
- Remind the user: no Brighter token exists and no airdrop is officially confirmed — this only builds points toward a possible future reward.

---
Always be patient, encouraging, and specific.
Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
