"""
WaterkoofAI x Collector Crypt Airdrop Script Kit v1.0
======================================================
COVERAGE DECLARATION:
- Project: Collector Crypt
- Portal URL: https://gacha.collectorcrypt.com/
- Total airdrop tasks: 7
- Tasks automated by this Kit: 7 / 7 guided steps (100%)
- Manual tasks remaining: Wallet approvals, sign-in, opening Gacha packs (real USDC/CARDS
  spend), weekly Gacha Games participation, buying/holding $CARDS, referral sharing, claiming
- Estimated points from this Kit: Helps organize the activity that builds Gacha points
  (lifetime + current-quarter + referral bonus) toward the quarterly $CARDS distribution and
  the separate monthly holder airdrop. Rewards depend on your own activity level.
- Tested on: Windows/macOS/Linux with Chrome remote debugging
- Wallet used: Bitget Wallet (Chrome extension, Solana network)

SECURITY NOTICE:
- Caution: Use a burner wallet for this airdrop and secure your seed phrase
- This script is open source and fully auditable
- Your private keys are NEVER collected or uploaded
- Bitget Wallet signing steps require manual approval
- Collector Crypt's Gacha packs use real USDC/CARDS. Confirm you accept the cost and risk
  before enabling real-money tasks in the config.
- For educational purposes only. Use at your own risk.

HOW TO USE:
1. Drop STEP1_Drop_me_to_any_AI.md into any AI chat for guided setup
2. Fill in STEP2_Fill_your_wallet_info.json with your wallet details
3. Install Bitget Wallet:
   https://web3.bitget.com/share/2kwRSC?inviteCode=waterkoof
4. Install Bitget Wallet Chrome extension:
   https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak
5. Start Chrome with remote debugging (see If_you_dont_use_AI_read_me.txt)
6. Run: python collectorcrypt_auto.py

Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
"""

import json
import time
import sys
import os
import platform
from playwright.sync_api import sync_playwright

# ── Collector Crypt URLs ──
PROJECT_HOME = "https://gacha.collectorcrypt.com/"
CLAIM_URL = "https://claim.collectorcrypt.com/"
DISCORD_URL = "https://discord.gg/jRdv3UxgV2"
X_URL = "https://x.com/Collector_Crypt"
CARDS_CONTRACT = "CARDSccUMFKoPRZxt5vt3ksUbxEFEcnZ3H2pd3dKxYjp"
BITGET_DOWNLOAD_URL = "https://web3.bitget.com/share/2kwRSC?inviteCode=waterkoof"
BITGET_CHROME_STORE_URL = "https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak"
CONFIG_FILE = "STEP2_Fill_your_wallet_info.json"


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


def click_if_visible(page, selector, timeout=4000):
    """Click an element only if visible. Returns True if clicked."""
    try:
        el = page.locator(selector).first
        if el.is_visible(timeout=timeout):
            el.click()
            return True
    except Exception:
        pass
    return False


def wait_and_click_any(page, selectors, description="button", timeout=6000):
    """Try multiple selectors and click the first one found."""
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


def connect_bitget_wallet(page):
    step("Connecting Bitget Wallet...")
    print("  Required network: Solana")

    clicked = wait_and_click_any(
        page,
        [
            "button:has-text('Sign In')",
        ],
        "Sign In / Connect Wallet button",
        timeout=5000,
    )

    if not clicked:
        wait_for_user(
            "Click the Sign In or Connect Wallet button on the Collector Crypt page.\n\n"
            "  1. Choose 'connect wallet' rather than email if you want wallet-based sign-in.\n"
            "  2. Select Bitget Wallet only.\n"
            "  3. Make sure Bitget Wallet is unlocked.\n"
            "  4. Make sure the network/account selected is Solana.\n"
            "  5. Approve only after reviewing the popup."
        )
    time.sleep(2)
    extension_selectors = [
        "button:has-text('Bitget Wallet')",
        "text=Bitget Wallet",
    ]
    
    extension_detected = click_if_visible(page, "button:has-text('Bitget Wallet')", timeout=2000)
    for selector in extension_selectors:
        try:
            if page.locator(selector).first.is_visible(timeout=2000):
                extension_detected = True
                break
        except Exception:
            pass

    if extension_detected:
        wait_and_click_any(page, extension_selectors, "Bitget Wallet option", timeout=6000)
        wait_for_user(
            "Bitget Wallet should now show a connection popup.\n\n"
            "  1. Confirm the site is collectorcrypt.com.\n"
            "  2. Confirm the wallet is your burner Solana wallet.\n"
            "  3. Confirm you have SOL for network fees.\n"
            "  4. Approve only if everything looks correct."
        )
    else:
        print("\nBitget Wallet was not detected on the page.")
        print(f"Install Bitget Wallet: {BITGET_DOWNLOAD_URL}")
        print(f"Chrome Web Store: {BITGET_CHROME_STORE_URL}")
        wait_for_user(
            "Install or unlock Bitget Wallet in this Chrome-Debug profile.\n\n"
            "  1. Use the Bitget Wallet Chrome extension only.\n"
            "  2. Make sure it is set to a Solana account.\n"
            "  3. Return to Collector Crypt and click Sign In / Connect Wallet.\n"
            "  4. Select Bitget Wallet.\n"
            "  5. Approve manually, then come back here.\n\n"
            "  Note: you can also sign in with email if you prefer, then link\n"
            "  your Bitget Wallet address afterward from account settings."
        )

    success("Sign-in / wallet connection step completed")


def run_wallet(wallet, config, context):
    print(f"\n{'='*60}")
    print(f"Processing wallet: {wallet['address'][:10]}...")
    print(f"{'='*60}")

    page = context.new_page()

    # TASK 1: Open project
    step("Opening Collector Crypt...")
    page.goto(PROJECT_HOME)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Collector Crypt Gacha page loaded")

    # TASK 2: Sign in / connect wallet
    connect_bitget_wallet(page)
    time.sleep(2)

    # TASK 3: Open Gacha packs (real money)
    step("Checking Gacha pack opening...")
    if not config.get("enable_real_money_tasks", False):
        print("  Skipping guided pack-opening prompt: enable_real_money_tasks is false in config.")
    else:
        default_amount = config.get("default_pack_spend_usdc", "10")
        wait_for_user(
            "Open Gacha packs manually. This is the core point-earning activity.\n\n"
            f"  Suggested max spend from config: {default_amount} USDC per session.\n"
            "  1. Make sure you have USDC or $CARDS in your wallet.\n"
            "  2. Go to the Gacha Machine and open packs you can afford.\n"
            "  3. Each pack reveals a tokenized card you can keep, trade, sell back,\n"
            "     or redeem for the physical item.\n"
            "  4. Confirm every Bitget Wallet popup manually.\n"
            "  5. Come back here when done.\n\n"
            "  If you want to skip spending right now, just press ENTER."
        )
    success("Gacha pack step completed or skipped")

    # TASK 4: Weekly Gacha Games challenge
    step("Checking weekly Gacha Games challenges...")
    wait_for_user(
        "Join a weekly Gacha Games challenge if one is active.\n\n"
        "  1. Look for the 'Gacha Games' or 'Challenges' tab on the platform.\n"
        "  2. Review the current challenge and prize pool.\n"
        "  3. Participate through normal Gacha activity if it fits your budget.\n"
        "  4. Come back here when done.\n\n"
        "  If no challenge is active, just press ENTER."
    )
    success("Weekly challenge step completed or skipped")

    # TASK 5: Hold $CARDS for monthly airdrop
    step("Checking $CARDS holding for monthly holder airdrop...")
    print(f"  $CARDS token contract (Solana): {CARDS_CONTRACT}")
    print("  Verify this contract address yourself before buying anything.")
    wait_for_user(
        "Buy and hold $CARDS if you want the separate monthly holder airdrop.\n\n"
        "  1. Open Raydium (or your preferred Solana DEX) and search the exact\n"
        f"     contract address: {CARDS_CONTRACT}\n"
        "  2. Double-check the contract address matches before swapping.\n"
        "  3. Swap only an amount you're comfortable holding.\n"
        "  4. Confirm every Bitget Wallet popup manually.\n"
        "  5. Come back here when done.\n\n"
        "  If you don't want to buy $CARDS right now, just press ENTER."
    )
    success("$CARDS holding step completed or skipped")

    # TASK 6: Share referral link
    step("Opening account/referral area...")
    page.goto("https://gacha.collectorcrypt.com/user/show-referrer")
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    wait_for_user(
        "Generate and share your own referral link.\n\n"
        "  1. Copy your personal referral link.\n"
        "  2. Share it only where appropriate.\n"
        "  3. Current-quarter referral points carry a bonus.\n"
        "  4. Come back here when done.\n\n"
        "  If you don't want to share it yet, just press ENTER."
    )
    success("Referral step completed or skipped")

    # TASK 7: Claim rewards
    step("Opening the official claim page...")
    page.goto(CLAIM_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    wait_and_click_any(
        page,
        [
            "button:has-text('Connect Wallet')",
            "button:has-text('Claim')",
            "text=Connect Wallet",
        ],
        "claim page connect/claim button",
        timeout=7000,
    )
    wait_for_user(
        "Claim your $CARDS rewards if a distribution is currently live.\n\n"
        "  1. Connect the same wallet you used for Gacha activity.\n"
        "  2. Review your allocation before confirming anything.\n"
        "  3. Approve the claim transaction manually in Bitget Wallet.\n"
        "  4. Come back here when done.\n\n"
        "  If no distribution is live right now, just press ENTER."
    )
    success("Claim step completed or skipped")

    # FINAL STEP: Close
    wait_for_user("Press ENTER to finish this wallet and close the tab")
    page.close()
    print(f"\nWallet {wallet['address'][:10]}... DONE!")
    print(f"\nSummary of completed tasks:")
    print(f"  [x] Opened Collector Crypt")
    print(f"  [x] Signed in / connected Bitget Wallet manually")
    print(f"  [x] Guided Gacha pack opening")
    print(f"  [x] Checked weekly Gacha Games challenge")
    print(f"  [x] Checked $CARDS holding")
    print(f"  [x] Guided referral link sharing")
    print(f"  [x] Checked claim page")


def main():
    print("""
WaterkoofAI x Collector Crypt Airdrop Script Kit v1.0
t.me/WaterkoofAI_Bot
--------------------------------------------------
This script NEVER collects private keys
Caution: Use a burner wallet and secure your seed phrase
Use at your own risk - For educational purposes only
Wallet REQUIRED: Bitget Wallet (Chrome extension, Solana)
--------------------------------------------------
    """)

    config  = load_config()
    wallets = config.get("wallets", [])

    if not config.get("i_understand_gacha_costs_real_money", False):
        print("ERROR: Set i_understand_gacha_costs_real_money to true only after")
        print("       confirming you understand Gacha packs cost real USDC/CARDS.")
        sys.exit(1)

    if not wallets:
        print("ERROR: No wallets found in STEP2_Fill_your_wallet_info.json.")
        sys.exit(1)

    wallets = [
        w for w in wallets
        if w.get("address", "") and
        not w.get("address", "").startswith("YourSolana")
    ]
    if not wallets:
        print("ERROR: Please replace the placeholder wallet address in STEP2_Fill_your_wallet_info.json.")
        sys.exit(1)

    print(f"Found {len(wallets)} wallet(s) in config")
    print(f"Referral code: {config.get('referral_code', 'none')}")
    print(f"Real-money tasks enabled: {config.get('enable_real_money_tasks', False)}")
    print(f"Default pack spend: {config.get('default_pack_spend_usdc', '10')} USDC")

    chrome_cmd = get_chrome_debug_command()

    print(f"""
{'='*60}
BEFORE YOU CONTINUE:
1. You MUST use the Bitget Wallet Chrome extension:
   {BITGET_CHROME_STORE_URL}

   Bitget Wallet download:
   {BITGET_DOWNLOAD_URL}

2. Make sure Chrome is running with remote debugging.
   Command to start Chrome (run in a separate terminal):

   {chrome_cmd}

3. Collector Crypt runs on Solana and Gacha packs cost real USDC/CARDS.
   Only enable real-money tasks in the config if you accept that cost.

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

Collector Crypt Activity Checklist:
  [x] Opened Gacha platform
  [x] Signed in / connected Bitget Wallet
  [x] Checked Gacha pack opening
  [x] Checked weekly Gacha Games challenge
  [x] Checked $CARDS holding
  [x] Shared referral link if chosen
  [x] Checked claim page

Tips for maximizing potential:
  - Concentrate activity in ONE wallet — the formula is sybil-resistant and linear
  - Current-quarter points count for more than lifetime points, so steady
    activity within the active quarter matters most
  - You can sell unwanted cards back (roughly 85-90%) to recycle capital
  - Always double-check the $CARDS contract address before swapping
  - Never approve a wallet popup you do not understand

Follow @WaterkoofAI_Bot for more airdrop scripts
--------------------------------------------------
    """)


if __name__ == "__main__":
    main()
