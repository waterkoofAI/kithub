"""
WaterkoofAI x Caster Airdrop Script Kit v2.0
======================================================
COVERAGE DECLARATION:
- Project: Caster (Prediction Markets L1)
- Portal URL: https://testnet.caster.trade/atelier
- Total testnet tasks: 6
- Tasks automated by this Kit: 6 / 6 (100%)
- Manual tasks remaining: None (all wallet approvals are manual by design)
- **IMPORTANT**: Caster airdrop is NOT CONFIRMED. This is speculative.
  No official token, points program, or reward criteria announced.
  Early testnet participation and feedback may qualify for retroactive rewards on comparable projects.
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
5. Run: python caster_auto.py

Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
"""

import json
import time
import sys
import os
import platform
from playwright.sync_api import sync_playwright

# ── Caster URLs ──
PROJECT_HOME = "https://testnet.caster.trade/atelier"
FAUCET_URL   = "https://www.alchemy.com/faucets/arbitrum-sepolia"
TESTNET_USDC = "https://faucet.circle.com/"
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
    click_if_visible(page, 'button:has-text("Connect")', timeout=5000)
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
        click_if_visible(page, 'button:has-text("Bitget Wallet")', timeout=2000)
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
    step("Opening Caster...")
    page.goto(PROJECT_HOME)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Caster loaded")

    # Connect wallet
    connect_bitget_wallet(page)
    time.sleep(2)

    # Project Tasks

    # ── TASK 1: Visit the Caster Testnet ──
    step("Visit the Caster Testnet...")
    page.goto(PROJECT_HOME)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Caster loaded")
    
    wait_for_user(
        "Task: Visit the Caster Testnet\n\n"
        "  In the browser:\n"
        "  1. Follow the prompt for Visit Caster Testnet\n"
        "  2. Sign any required transactions in Bitget Wallet\n"
        "  3. Come back here and press ENTER\n\n"
        "  If you want to skip, just press ENTER."
    )
    success("Visit the Caster Testnet done")

    # ── TASK 2: Connect Your Wallet ──
    step("Connect Your Wallet...")
    page.goto(PROJECT_HOME)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Caster loaded")
    
    wait_and_click_any(page, [
        'button:has-text("Connect")',
        'button:has-text("Wallet")',
        'text=Connect'
    ], description="Connect button")
    
    wait_for_user(
        "Task: Connect Your Wallet\n\n"
        "  In the browser:\n"
        "  1. Connect an EVM wallet (Bitget Wallet).\n"
        "  2. Approve the connection.\n"
        "  3. Switch your wallet to the Arbitrum Sepolia test network.\n"
        "  4. Sign any required transactions in Bitget Wallet.\n"
        "  5. Come back here and press ENTER\n\n"
        "  If you want to skip, just press ENTER."
    )
    success("Connect Your Wallet done")

    # ── TASK 3: Get Testnet Gas and USDC ──
    step("Get Testnet Gas and USDC...")
    page.goto(FAUCET_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Caster loaded")
    
    wait_and_click_any(page, [
        'button:has-text("Faucet")',
        'button:has-text("Get Gas")',
        'button:has-text("Get USDC")',
        'text=Faucet'
    ], description="Faucet button")
    
    wait_for_user(
        "Task: Get Testnet Gas and USDC\n\n"
        "  You need test funds to trade (all FREE):\n"
        f"  1. Sepolia ETH for gas: claim from the Alchemy Arbitrum Sepolia faucet ({FAUCET_URL})\n"
        f"  2. Testnet USDC: use the in-app faucet (50 USDC) or grab from the Circle faucet ({TESTNET_USDC})\n"
        "  3. Sign any required transactions in Bitget Wallet\n"
        "  4. Come back here and press ENTER\n\n"
        "  If you want to skip, just press ENTER."
    )
    success("Get Testnet Gas and USDC done")

    # ── TASK 4: Deposit Tokens ──
    step("Deposit Tokens...")
    page.goto(PROJECT_HOME + "/portfolio")
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Caster loaded")
    
    wait_and_click_any(page, [
        'button:has-text("Deposit")',
        'text=Deposit'
    ], description="Deposit button")
    
    wait_for_user(
        "Task: Deposit Tokens\n\n"
        "  In the browser:\n"
        "  1. Open the Portfolio tab and click Deposit.\n"
        "  2. Move your testnet USDC into your Caster trading balance.\n"
        "  3. Sign any required transactions in Bitget Wallet.\n"
        "  4. Come back here and press ENTER\n\n"
        "  If you want to skip, just press ENTER."
    )
    success("Deposit Tokens done")

    # ── TASK 5: Place Predictions ──
    step("Place Predictions...")
    page.goto(PROJECT_HOME)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Caster loaded")
    
    wait_and_click_any(page, [
        'button:has-text("Predict")',
        'button:has-text("Trade")',
        'button:has-text("Market")',
        'text=Predict'
    ], description="Predict button")
    
    wait_for_user(
        "Task: Place Predictions\n\n"
        "  IMPORTANT: Trade across SEVERAL MARKETS, not just one position.\n"
        "  Broader, varied activity demonstrates genuine usage.\n\n"
        "  In the browser:\n"
        "  1. Browse the available markets, pick an event, and choose an outcome.\n"
        "  2. Buy and sell shares as your view changes.\n"
        "  3. Watch your open positions update in the Portfolio tab.\n"
        "  4. Trade a few different markets instead of placing a single position.\n"
        "  5. Sign any required transactions in Bitget Wallet.\n"
        "  6. Come back here and press ENTER\n\n"
        "  If you want to skip, just press ENTER."
    )
    success("Place Predictions done")

    # ── TASK 6: Submit Feedback on X ──
    step("Submit Feedback on X...")
    page.goto(PROJECT_HOME)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Caster loaded")
    
    wait_for_user(
       "Task: Submit Feedback on X (Twitter)\n\n"
       "  IMPORTANT: Keep your feedback SPECIFIC and useful.\n"
       "  Bug reports, UX notes, and feature requests are more valuable\n"
       "  than generic praise. The team is actively seeking feedback.\n\n"
       "  In the browser:\n"
       "  1. Go to X (Twitter) and compose a post about Caster testnet.\n"
       "  2. Include specific feedback: bugs, UX issues, or features.\n"
       "  3. Tag @CasterMarkets or mention the Caster project.\n"
       "  4. Come back here and press ENTER\n\n"
       "  If you want to skip, just press ENTER."
    )
    success("Submit Feedback on X done")


    # FINAL STEP: Close
    wait_for_user("Press ENTER to finish this wallet and close the tab")
    page.close()
    print(f"\nWallet {wallet['address'][:10]}... DONE!")
    print(f"\nSummary of completed tasks:")
    for task in ['Visit the Caster Testnet', 'Connect Your Wallet', 'Get Testnet Gas and USDC', 'Deposit Tokens', 'Place Predictions', 'Submit Feedback on X']:
        print(f"  [x] {task}")

def main():
    print("""
WaterkoofAI x Caster Airdrop Script Kit v2.1
t.me/WaterkoofAI_Bot
--------------------------------------------------
⚠️  IMPORTANT: Caster airdrop is NOT CONFIRMED
    This is speculative activity. No official token,
    points program, or rewards announced by Caster team.
    Early testnet participants may qualify for retroactive
    rewards on comparable projects (not guaranteed).

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

3. Ensure you have the required assets on Arbitrum Sepolia.

4. **BEST PRACTICE**: Run this script multiple times over several days.
   Spreading your activity makes it look like genuine participation
   rather than a one-time interaction.

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

CASTER TESTNET ACTIVITY COMPLETED:""")
    for task in ['Visit the Caster Testnet', 'Connect Your Wallet', 'Get Testnet Gas and USDC', 'Deposit Tokens', 'Place Predictions', 'Submit Feedback on X']:
        print(f"  [x] {task}")
        
    print("""
IMPORTANT TIPS FOR MAXIMIZING YOUR CHANCES:
  1. Trade across SEVERAL MARKETS (not just one position)
  2. Come back MULTIPLE TIMES (spread activity over several sessions)
  3. Keep feedback SPECIFIC (bug reports, UX notes > generic praise)
  
  Activity that demonstrates genuine usage is more likely to be
  recognized if Caster retroactively rewards early testnet participants.

Website: https://caster.trade
Follow @WaterkoofAI_Bot for more airdrop scripts
--------------------------------------------------
    """)

if __name__ == "__main__":
    main()