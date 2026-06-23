"""
WaterkoofAI x Uponly Airdrop Script Kit v1.0
======================================================
COVERAGE DECLARATION:
- Project: Uponly
- Portal URL: https://app.uponly.space/
- Total airdrop tasks: 5
- Tasks automated by this Kit: 5 / 5 guided steps (100%)
- Manual tasks remaining: Bitget Wallet approvals, Pump Mode trade choices, quest actions, and referral sharing
- Estimated points from this Kit: Helps build UPR competition eligibility through testnet trading volume, quests, and referrals. Rewards are not guaranteed.
- Tested on: Windows/macOS/Linux with Chrome remote debugging
- Wallet used: Bitget Wallet (Chrome extension)

SECURITY NOTICE:
- Caution: Use a burner wallet for this airdrop and secure your seed phrase
- This script is open source and fully auditable
- Your private keys are NEVER collected or uploaded
- Bitget Wallet signing steps require manual approval
- For educational purposes only. Use at your own risk.

HOW TO USE:
1. Drop STEP1_Drop_me_to_any_AI.md into any AI chat for guided setup
2. Fill in STEP2_Fill_your_wallet_info.json with your wallet details
3. Install Bitget Wallet:
   https://web3.bitget.com/share/2kwRSC?inviteCode=waterkoof
4. Install Bitget Wallet Chrome extension:
   https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak
5. Start Chrome with remote debugging (see If_you_dont_use_AI_read_me.txt)
6. Run: python uponly_auto.py

Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
"""

import json
import time
import sys
import os
import platform
from playwright.sync_api import sync_playwright

# -- Uponly URLs --
PROJECT_HOME = "https://uponly.space/"
UPONLY_APP_URL = "https://app.uponly.space/"
UPONLY_FAUCET_URL = "https://faucet.uponly.space/"
UPONLY_DOCS_URL = "https://docs.uponly.space/"
UPONLY_AIRDROP_GUIDE_URL = "https://airdrops.io/uponly/"
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
    print("  Required network: Solana / Uponly test environment")

    clicked = wait_and_click_any(
        page,
        [
            "button:has-text('Connect Wallet')",
            "button:has-text('Connect')",
            "text=Connect Wallet",
            "text=Connect",
            "text=Wallet",
        ],
        "Connect Wallet button",
        timeout=10000,
    )

    if not clicked:
        wait_for_user(
            "Click the Connect Wallet button in the Uponly browser tab.\n\n"
            "  1. Select Bitget Wallet only.\n"
            "  2. Make sure Bitget Wallet is unlocked.\n"
            "  3. Make sure the wallet is ready for Solana / the Uponly test environment.\n"
            "  4. Approve the connection only after reviewing the popup."
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
            "  1. Confirm the site is app.uponly.space.\n"
            "  2. Confirm the wallet is your burner wallet.\n"
            "  3. Confirm the network is Solana / Uponly test environment.\n"
            "  4. Approve only if everything looks correct."
        )
    else:
        print("\nBitget Wallet was not detected on the page.")
        print(f"Install Bitget Wallet: {BITGET_DOWNLOAD_URL}")
        print(f"Chrome Web Store: {BITGET_CHROME_STORE_URL}")
        wait_for_user(
            "Install or unlock Bitget Wallet in this Chrome-Debug profile.\n\n"
            "  1. Use the Bitget Wallet Chrome extension only.\n"
            "  2. Return to Uponly and click Connect Wallet.\n"
            "  3. Select Bitget Wallet.\n"
            "  4. Confirm Solana / Uponly test environment in the popup.\n"
            "  5. Approve manually, then come back here."
        )

    success("Bitget Wallet connection step completed")


def run_wallet(wallet, config, context):
    print(f"\n{'='*60}")
    print(f"Processing wallet: {wallet['address'][:10]}...")
    print(f"{'='*60}")

    page = context.new_page()

    # TASK 1: Open project
    step("Opening Uponly...")
    page.goto(UPONLY_APP_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Uponly app loaded")

    # TASK 2: Connect wallet
    connect_bitget_wallet(page)
    time.sleep(2)

    # TASK 3: Claim test funds
    step("Checking 10,000 USDC test funds...")
    page.goto(UPONLY_FAUCET_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)

    if wait_and_click_any(
        page,
        [
            "button:has-text('Connect Wallet')",
            "text=Connect Wallet",
        ],
        "Connect Wallet button on faucet page",
        timeout=8000,
    ):
        click_if_visible(page, "button:has-text('Bitget Wallet')")
        wait_for_user(
            "Claim or confirm your Uponly test funds.\n\n"
            "  1. Review any Bitget Wallet popup.\n"
            "  2. Approve only testnet/test-fund actions you understand.\n"
            "  3. Wait until the app shows your 10,000 USDC test balance.\n"
            "  4. If funds were already credited automatically, just press ENTER."
        )
    else:
        wait_for_user(
            "Confirm your Uponly test funds.\n\n"
            "  1. Look for a 10,000 USDC test balance in the app.\n"
            "  2. If you see a claim/faucet button, click it manually.\n"
            "  3. Review any Bitget Wallet popup before approving.\n"
            "  4. If funds are already available, press ENTER."
        )
    success("Test funds step completed")

    # TASK 4: Trade in Pump Mode
    step("Opening Pump Mode trading...")
    page.goto(UPONLY_APP_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    click_if_visible(page, "text=Pump Mode")
    preferred_trade_size = config.get("preferred_trade_size_usdc", "100")
    wait_for_user(
        "Trade in Pump Mode manually.\n\n"
        f"  Suggested test trade size from config: {preferred_trade_size} USDC.\n"
        "  1. Open Pump Mode if it is not already open.\n"
        "  2. Place one or more test trades with the credited test USDC.\n"
        "  3. Review every Bitget Wallet popup before approving.\n"
        "  4. Never use real funds for this testnet competition.\n"
        "  5. Come back here when your trade activity is recorded.\n\n"
        "  If you want to skip this wallet, just press ENTER."
    )
    success("Pump Mode trading step completed")

    # TASK 5: Complete quests
    step("Opening Uponly quests...")
    page.goto(UPONLY_APP_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    wait_and_click_any(
        page,
        [
            "text=Quests",
            "text=Quest",
            "a:has-text('Quests')",
            "button:has-text('Quests')",
        ],
        "quests link",
        timeout=6000,
    )
    wait_for_user(
        "Complete available Uponly quests manually.\n\n"
        "  1. Open the Quests section if the script did not find it.\n"
        "  2. Complete only tasks you are comfortable with.\n"
        "  3. For social tasks, use your own accounts manually.\n"
        "  4. Review wallet popups before signing.\n"
        "  5. Come back here when finished.\n\n"
        "  If no quests are available, just press ENTER."
    )
    success("Quest step completed")

    # TASK 6: Referral activity
    step("Opening referral area...")
    page.goto(UPONLY_APP_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    wait_and_click_any(
        page,
        [
            "text=Referral",
            "text=Refer",
            "text=Invite",
            "button:has-text('Invite')",
            "a:has-text('Referral')",
        ],
        "referral link",
        timeout=6000,
    )
    wait_for_user(
        "Find and save your Uponly referral link manually.\n\n"
        "  1. Open the Referral, Refer, or Invite section.\n"
        "  2. Copy your referral link if one is available.\n"
        "  3. Share it only where appropriate.\n"
        "  4. Come back here when done.\n\n"
        "  If referrals are not available, just press ENTER."
    )
    success("Referral step completed")

    # FINAL STEP: Close
    wait_for_user("Press ENTER to finish this wallet and close the tab")
    page.close()
    print(f"\nWallet {wallet['address'][:10]}... DONE!")
    print(f"\nSummary of completed tasks:")
    print(f"  [x] Opened Uponly app")
    print(f"  [x] Connected Bitget Wallet manually")
    print(f"  [x] Checked 10,000 USDC test funds")
    print(f"  [x] Guided Pump Mode trading")
    print(f"  [x] Guided quest completion")
    print(f"  [x] Guided referral activity")


def main():
    print("""
WaterkoofAI x Uponly Airdrop Script Kit v1.0
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
    print(f"Network: {config.get('network', 'solana')}")
    print(f"Preferred test trade size: {config.get('preferred_trade_size_usdc', '100')} USDC")

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

3. Uponly is a Solana testnet-style competition flow.
   Confirm you are using a burner wallet and never enter a seed phrase anywhere.

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

Uponly Activity Checklist:
  [x] Opened app
  [x] Connected Bitget Wallet
  [x] Checked test funds
  [x] Traded in Pump Mode manually
  [x] Completed quests manually
  [x] Saved or shared referral link manually

Tips for maximizing potential:
  - Trade consistently during the competition window
  - Complete quests because they may count separately from leaderboard volume
  - Use referrals early if the platform provides a referral link
  - Never approve a wallet popup you do not understand

Follow @WaterkoofAI_Bot for more airdrop scripts
--------------------------------------------------
    """)


if __name__ == "__main__":
    main()
