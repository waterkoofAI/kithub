"""
WaterkoofAI x Tulpea Airdrop Script Kit v1.0
======================================================
COVERAGE DECLARATION:
- Project: Tulpea
- Portal URL: https://app.tulpea.org/vault
- Total airdrop tasks: 6
- Tasks automated by this Kit: 3 / 6 (50%)
- Manual tasks remaining: wallet approvals, bridging USDT, vault deposit, Galxe quests.
- Estimated points from this Kit: Helps earn TULIP Bulbs and access to the Golden Key campaign.
- Tested on: Windows
- Wallet used: Bitget Wallet (Chrome extension)

SECURITY NOTICE:
- This script is open source and fully auditable
- Your private keys are NEVER collected or uploaded
- Bitget Wallet signing steps require manual approval
- This script NEVER approves tokens, bridges funds, deposits, or approves wallet popups for you
- For educational purposes only. Use at your own risk.

Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
"""

import json
import time
import sys
import os
import platform
from playwright.sync_api import sync_playwright

# -- Tulpea URLs --
PROJECT_HOME = "https://app.tulpea.org"
VAULT_URL = "https://app.tulpea.org/vault"
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
    Connect Bitget Wallet on Tulpea.
    Strictly requires Bitget Wallet extension to be installed.
    """
    step("Connecting Bitget Wallet on MegaETH network...")

    connect_selectors = [
        "button:has-text('Connect Wallet')",
        "button:has-text('Connect')",
        "#radix-_r_k_ > div > div.space-y-2 > button.w-full.py-3.text-sm.font-medium.font-satoshi.text-white.rounded-full.cursor-pointer.transition-opacity.hover\:opacity-90"
    ]

    connect_clicked = wait_and_click_any(
        page,
        connect_selectors,
        description="Connect Wallet button"
    )

    if not connect_clicked:
        wait_for_user(
            "Could not find the Connect Wallet button automatically.\n"
            "Please click Connect Wallet manually on the website, then press ENTER."
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
            "  2. Use MegaETH network in Bitget Wallet. (You may need to add it if it's new).\n"
            "  3. Approve only the connection or signature you recognize.\n"
            "  4. Do not approve any token approval or deposit unless you intended it.\n\n"
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
        "6. Confirm you are using MegaETH network.\n"
        "7. Press ENTER when connected and ready."
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
        "button:has-text('Deposit')",
        "button:has-text('Withdraw')",
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
    referral_code = config.get("referral_code", "a208315")
    
    # Build referral URL
    target_url = f"{VAULT_URL}?ref={referral_code}" if referral_code else VAULT_URL

    print(f"\n{'='*60}")
    print(f"Processing wallet: {wallet_address[:10]}...")
    print(f"{'='*60}")

    page = context.new_page()

    # -- TASK 1: Open Tulpea vault page with referral --
    step("Opening Tulpea vault page...")
    page.goto(target_url)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Tulpea page loaded")

    # -- TASK 2: Connect Bitget Wallet --
    connect_bitget_wallet(page)
    time.sleep(2)

    ensure_bitget_wallet_connected(page, "Vault page")

    # -- TASK 3: Check USDT Balance and Bridge --
    step("Reviewing USDT balance and bridging...")
    wait_for_user(
        "Ensure you have USDT on MegaETH:\n\n"
        "  1. Tulpea requires USDT on the MegaETH network.\n"
        "  2. If your USDT is on another chain, you will need to bridge it.\n"
        "  3. Use an official bridge or the one recommended by Tulpea.\n"
        "  4. Ensure you also have the native gas token for MegaETH.\n\n"
        "Press ENTER when you are ready to deposit."
    )
    success("Bridging step completed")

    # -- TASK 4: Vault Deposit --
    step("Reviewing Deposit options...")
    wait_for_user(
        "Deposit USDT into Tulpea Vault:\n\n"
        "  1. Look for the Vault or Rewards section.\n"
        "  2. Enter the amount of USDT you wish to deposit.\n"
        "  3. Approve the USDT spend in your Bitget Wallet.\n"
        "  4. Confirm the deposit transaction.\n"
        "  5. This currently gives a 5x multiplier on Bulbs.\n\n"
        "Press ENTER when you have completed or skipped your deposit."
    )
    success("Vault deposit step completed")

    # -- TASK 5: Galxe Quests --
    step("Reviewing Galxe Quests...")
    wait_for_user(
        "Complete the Golden Key Galxe Campaign:\n\n"
        "  1. Tulpea has an active campaign on Galxe.\n"
        "  2. Navigate to their Galxe page (link usually in their Discord/Twitter).\n"
        "  3. Complete the social tasks and verify your vault deposit.\n"
        "  4. Claim any available NFTs or points on Galxe.\n\n"
        "Press ENTER when you have checked the Galxe quests."
    )
    success("Galxe quests reviewed")

    # -- TASK 6: Referral sharing --
    step("Retrieving your referral link...")
    wait_for_user(
        "Share your referral link:\n\n"
        "  1. Find your personal referral code on the app.\n"
        "  2. Copy it and share with friends.\n"
        "  3. You can use your code in the STEP2 JSON file for your other wallets to stack bonuses!\n\n"
        "Press ENTER to finish this wallet."
    )
    success("Referral step completed")

    page.close()
    print(f"\nWallet {wallet_address[:10]}... DONE!")
    print(f"\nSummary of completed tasks:")
    print(f"  [x] Open Tulpea vault with referral: {referral_code}")
    print(f"  [x] Connect Bitget Wallet on MegaETH network")
    print(f"  [x] Review USDT bridging to MegaETH")
    print(f"  [x] Review and perform Vault deposit")
    print(f"  [x] Review Galxe campaign")
    print(f"  [x] Retrieve and share referral code")


def main():
    print("""
WaterkoofAI x Tulpea Airdrop Script Kit v1.0
t.me/WaterkoofAI_Bot
--------------------------------------------------
This script NEVER collects private keys
This script NEVER approves, bridges, deposits, or claims for you
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
    print(f"Network: {config.get('network', 'megaeth')}")
    print(f"Referral code: {config.get('referral_code', 'a208315')}")

    chrome_cmd = get_chrome_debug_command()

    print(f"""
{'='*60}
BEFORE YOU CONTINUE:
1. You MUST use the Bitget Wallet Chrome extension:
   https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak

2. Make sure Chrome is running with remote debugging.
   Command to start Chrome (run in a separate terminal):

   {chrome_cmd}

3. Use MegaETH network in Bitget Wallet.
4. Keep USDT and the native gas token on MegaETH if you plan to deposit.
5. This script will not bridge or deposit for you.

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

Tulpea Activity Checklist:
  [x] Connect Bitget Wallet on MegaETH
  [x] Ensure USDT is bridged
  [x] Deposit into Vault
  [x] Complete Galxe Quests

Tips for maximizing potential:
  - Depositing early often yields multiplier bonuses (currently 5x Bulbs).
  - Completing the Galxe quests is crucial for identifying as a real user.
  - Share your referral link to earn 10% on your referrals' deposits.

Follow @WaterkoofAI_Bot for more airdrop scripts
--------------------------------------------------
    """)


if __name__ == "__main__":
    main()
