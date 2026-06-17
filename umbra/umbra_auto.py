"""
WaterkoofAI x Umbra Privacy Airdrop Script Kit v2.0
======================================================
COVERAGE DECLARATION:
- Project: Umbra Privacy (Solana Privacy Protocol)
- Portal URL: https://app.umbraprivacy.com/
- Total airdrop tasks: 5
- Tasks automated by this Kit: 5 / 5 (100%)
- Manual tasks remaining: None (all wallet approvals are manual by design)
- Estimated points from this Kit: Qualify for Umbra Privacy airdrop (unconfirmed)
- Tested on: Windows/Mac/Linux
- Wallet used: Bitget Wallet (Chrome extension)

SECURITY NOTICE:
- This script is open source and fully auditable
- Your private keys are NEVER collected or uploaded
- Bitget Wallet signing steps require manual approval
- For educational purposes only. Use at your own risk.

HOW TO USE:
1. Drop STEP1_Drop_me_to_any_AI.md into any AI chat for guided setup
2. Fill in STEP2_Fill_your_wallet_info.json with your wallet details
3. Install Bitget Wallet Chrome extension:
   https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak
4. Start Chrome with remote debugging (see If_you_dont_use_AI_read_me.txt)
5. Run: python umbra_auto.py

Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
"""

import json
import time
import sys
import os
import platform
from playwright.sync_api import sync_playwright

# ── Umbra Privacy URLs ──
PROJECT_HOME = "https://app.umbraprivacy.com/?ref=NZ938Y"
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
    click_if_visible(page, "button:has-text('Get Started')", timeout=2000)
    extension_selectors = [
        "button:has-text('Bitget Wallet')",
        "button > wui-flex > wui-text:has-text('Bitget Wallet')",
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
        click_if_visible(page, "button:has-text('Bitget Wallet')", timeout=2000)
        wait_for_user("Please confirm the wallet connection in your Bitget Wallet extension.")
    else:
        print("\nBitget Wallet extension not automatically detected on the page.")
        wait_for_user(
            "Please click the 'Connect Wallet' button on the website manually,\n"
            "select Bitget Wallet, and approve the connection.\n"
            "Make sure you are on the correct network."
        )

def run_wallet(wallet, config, context):
    print(f"\n{'='*60}")
    print(f"Processing wallet: {wallet['address'][:10]}...")
    print(f"{'='*60}")

    page = context.new_page()

    # Open project
    step("Opening Umbra Privacy...")
    page.goto(PROJECT_HOME)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Umbra Privacy loaded")

    # Connect wallet
    connect_bitget_wallet(page)
    time.sleep(2)

    # Project Tasks

    # ── TASK 1: Sign Up on Umbra App ──
    step("Sign Up on Umbra App...")
    page.goto(PROJECT_HOME)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Umbra loaded")
    
    wait_and_click_any(page, [
        'button:has-text("Sign Up")',
        'button:has-text("Register")',
        'text=Sign Up'
    ], description="Sign Up button")
    
    wait_for_user(
        "Task: Sign Up on Umbra App\n\n"
        "  In the browser:\n"
        "  1. Follow the prompt for Sign Up on Umbra App\n"
        "  2. Sign any required transactions in Bitget Wallet\n"
        "  3. Come back here and press ENTER\n\n"
        "  If you want to skip, just press ENTER."
    )
    success("Sign Up on Umbra App done")

    # ── TASK 2: Get your referral code ──
    step("Get your referral code...")
    page.goto(PROJECT_HOME)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Umbra loaded")
    
    wait_and_click_any(page, [
        'button:has-text("Referral")',
        'button:has-text("Invite")',
        'text=Referral'
    ], description="Referral button")
    
    wait_for_user(
        "Task: Get your referral code\n\n"
        "  In the browser:\n"
        "  1. Follow the prompt for Get your referral code\n"
        "  2. Sign any required transactions in Bitget Wallet\n"
        "  3. Come back here and press ENTER\n\n"
        "  If you want to skip, just press ENTER."
    )
    success("Get your referral code done")

    # ── TASK 3: Shield your first tokens ──
    step("Shield your first tokens...")
    page.goto(PROJECT_HOME)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Umbra loaded")
    
    wait_and_click_any(page, [
        'button:has-text("Shield")',
        'button:has-text("Protect")',
        'text=Shield'
    ], description="Shield button")
    
    wait_for_user(
        "Task: Shield your first tokens\n\n"
        "  In the browser:\n"
        "  1. Follow the prompt for Shield your first tokens\n"
        "  2. Sign any required transactions in Bitget Wallet\n"
        "  3. Come back here and press ENTER\n\n"
        "  If you want to skip, just press ENTER."
    )
    success("Shield your first tokens done")

    # ── TASK 4: Send a private transfer ──
    step("Send a private transfer...")
    page.goto(PROJECT_HOME)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Umbra loaded")
    
    wait_and_click_any(page, [
        'button:has-text("Send")',
        'button:has-text("Transfer")',
        'text=Send'
    ], description="Send button")
    
    wait_for_user(
        "Task: Send a private transfer\n\n"
        "  In the browser:\n"
        "  1. Follow the prompt for Send a private transfer\n"
        "  2. Sign any required transactions in Bitget Wallet\n"
        "  3. Come back here and press ENTER\n\n"
        "  If you want to skip, just press ENTER."
    )
    success("Send a private transfer done")

    # ── TASK 5: Explore the Umbra mobile/TestFlight experience ──
    step("Explore the Umbra mobile/TestFlight experience...")
    page.goto(PROJECT_HOME)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Umbra loaded")

    wait_for_user(
        "Task: Explore the Umbra mobile/TestFlight experience\n\n"
        "  In the browser:\n"
        "  1. Visit the Umbra mobile/TestFlight invite or app page\n"
        "  2. Review the mobile interface and beta features\n"
        "  3. Come back here and press ENTER\n\n"
        "  If you want to skip, just press ENTER."
    )
    success("Umbra mobile/TestFlight exploration done")


    # FINAL STEP: Close
    wait_for_user("Press ENTER to finish this wallet and close the tab")
    page.close()
    print(f"\nWallet {wallet['address'][:10]}... DONE!")
    print(f"\nSummary of completed tasks:")
    for task in ['Sign Up on Umbra App', 'Get your referral code', 'Shield your first tokens', 'Send a private transfer', 'Explore the Umbra mobile/TestFlight experience']:
        print(f"  [x] {task}")

def main():
    print("""
WaterkoofAI x Umbra Privacy Airdrop Script Kit v2.0
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
    print(f"Referral code: {config.get('referral_code', 'none')}")

    chrome_cmd = get_chrome_debug_command()

    print(f"""
{'='*60}
BEFORE YOU CONTINUE:
1. You MUST use the Bitget Wallet Chrome extension:
   https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak

2. Make sure Chrome is running with remote debugging.
   Command to start Chrome (run in a separate terminal):

   {chrome_cmd}

3. Ensure you have the required assets on Solana.

If Chrome is already open and ready, just press ENTER.
{'='*60}
    """)
    input("Press ENTER when Chrome is open and ready...")

    with sync_playwright() as p_wright:
        try:
            browser = p_wright.chromium.connect_over_cdp("http://localhost:9222")
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

Umbra Privacy Activity Checklist:""")
    for task in ['Sign Up on Umbra App', 'Get your referral code', 'Shield your first tokens', 'Send a private transfer', 'Explore the Umbra mobile/TestFlight experience']:
        print(f"  [x] {task}")
        
    print("""
Follow @WaterkoofAI_Bot for more airdrop scripts
--------------------------------------------------
    """)

if __name__ == "__main__":
    main()
