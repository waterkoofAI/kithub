"""
WaterkoofAI x DAC Quantum Chain Airdrop Script Kit v1.0
======================================================
COVERAGE DECLARATION:
- Project: DAC Quantum Chain
- Portal URL: https://inception.dachain.io/
- Total airdrop tasks: 8
- Tasks automated by this Kit: 8 / 8 guided browser steps (wallet approvals and transactions stay manual)
- Manual tasks remaining: Bitget Wallet approvals, social account linking, faucet claim, badge claims, test transfers, QE Pool burn/stake, Quantum Crate opens, and referral sharing
- Estimated points from this Kit: Helps earn Quantum Energy (QE), badges, multiplier boosts, and DACC testnet activity for the DAC Inception points program
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
5. Run: python dac_auto.py

Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
"""

import json
import time
import sys
import os
import platform
from playwright.sync_api import sync_playwright

# -- DAC Quantum Chain URLs --
PROJECT_HOME = "https://inception.dachain.io/"
DAC_DASHBOARD = "https://inception.dachain.io/dashboard"
DAC_BADGES = "https://inception.dachain.io/badges"
DAC_FAUCET = "https://inception.dachain.io/faucet"
DAC_ACTIVITY = "https://inception.dachain.io/activity"
DAC_LEADERBOARD = "https://inception.dachain.io/leaderboard"
DAC_QUANTUM_CRATE = "https://inception.dachain.io/quantum-crate"
DAC_QE_POOL = "https://inception.dachain.io/exchange"
DAC_SETTINGS = "https://inception.dachain.io/settings"
DAC_EXPLORER = "https://exptest.dachain.tech/"
DAC_DOCS = "https://dacblockchain.gitbook.io/docs"
CONFIG_FILE = "STEP2_Fill_your_wallet_info.json"

DAC_TESTNET = {
    "network_name": "DAC Testnet",
    "rpc_url": "https://rpctest.dachain.tech",
    "ws_url": "wss://wstest.dachain.tech",
    "chain_id": "21894",
    "symbol": "DACC",
    "explorer": DAC_EXPLORER,
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


def print_dac_network_details():
    print("\nDAC Testnet network details:")
    print(f"  Network:  {DAC_TESTNET['network_name']}")
    print(f"  RPC URL:  {DAC_TESTNET['rpc_url']}")
    print(f"  WS URL:   {DAC_TESTNET['ws_url']}")
    print(f"  Chain ID: {DAC_TESTNET['chain_id']}")
    print(f"  Symbol:   {DAC_TESTNET['symbol']}")
    print(f"  Explorer: {DAC_TESTNET['explorer']}")


def build_referral_url(config):
    referral_code = config.get("referral_code", "")
    if referral_code and referral_code not in ["none", "YOUR_REFERRAL_CODE"]:
        return f"{PROJECT_HOME}?ref={referral_code}"
    return PROJECT_HOME


def select_dac_wallet_auth_method(page):
    """Select the WALLET authentication method in DAC's Inception popup."""
    wallet_auth_selectors = [
        "button:has-text('WALLET')",
        "button:has-text('Wallet')",
        "[role='button']:has-text('WALLET')",
        "text=WALLET",
    ]

    selected = wait_and_click_any(
        page,
        wallet_auth_selectors,
        "WALLET authentication option",
        timeout=6000,
    )

    if selected:
        success("WALLET authentication method selected")
        time.sleep(2)

    return selected


def connect_bitget_wallet(page):
    step("Connecting Bitget Wallet...")
    print("  Required network: DAC Testnet (chain ID 21894)")

    wallet_auth_selected = False

    if click_if_visible(page, "button:has-text('Enter Inception')", timeout=5000):
        time.sleep(2)
        wallet_auth_selected = select_dac_wallet_auth_method(page)
    else:
        wallet_auth_selected = select_dac_wallet_auth_method(page)

    connect_clicked = wallet_auth_selected
    if not connect_clicked:
        connect_clicked = wait_and_click_any(
            page,
            [
                "button:has-text('Connect Wallet')",
                "button:has-text('Connect')",
                "w3m-button",
                "text=Connect Wallet",
                "text=Enter Inception",
            ],
            "Connect Wallet button",
            timeout=10000,
        )

        if connect_clicked:
            time.sleep(2)
            select_dac_wallet_auth_method(page)

    if not connect_clicked:
        wait_for_user(
            "Connect Bitget Wallet manually:\n\n"
            "  1. Click Enter Inception or Connect Wallet on the DAC page.\n"
            "  2. Select the WALLET authentication method.\n"
            "  3. Select Bitget Wallet only.\n"
            "  4. Approve the connection in Bitget Wallet.\n"
            "  5. Confirm Bitget Wallet is on DAC Testnet (chain ID 21894).\n\n"
            "If the wallet is already connected, just press ENTER."
        )
        success("Bitget Wallet connection step complete")
        return

    time.sleep(2)

    wait_and_click_any(
        page,
        [
            "text=Continue with a wallet",
            "button:has-text('Continue with a wallet')",
            "wui-list-button:has-text('Continue with a wallet')",
        ],
        "Continue with a wallet button",
        timeout=4000,
    )

    time.sleep(1)

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
            "Before approving, confirm the network is DAC Testnet:\n"
            "  RPC URL: https://rpctest.dachain.tech\n"
            "  Chain ID: 21894\n"
            "  Symbol: DACC\n\n"
            "If Bitget asks to add or switch the network, review the details above first.\n"
            "Do not approve anything you do not understand."
        )
    else:
        print("\nBitget Wallet was not detected in the wallet list.")
        print("Install or enable Bitget Wallet in this Chrome-Debug profile:")
        print("https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak")
        wait_for_user(
            "Manual Bitget Wallet connection:\n\n"
            "  1. Install or enable Bitget Wallet in this Chrome window.\n"
            "  2. Click Enter Inception or Connect Wallet again.\n"
            "  3. Choose Bitget Wallet only.\n"
            "  4. Approve the connection manually.\n"
            "  5. Add or switch to DAC Testnet (chain ID 21894).\n\n"
            "Then return here and press ENTER."
        )

    wait_for_user(
        "Finish DAC sign-in if prompted:\n\n"
        "  1. If DAC asks for a wallet signature, review it in Bitget Wallet.\n"
        "  2. Approve only the expected DAC Inception sign-in message.\n"
        "  3. Wait until the dashboard loads.\n\n"
        "Then press ENTER here."
    )
    success("Bitget Wallet connection step complete")


def open_inception_and_connect(page, wallet, config):
    target_url = build_referral_url(config)
    open_page(page, target_url, "DAC Inception")
    connect_bitget_wallet(page)
    wait_for_user(
        "Confirm DAC Inception is ready:\n\n"
        "  1. You should be signed in on the DAC dashboard.\n"
        f"  2. The connected wallet should start with {wallet['address'][:10]}...\n"
        "  3. Bitget Wallet should be on DAC Testnet.\n\n"
        "If DAC created or displayed your referral link, you can copy it later from the dashboard."
    )
    success("DAC Inception connection checked")


def claim_badges(page):
    open_page(page, DAC_DASHBOARD, "DAC Dashboard")
    wait_for_user(
        "Claim dashboard badges and multipliers:\n\n"
        "  1. Check for any Early Badge or Flash Badge prompt.\n"
        "  2. Click Claim Badge if it is available.\n"
        "  3. If a wallet signature or NFT mint appears, approve it manually only after reviewing it.\n"
        "  4. Q-Chip or Keycard holders should also check for Gold Early Badge eligibility.\n\n"
        "If no badge is available, press ENTER to continue."
    )
    open_page(page, DAC_BADGES, "DAC Badges")
    wait_for_user(
        "Review the Badges page:\n\n"
        "  1. Claim any free status badges available to your account.\n"
        "  2. Review locked badges for faucet, transactions, holding, streaks, QE Pool, and NFT minting.\n"
        "  3. Return here and press ENTER when done.\n\n"
        "Every wallet approval must stay manual."
    )
    success("Badge step done")


def claim_faucet(page):
    open_page(page, DAC_FAUCET, "DAC Faucet")
    wait_for_user(
        "Prepare the DACC faucet:\n\n"
        "  1. DAC may require you to link X or Discord before the faucet unlocks.\n"
        "  2. Use the official buttons on the faucet page for X or Discord linking.\n"
        "  3. Return to the faucet after the social login redirects back.\n"
        "  4. Confirm Bitget Wallet is on DAC Testnet.\n\n"
        "Do not paste private keys, seed phrases, or wallet passwords into any page."
    )

    clicked = wait_and_click_any(
        page,
        [
            "button:has-text('Claim Testnet')",
            "button:has-text('Claim Testnet DACC')",
            "button:has-text('Claim Faucet')",
            "text=Claim Testnet",
        ],
        "Claim Testnet DACC button",
        timeout=8000,
    )

    if clicked:
        wait_for_user(
            "Faucet claim submitted or opened:\n\n"
            "  1. If DAC shows a confirmation or queue status, wait for it to finish.\n"
            "  2. If Bitget Wallet opens, review the action manually.\n"
            "  3. If the page shows a cooldown, note when the next claim is available.\n\n"
            "Press ENTER when the faucet step is done."
        )
    else:
        wait_for_user(
            "Claim DACC manually:\n\n"
            "  1. Click Claim Testnet DACC when it is available.\n"
            "  2. If the button is disabled, check whether social linking or cooldown is required.\n"
            "  3. Optional: click Check queue status after claiming.\n\n"
            "Press ENTER when complete or skipped."
        )

    success("Faucet step done")


def complete_home_and_activity_missions(page):
    open_page(page, DAC_ACTIVITY, "DAC My Activity")
    wait_for_user(
        "Complete DAC missions:\n\n"
        "  1. Finish the onboarding checklist and daily check-in tasks.\n"
        "  2. Visit exploration tasks: Faucet, Leaderboard, Badges, and Explorer.\n"
        "  3. Link X, Discord, Telegram, or email only if you are comfortable doing so.\n"
        "  4. Claim completed mission rewards if the page offers them.\n\n"
        "Press ENTER when the activity tasks are complete or skipped."
    )
    success("Home and activity missions reviewed")


def run_transaction_activity(page, config):
    transfer_addresses = config.get("test_transfer_addresses", [])
    addresses = [
        address for address in transfer_addresses
        if address.startswith("0x") and not address.startswith("0xYour")
    ]

    open_page(page, DAC_EXPLORER, "DAC Testnet Explorer")
    wait_for_user(
        "Create small DAC Testnet transfer activity:\n\n"
        "  1. Open Bitget Wallet while it is on DAC Testnet.\n"
        "  2. Send tiny DACC amounts only, for example 0.001 DACC.\n"
        "  3. Use your own spare wallets or trusted test addresses.\n"
        f"  4. Configured spare addresses found: {len(addresses)}.\n"
        "  5. Manually review and approve each transfer in Bitget Wallet.\n"
        "  6. Confirm the transaction appears on the DAC explorer.\n\n"
        "Never send mainnet funds. If you want to skip, press ENTER."
    )

    open_page(page, DAC_ACTIVITY, "DAC My Activity")
    wait_for_user(
        "Sync on-chain mission progress:\n\n"
        "  1. Look for transaction missions such as First transaction, 3 tx, 5 tx, or Send to 3 distinct wallets.\n"
        "  2. Click any visible Sync or Check button on the mission cards.\n"
        "  3. Wait for DAC to credit the matching badges and QE.\n\n"
        "Press ENTER when done."
    )
    success("Transaction activity step done")


def use_qe_pool(page, config):
    open_page(page, DAC_QE_POOL, "DAC QE Pool")
    burn_amount = config.get("burn_dacc_amount", "0.1")
    stake_amount = config.get("stake_dacc_amount", "0.1")
    wait_for_user(
        "Use the QE Pool:\n\n"
        "  1. Confirm the page shows your DACC balance.\n"
        f"  2. Optional burn amount from config: {burn_amount} DACC.\n"
        "  3. Burn DACC for instant QE if you want the immediate points.\n"
        f"  4. Optional stake amount from config: {stake_amount} DACC.\n"
        "  5. Stake DACC if you want a share of future burn fees.\n"
        "  6. Claim fees only if pending fees are visible.\n"
        "  7. Manually approve every Bitget Wallet popup.\n\n"
        "If you do not want to burn or stake, press ENTER to skip."
    )
    success("QE Pool step done")


def open_quantum_crates(page, config):
    open_page(page, DAC_QUANTUM_CRATE, "DAC Quantum Crates")
    crate_limit = config.get("crate_opens_per_day", 5)
    wait_for_user(
        "Open Quantum Crates:\n\n"
        "  1. Check your QE balance. The current free crate flow requires 150 QE per open.\n"
        f"  2. Open up to {crate_limit} crates today, or fewer if the page shows a lower remaining limit.\n"
        "  3. Click Open Free, then Open for 150 QE.\n"
        "  4. Wait for the reveal. Rewards can include QE, DACC, or multipliers.\n"
        "  5. If DACC is sent on-chain, review any Bitget Wallet or explorer status manually.\n\n"
        "Press ENTER when crate openings are complete or skipped."
    )
    success("Quantum Crate step done")


def review_leaderboard_and_referrals(page):
    open_page(page, DAC_LEADERBOARD, "DAC Leaderboard")
    wait_for_user(
        "Review leaderboard and referrals:\n\n"
        "  1. Check your rank and QE total.\n"
        "  2. Return to the dashboard and copy your personal referral link if you want to invite friends.\n"
        "  3. Referral links use this format: https://inception.dachain.io/?ref=YOUR_CODE\n"
        "  4. Complete only genuine referrals; do not spam social platforms.\n\n"
        "Press ENTER when done."
    )
    success("Leaderboard and referral step done")


def run_wallet(wallet, config, context):
    print(f"\n{'='*60}")
    print(f"Processing wallet: {wallet['address'][:10]}...")
    print(f"{'='*60}")

    page = context.new_page()

    # TASK 1: Open DAC Inception and connect Bitget Wallet
    open_inception_and_connect(page, wallet, config)

    # TASK 2: Claim badges and review multipliers
    claim_badges(page)

    # TASK 3: Claim DACC faucet
    claim_faucet(page)

    # TASK 4: Home and activity missions
    complete_home_and_activity_missions(page)

    # TASK 5: Testnet transfers and sync
    run_transaction_activity(page, config)

    # TASK 6: QE Pool burn/stake
    use_qe_pool(page, config)

    # TASK 7: Quantum Crates
    open_quantum_crates(page, config)

    # TASK 8: Leaderboard and referrals
    review_leaderboard_and_referrals(page)

    wait_for_user("Press ENTER to finish this wallet and close the tab")
    page.close()
    print(f"\nWallet {wallet['address'][:10]}... DONE!")
    print(f"\nSummary of completed tasks:")
    print(f"  [x] Connected Bitget Wallet to DAC Inception")
    print(f"  [x] Claimed or reviewed Early/Flash badges")
    print(f"  [x] Claimed or reviewed DACC faucet")
    print(f"  [x] Completed or reviewed Home/My Activity missions")
    print(f"  [x] Created or synced DAC Testnet transfer activity")
    print(f"  [x] Used or reviewed QE Pool burn/stake")
    print(f"  [x] Opened or reviewed Quantum Crates")
    print(f"  [x] Checked leaderboard and referral link")


def main():
    print("""
WaterkoofAI x DAC Quantum Chain Airdrop Script Kit v1.0
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
    print(f"Network: {config.get('network', 'dac-testnet')}")
    print(f"Burn amount: {config.get('burn_dacc_amount', '0.1')} DACC")
    print(f"Stake amount: {config.get('stake_dacc_amount', '0.1')} DACC")
    print(f"Crate opens per day: {config.get('crate_opens_per_day', 5)}")

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

4. Make sure Bitget Wallet is on DAC Testnet:
   RPC URL: https://rpctest.dachain.tech
   Chain ID: 21894
   Symbol: DACC
   Explorer: https://exptest.dachain.tech

5. All transaction, approval, social login, faucet, and crate steps are manual.

If Chrome is already open and ready, just press ENTER.
{'='*60}
    """)
    input("Press ENTER when Chrome is open and ready...")

    print_dac_network_details()

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

DAC Quantum Chain Activity Checklist:
  [x] Connect Bitget Wallet to DAC Inception
  [x] Claim Early Badge or Flash Badge if available
  [x] Link social account if desired and claim DACC faucet
  [x] Complete Home/My Activity missions
  [x] Create small DAC Testnet transfer activity and sync tasks
  [x] Burn and/or stake DACC in the QE Pool
  [x] Open Quantum Crates
  [x] Check leaderboard and share referral link

Tips for maximizing potential:
  - Return daily for faucet claims, check-ins, crate opens, and streak progress.
  - Use tiny DACC amounts for test transfers.
  - Split DACC between burning for immediate QE and staking for ongoing pool fees only if you understand the tradeoff.
  - Keep one consistent wallet and social identity for DAC Inception.
  - Never share private keys, seed phrases, or wallet passwords.

Follow @WaterkoofAI_Bot for more airdrop scripts
--------------------------------------------------
    """)


if __name__ == "__main__":
    main()
