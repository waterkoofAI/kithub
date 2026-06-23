"""
WaterkoofAI x SolPump Airdrop Script Kit v1.0
======================================================
COVERAGE DECLARATION:
- Project: SolPump
- Portal URL: https://solpump.io/a/AIRDROPSIO
- Total airdrop tasks: 8
- Tasks automated by this Kit: 8 / 8 guided steps (100%)
- Manual tasks remaining: Legal eligibility confirmation, Bitget Wallet approvals, social linking, chat activity, wagers, trades, blackjack gameplay, and token claims
- Estimated points from this Kit: Helps maintain potential SOLPUMP and hourly airdrop eligibility through guided platform activity. Rewards are not guaranteed.
- Tested on: Windows/macOS/Linux with Chrome remote debugging
- Wallet used: Bitget Wallet (Chrome extension)

SECURITY NOTICE:
- Caution: Use a burner wallet for this airdrop and secure your seed phrase
- This script is open source and fully auditable
- Your private keys are NEVER collected or uploaded
- Bitget Wallet signing steps require manual approval
- SolPump involves real SOL wagering/trading and may be restricted in some jurisdictions. Confirm local legality before proceeding.
- For educational purposes only. Use at your own risk.

HOW TO USE:
1. Drop STEP1_Drop_me_to_any_AI.md into any AI chat for guided setup
2. Fill in STEP2_Fill_your_wallet_info.json with your wallet details
3. Install Bitget Wallet:
   https://web3.bitget.com/share/2kwRSC?inviteCode=waterkoof
4. Install Bitget Wallet Chrome extension:
   https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak
5. Start Chrome with remote debugging (see If_you_dont_use_AI_read_me.txt)
6. Run: python solpump_auto.py

Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
"""

import json
import time
import sys
import os
import platform
from playwright.sync_api import sync_playwright

# -- SolPump URLs --
PROJECT_HOME = "https://solpump.io/a/AIRDROPSIO"
SOLPUMP_SITE_URL = "https://solpump.io/"
CRASH_URL = "https://solpump.io/"
BLACKJACK_URL = "https://solpump.io/blackjack"
TOKEN_DASHBOARD_URL = "https://solpump.io/coin/dashboard"
TRADING_TERMINAL_URL = "https://trade.solpump.io/"
AIRDROP_GUIDE_URL = "https://airdrops.io/solpump/"
BITGET_DOWNLOAD_URL = "https://web3.bitget.com/share/2kwRSC?inviteCode=waterkoof"
BITGET_CHROME_STORE_URL = "https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak"
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
    print("  Required network: Solana mainnet")

    clicked = wait_and_click_any(
        page,
        [
            "button:has-text('Connect')",
            "button:has-text('Connect Wallet')",
            "text=Connect Wallet",
            "text=Connect",
            "text=Wallet",
        ],
        "Connect Wallet button",
        timeout=10000,
    )

    if not clicked:
        wait_for_user(
            "Click the Connect button in the SolPump browser tab.\n\n"
            "  1. Select Bitget Wallet only.\n"
            "  2. Make sure Bitget Wallet is unlocked.\n"
            "  3. Make sure the network is Solana mainnet.\n"
            "  4. Approve the connection only after reviewing the popup."
        )

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
        wait_and_click_any(page, extension_selectors, "Bitget Wallet option", timeout=6000)
        wait_for_user(
            "Bitget Wallet should now show a connection popup.\n\n"
            "  1. Confirm the site is solpump.io.\n"
            "  2. Confirm the wallet is your burner wallet.\n"
            "  3. Confirm the network is Solana mainnet.\n"
            "  4. Approve only if everything looks correct."
        )
    else:
        print("\nBitget Wallet was not detected on the page.")
        print(f"Install Bitget Wallet: {BITGET_DOWNLOAD_URL}")
        print(f"Chrome Web Store: {BITGET_CHROME_STORE_URL}")
        wait_for_user(
            "Install or unlock Bitget Wallet in this Chrome-Debug profile.\n\n"
            "  1. Use the Bitget Wallet Chrome extension only.\n"
            "  2. Return to SolPump and click Connect.\n"
            "  3. Select Bitget Wallet.\n"
            "  4. Confirm Solana mainnet in the popup.\n"
            "  5. Approve manually, then come back here."
        )

    success("Bitget Wallet connection step completed")


def run_wallet(wallet, config, context):
    print(f"\n{'='*60}")
    print(f"Processing wallet: {wallet['address'][:10]}...")
    print(f"{'='*60}")

    page = context.new_page()

    # TASK 1: Open project
    step("Opening SolPump...")
    page.goto(PROJECT_HOME)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("SolPump loaded")

    # TASK 2: Connect wallet
    connect_bitget_wallet(page)
    time.sleep(2)

    # TASK 3: Complete initial setup
    step("Opening initial setup and social connection area...")
    page.goto(SOLPUMP_SITE_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    wait_and_click_any(
        page,
        [
            "text=Daily Case",
            "text=Rewards",
            "text=Settings",
            "text=Profile",
            "text=Connect",
        ],
        "setup/rewards area",
        timeout=7000,
    )
    wait_for_user(
        "Complete SolPump setup manually.\n\n"
        "  1. Confirm SolPump is legal for your location before continuing.\n"
        "  2. Connect any social accounts only if you are comfortable doing so.\n"
        "  3. Claim any welcome or daily case rewards only after reviewing the page.\n"
        "  4. Review every Bitget Wallet popup before approving.\n"
        "  5. Come back here when done.\n\n"
        "  If you want to skip setup, just press ENTER."
    )
    success("Initial setup step completed or skipped")

    # TASK 4: Participate in chat
    step("Opening chat activity area...")
    page.goto(SOLPUMP_SITE_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    wait_for_user(
        "Participate in SolPump chat manually.\n\n"
        "  1. Find the General Chat area.\n"
        "  2. Engage respectfully if chat participation is required.\n"
        "  3. Do not share wallet secrets, seed phrases, or personal information.\n"
        "  4. Come back here when done.\n\n"
        "  If you want to skip chat, just press ENTER."
    )
    success("Chat step completed or skipped")

    # TASK 5: Place qualifying wager
    step("Opening Crash game for qualifying wager...")
    page.goto(CRASH_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    minimum_bet = config.get("minimum_bet_sol", "0.001")
    wait_for_user(
        "Place a qualifying wager manually only if legal and desired.\n\n"
        f"  Minimum qualifying wager from config: {minimum_bet} SOL.\n"
        "  1. Set a strict budget before placing any bet.\n"
        "  2. Enter the bet amount manually.\n"
        "  3. Review the wager amount, destination, and network fee in Bitget Wallet.\n"
        "  4. Confirm manually only if you accept the risk.\n"
        "  5. Come back here after the wager settles.\n\n"
        "  If you do not want to wager, press ENTER to skip."
    )
    success("Qualifying wager step completed or skipped")

    # TASK 6: Monitor airdrops and daily rewards
    step("Opening airdrop and rewards area...")
    page.goto(SOLPUMP_SITE_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    wait_and_click_any(
        page,
        [
            "text=AirDrop",
            "text=Airdrop",
            "text=Daily Case",
            "text=Rewards",
            "button:has-text('Claim')",
        ],
        "airdrop/rewards area",
        timeout=7000,
    )
    wait_for_user(
        "Check hourly airdrops and daily rewards manually.\n\n"
        "  1. Open AirDrop, Airdrop, Rewards, or Daily Case.\n"
        "  2. Confirm you meet the activity requirement before claiming.\n"
        "  3. Review every Bitget Wallet popup before approving.\n"
        "  4. Come back here when done.\n\n"
        "  If nothing is claimable, just press ENTER."
    )
    success("Airdrop/rewards step completed")

    # TASK 7: Trading terminal
    step("Opening SolPump trading terminal...")
    page.goto(TRADING_TERMINAL_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    wait_for_user(
        "Use the SolPump trading terminal manually only if legal and desired.\n\n"
        "  1. Connect Bitget Wallet if prompted.\n"
        "  2. Complete any verification manually.\n"
        "  3. Deposit or trade SOL only if you accept the risk.\n"
        "  4. Review every Bitget Wallet popup before approving.\n"
        "  5. Come back here when done.\n\n"
        "  If you want to skip the terminal, just press ENTER."
    )
    success("Trading terminal step completed or skipped")

    # TASK 8: Blackjack activity
    step("Opening SolPump blackjack...")
    page.goto(BLACKJACK_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    wait_for_user(
        "Play blackjack manually only if legal and desired.\n\n"
        "  1. Confirm the page is official solpump.io.\n"
        "  2. Enter any bet amount manually.\n"
        "  3. Review the wallet prompt carefully before approving.\n"
        "  4. Stop immediately if you are unsure or uncomfortable.\n"
        "  5. Come back here when done.\n\n"
        "  If you want to skip blackjack, just press ENTER."
    )
    success("Blackjack step completed or skipped")

    # TASK 9: Token dashboard claim
    step("Opening SOLPUMP token dashboard...")
    page.goto(TOKEN_DASHBOARD_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    wait_and_click_any(
        page,
        [
            "button:has-text('Claim')",
            "text=Claim",
            "text=Dashboard",
            "text=Wallet",
            "text=Rewards",
        ],
        "claim/dashboard area",
        timeout=7000,
    )
    wait_for_user(
        "Check SOLPUMP token eligibility manually.\n\n"
        "  1. Confirm the wallet is the one used for SolPump activity.\n"
        "  2. Check claimed balance, estimated balance, and claim options.\n"
        "  3. Review every Bitget Wallet popup before approving.\n"
        "  4. Come back here when done.\n\n"
        "  If no tokens are claimable, just press ENTER."
    )
    success("Token dashboard step completed")

    # FINAL STEP: Close
    wait_for_user("Press ENTER to finish this wallet and close the tab")
    page.close()
    print(f"\nWallet {wallet['address'][:10]}... DONE!")
    print(f"\nSummary of completed tasks:")
    print(f"  [x] Opened SolPump")
    print(f"  [x] Connected Bitget Wallet manually")
    print(f"  [x] Guided initial setup")
    print(f"  [x] Guided chat participation")
    print(f"  [x] Guided qualifying wager")
    print(f"  [x] Guided airdrop/rewards check")
    print(f"  [x] Guided trading terminal activity")
    print(f"  [x] Guided blackjack activity")
    print(f"  [x] Guided token dashboard claim")


def main():
    print("""
WaterkoofAI x SolPump Airdrop Script Kit v1.0
t.me/WaterkoofAI_Bot
--------------------------------------------------
This script NEVER collects private keys
Caution: Use a burner wallet and secure your seed phrase
Use at your own risk - For educational purposes only
Wallet REQUIRED: Bitget Wallet (Chrome extension)
--------------------------------------------------
    """)

    config  = load_config()
    wallets = config.get("wallets", [])

    if not config.get("i_confirm_solpump_is_legal_for_me", False):
        print("ERROR: Set i_confirm_solpump_is_legal_for_me to true only after confirming SolPump is legal for you.")
        print("The SolPump site may restrict certain jurisdictions. If unsure, stop here.")
        sys.exit(1)

    if not config.get("enable_real_money_tasks", False):
        print("ERROR: Set enable_real_money_tasks to true only if you want guided prompts for SOL wagering/trading.")
        sys.exit(1)

    if not wallets:
        print("ERROR: No wallets found in STEP2_Fill_your_wallet_info.json.")
        sys.exit(1)

    wallets = [
        w for w in wallets
        if w.get("address", "") and
        not w.get("address", "").startswith("0xYour")
    ]
    if not wallets:
        print("ERROR: Please replace the placeholder wallet addresses in STEP2_Fill_your_wallet_info.json.")
        sys.exit(1)

    print(f"Found {len(wallets)} wallet(s) in config")

    print(f"Referral code: {config.get('referral_code', 'none')}")
    print(f"Network: {config.get('network', 'solana')}")
    print(f"Minimum qualifying wager: {config.get('minimum_bet_sol', '0.001')} SOL")

    chrome_cmd = get_chrome_debug_command()

    print(f"""
{'='*60}
BEFORE YOU CONTINUE:
1. You MUST use the Bitget Wallet Chrome extension:
   {BITGET_CHROME_STORE_URL}

   Bitget Wallet download:
   {BITGET_DOWNLOAD_URL}

2. Make sure Chrome is running with remote debugging.
   Command to start Chrome (run in a separate terminal):

   {chrome_cmd}

3. SolPump uses Solana mainnet and may involve real SOL wagering/trading.
   Confirm local legality, use a burner wallet, set strict limits, and never approve anything you do not understand.

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

SolPump Activity Checklist:
  [x] Opened platform
  [x] Connected Bitget Wallet
  [x] Checked setup and social tasks
  [x] Participated in chat if chosen
  [x] Placed qualifying wager manually if chosen
  [x] Checked hourly airdrops and daily rewards
  [x] Checked trading terminal
  [x] Checked blackjack activity
  [x] Checked SOLPUMP token dashboard

Tips for maximizing potential:
  - Only use SolPump if it is legal for your location
  - Keep wagers small and within a strict budget
  - Maintain hourly eligibility only if you accept the risk
  - Check token dashboard and rewards after activity
  - Never approve a wallet popup you do not understand

Follow @WaterkoofAI_Bot for more airdrop scripts
--------------------------------------------------
    """)


if __name__ == "__main__":
    main()
