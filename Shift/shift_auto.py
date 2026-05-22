"""
WaterkoofAI x SHIFT Airdrop Script Kit v1.0
======================================================
COVERAGE DECLARATION:
- Project: SHIFT
- Portal URL: https://loyalty.shiftrwa.xyz/loyalty
- Total airdrop tasks: 6
- Tasks automated by this Kit: 3 / 6 (50%)
- Manual tasks remaining: Step 3–6 are manual by design (wallet approvals and quest completion require browser interaction)
- Estimated points from this Kit: Helps start pre-registration, connect Bitget Wallet, and guide you toward SHIFT loyalty badge setup
- Tested on: Windows
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
5. Run: python shift_auto.py

Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
"""

import json
import time
import sys
import os
import platform
from playwright.sync_api import sync_playwright

# ── SHIFT URLs ──
PROJECT_HOME = "https://loyalty.shiftrwa.xyz/loyalty"
CONFIG_FILE = "STEP2_Fill_your_wallet_info.json"


def get_chrome_debug_command():
    system = platform.system()
    home = os.path.expanduser("~")
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
    if os.environ.get("AUTO_CONFIRM") == "1":
        print("AUTO_CONFIRM: Automatically continuing in 5 seconds...")
        print(f"{'='*50}")
        time.sleep(5)
    else:
        print("Press ENTER when done...")
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
        el.wait_for(state="visible", timeout=timeout)
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
            el.wait_for(state="visible", timeout=timeout // len(selectors))
            el.click()
            return True
        except Exception:
            continue
    print(f"  {description} not found with any selector")
    return False

def connect_bitget_wallet(page):
    step("Connecting Bitget Wallet on Solana network...")
    connect_selectors = [
        "button:has-text('Connect Wallet')",
        "text=Connect Wallet",
    ]
    close_btn = page.locator("[class*='close']").first
    if close_btn.is_visible():
        close_btn.click(timeout=2000)
    
    if wait_and_click_any(page, connect_selectors, description="Connect wallet button", timeout=10000):
        time.sleep(2)
    else:
        wait_for_user(
            "Bitget Wallet connect already connected!\n\n"
            "Press Enter to continue..."
        )
        return

    extension_selectors = [
        "button:has-text('Bitget Wallet')",
        "text=Bitget Wallet",
        "text=BitKeep",
    ]
    extension_detected = False
    for selector in extension_selectors:
        try:
            el = page.locator(selector).first
            if el.is_visible(timeout=3000):
                el.click()
                extension_detected = True
                break
        except Exception:
            pass

    if extension_detected:
        success("Bitget Wallet prompt detected")
        wait_for_user(
            "Bitget Wallet should be asking you to connect or approve the wallet now.\n\n"
            "  1. Approve the connection in the Bitget Wallet extension.\n"
            "  2. Make sure the wallet is using the Solana network if prompted.\n"
            "  3. Confirm the wallet connection in the browser.\n\n"
            "Press ENTER when the wallet is connected."
        )
    else:
        print("Bitget Wallet extension was not detected automatically.")
        print("Please install Bitget Wallet and complete the wallet connection manually.")
        print("Chrome Web Store: https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak")
        wait_for_user(
            "Manual Bitget Wallet setup:\n\n"
            "  1. Install Bitget Wallet in the Chrome Debug profile.\n"
            "  2. Open Bitget Wallet and import or unlock your wallet.\n"
            "  3. Connect the wallet to the SHIFT loyalty dashboard.\n"
            "  4. Select Solana network if prompted.\n\n"
            "Press ENTER when the wallet is connected."
        )


def run_wallet(wallet, config, context):
    print(f"\n{'='*60}")
    print(f"Processing wallet: {wallet['address'][:10]}...")
    print(f"{'='*60}")

    page = context.new_page()

    # Get referral code, fallback to campaign default 'ICH3SIXS' if placeholder or empty
    ref_code = config.get("referral_code", "").strip()
    if ref_code and ref_code != "YOUR_REFERRAL_CODE":
        ref_code = f"?referral_code={ref_code}"
    else:
        ref_code = ""
    target_url = f"https://loyalty.shiftrwa.xyz/loyalty{ref_code}"

    step("Opening SHIFT loyalty dashboard...")
    page.goto(target_url)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("SHIFT loyalty dashboard loaded")

    connect_bitget_wallet(page)
    time.sleep(2)

    step("Preparing SHIFT pre-registration tasks...")
    if click_if_visible(page, "button:has-text('Join Pre-registration')") or click_if_visible(page, "text=Join Pre-registration"):
        wait_for_user(
            "Approve any Bitget Wallet connection or signing prompt now.\n\n"
            "  1. Approve the wallet connection in Bitget Wallet.\n"
            "  2. If a signature request appears, do not auto-approve it. Approve only if you recognize the request.\n"
            "  3. Return to the script and press ENTER."
        )
        success("Pre-registration entry attempted")
    else:
        print("  No direct pre-registration button was found, so the next steps will be manual.")

    wait_for_user(
        "Complete the SHIFT pre-registration loyalty tasks manually:\n\n"
        "  1. In the browser, finish the email submission, X account link, and social quest tasks shown on the SHIFT dashboard.\n"
        "  2. Complete all available missions for follow, repost, like, comment, and referral setup.\n"
        "  3. Reveal your badge once you have completed the pre-registration quests.\n"
        "  4. If you want, copy your referral link from the dashboard and save it for future sharing.\n\n"
        "Press ENTER when these steps are done or when you want to move to the next wallet."
    )
    success("Manual SHIFT quest guidance completed")

    wait_for_user("Press ENTER to finish this wallet and close the tab")
    page.close()

    print(f"\nWallet {wallet['address'][:10]}... DONE!")
    print(f"\nSummary of completed tasks:")
    print(f"  [x] Open SHIFT loyalty dashboard")
    print(f"  [x] Connect Bitget Wallet")
    print(f"  [ ] Complete SHIFT quest steps in browser")
    print(f"  [ ] Reveal SHIFT badge")
    print(f"  [ ] Fund wallet with SOL or BNB")
    print(f"  [ ] Trade SHIFT tokenized assets")
    print(f"  [ ] Share referral link")


def main():
    print("""
WaterkoofAI x SHIFT Airdrop Script Kit v1.0
t.me/WaterkoofAI_Bot
--------------------------------------------------
This script NEVER collects private keys
Use at your own risk - For educational purposes only
Wallet REQUIRED: Bitget Wallet (Chrome extension)
--------------------------------------------------
    """)

    config = load_config()
    wallets = config.get("wallets", [])

    if not wallets:
        print("ERROR: No wallets found in STEP2_Fill_your_wallet_info.json.")
        sys.exit(1)

    wallets = [
        w for w in wallets
        if w.get("address", "").strip() and
        not w.get("address", "").strip().startswith("0xYour")
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

3. Use the Solana network in Bitget Wallet for the SHIFT loyalty dashboard.
4. This script guides the pre-registration flow; most SHIFT quest steps remain manual.

If Chrome is already open and ready, just press ENTER.
{'='*60}
    """)
    if os.environ.get("AUTO_CONFIRM") == "1":
        print("AUTO_CONFIRM: Automatically continuing in 3 seconds...")
        time.sleep(3)
    else:
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
                if os.environ.get("AUTO_CONFIRM") == "1":
                    print("\nAUTO_CONFIRM: Continuing to the next wallet in 3 seconds...")
                    time.sleep(3)
                else:
                    input("\nPress ENTER to continue to the next wallet...")

    print("""
--------------------------------------------------
All wallets processed!

SHIFT Activity Checklist:
  [x] Open SHIFT loyalty dashboard
  [x] Connect Bitget Wallet
  [ ] Complete pre-registration quests
  [ ] Reveal loyalty badge
  [ ] Fund wallet with SOL or BNB
  [ ] Trade SHIFT tokenized assets
  [ ] Share referral link

Tips for maximizing potential:
  - Finish every reward quest before revealing your badge.
  - Keep an eye on the dashboard for new tasks and bonus quests.
  - Save your referral link so new users can join through you.

Follow @WaterkoofAI_Bot for more airdrop scripts
--------------------------------------------------
    """)


if __name__ == "__main__":
    main()
