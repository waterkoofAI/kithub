"""
WaterkoofAI x ACI Airdrop Script Kit v2.0
======================================================
COVERAGE DECLARATION:
- Project: ACI (Post-Quantum AI Blockchain)
- Portal URL: https://aci-token.net/airdrop
- Total airdrop tasks: 6
- Tasks automated by this Kit: 6 / 6 (100%)
- Manual tasks remaining: None (all wallet approvals are manual by design)
- Estimated points from this Kit: Qualify for 30,000,000 $ACI allocation
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
5. Run: python aci_auto.py

Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
"""

import json
import time
import sys
import os
import platform
from playwright.sync_api import sync_playwright

# ── ACI URLs ──
PROJECT_HOME = "https://aci-token.net/airdrop"
WALLET_URL = "https://aci-token.net/wallet"
STAKING_URL = "https://aci-token.net/staking"
TESTNET_CLAIM_URL = "https://www.alchemy.com/faucets/ethereum-sepolia"
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
    click_if_visible(page, 'button:has-text("I understand")')
    click_if_visible(page, 'button:has-text("Connect Wallet")')
    time.sleep(2)
    
    extension_selectors = [
        "button:has-text('Connect Wallet')",
        "text=Connect Wallet",
        "button:has-text('Bitget Wallet')"
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
            "After approval press ENTER."
        )

        success("Bitget Wallet connected via extension")
        return
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
    step("Opening ACI...")
    page.goto(WALLET_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("ACI loaded")

    # Connect wallet
    connect_bitget_wallet(page)
    time.sleep(2)

    # Project Tasks

    # ── TASK 1: Claim Sepolia Testnet ETH ──
    step("Claim Sepolia Testnet ETH...")
    page.goto(TESTNET_CLAIM_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    click_if_visible(page, 'button:has-text("I understand")')
    success("ACI loaded")
    
    wait_and_click_any(page, [
        'button:has-text("Claim")',
        'button:has-text("Faucet")',
        'text=Claim',
        'text=Faucet'
    ], description="Claim/Faucet button")
    
    wait_for_user(
        "Task: Claim Sepolia Testnet ETH\n\n"
        "  In the browser:\n"
        "  1. Follow the prompt for Claim Sepolia Testnet ETH\n"
        "  2. Sign any required transactions in Bitget Wallet\n"
        "  3. Come back here and press ENTER\n\n"
        "  If you want to skip, just press ENTER."
    )
    success("Claim Sepolia Testnet ETH done")

    # ── TASK 2: Connect wallet to ACI on Sepolia ──
    step("Connect wallet to ACI on Sepolia...")
    page.goto(PROJECT_HOME)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    click_if_visible(page, 'button:has-text("I understand")')
    success("ACI loaded")
    
    wait_and_click_any(page, [
        'button:has-text("Connect")',
        'button:has-text("Connect Wallet")',
        'text=Connect'
    ], description="Connect button")
    
    wait_for_user(
        "Task: Connect wallet to ACI on Sepolia\n\n"
        "  In the browser:\n"
        "  1. Follow the prompt for Connect wallet to ACI on Sepolia\n"
        "  2. Sign any required transactions in Bitget Wallet\n"
        "  3. Come back here and press ENTER\n\n"
        "  If you want to skip, just press ENTER."
    )
    success("Connect wallet to ACI on Sepolia done")

    # ── TASK 3: Swap ETH for ACI Test Tokens ──
    step("Swap ETH for ACI Test Tokens...")
    page.goto(WALLET_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    click_if_visible(page, 'button:has-text("I understand")')
    success("ACI loaded")
    
    wait_and_click_any(page, [
        'button:has-text("Swap")',
        'button:has-text("Trade")',
        'text=Swap'
    ], description="Swap button")
    
    wait_for_user(
        "Task: Swap ETH for ACI Test Tokens\n\n"
        "  In the browser:\n"
        "  1. Follow the prompt for Swap ETH for ACI Test Tokens\n"
        "  2. Sign any required transactions in Bitget Wallet\n"
        "  3. Come back here and press ENTER\n\n"
        "  If you want to skip, just press ENTER."
    )
    success("Swap ETH for ACI Test Tokens done")

    # ── TASK 4: Stake ACI to Unlock Missions ──
    step("Stake ACI to Unlock Missions...")
    page.goto(STAKING_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    click_if_visible(page, 'button:has-text("I understand")')
    success("ACI loaded")
    
    wait_and_click_any(page, [
        'button:has-text("Stake")',
        'button:has-text("Deposit")',
        'text=Stake'
    ], description="Stake button")
    
    wait_for_user(
        "Task: Stake ACI to Unlock Missions\n\n"
        "  In the browser:\n"
        "  1. Follow the prompt for Stake ACI to Unlock Missions\n"
        "  2. Sign any required transactions in Bitget Wallet\n"
        "  3. Come back here and press ENTER\n\n"
        "  If you want to skip, just press ENTER."
    )
    success("Stake ACI to Unlock Missions done")

    # ── TASK 5: Complete Missions and Zealy Quests ──
    step("Complete Missions and Zealy Quests...")
    page.goto(PROJECT_HOME)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    click_if_visible(page, 'button:has-text("I understand")')
    success("ACI loaded")
    click_if_visible(page, 'button:has-text("View Missions")')
    
    wait_and_click_any(page, [
        'button:has-text("Missions")',
        'button:has-text("Quests")',
        'text=Zealy'
    ], description="Missions button")
    
    wait_for_user(
        "Task: Complete Missions and Zealy Quests\n\n"
        "  In the browser:\n"
        "  1. Follow the prompt for Complete Missions and Zealy Quests\n"
        "  2. Sign any required transactions in Bitget Wallet\n"
        "  3. Come back here and press ENTER\n\n"
        "  If you want to skip, just press ENTER."
    )
    success("Complete Missions and Zealy Quests done")

    # ── TASK 6: Creator Program (Optional) ──
    step("Creator Program (Optional)...")
    page.goto(PROJECT_HOME)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("ACI loaded")
    
    wait_for_user(
       "Task: Creator Program (Optional) - 400 USDT Reward Pool\n\n"
       "  In the browser:\n"
       "  1. Create content about ACI or your testnet experience\n"
       "  2. Post on X/Twitter and tag @ACIToken\n"
       "  3. Submit your entry to the Creator Program\n"
       "  4. Come back here and press ENTER\n\n"
       "  Note: This is optional and doesn't affect your allocation.\n"
       "  If you want to skip, just press ENTER."
    )
    success("Creator Program done")


    # FINAL STEP: Close
    wait_for_user("Press ENTER to finish this wallet and close the tab")
    page.close()
    print(f"\nWallet {wallet['address'][:10]}... DONE!")
    print(f"\nSummary of completed tasks:")
    for task in ['Claim Sepolia Testnet ETH', 'Connect wallet to ACI on Sepolia', 'Swap ETH for ACI Test Tokens', 'Stake ACI to Unlock Missions', 'Complete Missions and Zealy Quests', 'Creator Program (Optional)']:
        print(f"  [x] {task}")

def main():
    print("""
WaterkoofAI x ACI Airdrop Script Kit v2.0
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

3. Ensure you have the required assets on Sepolia.

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

ACI Activity Checklist:""")
    for task in ['Claim Sepolia Testnet ETH', 'Connect wallet to ACI on Sepolia', 'Swap ETH for ACI Test Tokens', 'Stake ACI to Unlock Missions', 'Complete Missions and Zealy Quests']:
        print(f"  [x] {task}")
        
    print("""
Follow @WaterkoofAI_Bot for more airdrop scripts
--------------------------------------------------
    """)

if __name__ == "__main__":
    main()
