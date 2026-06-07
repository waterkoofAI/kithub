"""
WaterkoofAI x Pod Network Airdrop Script Kit v1.0
======================================================
COVERAGE DECLARATION:
- Project: Pod Network
- Portal URL: https://test.pod.network/
- Total airdrop tasks: 6
- Tasks automated by this Kit: 6 / 6 guided browser steps (wallet approvals, X verification, trades, and deposits stay manual)
- Manual tasks remaining: Bitget Wallet approvals/signatures, X verification, paper testnet trades, optional waitlist signup, optional real-fund deposit, and Discord role claiming
- Estimated points from this Kit: Helps create Pod testnet competition activity through wallet signup, X verification, paper trading, leaderboard review, waitlist, and community follow-up
- Tested on: Windows/macOS/Linux with Chrome remote debugging
- Wallet used: Bitget Wallet (Chrome extension)

SECURITY NOTICE:
- This script is open source and fully auditable
- Your private keys are NEVER collected or uploaded
- Bitget Wallet signing steps require manual approval
- Trading orders and any waitlist deposit are manual only
- For educational purposes only. Use at your own risk.

HOW TO USE:
1. Drop STEP1_Drop_me_to_any_AI.md into any AI chat for guided setup
2. Fill in STEP2_Fill_your_wallet_info.json with your wallet details
3. Install Bitget Wallet Chrome extension:
   https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak
4. Start Chrome with remote debugging (see If_you_dont_use_AI_read_me.txt)
5. Run: python pod_auto.py

Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
"""

import json
import time
import sys
import os
import platform
from playwright.sync_api import sync_playwright

# -- Pod Network URLs --
POD_TESTNET = "https://test.pod.network/"
POD_HOME = "https://pod.network/"
POD_MAIN_APP = "https://app.pod.network/"
POD_DOCS = "https://docs.v2.pod.network/"
POD_EXPLORER = "https://explorer.v1.pod.network/"
CONFIG_FILE = "STEP2_Fill_your_wallet_info.json"

POD_DEVNET = {
    "network_name": "Pod Devnet / Testnet",
    "rpc_url": "https://rpc.v1.dev.pod.network",
    "chain_id": "1293",
    "symbol": "pUSD",
    "explorer": POD_EXPLORER,
}


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


def open_page(page, url, label):
    step(f"Opening {label}...")
    page.goto(url)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success(f"{label} loaded")


def print_pod_network_details():
    print("\nPod network details from official docs:")
    print(f"  Network:  {POD_DEVNET['network_name']}")
    print(f"  RPC URL:  {POD_DEVNET['rpc_url']}")
    print(f"  Chain ID: {POD_DEVNET['chain_id']}")
    print(f"  Symbol:   {POD_DEVNET['symbol']}")
    print(f"  Explorer: {POD_DEVNET['explorer']}")


def click_join_competition_if_present(page):
    time.sleep(5)
    joined = wait_and_click_any(
        page,
        [
            "button:has-text('Join the Competition')",
            "[role='button']:has-text('Join the Competition')",
            "text=Join the Competition",
            ""
        ],
        "Join the Competition button",
        timeout=5000,
    )
    if joined:
        time.sleep(2)
        success("Join the Competition popup handled")
    else:
        print("  Join the Competition popup was not visible; continuing.")
    return joined


def connect_bitget_wallet(page):
    step("Connecting Bitget Wallet to Pod Testnet...")
    print("  Required network if prompted: Pod Devnet / Testnet (chain ID 1293)")

    click_join_competition_if_present(page)

    login_clicked = wait_and_click_any(
        page,
        [
            "button:has-text('Login')",
            "[role='button']:has-text('Login')",
            "text=Login",
            "button:has-text('Log in')",
            "text=Log in",
        ],
        "Login button",
        timeout=1000,
    )

    if login_clicked:
        time.sleep(2)
        success("Login popup opened")
    else:
        print("  Login button was not visible; wallet may already be connected.")

    wallet_option_clicked = wait_and_click_any(
        page,
        [
            "button:has-text('Continue with a wallet')",
            "[role='button']:has-text('Continue with a wallet')",
            "text=Continue with a wallet",
            "button:has-text('Wallet')",
            "text=Wallet",
        ],
        "Continue with a wallet option",
        timeout=8000,
    )

    if not wallet_option_clicked:
        wait_for_user(
            "Continue with wallet manually:\n\n"
            "  1. If the Pod login popup is open, choose Continue with a wallet.\n"
            "  2. Do not use the email login for this kit unless you prefer to handle it yourself.\n"
            "  3. Choose Bitget Wallet only when the wallet list opens.\n\n"
            "If you are already connected, just press ENTER."
        )
    else:
        time.sleep(2)

    extension_selectors = [
        "button:has-text('Bitget Wallet')",
        "text=Bitget Wallet",
        "text=BitKeep",
    ]

    extension_detected = False
    detected_selector = None
    for selector in extension_selectors:
        try:
            if page.locator(selector).first.is_visible(timeout=2000):
                extension_detected = True
                detected_selector = selector
                break
        except Exception:
            pass

    if extension_detected:
        try:
            page.locator(detected_selector).first.click()
        except Exception:
            wait_and_click_any(page, extension_selectors, "Bitget Wallet option", timeout=6000)

        wait_for_user(
            "Approve the Bitget Wallet connection or sign-in popup manually.\n\n"
            "Before approving:\n"
            "  1. Confirm the site is test.pod.network or an official Pod login popup.\n"
            "  2. Confirm the wallet address is the one you added to the config.\n"
            "  3. If Bitget asks to add or switch network, review Pod details:\n"
            "     RPC: https://rpc.v1.dev.pod.network\n"
            "     Chain ID: 1293\n"
            "     Symbol: pUSD\n\n"
            "Approve only the expected connection or sign-in message."
        )
    else:
        print("\nBitget Wallet was not detected in the wallet list.")
        print("Install or enable Bitget Wallet in this Chrome-Debug profile:")
        print("https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak")
        wait_for_user(
            "Manual Bitget Wallet connection:\n\n"
            "  1. Install or enable Bitget Wallet in this Chrome window.\n"
            "  2. On Pod, click Login.\n"
            "  3. Choose Continue with a wallet.\n"
            "  4. Choose Bitget Wallet only.\n"
            "  5. Approve the connection manually.\n"
            "  6. If prompted, add or switch to Pod Devnet / Testnet (chain ID 1293).\n\n"
            "Then return here and press ENTER."
        )

    wait_for_user(
        "Finish Pod sign-in:\n\n"
        "  1. Wait until the Pod testnet page shows you as logged in.\n"
        "  2. If a second wallet signature appears, review and approve only the expected Pod sign-in message.\n"
        "  3. If the competition welcome modal remains open, close or continue through it.\n\n"
        "Then press ENTER here."
    )
    success("Bitget Wallet connection step complete")


def open_testnet_and_connect(page, wallet):
    open_page(page, POD_TESTNET, "Pod Testnet")
    connect_bitget_wallet(page)
    wait_for_user(
        "Confirm Pod Testnet is ready:\n\n"
        "  1. The page should show Testnet or Competition information.\n"
        f"  2. The connected wallet should start with {wallet['address'][:10]}...\n"
        "  3. If the page shows markets, account value, or X verification status, you are in the right place.\n\n"
        "Press ENTER when ready."
    )
    success("Pod testnet connection checked")


def verify_x_account(page):
    open_page(page, POD_TESTNET, "Pod Testnet X Verification")

    clicked = wait_and_click_any(
        page,
        [
            "button:has-text('Verify X')",
            "button:has-text('Connect X')",
            "button:has-text('Continue with X')",
            "button:has-text('Link X')",
            "text=Verify X",
            "text=Connect X",
            "text=Continue with X",
            "text=Link X",
        ],
        "X verification button",
        timeout=7000,
    )

    if clicked:
        wait_for_user(
            "Complete X verification manually:\n\n"
            "  1. Follow the official X login/authorization popup.\n"
            "  2. Use only your own X account.\n"
            "  3. Return to Pod and wait for the verification status to update.\n"
            "  4. One person should use one account only; avoid sybil behavior.\n\n"
            "If verification is already complete or closed, press ENTER."
        )
    else:
        wait_for_user(
            "Check X verification status manually:\n\n"
            "  1. Look for Checking X verification status, Verify X, Connect X, or Account status.\n"
            "  2. If Pod offers X verification, complete it through the official popup.\n"
            "  3. If it says already verified or no longer available, note the status.\n\n"
            "Press ENTER when done."
        )

    success("X verification step reviewed")


def trade_testnet_markets(page, config):
    open_page(page, POD_TESTNET, "Pod Testnet Markets")

    preferred_markets = config.get("preferred_markets", [])
    for market in preferred_markets:
        if click_if_visible(page, f"text={market}", timeout=1500):
            print(f"  Opened preferred market: {market}")
            time.sleep(2)
            break

    wait_for_user(
        "Place paper testnet trades manually:\n\n"
        "  1. Choose a market such as S&P 500, NASDAQ 100, Gold, AAPL, NVDA, or GOOGL.\n"
        f"  2. Suggested trade size from config: {config.get('trade_size_usd', 'small')}.\n"
        f"  3. Suggested max leverage from config: {config.get('max_leverage', '2x')}.\n"
        "  4. Open a small long or short position only if you understand the risk to your competition score.\n"
        "  5. Review any order confirmation or Bitget Wallet signature manually.\n"
        "  6. Do not use real funds for the testnet trading competition.\n\n"
        "If you do not want to trade now, press ENTER to skip."
    )
    success("Testnet market trading step reviewed")


def review_positions_and_leaderboard(page):
    open_page(page, POD_TESTNET, "Pod Account and Leaderboard")

    wait_and_click_any(
        page,
        [
            "button:has-text('Portfolio')",
            "button:has-text('Positions')",
            "button:has-text('Leaderboard')",
            "text=Portfolio",
            "text=Positions",
            "text=Leaderboard",
        ],
        "portfolio or leaderboard tab",
        timeout=4000,
    )

    wait_for_user(
        "Review competition progress:\n\n"
        "  1. Check account value, open positions, P&L, and available paper balance.\n"
        "  2. Check leaderboard or ranking if visible.\n"
        "  3. Close or reduce risky positions if you do not want them open.\n"
        "  4. Note that the competition ranking is based on performance, so avoid reckless leverage.\n\n"
        "Press ENTER when done."
    )
    success("Portfolio and leaderboard step reviewed")


def join_waitlist(page):
    open_page(page, POD_HOME, "Pod Network Website")

    clicked = wait_and_click_any(
        page,
        [
            "a:has-text('Join the Waitlist')",
            "button:has-text('Join the Waitlist')",
            "text=Join the Waitlist",
            "a:has-text('Join Waitlist')",
            "text=Join Waitlist",
        ],
        "Join the Waitlist link",
        timeout=7000,
    )

    if not clicked:
        open_page(page, POD_MAIN_APP, "Pod Main App / Waitlist")

    wait_for_user(
        "Optional mainnet waitlist:\n\n"
        "  1. Join the waitlist only if you want mainnet early access.\n"
        "  2. Use the official Pod page only.\n"
        "  3. Email, X login, and any deposit are manual; this script does not type them for you.\n"
        "  4. If a deposit is offered, it may involve real funds. Deposit only if you intentionally choose to.\n"
        "  5. Save proof or a screenshot only if you need it for Discord roles later.\n\n"
        "If you do not want to join the waitlist, press ENTER to skip."
    )
    success("Waitlist step reviewed")


def review_discord_roles(page):
    open_page(page, POD_DOCS, "Pod Official Docs")

    wait_for_user(
        "Optional Discord and role follow-up:\n\n"
        "  1. Use official Pod links from the website or docs only.\n"
        "  2. Join Discord if you want community and waitlist role follow-up.\n"
        "  3. If a Waitlist role requires proof, use the instructions inside the official Discord.\n"
        "  4. Ignore DMs asking for seed phrases, private keys, or wallet passwords.\n\n"
        "Press ENTER when done or skipped."
    )
    success("Discord and roles step reviewed")


def run_wallet(wallet, config, context):
    print(f"\n{'='*60}")
    print(f"Processing wallet: {wallet['address'][:10]}...")
    print(f"{'='*60}")

    page = context.new_page()

    # TASK 1: Enter Pod testnet competition and connect wallet
    open_testnet_and_connect(page, wallet)

    # TASK 2: Verify X account if available
    verify_x_account(page)

    # TASK 3: Place or review paper testnet trades
    trade_testnet_markets(page, config)

    # TASK 4: Review account, positions, and leaderboard
    review_positions_and_leaderboard(page)

    # TASK 5: Join mainnet waitlist if desired
    join_waitlist(page)

    # TASK 6: Review Discord and role follow-up
    review_discord_roles(page)

    wait_for_user("Press ENTER to finish this wallet and close the tab")
    page.close()
    print(f"\nWallet {wallet['address'][:10]}... DONE!")
    print(f"\nSummary of completed tasks:")
    print(f"  [x] Entered or reviewed Pod testnet competition")
    print(f"  [x] Connected Bitget Wallet to Pod")
    print(f"  [x] Verified or reviewed X verification")
    print(f"  [x] Placed or reviewed paper testnet trades")
    print(f"  [x] Reviewed positions, account value, and leaderboard")
    print(f"  [x] Reviewed waitlist and Discord role follow-up")


def main():
    print("""
WaterkoofAI x Pod Network Airdrop Script Kit v1.0
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
    print(f"Network: {config.get('network', 'pod-devnet')}")
    print(f"Preferred markets: {', '.join(config.get('preferred_markets', []))}")
    print(f"Suggested trade size: {config.get('trade_size_usd', 'small')}")
    print(f"Suggested max leverage: {config.get('max_leverage', '2x')}")

    chrome_cmd = get_chrome_debug_command()

    print(f"""
{'='*60}
BEFORE YOU CONTINUE:
1. You MUST use the Bitget Wallet Chrome extension:
   https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak

2. Make sure Chrome is running with remote debugging.
   Command to start Chrome (run in a separate terminal):

   {chrome_cmd}

3. First time only: install or set up Bitget Wallet in the Chrome-Debug profile.
   Never paste a seed phrase, private key, or wallet password into this script or any AI chat.

4. If Pod asks for network details, use:
   RPC URL: https://rpc.v1.dev.pod.network
   Chain ID: 1293
   Symbol: pUSD
   Explorer: https://explorer.v1.pod.network

5. Wallet signatures, paper trades, X verification, waitlist signup, and any deposit are manual.

If Chrome is already open and ready, just press ENTER.
{'='*60}
    """)
    input("Press ENTER when Chrome is open and ready...")

    print_pod_network_details()

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

Pod Network Activity Checklist:
  [x] Enter Pod testnet competition
  [x] Login with Bitget Wallet
  [x] Verify X account if available
  [x] Place or review paper testnet trades
  [x] Review positions and leaderboard
  [x] Review mainnet waitlist and Discord roles

Tips for maximizing potential:
  - Use one consistent wallet and X account for Pod activity.
  - Trade steadily with small paper positions instead of max leverage.
  - Check leaderboard and account value after each session.
  - Join the waitlist only from official Pod links.
  - Never share private keys, seed phrases, or wallet passwords.

Follow @WaterkoofAI_Bot for more airdrop scripts
--------------------------------------------------
    """)


if __name__ == "__main__":
    main()
