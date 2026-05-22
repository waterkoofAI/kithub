"""
WaterkoofAI x Monetrix Airdrop Script Kit v1.0
======================================================
COVERAGE DECLARATION:
- Project: Monetrix
- Portal URL: https://www.monetrix.xyz/app/signal
- Total airdrop tasks: 7
- Tasks automated by this Kit: 4 / 7 (57%)
- Manual tasks remaining: Connect X account, follow on X, Telegram join, Discord join, amplify announcement, final claim steps
- Estimated points from this Kit: complete the Genesis Signal missions to claim the Pioneer SBT and 5 Genesis invite codes
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
5. Run: python monetrix_auto.py

Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
"""

import json
import time
import sys
import os
import platform
from playwright.sync_api import sync_playwright

# ── Monetrix URLs ──
PROJECT_HOME = "https://www.monetrix.xyz/app/signal"
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
    clicked = wait_and_click_any(
        page,
        [
            "button:has-text('Connect Wallet')",
            "button:has-text('Connect')",
            "text=Connect Wallet",
            "text=Connect",
            "button:has-text('Claim Signal')",
        ],
        "connect wallet button",
        timeout=10000,
    )

    if not clicked:
        print("  Unable to auto-click a connect wallet button.")
        wait_for_user(
            "On the Monetrix page: click the connect wallet or Claim Signal button, then choose Bitget Wallet when prompted."
        )
    else:
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
        success("Bitget Wallet prompt detected")
        wait_for_user(
            "Approve the Bitget Wallet connection popup and make sure the Hyperliquid network is selected. Do NOT auto-approve or skip the wallet approval."
        )
    else:
        print("Bitget Wallet was not detected on the page.")
        print("Install Bitget Wallet from the Chrome Web Store if needed:")
        print("  https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak")
        wait_for_user(
            "Open Bitget Wallet in Chrome, connect manually to Monetrix, and confirm the network is Hyperliquid. Then press ENTER."
        )

    success("Wallet connection step completed")


def run_wallet(wallet, config, context):
    print(f"\n{'='*60}")
    print(f"Processing wallet: {wallet['address'][:10]}...")
    print(f"{'='*60}")

    page = context.new_page()

    step("Opening Monetrix Genesis Signal page...")
    page.goto(PROJECT_HOME)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Monetrix page loaded")

    step("Connecting Bitget Wallet on Monetrix...")
    connect_bitget_wallet(page)
    time.sleep(2)

    # ── TASK 1: Verify wallet ──
    step("Verifying wallet ownership...")
    if wait_and_click_any(
        page,
        [
            "button:has-text('Verify Wallet')",
            "button:has-text('Verify')",
            "button:has-text('Verify Signal')",
            "button:has-text('Confirm')",
        ],
        "verify wallet button",
        timeout=10000,
    ):
        wait_for_user(
            "Approve the gasless wallet verification signature in Bitget Wallet. This is a manual approval and no gas is spent."
        )
        success("Wallet verification completed")
    else:
        print("  Verify wallet button may already be completed or not visible yet.")

    # ── TASK 2: Connect X account ──
    step("Connecting your X account...")
    if wait_and_click_any(
        page,
        [
            "button:has-text('Connect X')",
            "button:has-text('Connect Twitter')",
            "text=Connect X",
            "text=Connect Twitter",
        ],
        "connect X account button",
        timeout=10000,
    ):
        wait_for_user(
            "Sign in to your X account and authorize Monetrix to link your handle. Then return and press ENTER."
        )
        success("X account connected")
    else:
        wait_for_user(
            "On the Monetrix page, manually connect your X account by using the Connect X or Connect Twitter button. Press ENTER when done."
        )

    # ── TASK 3: Follow Monetrix on X ──
    step("Following Monetrix on X...")
    wait_for_user(
        "Open your X account, follow @monetrix_xyz, then return to Monetrix and click the Verify button for the follow task if needed. Press ENTER when done."
    )
    success("Follow on X completed")

    # ── TASK 4: Subscribe to announcements on Telegram ──
    step("Joining Monetrix announcements on Telegram...")
    wait_for_user(
        "Join the Monetrix announcement Telegram channel, then return to Monetrix and click Verify for the Telegram task. Press ENTER when done."
    )
    success("Telegram verification task completed")

    # ── TASK 5: Join Monetrix Discord ──
    step("Joining Monetrix Discord...")
    wait_for_user(
        "Join the Monetrix Discord server, then return to Monetrix and click Verify for the Discord task. Press ENTER when done."
    )
    success("Discord verification task completed")

    # ── TASK 6: Amplify the Genesis announcement ──
    step("Amplifying the Genesis announcement...")
    wait_for_user(
        "Share or quote the Monetrix Genesis announcement from your connected X account, then return to Monetrix and verify the amplify task. Press ENTER when done."
    )
    success("Announcement amplification completed")

    # ── TASK 7: Claim Pioneer SBT ──
    step("Claiming the Pioneer SBT and invite codes...")
    if wait_and_click_any(
        page,
        [
            "button:has-text('Claim Signal')",
            "button:has-text('Claim Pioneer SBT')",
            "button:has-text('Claim')",
            "text=Claim Signal",
        ],
        "claim button",
        timeout=10000,
    ):
        wait_for_user(
            "If a final Bitget Wallet approval appears, approve it and confirm your Pioneer SBT claim. Then return and press ENTER."
        )
        success("Claim step completed")
    else:
        wait_for_user(
            "If the claim button is not auto-detected, use Monetrix to claim your Pioneer SBT and invite codes manually. Press ENTER when finished."
        )

    wait_for_user("Press ENTER to finish this wallet and close the tab")
    page.close()
    print(f"\nWallet {wallet['address'][:10]}... DONE!")
    print(f"\nSummary of completed tasks:")
    print(f"  [x] Open Monetrix Signal page")
    print(f"  [x] Connect Bitget Wallet")
    print(f"  [x] Verify wallet ownership")
    print(f"  [x] Connect X account")
    print(f"  [x] Follow @monetrix_xyz on X")
    print(f"  [x] Join Telegram")
    print(f"  [x] Join Discord")
    print(f"  [x] Amplify Genesis announcement")
    print(f"  [x] Claim Pioneer SBT")


def main():
    print("""
WaterkoofAI x Monetrix Airdrop Script Kit v1.0
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
        if w.get("address", "").startswith("0x") and
        not w.get("address", "").startswith("0xYour")
    ]
    if not wallets:
        print("ERROR: Please replace the placeholder wallet addresses in STEP2_Fill_your_wallet_info.json.")
        sys.exit(1)

    print(f"Found {len(wallets)} wallet(s) in config")
    print(f"Network: {config.get('network', 'Hyperliquid')}")

    chrome_cmd = get_chrome_debug_command()

    print(f"""
{'='*60}
BEFORE YOU CONTINUE:
1. You MUST use the Bitget Wallet Chrome extension:
   https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak

2. Make sure Chrome is running with remote debugging.
   Command to start Chrome (run in a separate terminal):

   {chrome_cmd}

3. Open Monetrix Genesis Signal and connect Bitget Wallet in the Chrome-Debug window.
4. The correct network to use is Hyperliquid.

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

Monetrix Activity Checklist:
  [x] Open Monetrix Signal page
  [x] Connect Bitget Wallet
  [x] Verify wallet ownership
  [x] Connect X account
  [x] Follow @monetrix_xyz
  [x] Join Telegram
  [x] Join Discord
  [x] Amplify the Genesis announcement
  [x] Claim Pioneer SBT

Tips for maximizing potential:
  - Use the same X account you want engraved on the Pioneer SBT.
  - Keep your Bitget Wallet on Hyperliquid.
  - Save your 5 invite codes for trusted friends.

Follow @WaterkoofAI_Bot for more airdrop scripts
--------------------------------------------------
    """)


if __name__ == "__main__":
    main()
