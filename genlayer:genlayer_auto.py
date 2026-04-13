"""
WaterkoofAI x GenLayer Airdrop Script Kit v1.5
================================================
SECURITY NOTICE:
- This script is open source and fully auditable
- Your private keys are NEVER collected or uploaded
- MetaMask signing steps require manual approval
- For educational purposes only. Use at your own risk.

HOW TO USE:
1. Drop STEP1_Drop_me_to_any_AI.md into any AI chat for guided setup
2. Fill in STEP2_Fill_your_wallet_info.json with your wallet details
3. Start Chrome with remote debugging (see If_you_dont_use_AI_read_me.txt)
4. Run: python genlayer_auto.py

Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
"""

import json
import time
import sys
import os
import platform
from playwright.sync_api import sync_playwright

PORTAL_URL  = "https://portal.genlayer.foundation/#/"
STUDIO_URL  = "https://studio.genlayer.com/contracts"
CONFIG_FILE = "STEP2_Fill_your_wallet_info.json"


# ─────────────────────────────────────────────
#  Chrome debug command helper
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
#  Helpers
# ─────────────────────────────────────────────

def load_config():
    if not os.path.exists(CONFIG_FILE):
        print(f"ERROR: {CONFIG_FILE} not found.")
        print("Please make sure STEP2_Fill_your_wallet_info.json is in the same folder as this script.")
        sys.exit(1)
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


def wait_for_user(msg):
    print(f"\n{'='*50}")
    print(f"ACTION NEEDED: {msg}")
    print(f"Press ENTER when done...")
    print(f"{'='*50}")
    input()


def step(msg):
    print(f"\n> {msg}")


def success(msg):
    print(f"OK  {msg}")


def click_if_visible(page, selector, timeout=4000):
    try:
        el = page.locator(selector).first
        if el.is_visible(timeout=timeout):
            el.click()
            return True
    except Exception:
        pass
    return False


# ─────────────────────────────────────────────
#  Per-Wallet Flow
# ─────────────────────────────────────────────

def run_wallet(wallet, config, context):
    print(f"\n{'='*60}")
    print(f"Processing wallet: {wallet['address'][:10]}...")
    print(f"{'='*60}")

    page = context.new_page()

    # ── Step 1: Open Portal ──
    step("Opening GenLayer Portal...")
    page.goto(PORTAL_URL)
    page.wait_for_load_state("networkidle")
    time.sleep(2)
    success("Portal opened")

    # ── Step 2: Connect Wallet ──
    step("Connecting wallet...")
    try:
        page.locator("text=Connect Wallet").first.click()
        time.sleep(1)
        page.locator("text=MetaMask").first.click()
        time.sleep(1)
    except Exception as e:
        print(f"  Auto-click failed: {e}")

    wait_for_user(
        "In Chrome / MetaMask:\n"
        "  1. Switch to the correct wallet\n"
        "  2. Click Connect in the MetaMask popup\n"
        "  3. Come back here and press ENTER"
    )

    # ── Step 3: Profile Setup ──
    step("Profile setup check...")
    wait_for_user(
        "Check the browser:\n"
        "  - If you see a 'Complete Your Profile' form:\n"
        "    1. Fill in your Display Name\n"
        "    2. Fill in your Email Address\n"
        "    3. Click Save\n"
        "    4. Come back here and press ENTER\n"
        "  - If NO form appears, just press ENTER to continue"
    )
    success("Profile step done")

    # ── Step 4: Get full participant URL ──
    step("Getting participant page URL...")
    page.goto(PORTAL_URL)
    page.wait_for_load_state("networkidle")
    time.sleep(2)

    connected_address = None
    try:
        user_btn = page.locator("header").locator("button").last
        user_btn.click()
        time.sleep(2)
        current_url = page.url
        if "/participant/0x" in current_url:
            connected_address = current_url.split("/participant/")[-1]
            success(f"Got address: {connected_address[:10]}...")
    except Exception:
        pass

    if not connected_address:
        wait_for_user(
            "Could not auto-detect your address.\n"
            "Please click your username in the top right corner\n"
            "to go to your participant page, then press ENTER"
        )
        current_url = page.url
        if "/participant/0x" in current_url:
            connected_address = current_url.split("/participant/")[-1]
            success(f"Got address: {connected_address[:10]}...")

    # ── Step 5: Enter Builder Journey ──
    step("Entering Builder Journey...")
    if connected_address:
        page.goto(f"https://portal.genlayer.foundation/#/participant/{connected_address}")
        page.wait_for_load_state("networkidle")
        time.sleep(3)

    for selector in ["text=Apply for the role", "text=Finish the journey", "text=Start as a Builder"]:
        if click_if_visible(page, selector):
            time.sleep(2)
            success("Entered Builder Journey")
            break
    else:
        print("  Already in Builder Journey or button not found")

    page.wait_for_load_state("networkidle")
    time.sleep(2)

    # ── Step 6: Connect GitHub ──
    step("Connect GitHub...")
    if click_if_visible(page, "text=Connect GitHub"):
        wait_for_user(
            "In the GitHub popup:\n"
            "  1. Authorize GenLayer\n"
            "  2. Come back here and press ENTER"
        )
        success("GitHub connected")
    else:
        print("  GitHub may already be connected")

    # ── Step 7: Star Boilerplate Repo ──
    step("Star Boilerplate repo...")
    if click_if_visible(page, "text=Star Repo"):
        wait_for_user(
            "In GitHub:\n"
            "  1. Click the Star button on the repo\n"
            "  2. Come back here and press ENTER"
        )
        success("Repo starred")
    else:
        print("  Star may already be done")

    # ── Step 8: Add GenLayer Testnet Chain ──
    step("Add GenLayer Testnet Chain...")
    buttons = page.locator("text=Add Network").all()
    if len(buttons) >= 1:
        try:
            buttons[0].click()
            wait_for_user(
                "In MetaMask:\n"
                "  1. Approve adding GenLayer Testnet\n"
                "  2. Come back here and press ENTER"
            )
            success("Testnet chain added")
        except Exception:
            print("  Testnet chain may already be added")
    else:
        print("  Testnet chain may already be added")

    # ── Step 9: Top-up with Testnet GEN ──
    step("Get testnet tokens...")
    if click_if_visible(page, "text=Get Tokens"):
        wait_for_user(
            "In the faucet page:\n"
            "  1. Complete the token claim\n"
            "  2. Come back here and press ENTER"
        )
        success("Tokens claimed")
    else:
        print("  Tokens may already be claimed")

    # ── Step 10: Add Studio Network ──
    step("Add Studio Network...")
    page.wait_for_load_state("networkidle")
    time.sleep(1)
    buttons = page.locator("text=Add Network").all()
    if len(buttons) >= 1:
        try:
            buttons[-1].click()
            wait_for_user(
                "In MetaMask:\n"
                "  1. Approve adding Studio Network\n"
                "  2. Come back here and press ENTER"
            )
            success("Studio Network added")
        except Exception:
            print("  Studio Network may already be added")
    else:
        print("  Studio Network may already be added")

    # ── Step 11: Deploy Contract ──
    step("Deploy contract in Studio...")
    if not click_if_visible(page, "text=Open Studio"):
        page.goto(STUDIO_URL)
    page.wait_for_load_state("networkidle")
    time.sleep(3)
    success("Studio opened")

    wait_for_user(
        "In GenLayer Studio:\n"
        "  1. Select llm_erc20.py from the left panel\n"
        "  2. Click the Run and Debug icon (left sidebar)\n"
        "  3. Click Deploy button\n"
        "  4. Wait for 'Contract deployed' message\n"
        "  5. Come back here and press ENTER"
    )
    success("Contract deployed")

    # ── Step 12: Complete Builder Journey ──
    step("Completing Builder Journey...")
    wait_for_user(
        "In the browser:\n"
        "  1. Click your username in the top right corner\n"
        "  2. Scroll down to find 'Complete Builder Journey' button\n"
        "  3. Click it\n"
        "  4. Come back here and press ENTER"
    )
    success("Builder Journey completed")

    # ── Step 13: Referral Link ──
    step("Getting referral link...")
    wait_for_user(
        "In the browser:\n"
        "  1. Scroll down to 'Join the community' section\n"
        "  2. Click 'Become a referrer'\n"
        "  3. Copy your referral link and save it\n"
        "  4. Come back here and press ENTER"
    )
    success("Referral link saved")

    wait_for_user("Press ENTER to finish this wallet and close the tab")
    page.close()
    print(f"\nWallet {wallet['address'][:10]}... DONE!")


# ─────────────────────────────────────────────
#  Main
# ─────────────────────────────────────────────

def main():
    print("""
WaterkoofAI x GenLayer Airdrop Script Kit v1.5
t.me/WaterkoofAI_Bot
--------------------------------------------------
This script NEVER collects private keys
Use at your own risk - For educational purposes only
--------------------------------------------------
    """)

    config  = load_config()
    wallets = config.get("wallets", [])

    if not wallets:
        print("ERROR: No wallets found in STEP2_Fill_your_wallet_info.json.")
        sys.exit(1)

    # Filter out placeholder wallets
    wallets = [w for w in wallets if not w["address"].startswith("0xYour")]
    if not wallets:
        print("ERROR: Please replace the placeholder wallet addresses in STEP2_Fill_your_wallet_info.json.")
        sys.exit(1)

    print(f"Found {len(wallets)} wallet(s) in config")
    print(f"Referral code: {config.get('referral_code', 'none')}")

    chrome_cmd = get_chrome_debug_command()

    print(f"""
{'='*60}
BEFORE YOU CONTINUE:
Make sure Chrome is already running with remote debugging.
Command to start Chrome (run in a separate terminal):

  {chrome_cmd}

If Chrome is already open and ready, just press ENTER.
{'='*60}
    """)
    input("Press ENTER when Chrome is open and ready...")

    with sync_playwright() as p:
        try:
            browser = p.chromium.connect_over_cdp("http://localhost:9222")
            context = browser.contexts[0]
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
Check your points: portal.genlayer.foundation
Follow @WaterkoofAI_Bot for more airdrops
--------------------------------------------------
    """)


if __name__ == "__main__":
    main()
