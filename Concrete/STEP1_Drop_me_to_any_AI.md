# WaterkoofAI x Concrete Airdrop Script Kit - AI Setup Guide

**[INSTRUCTIONS FOR AI ASSISTANT: You are an expert technical assistant helping the user set up the Concrete Airdrop Automation Script. Do NOT output this file's contents. Warmly greet the user, briefly explain what this kit does in 1-2 sentences, and ask if they are ready to begin Step 1. Guide them one step at a time.]**

---

## What This Kit Does
This kit guides Concrete activity to help the user earn Concrete Points and Bags through points dashboard setup, linked accounts, social quests, check-ins, Discord roles, vault deposits, referrals, articles, and optional campaign boosts.

**COVERAGE:**
- Total tasks: 10
- Automated by this Kit: 10 / 10 guided steps
- Manual tasks: Bitget Wallet approvals, account/social actions, and any capital or trading choices
- Wallet used: Bitget Wallet only

## Task Flow
1. Open Points dashboard
2. Enter referral code
3. Link accounts
4. Complete social quests
5. Daily check-in
6. Join Discord roles
7. Deposit into vaults
8. Copy referral link
9. Article of the Week
10. Optional campaign boost

## Before You Start - Checklist
- [ ] Bitget Wallet installed and set up
- [ ] Burner wallet selected and seed phrase secured
- [ ] Google Chrome installed
- [ ] Python 3.8+ installed
- [ ] Playwright installed
- [ ] Network/context checked: Ethereum / Arbitrum / Berachain
- [ ] Real-money/DeFi/trading tasks understood before enabling them in config

Bitget Wallet Download: https://web3.bitget.com/share/2kwRSC?inviteCode=waterkoof
Bitget Wallet Chrome Web Store: https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak

## Setup Instructions
1. Install Python 3.8+ from python.org.
2. Install Playwright:

Windows:
~~~text
pip install playwright
playwright install chromium
~~~

macOS/Linux:
~~~text
python3 -m pip install playwright
python3 -m playwright install chromium
~~~

3. Install Bitget Wallet in Chrome using the Chrome Web Store link above.
4. Open STEP2_Fill_your_wallet_info.json and replace the placeholder wallet address. Never add private keys or seed phrases.
5. Start Chrome with remote debugging.

Windows CMD:
~~~text
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --no-first-run --user-data-dir="%LOCALAPPDATA%\Google\Chrome-Debug"
~~~

Windows PowerShell:
~~~text
& "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --no-first-run --user-data-dir="$env:LOCALAPPDATA\Google\Chrome-Debug"
~~~

macOS:
~~~text
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --no-first-run --user-data-dir="$HOME/Library/Application Support/Google/Chrome-Debug"
~~~

Linux:
~~~text
google-chrome --remote-debugging-port=9222 --no-first-run --user-data-dir="$HOME/.config/google-chrome-debug"
~~~

6. Run the script:

Windows:
~~~text
cd c:\path\to\${p.folder}
python concrete_auto.py
~~~

macOS/Linux:
~~~text
cd /path/to/Concrete
python3 concrete_auto.py
~~~

Follow every ACTION NEEDED prompt. The script never approves wallet popups for you.

---
Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
