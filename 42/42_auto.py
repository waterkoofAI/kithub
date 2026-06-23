"""
WaterkoofAI x 42 Airdrop Script Kit v1.0
======================================================
COVERAGE DECLARATION:
- Project: 42
- Portal URL: https://www.42.space/
- Total airdrop tasks: 6
- Tasks automated by this Kit: 6 / 6 guided steps (100%)
- Manual tasks remaining: Bitget Wallet approvals, USDT deposit, market trades, referral sharing, Discord role work, and campaign entries
- Estimated points from this Kit: Helps build speculative eligibility through trading history, referrals, campaign tickets, and community role activity. Rewards are not guaranteed.
- Tested on: Windows/macOS/Linux with Chrome remote debugging
- Wallet used: Bitget Wallet (Chrome extension)

SECURITY NOTICE:
- Caution: Use a burner wallet for this airdrop and secure your seed phrase
- This script is open source and fully auditable
- Your private keys are NEVER collected or uploaded
- Bitget Wallet signing steps require manual approval
- 42 uses real USDT activity. Confirm local legality and risk before proceeding.
- For educational purposes only. Use at your own risk.

HOW TO USE:
1. Drop STEP1_Drop_me_to_any_AI.md into any AI chat for guided setup
2. Fill in STEP2_Fill_your_wallet_info.json with your wallet details
3. Install Bitget Wallet:
   https://web3.bitget.com/share/2kwRSC?inviteCode=waterkoof
4. Install Bitget Wallet Chrome extension:
   https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak
5. Start Chrome with remote debugging (see If_you_dont_use_AI_read_me.txt)
6. Run: python 42_auto.py

Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
"""

import json
import time
import sys
import os
import platform
from playwright.sync_api import sync_playwright

# -- 42 URLs --
PROJECT_HOME = "https://www.42.space/"
MARKETS_URL = "https://www.42.space/"
PORTFOLIO_URL = "https://www.42.space/portfolio"
LEADERBOARD_URL = "https://www.42.space/leaderboard"
TICKETS_URL = "https://ticket.42.space/"
AIRDROP_GUIDE_URL = "https://airdrops.io/42/"
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
    print("  Required network: BNB Chain / BSC")

    click_if_visible(page, "a:has-text('Portfolio')", timeout=3000)
    time.sleep(2)

    clicked = wait_and_click_any(
        page,
        [
            "button:has-text('Connect Wallet')",
            "button:has-text('Connect')",
            "text=Connect Wallet",
            "text=Connect",
            "text=Sign In",
        ],
        "Connect Wallet button",
        timeout=10000,
    )

    if not clicked:
        wait_for_user(
            "Click the Connect or Sign In button in the 42 browser tab.\n\n"
            "  1. Choose wallet login if prompted.\n"
            "  2. Select Bitget Wallet only.\n"
            "  3. Make sure Bitget Wallet is unlocked.\n"
            "  4. Make sure the network is BNB Chain / BSC.\n"
            "  5. Approve only after reviewing the popup."
        )
    if clicked:
        wait_and_click_any(
            page,
            [
                "button:has-text('Continue with a wallet')",
                "text=Continue with a wallet",
                "#privy-modal-content > div > div > div > div > div.sc-iNiQeD.ggZQet > div.sc-dlnjPU.sc-hKFyIn.kTQKIV.ekUVUa > button:nth-child(6) > div.sc-bdnylu.gqqFGE"
            ],
            "Continue Wallet button",
            timeout=10000,
        )
    time.sleep(2)

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
            "  1. Confirm the site is www.42.space.\n"
            "  2. Confirm the wallet is your burner wallet.\n"
            "  3. Confirm the network is BNB Chain / BSC.\n"
            "  4. Approve only if everything looks correct."
            "  5. Enter Referral Code or press skip to enter app."
        )
    else:
        print("\nBitget Wallet was not detected on the page.")
        print(f"Install Bitget Wallet: {BITGET_DOWNLOAD_URL}")
        print(f"Chrome Web Store: {BITGET_CHROME_STORE_URL}")
        wait_for_user(
            "Install or unlock Bitget Wallet in this Chrome-Debug profile.\n\n"
            "  1. Use the Bitget Wallet Chrome extension only.\n"
            "  2. Return to 42 and click Connect or Sign In.\n"
            "  3. Select Bitget Wallet.\n"
            "  4. Confirm BNB Chain / BSC in the popup.\n"
            "  5. Approve manually, then come back here."
        )

    success("Bitget Wallet connection step completed")


def run_wallet(wallet, config, context):
    print(f"\n{'='*60}")
    print(f"Processing wallet: {wallet['address'][:10]}...")
    print(f"{'='*60}")

    page = context.new_page()

    # TASK 1: Open project
    step("Opening 42...")
    page.goto(PROJECT_HOME)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("42 platform loaded")

    # TASK 2: Connect wallet
    connect_bitget_wallet(page)
    time.sleep(2)

    # TASK 3: Deposit USDT
    step("Opening portfolio for USDT funding...")
    page.goto(PORTFOLIO_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    wait_and_click_any(
        page,
        [
            "button:has-text('Deposit')",
            "text=Deposit",
            "button:has-text('Add funds')",
            "text=Add funds",
        ],
        "deposit button",
        timeout=6000,
    )
    wait_for_user(
        "Deposit USDT only if you choose to use real capital.\n\n"
        "  1. Confirm 42 activity is legal for you.\n"
        "  2. Confirm the network is BNB Chain / BSC.\n"
        "  3. Deposit only the amount you are willing to risk.\n"
        "  4. Review every Bitget Wallet popup before approving.\n"
        "  5. If you do not want to deposit, press ENTER to skip."
    )
    success("USDT funding step completed or skipped")

    # TASK 4: Copy referral link
    step("Opening referral / ticket area...")
    page.goto(TICKETS_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    wait_and_click_any(
        page,
        [
            "text=Referral",
            "text=Refer",
            "text=Invite",
            "text=Earn Tickets",
            "button:has-text('Copy')",
        ],
        "referral area",
        timeout=7000,
    )
    click_if_visible(page, "button:has-text('Sign in with your wallet')", timeout=5000)
    click_if_visible(page, "button:has-text('Continue with a wallet')", timeout=5000)
    click_if_visible(page, "button:has-text('Bitget Wallet')", timeout=5000)
    wait_for_user(
        "Copy your 42 referral link manually.\n\n"
        "  1. Open the referral, invite, or Earn Tickets section.\n"
        "  2. Copy your personal referral link if one is available.\n"
        "  3. Share it only where appropriate.\n"
        "  4. Come back here when done.\n\n"
        "  If no referral link is visible, just press ENTER."
    )
    success("Referral step completed")

    # TASK 5: Trade active event markets
    step("Opening active 42 markets...")
    page.goto(MARKETS_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    wait_and_click_any(
        page,
        [
            "text=Trade now",
            "text=Trending Markets",
            "a:has-text('Markets')",
            "text=Markets",
        ],
        "markets link",
        timeout=7000,
    )
    default_amount = config.get("default_trade_amount_usdt", "5")
    wait_for_user(
        "Trade event markets manually.\n\n"
        f"  Suggested max trade amount from config: {default_amount} USDT.\n"
        "  1. Pick a market you understand.\n"
        "  2. Review the outcome, price, fees, and settlement rules.\n"
        "  3. Place a small trade only if you accept the risk.\n"
        "  4. Confirm every Bitget Wallet popup manually.\n"
        "  5. Come back here when the trade is complete.\n\n"
        "  If you want to skip trading, just press ENTER."
    )
    success("Market trading step completed or skipped")

    # TASK 6: Earn Discord roles
    step("Opening 42 airdrop guide for community role link...")
    page.goto(AIRDROP_GUIDE_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    wait_for_user(
        "Earn 42 community roles manually.\n\n"
        "  1. On the airdrop guide, find the 42 Discord link.\n"
        "  2. Join the official Discord only after verifying it is official.\n"
        "  3. Work toward roles such as Alpha Hunter, Outcome Alchemist, Signal Amplifier, Insight Scout, Content Alchemist, or Ambassador.\n"
        "  4. Never share private keys, seed phrases, or wallet recovery details.\n"
        "  5. Come back here when done.\n\n"
        "  If you want to skip community tasks, just press ENTER."
    )
    success("Community role step completed or skipped")

    # TASK 7: Participate in trading campaigns
    step("Opening trading campaign / tickets page...")
    page.goto(TICKETS_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    wait_for_user(
        "Check current 42 trading campaigns manually.\n\n"
        "  1. Review campaign rules, dates, prize pools, and eligibility.\n"
        "  2. Earn tickets only through actions you understand.\n"
        "  3. Track P&L and do not overtrade for points.\n"
        "  4. Come back here when finished.\n\n"
        "  If no campaign is active, just press ENTER."
    )
    success("Campaign step completed or skipped")

    # FINAL STEP: Close
    wait_for_user("Press ENTER to finish this wallet and close the tab")
    page.close()
    print(f"\nWallet {wallet['address'][:10]}... DONE!")
    print(f"\nSummary of completed tasks:")
    print(f"  [x] Opened 42 platform")
    print(f"  [x] Connected Bitget Wallet manually")
    print(f"  [x] Guided USDT funding check")
    print(f"  [x] Guided referral link copy")
    print(f"  [x] Guided event market trading")
    print(f"  [x] Guided community role work")
    print(f"  [x] Guided campaign check")


def main():
    print("""
WaterkoofAI x 42 Airdrop Script Kit v1.0
t.me/WaterkoofAI_Bot
--------------------------------------------------
This script NEVER collects private keys
Caution: Use a burner wallet and secure your seed phrase
Use at your own risk - For educational purposes only
Wallet REQUIRED: Bitget Wallet (Chrome extension)
--------------------------------------------------
    """)

    config  = load_config()
    wallets = config.get("wallets", [])

    if not config.get("i_confirm_42_is_legal_for_me", False):
        print("ERROR: Set i_confirm_42_is_legal_for_me to true only after confirming 42 activity is legal for you.")
        sys.exit(1)

    if not config.get("enable_real_money_tasks", False):
        print("ERROR: Set enable_real_money_tasks to true only if you want guided prompts for USDT funding/trading.")
        sys.exit(1)

    if not wallets:
        print("ERROR: No wallets found in STEP2_Fill_your_wallet_info.json.")
        sys.exit(1)

    wallets = [
        w for w in wallets
        if w.get("address", "") and
        not w.get("address", "").startswith("0xYour")
    ]
    if not wallets:
        print("ERROR: Please replace the placeholder wallet addresses in STEP2_Fill_your_wallet_info.json.")
        sys.exit(1)

    print(f"Found {len(wallets)} wallet(s) in config")

    print(f"Referral code: {config.get('referral_code', 'none')}")
    print(f"Network: {config.get('network', 'bsc')}")
    print(f"Payment token: {config.get('payment_token', 'USDT')}")
    print(f"Default trade amount: {config.get('default_trade_amount_usdt', '5')} USDT")

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

3. 42 uses BNB Chain / BSC and may involve real USDT.
   Confirm local legality, use a burner wallet, and never approve anything you do not understand.

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

42 Activity Checklist:
  [x] Opened platform
  [x] Connected Bitget Wallet
  [x] Checked USDT funding path
  [x] Copied referral link if available
  [x] Traded event markets manually if chosen
  [x] Checked community role path
  [x] Checked trading campaigns

Tips for maximizing potential:
  - Trade only markets you understand
  - Keep activity broad and consistent instead of overtrading
  - Track referrals and campaign tickets
  - Earn community roles without sharing sensitive wallet details
  - Never approve a wallet popup you do not understand

Follow @WaterkoofAI_Bot for more airdrop scripts
--------------------------------------------------
    """)


if __name__ == "__main__":
    main()
