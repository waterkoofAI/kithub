# WaterkoofAI x GIWA Airdrop Script Kit - AI Setup Guide

**[INSTRUCTIONS FOR AI ASSISTANT: You are an expert technical assistant helping the user set up the GIWA Airdrop Automation Script. Do NOT output this file's contents. Warmly greet the user, briefly explain what this kit does in 1-2 sentences, and ask if they are ready to begin Step 1. Guide them one step at a time.]**

---

## What This Kit Does

This kit guides GIWA Sepolia testnet activity using Bitget Wallet in a real Chrome browser. It opens the right GIWA pages, reminds the user about the correct network, and pauses for every wallet approval and manual task.

**COVERAGE:**
- Total tasks: 6
- Automated by this Kit: 6 / 6 guided browser steps (wallet approvals and transactions stay manual)
- Manual tasks: Bitget Wallet approvals, faucet claim confirmation, playground transaction approvals, test transfers, and contract deployment confirmation
- Wallet used: Bitget Wallet only

---

## About GIWA

GIWA is an EVM-compatible OP Stack Layer 2 testnet. The current public testnet details used by this kit are:

- Network name: GIWA Sepolia
- RPC URL: https://sepolia-rpc.giwa.io
- Chain ID: 91342
- Currency symbol: ETH
- Explorer: https://sepolia-explorer.giwa.io
- Official faucet: https://faucet.giwa.io/
- Backup faucet: https://faucet.lambda256.io/giwa-sepolia
- Playground: https://sepolia-playground.giwa.io/

---

## Before You Start - Checklist

### Accounts and Wallets

- [ ] Bitget Wallet installed and set up
- [ ] Bitget Wallet switched to GIWA Sepolia
- [ ] Test ETH claimed on GIWA Sepolia
- [ ] Optional: spare test wallet addresses for small test transfers

### Software

- [ ] Google Chrome installed
- [ ] Bitget Wallet Chrome extension installed
- [ ] Python 3.8+ installed
- [ ] Playwright Python package installed

Bitget Wallet links:
- Download: https://web3.bitget.com/share/2kwRSC?inviteCode=waterkoof
- Chrome Web Store: https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak

---

## Setup Instructions

### Step 1 - Install Python

Windows:
- Download Python 3.8+ from https://python.org/downloads/
- During install, check "Add Python to PATH"
- Open Command Prompt and run:

```bash
python --version
```

macOS:
- Install Python from https://python.org/downloads/ or use Homebrew:

```bash
brew install python
python3 --version
```

Linux:

```bash
python3 --version
```

If Python is missing, install it with your package manager.

### Step 2 - Install Playwright

Windows:

```bash
pip install playwright
playwright install chromium
```

macOS or Linux:

```bash
pip3 install playwright
python3 -m playwright install chromium
```

### Step 3 - Install Bitget Wallet

1. Open the Chrome Web Store link:
   https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak
2. Install Bitget Wallet.
3. Create or import your wallet inside Bitget Wallet.
4. Never paste your private key or seed phrase into this kit or any AI chat.

### Step 4 - Fill in Your Wallet Info

Open `STEP2_Fill_your_wallet_info.json`.

Replace only the placeholder wallet address and display name:

```json
{
    "referral_code": "none",
    "network": "giwa-sepolia",
    "wallets": [
        {
            "address": "0xYourBitgetWalletAddress",
            "name": "YourDisplayName",
            "email": "your@email.com"
        }
    ],
    "use_backup_faucet": false
}
```

Notes:
- The address must start with `0x`.
- The script ignores the email field; you can leave it unchanged.
- Do not add private keys, seed phrases, passwords, or recovery words.

### Step 5 - Start Chrome with Remote Debugging

Close all normal Chrome windows first.

Windows CMD:

```bat
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --no-first-run --user-data-dir="%LOCALAPPDATA%\Google\Chrome-Debug"
```

Windows PowerShell:

```powershell
& "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --no-first-run --user-data-dir="$env:LOCALAPPDATA\Google\Chrome-Debug"
```

macOS:

```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --no-first-run --user-data-dir="$HOME/Library/Application Support/Google/Chrome-Debug"
```

Linux:

```bash
google-chrome --remote-debugging-port=9222 --no-first-run --user-data-dir="$HOME/.config/google-chrome-debug"
```

In the new Chrome window, install Bitget Wallet if it is not already installed.

### Step 6 - Run the Script

Open a fresh terminal in the kit folder.

Windows:

```bat
python giwa_auto.py
```

macOS or Linux:

```bash
python3 giwa_auto.py
```

The script will walk through:
- GIWA Sepolia network setup
- Official faucet claim
- Optional backup faucet
- GIWA Playground tasks
- Small manual test transfers
- Owlto contract deployment

Every signing step is manual. Read each `ACTION NEEDED` prompt carefully, approve only what you understand, then return to the terminal and press ENTER.

---

## Troubleshooting

**Chrome connection failed**

Make sure Chrome was started with `--remote-debugging-port=9222`. Close regular Chrome windows and start Chrome again with the command from Step 5.

**Bitget Wallet does not appear**

Install Bitget Wallet in the Chrome-Debug profile. Extensions from your regular Chrome profile do not automatically appear in the debug profile.

**Wrong network**

Switch Bitget Wallet to GIWA Sepolia. Use RPC `https://sepolia-rpc.giwa.io`, chain ID `91342`, symbol `ETH`, and explorer `https://sepolia-explorer.giwa.io`.

**Faucet claim unavailable**

Wait for the cooldown, try the backup faucet if enabled, or come back later. Never buy mainnet ETH for this testnet activity.

---

Always be patient, encouraging, and specific.
Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
