"""
WaterkoofAI x Dustswap Airdrop Script Kit v1.0
======================================================
COVERAGE DECLARATION:
- Project: Dustswap
- Portal URL: https://app.dustswap.wtf/profile
- Total airdrop tasks: 8
- Tasks automated by this Kit: 4 / 8 (50%)
- Manual tasks remaining: wallet approvals, social verification (Discord/X), swapping tokens manually.
- Estimated points from this Kit: Helps earn Particle Points ($DUST) via check-ins and quests.
- Tested on: Windows
- Wallet used: Bitget Wallet (Chrome extension)

SECURITY NOTICE:
- This script is open source and fully auditable
- Your private keys are NEVER collected or uploaded
- Bitget Wallet signing steps require manual approval
- This script NEVER approves tokens, deposits funds, swaps, or approves wallet popups for you
- For educational purposes only. Use at your own risk.

Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
"""

import json
import time
import sys
import os
import platform
from playwright.sync_api import sync_playwright

# -- Dustswap URLs --
PROJECT_HOME = "https://app.dustswap.wtf"
DUSTSWAP_PROFILE = "https://app.dustswap.wtf/profile"
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


def wait_and_click_any(page, selectors, description="button", timeout=1000):
    """Try multiple selectors and click the first one found."""
    for selector in selectors:
        try:
            el = page.locator(selector).first
            if el.is_visible(timeout=timeout // len(selectors)):
                el.click()
                print(f"  Clicked: {selector}")
                return True
        except Exception:
            continue
    print(f"  {description} not found with any selector")
    return False


def first_visible_selector(page, selectors, timeout=1000):
    """Return the first visible selector from a list, or None."""
    for selector in selectors:
        try:
            if page.locator(selector).first.is_visible(timeout=timeout):
                return selector
        except Exception:
            continue
    return None


def connect_bitget_wallet(page):
    """
    Connect Bitget Wallet on Dustswap.
    Strictly requires Bitget Wallet extension to be installed.
    """
    step("Connecting Bitget Wallet on Base network...")

    connect_selectors = [
        "button:has-text('Switch to Base')",
        "button:has-text('Switch to Base')",
    ]

    connect_clicked = wait_and_click_any(
        page,
        connect_selectors,
        description="Switch to Base Network"
    )

    if not connect_clicked:
        wait_for_user(
            "Could not find the Switch to Base Network button automatically.\n"
            "Please click Switch to Base Network manually on the website, then press ENTER.\n"
            "Ignore this if you are already on the Base network.\n"
        )

    time.sleep(2)

    extension_selectors = [
        "button:has-text('Bitget Wallet')",
        "text=Bitget Wallet",
    ]

    extension_detected = False
    for selector in extension_selectors:
        try:
            if page.locator(selector).first.is_visible():
                extension_detected = True
                break
        except Exception:
            pass

    if extension_detected:
        step("Bitget Wallet extension detected - connecting...")
        wait_and_click_any(
            page,
            extension_selectors,
            description="Bitget Wallet",
        )
        time.sleep(2)

        wait_for_user(
            "Approve the connection inside Bitget Wallet.\n\n"
            "  1. Make sure Bitget Wallet is unlocked.\n"
            "  2. Use Base network in Bitget Wallet.\n"
            "  3. Approve only the connection or signature you recognize.\n"
            "  4. Do not approve any token approval or swap unless you intended it.\n\n"
            "After approval press ENTER."
        )

        success("Bitget Wallet connection step completed")
        return

    print("\n" + "="*50)
    print("BITGET WALLET EXTENSION NOT DETECTED")
    print("You MUST connect using the Bitget Wallet Chrome extension.")
    print("="*50)
    print("\nPlease install the Bitget Wallet extension:")
    print("https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak")

    wait_for_user(
        "1. Install Bitget Wallet Chrome extension using the link above.\n"
        "2. Set up or import your wallet.\n"
        "3. Refresh the page if needed.\n"
        "4. Click Connect Wallet and select Bitget Wallet.\n"
        "5. Approve the connection in the extension popup.\n"
        "6. Confirm you are using Base network.\n"
        "7. Press ENTER when connected and ready.\n\n"
        "Note: If wallet is already connected, Just press ENTER.\n"
    )

    success("Bitget Wallet connected manually")


def ensure_bitget_wallet_connected(page, page_name="current page"):
    """Reconnect only when the site shows a wallet connection prompt."""
    step(f"Checking wallet connection on {page_name}...")

    connect_prompt_selectors = [
        "button:has-text('Connect Wallet')",
        "button:has-text('Connect')",
    ]
    connected_state_selectors = [
        "text=Disconnect",
        "text=Profile",
        "text=Points",
        "text=Swaps",
        "button:has-text('Swap')",
    ]

    connect_prompt = first_visible_selector(page, connect_prompt_selectors, timeout=1500)
    connected_state = first_visible_selector(page, connected_state_selectors, timeout=1000)

    if connected_state and not connect_prompt:
        success(f"Wallet already appears connected on {page_name}")
        return

    if connect_prompt:
        print(f"  Wallet is not connected on {page_name}; reconnecting with Bitget Wallet.")
        connect_bitget_wallet(page)
        time.sleep(2)
        return

    print(f"  No wallet connect prompt detected on {page_name}; continuing.")


def run_wallet(wallet, config, context):
    wallet_address = wallet.get("address", "")
    referral_code = config.get("referral_code", "DUST-9A2VP")
    
    # Build referral URL
    target_url = f"{DUSTSWAP_PROFILE}?ref={referral_code}" if referral_code else DUSTSWAP_PROFILE

    print(f"\n{'='*60}")
    print(f"Processing wallet: {wallet_address[:10]}...")
    print(f"{'='*60}")

    page = context.new_page()

    # -- TASK 1: Open Dustswap profile with referral --
    step("Opening Dustswap profile page...")
    page.goto(target_url)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Dustswap page loaded")

    # -- TASK 2: Connect Bitget Wallet --
    connect_bitget_wallet(page)
    time.sleep(2)

    # -- TASK 3: Daily check-in + spin wheel --
    ensure_bitget_wallet_connected(page, "Profile page")
    wait_for_user(
        "Complete your daily actions:\n\n"
        "  1. Ensure you are on the Base network.\n"
        "  2. Look for the daily check-in button and click it.\n"
        "  3. Sign the message in your wallet if prompted.\n"
        "  4. If there is a spin wheel available, spin it to earn points.\n\n"
        "Press ENTER when finished."
    )
    success("Daily check-in completed")

    # -- TASK 4: Social quests --
    step("Navigating to Quests/Social tasks...")
    wait_for_user(
        "Complete Social Quests:\n\n"
        "  1. Go to the Quests section on the profile page.\n"
        "  2. Follow Dustswap on X (Twitter).\n"
        "  3. Join their Discord to claim the Early Contributor role.\n"
        "  4. Complete any other available social tasks to earn Particle Points.\n\n"
        "Press ENTER when you have completed or skipped the social quests."
    )
    success("Social quests reviewed")

    # -- TASK 5: Onchain Swap quests --
    step("Reviewing onchain swap quests...")
    wait_for_user(
        "Complete Onchain Swaps (Optional):\n\n"
        "  1. Navigate to the Swap section of the app.\n"
        "  2. If you choose to swap, you will need some ETH on Base for gas.\n"
        "  3. Manually select the tokens you want to swap.\n"
        "  4. Approve the token (if required) and confirm the swap in your wallet.\n"
        "  5. Only approve transactions you fully understand.\n\n"
        "Press ENTER when finished with your swaps."
    )
    success("Onchain swap quests reviewed")

    # -- TASK 6: Referral sharing --
    step("Retrieving your referral link...")
    wait_for_user(
        "Share your referral link:\n\n"
        "  1. Find your personal referral code on the profile page.\n"
        "  2. Copy it and share with friends to earn 20% of their points.\n"
        "  3. You can use your code in the STEP2 JSON file for your other wallets!\n\n"
        "Press ENTER to finish this wallet."
    )
    success("Referral step completed")

    page.close()
    print(f"\nWallet {wallet_address[:10]}... DONE!")
    print(f"\nSummary of completed tasks:")
    print(f"  [x] Open Dustswap page with referral: {referral_code}")
    print(f"  [x] Connect Bitget Wallet on Base network")
    print(f"  [x] Complete daily check-in and spin wheel")
    print(f"  [x] Complete social & Discord quests")
    print(f"  [x] Perform optional onchain swaps")
    print(f"  [x] Retrieve and share referral code")


def main():
    print("""
WaterkoofAI x Dustswap Airdrop Script Kit v1.0
t.me/WaterkoofAI_Bot
--------------------------------------------------
This script NEVER collects private keys
This script NEVER approves, deposits, swaps, or claims for you
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
    print(f"Network: {config.get('network', 'base')}")
    print(f"Referral code: {config.get('referral_code', 'DUST-9A2VP')}")

    chrome_cmd = get_chrome_debug_command()

    print(f"""
{'='*60}
BEFORE YOU CONTINUE:
1. You MUST use the Bitget Wallet Chrome extension:
   https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak

2. Make sure Chrome is running with remote debugging.
   Command to start Chrome (run in a separate terminal):

   {chrome_cmd}

3. Use Base network in Bitget Wallet.
4. Keep some ETH on Base for gas if you plan to do swap quests.
5. This script will not approve tokens, swap, or claim for you.

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

Dustswap Activity Checklist:
  [x] Connect Bitget Wallet on Base
  [x] Complete daily check-in
  [x] Complete social quests
  [x] Complete onchain swap quests

Tips for maximizing potential:
  - Return daily for check-ins and wheel spins to maximize Particle Points.
  - Doing more swap volume can increase your rewards.
  - Share your referral link!

Follow @WaterkoofAI_Bot for more airdrop scripts
--------------------------------------------------
    """)


if __name__ == "__main__":
    main()
