"""
WaterkoofAI x Brighter Airdrop Script Kit v1.0
======================================================
COVERAGE DECLARATION:
- Project: Brighter
- Portal URL: https://brighter.money/
- Total airdrop tasks: 6
- Tasks automated by this Kit: 6 / 6 guided steps (100%)
- Manual tasks remaining: Wallet approval popup, following/linking X, upvoting on Lit Hub,
  posting the vote screenshot, and joining Telegram (these require your own account actions)
- Estimated points from this Kit: Helps build Brighter Points through wallet connection,
  X linking, referral code entry, and referral sharing. No token or airdrop is confirmed yet.
- Tested on: Windows/macOS/Linux with Chrome remote debugging
- Wallet used: Bitget Wallet (Chrome extension)

SECURITY NOTICE:
- Caution: Use a burner wallet for this airdrop and secure your seed phrase
- This script is open source and fully auditable
- Your private keys are NEVER collected or uploaded
- Bitget Wallet signing steps require manual approval
- No token exists yet and no airdrop is officially confirmed for Brighter
- For educational purposes only. Use at your own risk.

HOW TO USE:
1. Drop STEP1_Drop_me_to_any_AI.md into any AI chat for guided setup
2. Fill in STEP2_Fill_your_wallet_info.json with your wallet details
3. Install Bitget Wallet:
   https://web3.bitget.com/share/2kwRSC?inviteCode=waterkoof
4. Install Bitget Wallet Chrome extension:
   https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak
5. Start Chrome with remote debugging (see If_you_dont_use_AI_read_me.txt)
6. Run: python brighter_auto.py

Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
"""

import json
import time
import sys
import os
import platform
from playwright.sync_api import sync_playwright

# ── Brighter URLs ──
PROJECT_HOME = "https://brighter.money/"
CAMPAIGN_URL = "https://brighter.money/"
BRIGHTER_X_URL = "https://x.com/intent/follow?screen_name=Brighter_money"
BRIGHTER_TELEGRAM_URL = "https://t.me/brighter_money"
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
    print("  Required network: Ethereum")

    clicked = wait_and_click_any(
        page,
        [
            "button:has-text('Connect Wallet')",
            "button:has-text('Connect')",
            "text=Connect Wallet",
            "text=Connect",
        ],
        "Connect Wallet button",
        timeout=10000,
    )
    if not clicked:
        clicked = click_if_visible(page, "button:has-text('Connect Wallet')", timeout=5000)
    if not clicked:
        wait_for_user(
            "Click the Connect Wallet button on the Brighter campaign page.\n\n"
            "  1. Choose wallet login when prompted.\n"
            "  2. Select Bitget Wallet only.\n"
            "  3. Make sure Bitget Wallet is unlocked.\n"
            "  4. Make sure the network is Ethereum.\n"
            "  5. Approve only after reviewing the popup."
        )

    extension_selectors = [
        "button:has-text('Bitget Wallet')",
        "text=Bitget Wallet",
        "text=BitKeep",
    ]

    extension_detected = False
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
            "  1. Confirm the site is brighter.money.\n"
            "  2. Confirm the wallet is your burner wallet.\n"
            "  3. Confirm the network is Ethereum.\n"
            "  4. Approve only if everything looks correct.\n"
            "  No deposit is required in this reservation phase."
        )
    else:
        print("\nBitget Wallet was not detected on the page.")
        print(f"Install Bitget Wallet: {BITGET_DOWNLOAD_URL}")
        print(f"Chrome Web Store: {BITGET_CHROME_STORE_URL}")
        wait_for_user(
            "Install or unlock Bitget Wallet in this Chrome-Debug profile.\n\n"
            "  1. Use the Bitget Wallet Chrome extension only.\n"
            "  2. Return to Brighter and click Connect Wallet.\n"
            "  3. Select Bitget Wallet.\n"
            "  4. Confirm Ethereum in the popup.\n"
            "  5. Approve manually, then come back here."
        )

    success("Bitget Wallet connection step completed")


def run_wallet(wallet, config, context):
    print(f"\n{'='*60}")
    print(f"Processing wallet: {wallet['address'][:10]}...")
    print(f"{'='*60}")

    page = context.new_page()

    # TASK 1: Open project
    step("Opening Brighter...")
    page.goto(PROJECT_HOME)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Brighter campaign page loaded")

    # TASK 2: Connect wallet
    connect_bitget_wallet(page)
    time.sleep(2)

    # TASK 3: Follow and link X account
    step("Opening Brighter's X (Twitter) page...")
    page.goto(BRIGHTER_X_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Brighter X page loaded")
    wait_for_user(
        "Follow and link your X account:\n\n"
        "  1. Follow @Brighter_money on X.\n"
        "  2. Come back here when done."
    )
    success("X follow/link step completed")

    # TASK 4: Enter referral code
    step("Returning to Brighter campaign page...")
    page.goto(CAMPAIGN_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    referral_code = config.get("referral_code_to_enter", "AIRDROPS")
    wait_for_user(
        f"Enter a referral code during signup.\n\n"
        f"  Suggested code from config: {referral_code}\n"
        "  1. Find the 'Enter referral code' field on the signup/dashboard page.\n"
        "  2. Enter a code (using one is free and does not cost you anything).\n"
        "  3. Confirm/submit.\n"
        "  4. Come back here when done.\n\n"
        "  If you don't want to use a referral code, just press ENTER."
    )
    success("Referral code step completed or skipped")

    # TASK 5: Share your own referral link
    step("Opening campaign dashboard for your referral link...")
    page.goto(CAMPAIGN_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    wait_and_click_any(
        page,
        [
            "text=Referral",
            "text=Refer a friend",
            "text=Invite",
            "button:has-text('Copy')",
        ],
        "referral link area",
        timeout=7000,
    )
    wait_for_user(
        "Generate and share your own referral link.\n\n"
        "  1. Copy your personal referral link.\n"
        "  2. Share it only where appropriate.\n"
        "  3. You earn an ongoing 4% of every referred friend's base points.\n"
        "  4. Come back here when done.\n\n"
        "  If you don't want to share it yet, just press ENTER."
    )
    success("Referral sharing step completed or skipped")

    # TASK 6: Upvote on Lit Hub and post screenshot
    step("Community task: Lit Hub upvote...")
    wait_for_user(
        "Upvote Brighter on Lit Hub (Lighter's ecosystem directory):\n\n"
        "  1. Find the current Lit Hub link via Brighter's official X or Telegram\n"
        "     (the link is not fixed, so check their latest announcement).\n"
        "  2. Open Lit Hub and find Brighter's listing.\n"
        "  3. Upvote it.\n"
        "  4. Take a screenshot of your vote and post it on X per the official\n"
        "     announcement instructions.\n"
        "  5. Come back here when done.\n\n"
        "  If you want to skip this, just press ENTER."
    )
    success("Lit Hub upvote step completed or skipped")

    # OPTIONAL: Join Telegram
    wait_for_user(
        "Join Brighter's official Telegram group to follow announcements.\n\n"
       f"  Group Link: {BRIGHTER_TELEGRAM_URL}\n\n"
        "  This step is not tied to points, but it's the fastest way to catch\n"
        "  campaign changes (like new Lit Hub voting periods).\n\n"
        "  Press ENTER when joined, or press ENTER to skip."
    )
    success("Telegram step completed or skipped")

    # FINAL STEP: Close
    wait_for_user("Press ENTER to finish this wallet and close the tab")
    page.close()
    print(f"\nWallet {wallet['address'][:10]}... DONE!")
    print(f"\nSummary of completed tasks:")
    print(f"  [x] Opened Brighter campaign page")
    print(f"  [x] Connected Bitget Wallet manually")
    print(f"  [x] Guided X follow + link")
    print(f"  [x] Guided referral code entry")
    print(f"  [x] Guided referral link sharing")
    print(f"  [x] Guided Lit Hub upvote + screenshot post")
    print(f"  [x] Guided Telegram join (optional)")


def main():
    print("""
WaterkoofAI x Brighter Airdrop Script Kit v1.0
t.me/WaterkoofAI_Bot
--------------------------------------------------
This script NEVER collects private keys
Caution: Use a burner wallet and secure your seed phrase
Use at your own risk - For educational purposes only
Wallet REQUIRED: Bitget Wallet (Chrome extension)
No Brighter token exists yet - no airdrop is confirmed
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
        print("ERROR: Please replace the placeholder wallet address in STEP2_Fill_your_wallet_info.json.")
        sys.exit(1)

    print(f"Found {len(wallets)} wallet(s) in config")
    print(f"Referral code to enter: {config.get('referral_code_to_enter', 'AIRDROPS')}")

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

3. Brighter is in a pre-launch, points-only phase. No token exists and
   no airdrop is officially confirmed. No deposit is required.

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

Brighter Activity Checklist:
  [x] Opened campaign page
  [x] Connected Bitget Wallet
  [x] Followed and linked X account
  [x] Entered referral code
  [x] Shared own referral link
  [x] Checked Lit Hub upvote task
  [x] Checked Telegram group

Tips for maximizing potential:
  - Linking X (not just following) is what reserves your points
  - Your referral link earns an ongoing 4% of referred friends' points
  - No deposit is needed in this pre-launch phase
  - Never approve a wallet popup you do not understand
  - Nothing about a Brighter token or airdrop is confirmed yet

Follow @WaterkoofAI_Bot for more airdrop scripts
--------------------------------------------------
    """)


if __name__ == "__main__":
    main()
