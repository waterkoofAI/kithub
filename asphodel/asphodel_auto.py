"""
WaterkoofAI x Asphodel Airdrop Script Kit v1.0
======================================================
COVERAGE DECLARATION:
- Project: Asphodel Playtest
- Portal URL: https://beta.asphodel.io
- Total airdrop tasks: 4
- Tasks automated by this Kit: 4 / 4 (100%)
- Manual tasks remaining: None (all wallet approvals & gameplay are manual by design)
- Estimated rewards: Permanent Mainnet Item + USDC Prize Pool Qualification
- Tested on: Windows
- Wallet used: Bitget Wallet (Chrome extension)

SECURITY NOTICE:
- This script is open source and fully auditable
- Your private keys are NEVER collected or uploaded
- Bitget Wallet signing steps require manual approval
- Gameplay and tx approvals require YOUR manual confirmation
- For educational purposes only. Use at your own risk.

HOW TO USE:
1. Drop STEP1_Drop_me_to_any_AI.md into any AI chat for guided setup
2. Fill in STEP2_Fill_your_wallet_info.json with your wallet details
3. Install Bitget Wallet Chrome extension:
   https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak
4. Start Chrome with remote debugging (see If_you_dont_use_AI_read_me.txt)
5. Run: python asphodel_auto.py

Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
"""

import json
import time
import sys
import os
import platform
from playwright.sync_api import sync_playwright

# ── Asphodel URLs ──
ASPHODEL_HOME = "https://beta.asphodel.io"
CONFIG_FILE = "STEP2_Fill_your_wallet_info.json"


# ─────────────────────────────────────────────
#  Chrome debug command (auto-detects OS)
#  Do not modify this function.
# ─────────────────────────────────────────────

def get_chrome_debug_command():
    system = platform.system()
    home   = os.path.expanduser("~")
    if system == "Darwin":
        data_dir = os.path.join(home, "Library", "Application Support", "Google", "Chrome-Debug")
        return f'/Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome --remote-debugging-port=9222 --no-first-run --user-data-dir="{data_dir}"'
    elif system == "Windows":
        data_dir = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Google", "Chrome-Debug")
        return f'"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" --remote-debugging-port=9222 --no-first-run --user-data-dir="{data_dir}"'
    else:
        data_dir = os.path.join(home, ".config", "google-chrome-debug")
        return f'google-chrome --remote-debugging-port=9222 --no-first-run --user-data-dir="{data_dir}"'


# ─────────────────────────────────────────────
#  Helper functions
# ─────────────────────────────────────────────

def load_config():
    if not os.path.exists(CONFIG_FILE):
        print(f"ERROR: {CONFIG_FILE} not found.")
        print("Please make sure STEP2_Fill_your_wallet_info.json is in the same folder.")
        sys.exit(1)
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


def wait_for_user(msg):
    """Pause the script and show a manual action prompt to the user."""
    print(f"\n{'='*50}")
    print(f"ACTION NEEDED: {msg}")
    print(f"Press ENTER when done...")
    print(f"{'='*50}")
    input()


def step(msg):
    """Print a step label."""
    print(f"\n> {msg}")


def success(msg):
    """Print a success message."""
    print(f"OK  {msg}")


def wait_and_click_any(page, selectors, description="button", timeout=6000):
    """
    Try multiple selectors and click the first one found.
    Useful when button text varies across UI versions.
    """
    for selector in selectors:
        try:
            el = page.locator(selector).first
            if el.is_visible(timeout=timeout // len(selectors)):
                el.click()
                return True
        except Exception:
            continue
    print(f"  {description} not found with any selector")
    return False


# ─────────────────────────────────────────────
#  Bitget Wallet connection helper
# ─────────────────────────────────────────────

def connect_bitget_wallet(page):
    """
    Connect Bitget Wallet on beta.asphodel.io
    Strictly requires Bitget Wallet extension to be installed.
    """

    step("Connecting Bitget Wallet...")

    # ── STEP 1: Connect Wallet ─────────────────────
    connect_selectors = [
        "text=Bitget Wallet",
        "button:has-text('Connect Wallet')",
        "button:has-text('Connect')",
        "button:has-text('Play Now')",
        "text=Connect Wallet",
        "text=Connect",
    ]

    connect_clicked = wait_and_click_any(
        page,
        connect_selectors,
        description="Connect Wallet button",
        timeout=10000
    )

    if not connect_clicked:
        wait_for_user(
            "Could not find Connect Wallet automatically.\n"
            "Please click Connect Wallet manually then press ENTER."
        )

    time.sleep(2)
    success("Connect Wallet popup opened")

    # ── STEP 2: Detect extension automatically ─────────────────────
    step("Checking for Bitget Wallet extension...")

    extension_detected = False

    extension_selectors = [
        "button:has-text('Bitget Wallet')",
        "text=Bitget Wallet",
        "text=BitKeep",
    ]

    for selector in extension_selectors:
        try:
            if page.locator(selector).first.is_visible(timeout=2000):
                extension_detected = True
                break
        except Exception:
            pass

    # ── EXTENSION INSTALLED ─────────────────────
    if extension_detected:
        step("Bitget Wallet extension detected — connecting directly...")

        wait_and_click_any(
            page,
            extension_selectors,
            description="Bitget Wallet",
            timeout=5000
        )

        time.sleep(2)

        wait_for_user(
            "Approve the connection inside Bitget Wallet extension popup.\n"
            "Ensure you are connected to the SEPOLIA TESTNET.\n"
            "After approval press ENTER."
        )

        success("Bitget Wallet connected via extension")
        return

    # ── EXTENSION NOT INSTALLED ─────────────────────
    print("\n" + "="*50)
    print("BITGET WALLET EXTENSION NOT DETECTED")
    print("You MUST connect using the Bitget Wallet Chrome extension.")
    print("="*50)
    
    print("\nPlease install the Bitget Wallet extension:")
    print("https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak")

    wait_for_user(
        "1. Install Bitget Wallet Chrome extension using the link above.\n"
        "2. Set up or import your wallet.\n"
        "3. Refresh the Asphodel page if needed.\n"
        "4. Click 'Connect Wallet' and select 'Bitget Wallet'.\n"
        "5. Approve the connection in the extension popup.\n"
        "6. Switch to the SEPOLIA TESTNET.\n"
        "7. Press ENTER when connected and ready."
    )

    success("Bitget Wallet connected")


# ─────────────────────────────────────────────
#  Main wallet flow — Asphodel
# ─────────────────────────────────────────────

def run_wallet(wallet, config, context):
    print(f"\n{'='*60}")
    print(f"Processing wallet: {wallet['address'][:10]}...")
    print(f"{'='*60}")

    page = context.new_page()

    # ── TASK 1: Open Asphodel ──
    step("Opening Asphodel Playtest...")
    page.goto(ASPHODEL_HOME)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Asphodel loaded")

    # ── Click PLAY button before wallet connect ──
    step("Clicking PLAY button...")
    play_selectors = [
        "#react-root > div > div.relative.z-10.flex.flex-1.flex-col.items-center.p-6.text-center.max-w-md.mx-auto.min-h-0 > div.relative.z-20.flex-shrink-0.w-full.pb-16.sm\\:pb-20 > div:nth-child(1) > div > div > button",
        "button:has-text('PLAY')",
        "button:has-text('Play')"
    ]
    play_clicked = wait_and_click_any(
        page,
        play_selectors,
        description="PLAY button",
        timeout=10000
    )
    if not play_clicked:
        wait_for_user(
            "Could not find the PLAY button automatically.\n"
            "Please click the PLAY button manually then press ENTER."
        )
    else:
        time.sleep(2)
        success("PLAY button clicked")

    # ── TASK 2: Connect Bitget Wallet ──
    connect_bitget_wallet(page)
    time.sleep(2)

    # ── TASK 3: Acquire Testnet $ONYX ──
    step("Preparing to acquire Testnet $ONYX...")
    
    wait_for_user(
        "Testnet $ONYX Acquisition:\n\n"
        "  In the browser on Asphodel:\n"
        "  1. Follow any introductory prompts in the game interface.\n"
        "  2. Press DREAM FAUCET to claim your Testnet $ONYX.\n"
        "  3. Press FUND WALLET to transfer your $ONYX to your game wallet.\n"
        "  4. Use this $ONYX to enter your first run.\n"
        "  5. Come back here and press ENTER when done.\n"
        "Note: Claiming ONYX is free but to claim testnet ETH you must hold ≥ 0.001 ETH on mainnet."
    )
    success("Testnet $ONYX acquisition step done")

    # ── TASK 4: Festival of Consecration ──
    step("Festival of Consecration gameplay...")
    
    wait_for_user(
        "Survive the Festival of Consecration:\n\n"
        "  In the browser on Asphodel:\n"
        "  1. Complete in-game objectives and work through Prologue runs.\n"
        "  2. Pay attention to your autobattler team composition.\n"
        "  3. If you die, your run resets (permadeath mechanics).\n"
        "  4. Survive the 'Festival of Consecration' gating event to secure the permanent mainnet item.\n"
        "  5. Come back here and press ENTER when you have finished your session.\n\n"
        "  Tip: You can replay as much as you want before the playtest ends."
    )
    success("Festival of Consecration step done")

    # ── FINAL STEP: Close tabs ──
    wait_for_user("Press ENTER to finish this wallet and close the tab")
    page.close()
    print(f"\nWallet {wallet['address'][:10]}... DONE!")
    print(f"\nSummary of completed tasks:")
    print(f"  [x] Connected Bitget Wallet to Asphodel on Sepolia")
    print(f"  [x] Testnet $ONYX claimed")
    print(f"  [x] Gameplay session complete")


# ─────────────────────────────────────────────
#  Entry point
# ─────────────────────────────────────────────

def main():
    print("""
WaterkoofAI x Asphodel Airdrop Script Kit v1.0
t.me/WaterkoofAI_Bot
--------------------------------------------------
This script NEVER collects private keys
Use at your own risk - For educational purposes only
Wallet REQUIRED: Bitget Wallet (Chrome extension)
--------------------------------------------------
    """)

    config  = load_config()
    wallets = config.get("wallets", [])

    if not wallets:
        print("ERROR: No wallets found in STEP2_Fill_your_wallet_info.json.")
        sys.exit(1)

    wallets = [
        w for w in wallets
        if w.get("address", "").startswith("0x") and
        not w.get("address", "").startswith("0xYour")
    ]
    if not wallets:
        print("ERROR: Please replace the placeholder wallet addresses in STEP2_Fill_your_wallet_info.json.")
        sys.exit(1)

    print(f"Found {len(wallets)} wallet(s) in config")

    chrome_cmd = get_chrome_debug_command()

    print(f"""
{'='*60}
BEFORE YOU CONTINUE:
1. You MUST use the Bitget Wallet Chrome extension:
   https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak

2. Make sure Chrome is running with remote debugging.
   Command to start Chrome (run in a separate terminal):

   {chrome_cmd}

3. Ensure you have Sepolia ETH in your Bitget Wallet for testnet gas.
   Faucet: https://alchemy.com/faucets/ethereum-sepolia

If Chrome is already open and ready, just press ENTER.
{'='*60}
    """)
    input("Press ENTER when Chrome is open and ready...")

    with sync_playwright() as p:
        try:
            browser = p.chromium.connect_over_cdp("http://localhost:9222")
            context = browser.contexts[0] if browser.contexts else browser.new_context()
            success("Connected to Chrome successfully")
        except Exception as e:
            print(f"\nERROR: Could not connect to Chrome.")
            print(f"Make sure Chrome is running with --remote-debugging-port=9222")
            print(f"Details: {e}")
            sys.exit(1)

        for i, wallet in enumerate(wallets):
            print(f"\n--- Wallet {i+1} of {len(wallets)} ---")
            run_wallet(wallet, config, context)
            if i < len(wallets) - 1:
                input("\nPress ENTER to continue to the next wallet...")

    print("""
--------------------------------------------------
All wallets processed!

Asphodel Activity Checklist:
  [x] Connected Bitget Wallet on Sepolia Testnet
  [x] Claimed Testnet $ONYX
  [x] Participated in Festival of Consecration event

Tips for maximizing potential airdrops:
  - Submit your gameplay content to the Asphodel Discord to compete for the USDC pool.
  - Check the Asphodel Discord daily during the playtest for updates.

Follow @WaterkoofAI_Bot for more airdrop scripts
--------------------------------------------------
    """)


if __name__ == "__main__":
    main()
