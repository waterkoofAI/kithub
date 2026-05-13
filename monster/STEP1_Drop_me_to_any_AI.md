# WaterkoofAI x Monster Strategy (mnstr.xyz) Airdrop Script Kit — AI Setup Guide

Drop this file into any AI (ChatGPT, Claude, Gemini, etc.) and it will walk you through setup.

---

## What This Kit Does

This Kit automates **Monster Strategy (mnstr.xyz)** activity to help you earn weekly leaderboard points and build on-chain history for a potential future airdrop. It covers:

- Connecting your **Bitget Wallet** to mnstr.xyz
- Navigating to Packs and opening packs (Starter / Monster / Ultra)
- Browsing and trading on the Marketplace
- Checking your Vault for collected graded cards
- Monitoring the weekly Leaderboard for points ranking
- Strategy guidance for maximizing points

**COVERAGE:**
- Total tasks: 6
- Automated by this Kit: 6 / 6 (100%)
- Manual tasks: None (all wallet approvals & purchases are manual by design)
- Estimated impact: Weekly leaderboard points + on-chain activity history
- Wallet used: Bitget Wallet (Chrome extension)

---

## About Monster Strategy (mnstr.xyz)

Monster Strategy is an on-chain trading card platform where you:
- **Open packs** to pull real, professionally graded Pokémon cards (PSA, CGC, BGS)
- **Ship or sell back** — get physical cards delivered or sell at 85% FMV
- **Earn weekly points** — leaderboard resets every Sunday
- **Trade on the marketplace** — buy and sell cards with other collectors

**Pack Tiers:**
| Tier | Price | Description |
|------|-------|-------------|
| Starter | $50 | Most cost-effective for points |
| Monster | $250 | Better card value odds |
| Ultra | $1,250 | Highest mythic card chance |

**Accepted Payments:** USDC, ETH, USDm

---

## Before You Start — Checklist

Make sure you have all of these ready:

### Accounts & Wallets
- [ ] **Bitget Wallet** installed and set up (required for this Kit)
  - Download: https://web3.bitget.com/share/2kwRSC?inviteCode=waterkoof
  - Install the Chrome extension, create or import your wallet.
- [ ] Funds available for pack purchases (USDC, ETH, or USDm)
- [ ] Enough native gas tokens on the chain mnstr.xyz uses

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

### Step 3 — Install Bitget Wallet

1. Open Chrome and go to: https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak
2. Click "Add to Chrome" to install the Bitget Wallet extension
3. Create a new wallet or import an existing one
4. **Write down your recovery phrase and store it safely**
5. Make sure the extension is pinned to your Chrome toolbar

### Step 4 — Fill in Your Wallet Info

Open `STEP2_Fill_your_wallet_info.json` in any text editor and fill in your details:

```json
{
    "referral_code": "YOUR_REFERRAL_CODE",
    "pack_tier": "starter",
    "wallets": [
        {
            "address": "0xYourBitgetWalletAddress",
            "name": "YourDisplayName",
            "email": "your@email.com"
        }
    ]
}
```

**Important fields:**
- `address`: Your Bitget Wallet address (starts with 0x...)
- `pack_tier`: Which pack to open — `starter` ($50), `monster` ($250), or `ultra` ($1,250)
- `payment_token`: How you want to pay — `USDC`, `ETH`, or `USDm`

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

> **Note:** If Chrome opens but you don't see the Bitget Wallet extension, you may need to install it again in this debug Chrome profile. Go to https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak and add the extension.

### Step 6 — Run the Script

Open a NEW terminal window (keep Chrome running in the other one) and run:

```bash
cd path/to/your/kit/monster/folder
python mnstr_auto.py
```

The script will guide you through each task with clear prompts. Follow the on-screen instructions.

---

## What the Script Does (Step by Step)

1. **Opens mnstr.xyz** — Navigates to the Monster Strategy homepage
2. **Connects Bitget Wallet** — Auto-clicks Connect Wallet and selects Bitget Wallet (you approve manually)
3. **Pack Opening** — Navigates to your chosen pack tier. You review odds, purchase, and approve in Bitget Wallet
4. **Marketplace** — Opens the marketplace for browsing and trading. Marketplace activity earns points
5. **Vault** — Shows your collected graded cards. You can request shipping or sell back at 85% FMV
6. **Leaderboard** — Opens the weekly leaderboard so you can track your points and ranking

---

## Tips for Maximizing Points & Potential Airdrop

- **Open packs consistently** — Spread activity throughout the week, not all at once
- **Stay active on the marketplace** — Daily marketplace interaction earns extra points
- **Points reset every Sunday** — Plan your biggest activity mid-week for the best ranking
- **Watch for Double Points events** — These are the fastest way to climb the leaderboard
- **Starter packs for points** — $50 Starter packs give the best points-per-dollar ratio
- **Monster/Ultra for value** — Higher tiers have better odds for rare graded cards
- **Keep cards in vault** — Holding valuable cards could matter for a future airdrop snapshot

---

## Troubleshooting

**"Could not connect to Chrome"**
- Make sure Chrome is running with the `--remote-debugging-port=9222` flag
- Make sure no other Chrome instances are running (close all Chrome windows first)

**"Bitget Wallet not found" in the wallet selection dialog**
- The extension may not be installed in the debug Chrome profile
- Install it again: https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak

**"Transaction failed" or "Insufficient funds"**
- Make sure you have enough USDC, ETH, or USDm for the pack tier you selected
- Make sure you have enough gas tokens for the transaction

**Windows users: "Chrome path not found"**
- Right-click the Chrome shortcut → Properties → copy the Target field path
- Replace the path in the command above

---

Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
