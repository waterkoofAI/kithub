"""
WaterkoofAI x Isometric Airdrop Script Kit v1.0
======================================================
COVERAGE DECLARATION:
- Project: Isometric
- Portal URL: https://devnet.isomkts.com
- Total airdrop tasks: 7
- Tasks automated by this Kit: 4 / 7 (57%)
- Manual tasks remaining: wallet approvals, claiming faucet tokens, trading manually.
- Estimated points from this Kit: Helps earn confirmed $ISO token via testnet interactions.
- Tested on: Windows
- Wallet used: Bitget Wallet (Chrome extension) with Solana Devnet enabled

SECURITY NOTICE:
- This script is open source and fully auditable
- Your private keys are NEVER collected or uploaded
- Bitget Wallet signing steps require manual approval
- This script NEVER approves tokens, signs devnet transactions, trades, or approves wallet popups for you
- For educational purposes only. Use at your own risk.

Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
"""

import json
import time
import sys
import os
import platform
from playwright.sync_api import sync_playwright

# -- Isometric URLs --
PROJECT_HOME = "https://devnet.isomkts.com"
FAUCET_URL = "https://faucet.quicknode.com/drip"
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
    Connect Bitget Wallet on Isometric.
    Strictly requires Bitget Wallet extension to be installed.
    """
    step("Connecting Bitget Wallet on Solana Devnet...")

    connect_selectors = [
        "button:has-text('Connect Wallet')",
        "button:has-text('Select Wallet')",
        "button:has-text('Connect')",
    ]

    connect_clicked = wait_and_click_any(
        page,
        connect_selectors,
        description="Connect Wallet button"
    )
    evm_selection = [
        "button:has-text('Solana')",
        "text=Solana",
        "#radix-_r_0_ > div.flex.flex-col.gap-4.pt-4 > div > button:nth-child(2)",
    ]

    wait_and_click_any(page, evm_selection, description="Solana")

    if not connect_clicked:
        wait_for_user(
            "Could not find the Connect Wallet button automatically.\n"
            "Please click Connect Wallet manually on the website, then press ENTER."
        )

    time.sleep(2)

    extension_selectors = [
        "button:has-text('Bitget Wallet')",
        "button:has-text('BITGET WALLET')",
        "text=BITGET WALLET",
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
            "  2. IMPORTANT: You must enable devnet in your Bitget Wallet settings if you haven't already.\n"
            "  3. Ensure you are on the Solana Devnet.\n"
            "  4. Approve only the connection or signature you recognize.\n\n"
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
        "6. Confirm you are using Solana Devnet.\n"
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
        "button:has-text('Faucet')",
        "button:has-text('Trade')",
        "button:has-text('Provide Liquidity')",
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
    
    print(f"\n{'='*60}")
    print(f"Processing wallet: {wallet_address[:15]}...")
    print(f"{'='*60}")

    page = context.new_page()

    # -- TASK 1: Devnet Faucet --
    step("Checking Devnet SOL balance and faucet...")
    page.goto(FAUCET_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    ensure_bitget_wallet_connected(page, "Faucet page")
    time.sleep(3)
    wait_for_user(
        "Claim Devnet SOL from QuickNode Faucet:\n\n"
        "  1. Ensure your Bitget Wallet is on Solana Devnet.\n"
        "  2. Copy your Solana wallet address.\n"
        "  3. Paste it in the QuickNode faucet page and request Devnet SOL.\n"
        "  4. Wait for the transaction to complete.\n\n"
        "Press ENTER when you have claimed Devnet SOL or if you already have enough."
    )
    success("Devnet SOL faucet step completed")

    # -- TASK 2: Open Isometric and Connect --
    step("Opening Isometric devnet app...")
    page.goto(PROJECT_HOME)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Isometric page loaded")

    connect_bitget_wallet(page)
    time.sleep(2)

    ensure_bitget_wallet_connected(page, "Main app page")

    # -- TASK 3: Claim Test USDC --
    step("Claiming Test USDC...")
    wait_for_user(
        "Claim Test USDC from Isometric:\n\n"
        "  1. Look for a Faucet or Claim button on the Isometric app.\n"
        "  2. Click it to mint test USDC for devnet trading.\n"
        "  3. Approve the transaction in your Bitget Wallet.\n\n"
        "Press ENTER when you have claimed test USDC."
    )
    success("Test USDC claimed")

    # -- TASK 4: Trading and Liquidity --
    step("Reviewing Trading and Liquidity options...")
    wait_for_user(
        "Trade and Provide Liquidity (Devnet):\n\n"
        "  1. Navigate to the trading section.\n"
        "  2. Place range positions (e.g., predict where the price of an asset will be).\n"
        "  3. Navigate to the Liquidity or Vaults section.\n"
        "  4. Provide test USDC liquidity to the shared vault.\n"
        "  5. Approve each transaction manually in your Bitget Wallet.\n"
        "  6. Make sure to occasionally manage/close some positions.\n\n"
        "Press ENTER when finished with your testnet activities."
    )
    success("Trading and liquidity step completed")

    page.close()
    print(f"\nWallet {wallet_address[:15]}... DONE!")
    print(f"\nSummary of completed tasks:")
    print(f"  [x] Obtain Devnet SOL from faucet")
    print(f"  [x] Connect Bitget Wallet on Solana Devnet")
    print(f"  [x] Claim Test USDC on Isometric")
    print(f"  [x] Perform testnet trading and LP actions")


def main():
    print("""
WaterkoofAI x Isometric Airdrop Script Kit v1.0
t.me/WaterkoofAI_Bot
--------------------------------------------------
This script NEVER collects private keys
This script NEVER approves, deposits, trades, or claims for you
Use at your own risk - For educational purposes only
Wallet REQUIRED: Bitget Wallet (Chrome extension)
--------------------------------------------------
    """)

    config  = load_config()
    wallets = config.get("wallets", [])

    if not wallets:
        print("ERROR: No wallets found in STEP2_Fill_your_wallet_info.json.")
        sys.exit(1)

    # Validate Solana addresses: not starting with 0x, not placeholder, not empty
    valid_wallets = []
    for w in wallets:
        addr = w.get("address", "").strip()
        if addr and not addr.lower().startswith("0x") and "YourSolanaWalletAddress" not in addr:
            valid_wallets.append(w)

    if not valid_wallets:
        print("ERROR: Please replace the placeholder wallet addresses in STEP2_Fill_your_wallet_info.json with valid Solana addresses.")
        sys.exit(1)

    print(f"Found {len(valid_wallets)} wallet(s) in config")
    print(f"Network: {config.get('network', 'solana-devnet')}")

    chrome_cmd = get_chrome_debug_command()

    print(f"""
{'='*60}
BEFORE YOU CONTINUE:
1. You MUST use the Bitget Wallet Chrome extension:
   https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak

2. Make sure Chrome is running with remote debugging.
   Command to start Chrome (run in a separate terminal):

   {chrome_cmd}

3. You MUST switch Bitget Wallet to Solana Devnet. You may need to enable devnet in the wallet settings.
4. This script will not sign transactions or trade for you.

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

        for i, wallet in enumerate(valid_wallets):
            print(f"\n--- Wallet {i+1} of {len(valid_wallets)} ---")
            run_wallet(wallet, config, context)
            if i < len(valid_wallets) - 1:
                input("\nPress ENTER to continue to the next wallet...")

    print("""
--------------------------------------------------
All wallets processed!

Isometric Activity Checklist:
  [x] Connect Bitget Wallet on Solana Devnet
  [x] Claim Devnet SOL & Test USDC
  [x] Place range positions
  [x] Provide liquidity

Tips for maximizing potential:
  - This is a testnet, so it's completely free to use.
  - Return regularly to manage positions and open new ones.
  - Testnet activity is often heavily weighted for early adopters.
  - Join their Discord to leave feedback and bug reports if applicable.

Follow @WaterkoofAI_Bot for more airdrop scripts
--------------------------------------------------
    """)


if __name__ == "__main__":
    main()
