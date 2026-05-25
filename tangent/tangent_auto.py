"""
WaterkoofAI x Tangent Airdrop Script Kit v1.0
======================================================
COVERAGE DECLARATION:
- Project: Tangent
- Portal URL: https://app.tangent.finance/predeposit
- Total airdrop tasks: 6
- Tasks automated by this Kit: 3 / 6 (50%)
- Manual tasks remaining: wallet approvals, USDC/frxUSD acquisition, Ethereum gas management, Curve pool deposit, LP-token strategy, retention, and future claim steps
- Estimated points from this Kit: Helps start Tangent predeposit activity for the listed 2% TAN predeposit allocation and 2x predeposit points boost
- Tested on: Windows
- Wallet used: Bitget Wallet (Chrome extension)

SECURITY NOTICE:
- This script is open source and fully auditable
- Your private keys are NEVER collected or uploaded
- Bitget Wallet signing steps require manual approval
- This script NEVER approves tokens, deposits funds, stakes LP tokens, withdraws, or approves wallet popups for you
- For educational purposes only. Use at your own risk.

HOW TO USE:
1. Drop STEP1_Drop_me_to_any_AI.md into any AI chat for guided setup
2. Fill in STEP2_Fill_your_wallet_info.json with your wallet details
3. Install Bitget Wallet Chrome extension:
   https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak
4. Start Chrome with remote debugging (see If_you_dont_use_AI_read_me.txt)
5. Run: python tangent_auto.py

Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
"""

import json
import time
import sys
import os
import platform
from playwright.sync_api import sync_playwright

# -- Tangent URLs --
PROJECT_HOME = "https://app.tangent.finance/predeposit"
PREDEPOSIT_URL = "https://app.tangent.finance/predeposit"
TANGENT_SITE = "https://www.tangent.finance/"
CURVE_SITE = "https://curve.fi/"
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


def clean_config_value(value):
    if value is None:
        return ""
    return str(value).strip()


def get_deposit_token(config):
    token = clean_config_value(config.get("deposit_token"))
    if token not in ["USDC", "frxUSD"]:
        return "USDC"
    return token


def get_pool_choice(config):
    pool = clean_config_value(config.get("pool_choice"))
    if pool not in ["USDC/USG", "frxUSD/USG"]:
        token = get_deposit_token(config)
        return "frxUSD/USG" if token == "frxUSD" else "USDC/USG"
    return pool


def get_lp_strategy(config):
    strategy = clean_config_value(config.get("lp_strategy"))
    if strategy not in ["hold", "stake"]:
        return "hold"
    return strategy


def connect_bitget_wallet(page):
    """
    Connect Bitget Wallet on app.tangent.finance.
    Strictly requires Bitget Wallet extension to be installed.
    """

    step("Connecting Bitget Wallet on Ethereum mainnet...")

    connect_selectors = [
        "button:has-text('Connect Wallet')",
        "button:has-text('Bitget Wallet')",
    ]

    connect_clicked = wait_and_click_any(
        page,
        connect_selectors,
        description="Connect Wallet button"
    )

    if not connect_clicked:
        wait_for_user(
            "Could not find the Tangent Connect Wallet button automatically.\n"
            "Please click Connect Wallet manually, then press ENTER."
        )

    time.sleep(2)

    wallet_step_selectors = [
        "button:has-text('Connect wallet')",
    ]
    wait_and_click_any(page, wallet_step_selectors, description="wallet option")
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
            "  2. Use Ethereum mainnet in Bitget Wallet.\n"
            "  3. Approve only the Tangent connection or signature you recognize.\n"
            "  4. Do not approve any token approval, deposit, stake, or withdrawal unless you intended it.\n\n"
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
        "3. Refresh Tangent if needed.\n"
        "4. Click Connect Wallet and select Bitget Wallet.\n"
        "5. Approve the connection in the extension popup.\n"
        "6. Confirm you are using Ethereum mainnet.\n"
        "7. Press ENTER when connected and ready."
    )

    success("Bitget Wallet connected manually")


def ensure_bitget_wallet_connected(page, page_name="current page"):
    """Reconnect only when Tangent shows a wallet connection prompt."""
    step(f"Checking wallet connection on {page_name}...")

    connect_prompt_selectors = [
        "button:has-text('Connect Wallet')",
        "button:has-text('Connect')",
        "button:has-text('Sign in')",
        "text=Connect Wallet",
    ]
    connected_state_selectors = [
        "button:has-text('Deposit')",
        "button:has-text('Approve')",
        "button:has-text('Withdraw')",
        "text=Predeposit",
        "text=USDC",
        "text=frxUSD",
        "text=USG",
        "text=LP",
        "text=Points",
        "text=Disconnect",
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


def select_predeposit_pool(page, config):
    token = get_deposit_token(config)
    pool = get_pool_choice(config)

    step(f"Selecting Tangent predeposit pool: {pool}...")

    pool_selectors = [
        f"button:has-text('{pool}')",
        f"text={pool}",
        f"button:has-text('{token}')",
        f"text={token}",
    ]

    if wait_and_click_any(page, pool_selectors, description=f"{pool} pool", timeout=10000):
        success(f"Selected or opened {pool}")
        return

    wait_for_user(
        "Select the Tangent predeposit pool manually:\n\n"
        f"  Preferred token: {token}\n"
        f"  Preferred pool: {pool}\n\n"
        "Choose the matching pool in the browser, then press ENTER."
    )
    success("Pool selection step completed")


def run_wallet(wallet, config, context):
    wallet_address = wallet.get("address", "")
    token = get_deposit_token(config)
    pool = get_pool_choice(config)
    lp_strategy = get_lp_strategy(config)

    print(f"\n{'='*60}")
    print(f"Processing wallet: {wallet_address[:10]}...")
    print(f"{'='*60}")

    page = context.new_page()

    # -- TASK 1: Open Tangent predeposit --
    step("Opening Tangent predeposit page...")
    page.goto(PREDEPOSIT_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Tangent predeposit page loaded")

    # -- TASK 2: Connect Bitget Wallet --
    connect_bitget_wallet(page)
    time.sleep(2)

    # -- TASK 3: Confirm Ethereum and funds --
    ensure_bitget_wallet_connected(page, "Tangent predeposit page")
    wait_for_user(
        "Predeposit prerequisites:\n\n"
        "  1. Confirm Bitget Wallet is on Ethereum mainnet.\n"
        "  2. Make sure you have enough ETH for mainnet gas.\n"
        f"  3. Make sure you have {token} available if you plan to deposit.\n"
        "  4. Review Tangent/Curve pool risk before continuing.\n\n"
        "Press ENTER when ready, or press ENTER to skip funding for this wallet."
    )
    success("Prerequisite check completed")

    # -- TASK 4: Select pool and deposit manually --
    page.goto(PREDEPOSIT_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    ensure_bitget_wallet_connected(page, "predeposit form")
    select_predeposit_pool(page, config)

    if wait_and_click_any(
        page,
        [
            "button:has-text('Deposit')",
            "button:has-text('Predeposit')",
            "button:has-text('Add Liquidity')",
            "button:has-text('Supply')",
            "text=Deposit",
            "text=Predeposit",
        ],
        description="deposit button",
        timeout=10000,
    ):
        wait_for_user(
            "Complete Tangent predeposit manually:\n\n"
            f"  1. Use the {pool} pool if that is still the pool shown by Tangent.\n"
            f"  2. Enter only the {token} amount you are comfortable depositing.\n"
            "  3. If an Approve transaction is needed, review token, spender, and amount before approving.\n"
            "  4. If a Deposit/Add Liquidity transaction follows, review pool, amount, slippage, and received LP token.\n"
            "  5. Approve each Bitget Wallet popup manually only if it matches your intent.\n\n"
            "If you do not want to deposit now, close the modal and press ENTER."
        )
    else:
        wait_for_user(
            "Could not find the Deposit/Predeposit button automatically.\n"
            "Use the Tangent page manually to approve and deposit into the configured pool if you choose.\n"
            "If you want to skip, just press ENTER."
        )
    success("Predeposit guidance completed")

    # -- TASK 5: Decide LP-token strategy --
    step("Reviewing LP-token strategy...")
    if lp_strategy == "stake":
        wait_for_user(
            "LP-token strategy from config: stake\n\n"
            "  Tangent notes that holding the LP token in your wallet is the usual way to maximize Tangent predeposit points.\n"
            "  Staking the LP token on Curve, Convex, or StakeDAO may earn external rewards but can reduce Tangent points.\n\n"
            "  If you still want to stake, open the official Curve/Convex/StakeDAO route yourself, verify the pool, and approve manually.\n"
            "  Press ENTER when the LP-token strategy is complete."
        )
    else:
        wait_for_user(
            "LP-token strategy from config: hold\n\n"
            "  1. Keep the received Curve LP token in the same wallet if you want to target maximum Tangent predeposit points.\n"
            "  2. Avoid moving, staking, or withdrawing the LP token unless you understand how it affects points.\n"
            "  3. Save a note of your deposit date, pool, token, and transaction hash.\n\n"
            "Press ENTER when you have recorded the details."
        )
    success("LP-token strategy reviewed")

    # -- TASK 6: Retention and future claim plan --
    step("Reviewing retention and future claim plan...")
    wait_for_user(
        "Final Tangent checklist:\n\n"
        "  1. Check that the Tangent page shows your position or points after deposit.\n"
        "  2. Keep track of the expected three-month active points phase and follow Tangent updates.\n"
        "  3. Do not withdraw early unless you accept the possible points impact.\n"
        "  4. When TAN claim opens, use only official Tangent links and approve manually.\n\n"
        "Press ENTER when finished."
    )
    success("Retention and claim plan reviewed")

    wait_for_user("Press ENTER to finish this wallet and close the tab")
    page.close()
    print(f"\nWallet {wallet_address[:10]}... DONE!")
    print(f"\nSummary of completed tasks:")
    print(f"  [x] Open Tangent predeposit page")
    print(f"  [x] Connect Bitget Wallet on Ethereum mainnet")
    print(f"  [x] Confirm ETH gas and {token} readiness")
    print(f"  [x] Review {pool} predeposit flow")
    print(f"  [x] Review LP-token strategy: {lp_strategy}")
    print(f"  [x] Review retention and future claim plan")


def main():
    print("""
WaterkoofAI x Tangent Airdrop Script Kit v1.0
t.me/WaterkoofAI_Bot
--------------------------------------------------
This script NEVER collects private keys
This script NEVER approves, deposits, stakes, withdraws, or claims for you
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
    print(f"Network: {config.get('network', 'ethereum')}")
    print(f"Deposit token: {get_deposit_token(config)}")
    print(f"Pool choice: {get_pool_choice(config)}")
    print(f"LP strategy: {get_lp_strategy(config)}")

    chrome_cmd = get_chrome_debug_command()

    print(f"""
{'='*60}
BEFORE YOU CONTINUE:
1. You MUST use the Bitget Wallet Chrome extension:
   https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak

2. Make sure Chrome is running with remote debugging.
   Command to start Chrome (run in a separate terminal):

   {chrome_cmd}

3. Use Ethereum mainnet in Bitget Wallet.
4. Keep ETH for mainnet gas and USDC or frxUSD only if you plan to predeposit.
5. Tangent predeposit uses Curve LP exposure, so review smart-contract and depeg risk.
6. This script will not approve tokens, deposit, stake, withdraw, or claim for you.

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

Tangent Activity Checklist:
  [x] Open Tangent predeposit page
  [x] Connect Bitget Wallet on Ethereum mainnet
  [x] Confirm ETH gas and deposit token readiness
  [x] Review USDC/USG or frxUSD/USG predeposit flow
  [x] Review LP-token hold/stake strategy
  [x] Review retention and future TAN claim plan

Tips for maximizing potential:
  - Hold the received LP token in the same wallet if targeting maximum Tangent points.
  - Keep a note of deposit date, pool, amount, and transaction hash.
  - Watch Tangent announcements for active points, retention, withdrawals, and claim timing.
  - Never approve unlimited allowances unless you intentionally accept that risk.
  - Use only official Tangent links for future TAN claim steps.

Follow @WaterkoofAI_Bot for more airdrop scripts
--------------------------------------------------
    """)


if __name__ == "__main__":
    main()
