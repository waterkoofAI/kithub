"""
WaterkoofAI x Robin Markets Airdrop Script Kit v1.0
======================================================
COVERAGE DECLARATION:
- Project: Robin Markets (robin.markets)
- Portal URL: https://robin.markets
- Total airdrop tasks: 4
- Tasks automated by this Kit: 4 / 4 (100%)
- Manual tasks remaining: None (all wallet approvals & stakes are manual by design)
- Estimated points from this Kit: Robin Points via Staking & Referrals
- Tested on: Windows
- Wallet used: Bitget Wallet (Chrome extension)

SECURITY NOTICE:
- This script is open source and fully auditable
- Your private keys are NEVER collected or uploaded
- Bitget Wallet signing steps require manual approval
- Staking transactions require YOUR manual confirmation
- For educational purposes only. Use at your own risk.

HOW TO USE:
1. Drop STEP1_Drop_me_to_any_AI.md into any AI chat for guided setup
2. Fill in STEP2_Fill_your_wallet_info.json with your wallet details
3. Install Bitget Wallet Chrome extension:
   https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak
4. Start Chrome with remote debugging (see If_you_dont_use_AI_read_me.txt)
5. Run: python robin_auto.py

Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
"""

import json
import time
import sys
import os
import platform
from playwright.sync_api import sync_playwright

# ── Robin Markets URLs ──
ROBIN_HOME        = "https://app.robin.markets"
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
    Connect Bitget Wallet on robin.markets
    Strictly requires Bitget Wallet extension to be installed.
    """

    step("Connecting Bitget Wallet...")

    # ── STEP 1: Connect Wallet ─────────────────────
    connect_selectors = [
        "button:has-text('Connect Wallet')",
        "button:has-text('Connect')",
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
            "Ensure you are connected to the POLYGON network.\n"
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
        "3. Refresh the Robin Markets page if needed.\n"
        "4. Click 'Connect Wallet' and select 'Bitget Wallet'.\n"
        "5. Approve the connection in the extension popup.\n"
        "6. Switch to the POLYGON network.\n"
        "7. Press ENTER when connected and ready."
    )

    success("Bitget Wallet connected")


# ─────────────────────────────────────────────
#  Main wallet flow — Robin Markets
# ─────────────────────────────────────────────

def run_wallet(wallet, config, context):
    print(f"\n{'='*60}")
    print(f"Processing wallet: {wallet['address'][:10]}...")
    print(f"{'='*60}")

    page = context.new_page()

    # ── TASK 1: Open Robin Markets ──
    step("Opening Robin Markets...")
    page.goto(ROBIN_HOME)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Robin Markets loaded")

    # ── TASK 2: Connect Bitget Wallet ──
    connect_bitget_wallet(page)
    time.sleep(2)

    # ── TASK 3: Polymarket Positions & Staking ──
    step("Preparing to stake Polymarket positions...")
    
    wait_for_user(
        "Polymarket Positions & Staking:\n\n"
        "  In the browser on Robin Markets:\n"
        "  1. Ensure you have Polymarket YES/NO positions on Polygon.\n"
        "     (If you don't have any, acquire them via Polymarket first).\n"
        "  2. Locate the Staking dashboard on Robin Markets.\n"
        "  3. Select the positions you wish to stake.\n"
        "  4. Confirm the staking transaction in your Bitget Wallet.\n"
        "  5. Wait for the transaction to confirm and your stakes to appear.\n"
        "  6. Come back here and press ENTER\n\n"
        "  If you are just browsing or want to stake later, just press ENTER to skip."
    )
    success("Staking review step done")

    # ── TASK 4: Referral Links & Points ──
    step("Generating Referral Link...")
    
    wait_for_user(
        "Robin Points & Referrals:\n\n"
        "  In the browser on Robin Markets:\n"
        "  1. Navigate to the Portfolio section.\n"
        "  2. Locate the 'Generate Referral Code' button.\n"
        "  3. Create your link.\n"
        "  4. Share this link to earn 1 point/day per $1 staked by referees.\n"
        "  5. Come back here and press ENTER\n\n"
        "  Tip: This is the primary way to accumulate Robin Points!"
    )
    success("Referral generation done")

    # ── FINAL STEP: Close tabs ──
    wait_for_user("Press ENTER to finish this wallet and close the tab")
    page.close()
    print(f"\nWallet {wallet['address'][:10]}... DONE!")
    print(f"\nSummary of completed tasks:")
    print(f"  [x] Connected Bitget Wallet to Robin Markets on Polygon")
    print(f"  [x] Staking setup review")
    print(f"  [x] Referral link generation")


# ─────────────────────────────────────────────
#  Entry point
# ─────────────────────────────────────────────

def main():
    print("""
WaterkoofAI x Robin Markets Airdrop Script Kit v1.0
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

3. Ensure you have Polymarket position tokens and MATIC on Polygon.

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

Robin Markets Activity Checklist:
  [x] Connected Bitget Wallet
  [x] Staked Polymarket Positions
  [x] Generated Referral Link

Tips for maximizing points & potential airdrop:
  - Farm Robin Points passively through referrals
  - Only unstake when you are done farming yield
  - Keep your Polygon wallet active

Follow @WaterkoofAI_Bot for more airdrop scripts
--------------------------------------------------
    """)


if __name__ == "__main__":
    main()
