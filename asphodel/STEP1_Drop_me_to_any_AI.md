# WaterkoofAI x Asphodel Airdrop Script Kit — AI Setup Guide

**[INSTRUCTIONS FOR AI ASSISTANT: You are an expert technical assistant helping the user set up the Asphodel Airdrop Automation Script. The user has just provided you with this file for context. Please do NOT just output the contents of this file back to the user. Instead, warmly greet the user, briefly explain what this kit does (1-2 sentences), and ask if they are ready to begin Step 1. Wait for their confirmation before moving to the next step. Guide them one step at a time through the "Setup Instructions" below. Only provide instructions for the current step, and help them troubleshoot any issues they may encounter.]**

---

## What This Kit Does

This Kit automates **Asphodel** activity to help you earn your place in the playtest and qualify for potential rewards. It covers:

- Connecting your **Bitget Wallet** to the Asphodel Playtest (Sepolia Testnet)
- Automating the wallet connection and prompting you to switch networks
- Setting up the playtest environment for you to acquire testnet $ONYX
- Guiding you through the "Festival of Consecration" event to secure the permanent mainnet item

**COVERAGE:**
- Total tasks: 4
- Automated by this Kit: 4 / 4 (100%)
- Manual tasks: None (all wallet approvals & gameplay are manual by design)
- Estimated impact: Potential mainnet item & share of USDC prize pool
- Wallet used: Bitget Wallet (Chrome extension)

---

## About Asphodel

Asphodel is a fully on-chain autobattler with roguelike mechanics built on Ethereum. The playtest takes place on the Sepolia Testnet.

**Requirements:**
- **Network:** Sepolia Testnet
- **Currency:** Testnet ETH (from Alchemy faucet)
- **Playtest Access:** Free to play

---

## Before You Start — Checklist

Make sure you have all of these ready:

### Accounts & Wallets
- [ ] **Bitget Wallet** installed and set up (REQUIRED for this Kit)
  - Download: https://web3.bitget.com/share/2kwRSC?inviteCode=waterkoof
  - Install the Chrome extension, create or import your wallet.
- [ ] Sepolia ETH available on the **Sepolia Testnet** for gas.
  - Faucet: https://alchemy.com/faucets/ethereum-sepolia

### Software
- [ ] **Google Chrome** installed
- [ ] **Bitget Wallet Chrome extension** installed and logged in
- [ ] **Python 3.8+** installed
- [ ] **Playwright** Python package installed

---

## Setup Instructions

### Step 1 — Install Python (if not already installed)

**Windows:**
1. Go to https://www.python.org/downloads/
2. Download the latest Python installer
3. Run the installer — **CHECK "Add Python to PATH"**
4. Click "Install Now"

**macOS:**
```bash
brew install python
```

**Linux:**
```bash
sudo apt update && sudo apt install python3 python3-pip
```

### Step 2 — Install Playwright

Open a terminal (Command Prompt on Windows, Terminal on macOS/Linux) and run:

```bash
pip install playwright
playwright install chromium
```

### Step 3 — Install Bitget Wallet (Skip if already installed)

1. Open Chrome and go to: https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak
2. Click "Add to Chrome" to install the Bitget Wallet extension
3. Create a new wallet or import an existing one
4. **Write down your recovery phrase and store it safely**
5. Make sure the extension is pinned to your Chrome toolbar

### Step 4 — Fill in Your Wallet Info

Open `STEP2_Fill_your_wallet_info.json` in any text editor and fill in your details:

```json
{
    "network": "sepolia",
    "wallets": [
        {
            "address": "0xYourBitgetWalletAddress",
            "name": "YourDisplayName",
            "email": "your@email.com"
        }
    ]
}
```

### Step 5 — Start Chrome with Remote Debugging

Close ALL Chrome windows first, then open a terminal and run:

**Windows:**
```
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --no-first-run --user-data-dir="%LOCALAPPDATA%\Google\Chrome-Debug"
```

**macOS:**
```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --no-first-run --user-data-dir="$HOME/Library/Application Support/Google/Chrome-Debug"
```

**Linux:**
```bash
google-chrome --remote-debugging-port=9222 --no-first-run --user-data-dir="$HOME/.config/google-chrome-debug"
```

> **Note:** If Chrome opens but you don't see the Bitget Wallet extension, you may need to install it again in this debug Chrome profile.

### Step 6 — Run the Script

Open a NEW terminal window (keep Chrome running in the other one) and run:

```bash
cd path/to/your/kit/asphodel/folder
python asphodel_auto.py
```

The script will guide you through each task with clear prompts. Follow the on-screen instructions.

---

Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
