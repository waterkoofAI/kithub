"""
WaterkoofAI x Ceitnot Protocol Airdrop Script Kit v1.0
======================================================
COVERAGE DECLARATION:
- Project: Ceitnot Protocol
- Portal URL: https://www.ceitnot.io/
- Total airdrop tasks: 6
- Tasks automated by this Kit: 6 / 6 guided browser steps (wallet approvals and transactions stay manual)
- Manual tasks remaining: Bitget Wallet approvals, faucet claim, test collateral mint, vault deposit/borrow, PSM swap, and social quests
- Estimated points from this Kit: Helps create eligible Arbitrum Sepolia testnet activity across gas, collateral, vault, ceitUSD, PSM, and social tasks
- Tested on: Windows/macOS/Linux with Chrome remote debugging
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
5. Run: python ceitnot_auto.py

Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
"""

import json
import time
import sys
import os
import platform
from playwright.sync_api import sync_playwright

# -- Ceitnot Protocol URLs --
PROJECT_HOME = "https://www.ceitnot.io/"
CEITNOT_DASHBOARD = "https://www.ceitnot.io/dashboard"
CEITNOT_MARKETS = "https://www.ceitnot.io/markets"
CEITNOT_POSITION = "https://www.ceitnot.io/position"
CEITNOT_SWAP = "https://www.ceitnot.io/swap"
CEITNOT_REWARDS = "https://www.ceitnot.io/rewards"
CEITNOT_LIGHTPAPER = "https://www.ceitnot.io/lightpaper"
ALCHEMY_ARBITRUM_SEPOLIA_FAUCET = "https://www.alchemy.com/faucets/arbitrum-sepolia"
QUICKNODE_ARBITRUM_SEPOLIA_FAUCET = "https://faucet.quicknode.com/arbitrum/sepolia"
CONFIG_FILE = "STEP2_Fill_your_wallet_info.json"

ARBITRUM_SEPOLIA = {
    "network_name": "Arbitrum Sepolia",
    "rpc_url": "https://sepolia-rollup.arbitrum.io/rpc",
    "chain_id": "421614",
    "symbol": "ETH",
    "explorer": "https://sepolia.arbiscan.io",
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


def print_arbitrum_sepolia_details():
    print("\nArbitrum Sepolia network details:")
    print(f"  Network:  {ARBITRUM_SEPOLIA['network_name']}")
    print(f"  RPC URL:  {ARBITRUM_SEPOLIA['rpc_url']}")
    print(f"  Chain ID: {ARBITRUM_SEPOLIA['chain_id']}")
    print(f"  Symbol:   {ARBITRUM_SEPOLIA['symbol']}")
    print(f"  Explorer: {ARBITRUM_SEPOLIA['explorer']}")


def choose_arbitrum_sepolia_in_app(page):
    """Select the app-level Ceitnot network dropdown when it is visible."""
    step("Checking Ceitnot app network selector...")

    selectors = [
        "select[aria-label='Select app network']",
        "select:has(option:has-text('Arbitrum Sepolia'))",
        "select",
    ]

    for selector in selectors:
        try:
            select = page.locator(selector).first
            if select.is_visible(timeout=2000):
                try:
                    select.select_option(value="421614")
                    success("Ceitnot app network set to Arbitrum Sepolia")
                    return
                except Exception:
                    select.select_option(label="Arbitrum Sepolia")
                    success("Ceitnot app network set to Arbitrum Sepolia")
                    return
        except Exception:
            continue

    print("  Ceitnot network selector was not visible; continuing.")


def connect_bitget_wallet(page):
    step("Connecting Bitget Wallet...")
    print("  Required network: Arbitrum Sepolia (chain ID 421614)")

    connect_clicked = wait_and_click_any(
        page,
        [
            "button:has-text('Connect Wallet')",
            "button:has-text('Connect')",
            "[data-rk] button:has-text('Connect Wallet')",
            "[data-rk] button:has-text('Connect')",
            "text=Connect Wallet",
            "text=Connect",
        ],
        "Connect Wallet button",
        timeout=10000,
    )

    if not connect_clicked:
        wait_for_user(
            "Connect Bitget Wallet manually:\n\n"
            "  1. Click the Connect Wallet button on the Ceitnot page.\n"
            "  2. Choose Bitget Wallet only.\n"
            "  3. Approve the connection in Bitget Wallet.\n"
            "  4. Confirm Bitget Wallet is on Arbitrum Sepolia (chain ID 421614).\n\n"
            "If the wallet is already connected, just press ENTER."
        )
        success("Bitget Wallet connection step complete")
        return

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
            "Approve the Bitget Wallet popup manually.\n\n"
            "Before approving, confirm the network is Arbitrum Sepolia:\n"
            "  RPC URL: https://sepolia-rollup.arbitrum.io/rpc\n"
            "  Chain ID: 421614\n"
            "  Symbol: ETH\n\n"
            "Do not approve anything you do not understand."
        )
    else:
        print("\nBitget Wallet was not detected in the wallet list.")
        print("Install or enable Bitget Wallet in this Chrome-Debug profile:")
        print("https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak")
        wait_for_user(
            "Manual Bitget Wallet connection:\n\n"
            "  1. Install or enable Bitget Wallet in this Chrome window.\n"
            "  2. Click Connect Wallet on the page again.\n"
            "  3. Choose Bitget Wallet only.\n"
            "  4. Approve the connection manually.\n"
            "  5. Switch to Arbitrum Sepolia (chain ID 421614).\n\n"
            "Then return here and press ENTER."
        )

    success("Bitget Wallet connection step complete")


def get_testnet_gas(page, wallet, config):
    open_page(page, ALCHEMY_ARBITRUM_SEPOLIA_FAUCET, "Alchemy Arbitrum Sepolia Faucet")
    wait_for_user(
        "Claim Arbitrum Sepolia test ETH:\n\n"
        "  1. Use only your public Bitget Wallet address.\n"
        f"  2. Your current wallet starts with: {wallet['address'][:10]}...\n"
        "  3. Request free Arbitrum Sepolia ETH for gas.\n"
        "  4. Wait until the faucet says the drip was sent.\n\n"
        "Never enter a private key, seed phrase, or wallet password."
    )

    if config.get("use_quicknode_faucet", False):
        open_page(page, QUICKNODE_ARBITRUM_SEPOLIA_FAUCET, "QuickNode Arbitrum Sepolia Faucet")
        wait_for_user(
            "Optional backup faucet:\n\n"
            "  1. Use only your public Bitget Wallet address.\n"
            "  2. Select Arbitrum Sepolia if the faucet asks for chain and network.\n"
            "  3. Complete any human verification yourself.\n"
            "  4. Wait for the drip to finish.\n\n"
            "If you do not want to use this faucet, press ENTER to skip."
        )

    success("Testnet gas step done")


def open_ceitnot_and_connect(page):
    open_page(page, CEITNOT_DASHBOARD, "Ceitnot Dashboard")
    choose_arbitrum_sepolia_in_app(page)
    connect_bitget_wallet(page)
    wait_for_user(
        "Confirm Ceitnot is ready:\n\n"
        "  1. The Ceitnot app should show your wallet as connected.\n"
        "  2. The app network selector should be Arbitrum Sepolia.\n"
        "  3. Bitget Wallet should also be on Arbitrum Sepolia.\n\n"
        "If the app asks you to switch networks, approve only the Arbitrum Sepolia switch."
    )
    success("Ceitnot app connection checked")


def mint_test_collateral(page, config):
    open_page(page, CEITNOT_MARKETS, "Ceitnot Markets")
    choose_arbitrum_sepolia_in_app(page)
    connect_bitget_wallet(page)
    wait_for_user(
        "Mint or claim test collateral:\n\n"
        "  1. Stay on Arbitrum Sepolia in both Ceitnot and Bitget Wallet.\n"
        "  2. Open the Faucet, Markets, or Get Vault Shares area.\n"
        f"  3. Preferred collateral from config: {config.get('preferred_collateral', 'mock-wstETH')}.\n"
        "  4. If Ceitnot shows a mock token mint button, mint a small test amount.\n"
        "  5. Review every Bitget Wallet popup and approve only the expected testnet transaction.\n"
        "  6. If an oracle feed is stale, use the app's refresh control only if you understand the popup.\n\n"
        "These are test tokens only. If you want to skip, press ENTER."
    )
    success("Test collateral step done")


def open_vault_and_mint_ceitusd(page, config):
    open_page(page, CEITNOT_POSITION, "Ceitnot Position")
    choose_arbitrum_sepolia_in_app(page)
    connect_bitget_wallet(page)
    wait_for_user(
        "Open a vault and mint ceitUSD:\n\n"
        "  1. Use the Borrow, Engine, Position, or Markets flow in Ceitnot.\n"
        "  2. Select your mock collateral market.\n"
        "  3. Deposit a small amount of test collateral into the vault.\n"
        f"  4. Borrow a small amount of ceitUSD ({config.get('borrow_amount_ceitusd', 'small')} from config).\n"
        "  5. Keep the collateral ratio safely above the minimum.\n"
        "  6. Manually approve each Bitget Wallet transaction only after checking the details.\n\n"
        "Do not use real funds. If you want to skip, press ENTER."
    )
    success("Vault and ceitUSD step done")


def use_psm_swap(page, config):
    open_page(page, CEITNOT_SWAP, "Ceitnot Swap / PSM")
    choose_arbitrum_sepolia_in_app(page)
    connect_bitget_wallet(page)
    wait_for_user(
        "Use the Peg Stability Module (PSM):\n\n"
        "  1. On the Swap page, choose a small swap amount.\n"
        f"  2. Suggested amount from config: {config.get('psm_swap_amount', 'small')}.\n"
        "  3. Swap between ceitUSD and the available mock stablecoin if the page supports it.\n"
        "  4. If you do a reverse swap, keep the amount tiny.\n"
        "  5. Review token approvals and swap transactions manually in Bitget Wallet.\n\n"
        "Only approve transactions you recognize. If you want to skip, press ENTER."
    )
    success("PSM swap step done")


def complete_social_and_rewards(page):
    open_page(page, CEITNOT_REWARDS, "Ceitnot Rewards")
    choose_arbitrum_sepolia_in_app(page)
    wait_for_user(
        "Review rewards and social quests:\n\n"
        "  1. Check whether the Ceitnot Rewards page has any claim, lock, or quest notices.\n"
        "  2. Do not lock or claim unless you understand the transaction.\n"
        "  3. Complete official social tasks from the current Ceitnot airdrop guide:\n"
        "     - Follow Ceitnot on X\n"
        "     - Join the official Telegram\n"
        "     - Follow the official LinkedIn\n"
        "  4. Check official announcements for Zealy or Galxe quests if they appear later.\n\n"
        "If no social links are visible, use only links from the official site or airdrops guide."
    )
    success("Social and rewards step done")


def run_wallet(wallet, config, context):
    print(f"\n{'='*60}")
    print(f"Processing wallet: {wallet['address'][:10]}...")
    print(f"{'='*60}")

    page = context.new_page()

    # TASK 1: Get Arbitrum Sepolia gas
    get_testnet_gas(page, wallet, config)

    # TASK 2: Open Ceitnot and connect Bitget Wallet
    open_ceitnot_and_connect(page)

    # TASK 3: Mint test collateral
    mint_test_collateral(page, config)

    # TASK 4: Open vault and mint ceitUSD
    open_vault_and_mint_ceitusd(page, config)

    # TASK 5: Use PSM / Swap
    use_psm_swap(page, config)

    # TASK 6: Rewards and social quests
    complete_social_and_rewards(page)

    wait_for_user("Press ENTER to finish this wallet and close the tab")
    page.close()
    print(f"\nWallet {wallet['address'][:10]}... DONE!")
    print(f"\nSummary of completed tasks:")
    print(f"  [x] Claimed or checked Arbitrum Sepolia test ETH")
    print(f"  [x] Connected Bitget Wallet to Ceitnot")
    print(f"  [x] Minted or reviewed test collateral")
    print(f"  [x] Opened a vault and minted or reviewed ceitUSD borrow flow")
    print(f"  [x] Used or reviewed the PSM swap flow")
    print(f"  [x] Reviewed rewards and social quests")


def main():
    print("""
WaterkoofAI x Ceitnot Protocol Airdrop Script Kit v1.0
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

    # Display any project-specific config
    print(f"Referral code: {config.get('referral_code', 'none')}")
    print(f"Network: {config.get('network', 'arbitrum-sepolia')}")
    print(f"Preferred collateral: {config.get('preferred_collateral', 'mock-wstETH')}")
    print(f"QuickNode backup faucet enabled: {config.get('use_quicknode_faucet', False)}")

    chrome_cmd = get_chrome_debug_command()

    print(f"""
{'='*60}
BEFORE YOU CONTINUE:
1. You MUST use the Bitget Wallet Chrome extension:
   https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak

2. Make sure Chrome is running with remote debugging.
   Command to start Chrome (run in a separate terminal):

   {chrome_cmd}

3. Make sure Bitget Wallet is installed in the Chrome-Debug profile.

4. Make sure Bitget Wallet is on Arbitrum Sepolia:
   RPC URL: https://sepolia-rollup.arbitrum.io/rpc
   Chain ID: 421614
   Symbol: ETH
   Explorer: https://sepolia.arbiscan.io

5. All transaction, approval, faucet, and social steps are manual.

If Chrome is already open and ready, just press ENTER.
{'='*60}
    """)
    input("Press ENTER when Chrome is open and ready...")

    print_arbitrum_sepolia_details()

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

Ceitnot Protocol Activity Checklist:
  [x] Get Arbitrum Sepolia test ETH
  [x] Connect Bitget Wallet to Ceitnot
  [x] Mint or claim test collateral
  [x] Deposit collateral and mint ceitUSD
  [x] Test the PSM / Swap page
  [x] Complete social quests from official links

Tips for maximizing potential:
  - Use all core features: faucet/collateral, vault borrow, and PSM swap.
  - Keep a vault open if you are comfortable managing the testnet position.
  - Repeat useful testnet activity over multiple days if the faucet and app allow it.
  - Use one consistent wallet for all Ceitnot testnet activity.
  - Never share private keys, seed phrases, or wallet passwords.

Follow @WaterkoofAI_Bot for more airdrop scripts
--------------------------------------------------
    """)


if __name__ == "__main__":
    main()
