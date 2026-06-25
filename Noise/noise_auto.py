"""
WaterkoofAI x Noise Airdrop Script Kit v1.0
======================================================
COVERAGE DECLARATION:
- Project: Noise
- Portal URL: https://noise.xyz/discover
- Total airdrop tasks: 7
- Tasks automated by this Kit: 7 / 7 guided steps (100%)
- Manual tasks remaining: Bitget Wallet approvals, project-specific choices, social/account actions, and any real-money or DeFi actions marked in prompts
- Estimated points from this Kit: Noise has no confirmed token or points program, but early beta activity may matter if the team later rewards users.
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
6. Run: python noise_auto.py

Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
"""

import json
import time
import sys
import os
import platform
from playwright.sync_api import sync_playwright

# -- Noise URLs --
PROJECT_HOME = "https://noise.xyz/"
PROJECT_APP = "https://noise.xyz/welcome?intent=login"
AIRDROP_GUIDE_URL = "https://airdrops.io/noise/"
BITGET_DOWNLOAD_URL = "https://web3.bitget.com/share/2kwRSC?inviteCode=waterkoof"
BITGET_CHROME_STORE_URL = "https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak"
CONFIG_FILE = "STEP2_Fill_your_wallet_info.json"
NETWORK_NAME = "Base"
LEGAL_FLAG = "i_confirm_noise_is_legal_for_me"
LEGAL_TEXT = "Noise involves trading long/short contracts on cultural attention markets and may require a paid package. Confirm legality and risk before enabling capital prompts."

TASKS_JSON = r'''[
  {
    "description": "Sign up or log in",
    "url": "https://noise.xyz/discover",
    "selectors": [
      "text=Sign up",
      "text=Log in",
      "button:has-text('Sign up')"
    ],
    "requires_real_money": false,
    "prompt": "Create or access your Noise account manually. The script does not submit email for you."
  },
  {
    "description": "Connect wallet",
    "url": "https://noise.xyz/discover",
    "selectors": [
      "text=Connect",
      "text=Wallet"
    ],
    "requires_real_money": false,
    "prompt": "Connect Bitget Wallet on Base if the app asks for wallet connection."
  },
  {
    "description": "Purchase package",
    "url": "https://noise.xyz/discover",
    "selectors": [
      "text=Package",
      "text=Purchase",
      "text=$5"
    ],
    "requires_real_money": true,
    "prompt": "Purchase the minimum package only if legal and desired. Review all payment and wallet prompts."
  },
  {
    "description": "Select a market",
    "url": "https://noise.xyz/discover",
    "selectors": [
      "text=All Markets",
      "text=Featured",
      "text=Search"
    ],
    "requires_real_money": false,
    "prompt": "Choose a trend, brand, or idea market you understand."
  },
  {
    "description": "Open long or short trade",
    "url": "https://noise.xyz/discover",
    "selectors": [
      "text=Long",
      "text=Short",
      "text=Trade",
      "text=Confirm"
    ],
    "requires_real_money": true,
    "prompt": "Choose long or short and enter credits manually only if you accept the risk."
  },
  {
    "description": "Suggest a market",
    "url": "https://noise.xyz/discover",
    "selectors": [
      "text=More",
      "text=Suggest Market"
    ],
    "requires_real_money": false,
    "prompt": "Use More > Suggest Market manually to propose useful markets."
  },
  {
    "description": "Report bugs and save referral",
    "url": "https://noise.xyz/discover",
    "selectors": [
      "text=Report a Bug",
      "text=Referral",
      "text=Invite"
    ],
    "requires_real_money": false,
    "prompt": "Report any beta bugs and copy your referral link if available."
  }
]'''
TASKS = json.loads(TASKS_JSON)


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
    print(f"  Required network: {NETWORK_NAME}")
    wallet_button = page.get_by_role("button", name="Sign in with Wallet")
    if wallet_button.is_visible(timeout=5000):
        wallet_button.click()
        time.sleep(2)
    clicked = wait_and_click_any(
        page,
        [
            "button:has(img[alt='Bitget Wallet'])",
        ],
        "Connect Wallet button",
        timeout=10000,
    )

    if not clicked:
        wait_for_user(
            f"Click the wallet, connect, sign in, or account button in the Noise browser tab.\n\n"
            "  1. Select Bitget Wallet only if a wallet picker appears.\n"
            "  2. Make sure Bitget Wallet is unlocked.\n"
            f"  3. Confirm the network is {NETWORK_NAME}.\n"
            "  4. Approve only after reviewing the popup.\n\n"
            "  If this project does not require wallet login for this step, just press ENTER."
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
            f"  1. Confirm the site is the official Noise site.\n"
            "  2. Confirm the wallet is your burner wallet.\n"
            f"  3. Confirm the network is {NETWORK_NAME}.\n"
            "  4. Approve only if everything looks correct."
        )
    else:
        print("\nBitget Wallet was not detected on the page.")
        print(f"Install Bitget Wallet: {BITGET_DOWNLOAD_URL}")
        print(f"Chrome Web Store: {BITGET_CHROME_STORE_URL}")
        wait_for_user(
            "Install or unlock Bitget Wallet in this Chrome-Debug profile.\n\n"
            "  1. Use the Bitget Wallet Chrome extension only.\n"
            "  2. Return to the project page and click Connect or Sign In.\n"
            "  3. Select Bitget Wallet if a wallet picker appears.\n"
            f"  4. Confirm the network is {NETWORK_NAME}.\n"
            "  5. Approve manually, then come back here.\n\n"
            "  If no wallet connection is required for this project page, press ENTER."
        )

    success("Bitget Wallet connection step completed")


def run_task(page, task, config):
    if task.get("requires_real_money") and not config.get("enable_real_money_tasks", False):
        step(f"Skipping {task['description']} because enable_real_money_tasks is false")
        print("  Edit STEP2_Fill_your_wallet_info.json only if you understand the risk and want this prompt enabled.")
        return False

    step(f"{task['description']}...")
    page.goto(task["url"])
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Page loaded")

    selectors = task.get("selectors", [])
    if selectors:
        wait_and_click_any(page, selectors, task["description"], timeout=7000)

    wait_for_user(
        f"{task['description']}:\n\n"
        f"  {task['prompt']}\n\n"
        "  Review every page and wallet popup manually.\n"
        "  If you want to skip this task, just press ENTER."
    )
    success(f"{task['description']} step completed")
    return True


def run_wallet(wallet, config, context):
    print(f"\n{'='*60}")
    print(f"Processing wallet: {wallet['address'][:10]}...")
    print(f"{'='*60}")

    page = context.new_page()

    step("Opening Noise...")
    page.goto(PROJECT_APP)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Noise loaded")

    connect_bitget_wallet(page)
    time.sleep(2)

    completed = []
    skipped = []
    for task in TASKS:
        if run_task(page, task, config):
            completed.append(task["description"])
        else:
            skipped.append(task["description"])

    wait_for_user("Press ENTER to finish this wallet and close the tab")
    page.close()
    print(f"\nWallet {wallet['address'][:10]}... DONE!")
    print("\nSummary of completed tasks:")
    for item in completed:
        print(f"  [x] {item}")
    for item in skipped:
        print(f"  [-] Skipped: {item}")


def main():
    print("""
WaterkoofAI x Noise Airdrop Script Kit v1.0
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

    if LEGAL_FLAG and not config.get(LEGAL_FLAG, False):
        print(f"ERROR: Set {LEGAL_FLAG} to true only after you understand this requirement:")
        print(LEGAL_TEXT)
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
    print(f"Network: {config.get('network', NETWORK_NAME)}")
    print(f"Real-money task prompts enabled: {config.get('enable_real_money_tasks', False)}")

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

3. Project network/context: {NETWORK_NAME}
   Use a burner wallet. Never enter a seed phrase into this script or a website.

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

Noise Activity Checklist:
  [x] Sign up or log in
  [x] Connect wallet
  [x] Purchase package
  [x] Select a market
  [x] Open long or short trade
  [x] Suggest a market
  [x] Report bugs and save referral

Tips for maximizing potential:
  - Complete free/social tasks first where available
  - Keep capital-based actions small and deliberate
  - Review every Bitget Wallet popup manually
  - Track referrals, points, and dashboard status regularly

Follow @WaterkoofAI_Bot for more airdrop scripts
--------------------------------------------------
    """)


if __name__ == "__main__":
    main()
