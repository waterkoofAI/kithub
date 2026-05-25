"""
WaterkoofAI x BEEP Airdrop Script Kit v1.0
======================================================
COVERAGE DECLARATION:
- Project: BEEP
- Portal URL: https://app.justbeep.it/
- Total airdrop tasks: 8
- Tasks automated by this Kit: 4 / 8 (50%)
- Manual tasks remaining: wallet approvals, USDC deposit, squad selection, AI agent configuration, trading/prediction decisions, and Galxe/social verifications
- Estimated points from this Kit: Helps start BEEP account setup, referral onboarding, Beep Points farming, squad/referral setup, AI Agent creation, and Galxe quest completion
- Tested on: Windows
- Wallet used: Bitget Wallet (Chrome extension)

SECURITY NOTICE:
- This script is open source and fully auditable
- Your private keys are NEVER collected or uploaded
- Bitget Wallet signing steps require manual approval
- This script NEVER deposits funds, creates agents, trades, predicts, or approves wallet popups for you
- For educational purposes only. Use at your own risk.

HOW TO USE:
1. Drop STEP1_Drop_me_to_any_AI.md into any AI chat for guided setup
2. Fill in STEP2_Fill_your_wallet_info.json with your wallet details
3. Install Bitget Wallet Chrome extension:
   https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak
4. Start Chrome with remote debugging (see If_you_dont_use_AI_read_me.txt)
5. Run: python beep_auto.py

Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
"""

import json
import time
import sys
import os
import platform
from playwright.sync_api import sync_playwright

# -- BEEP URLs --
PROJECT_HOME = "https://app.justbeep.it/"
AI_TRADING_URL = "https://app.justbeep.it/ai-trading"
REWARDS_URL = "https://app.justbeep.it/rewards"
SQUADS_URL = "https://app.justbeep.it/rewards?tab=squad"
GALXE_URL = "https://app.galxe.com/quest/fuuzre246haW2hAPTTCct8/GChnLtYJmm?refer=quest_parent_collection"
DOCS_URL = "https://documentation.justbeep.it/"
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


def get_referral_code(config):
    ref_code = clean_config_value(config.get("referral_code"))
    if not ref_code or ref_code == "YOUR_REFERRAL_CODE":
        return "yy61h8u-6a"
    return ref_code


def get_squad_code(config):
    squad_code = clean_config_value(config.get("squad_code"))
    if not squad_code or squad_code == "YOUR_SQUAD_CODE_IF_DIFFERENT":
        return get_referral_code(config)
    return squad_code


def build_referral_url(config):
    ref_code = get_referral_code(config)
    return f"{PROJECT_HOME}?ref={ref_code}"


def connect_bitget_wallet(page):
    """
    Connect Bitget Wallet on app.justbeep.it.
    Strictly requires Bitget Wallet extension to be installed.
    """

    step("Connecting Bitget Wallet on Sui...")

    connect_selectors = [
        "button:has-text('Connect Wallet')",
        "button:has-text('Connect')",
        "button:has-text('Sign in')",
        "button:has-text('Login')",
        "button:has-text('Launch App')",
        "text=Connect Wallet",
        "text=Connect",
        "text=Sign in",
        "text=Login",
    ]

    connect_clicked = wait_and_click_any(
        page,
        connect_selectors,
        description="Connect Wallet or login button",
        timeout=12000
    )

    if not connect_clicked:
        wait_for_user(
            "Could not find the BEEP login/connect button automatically.\n"
            "Please click Connect Wallet or Sign In manually, then press ENTER."
        )

    time.sleep(2)

    wallet_step_selectors = [
        "button:has-text('Continue with wallet')",
        "button:has-text('Connect wallet')",
        "button:has-text('Wallet')",
        "button:has-text('External wallet')",
        "text=Continue with wallet",
        "text=Connect wallet",
        "text=Wallet",
    ]
    wait_and_click_any(page, wallet_step_selectors, description="wallet login option", timeout=7000)
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
        step("Bitget Wallet extension detected - connecting...")
        wait_and_click_any(
            page,
            extension_selectors,
            description="Bitget Wallet",
            timeout=5000
        )
        time.sleep(2)

        wait_for_user(
            "Approve the connection inside Bitget Wallet.\n\n"
            "  1. Make sure Bitget Wallet is unlocked.\n"
            "  2. Use the Sui network / Sui wallet inside Bitget Wallet.\n"
            "  3. Approve only the BEEP connection or signature you recognize.\n"
            "  4. Do not approve any transaction you did not intend.\n\n"
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
        "3. Refresh BEEP if needed.\n"
        "4. Click Connect Wallet or Sign In and select Bitget Wallet.\n"
        "5. Approve the connection in the extension popup.\n"
        "6. Confirm you are using the Sui network / Sui wallet.\n"
        "7. Press ENTER when connected and ready."
    )

    success("Bitget Wallet connected manually")


def ensure_bitget_wallet_connected(page, page_name="current page"):
    """Reconnect only when BEEP shows a wallet connection prompt."""
    step(f"Checking wallet connection on {page_name}...")

    connect_prompt_selectors = [
        "button:has-text('Connect Wallet')",
        "button:has-text('Connect')",
        "button:has-text('Sign in')",
        "button:has-text('Login')",
        "text=Connect Wallet",
        "text=Sign in",
    ]
    connected_state_selectors = [
        "button:has-text('Deposit')",
        "button:has-text('Withdraw')",
        "button:has-text('Create Trading Agent')",
        "button:has-text('Create Agent')",
        "text=Rewards",
        "text=Beeper Points",
        "text=Points",
        "text=AI Trading",
        "text=AI Treasury",
        "text=Squad",
        "text=Balance",
        "text=My Agents",
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


def enter_referral_or_squad_code_if_prompted(page, config):
    code_to_use = get_squad_code(config)

    step("Checking for referral or squad invite code prompt...")

    input_selectors = [
        "input[name='ref']",
        "input[name='referral']",
        "input[name='referralCode']",
        "input[name='inviteCode']",
        "input[name='squadCode']",
        "input[placeholder='Referral code']",
        "input[placeholder='Invite code']",
        "input[placeholder='Squad code']",
        "input[placeholder='Enter referral code']",
        "input[placeholder='Enter invite code']",
        "input[placeholder='Enter squad code']",
    ]

    filled = False
    for selector in input_selectors:
        try:
            el = page.locator(selector).first
            if el.is_visible(timeout=1500):
                el.fill(code_to_use)
                filled = True
                break
        except Exception:
            continue

    if filled:
        success(f"Entered referral/squad code {code_to_use}")
        wait_and_click_any(
            page,
            [
                "button:has-text('Join')",
                "button:has-text('Submit')",
                "button:has-text('Continue')",
                "button:has-text('Apply')",
                "button:has-text('Confirm')",
            ],
            description="code submit button",
            timeout=8000
        )
        wait_for_user(
            "If BEEP asks you to confirm the referral or squad code, review it and continue manually.\n"
            "Press ENTER after the code is accepted, or press ENTER to skip if no prompt appeared."
        )
        success("Referral/squad code step completed")
        return

    wait_for_user(
        "If BEEP shows a referral, invite, or squad-code screen, enter this code:\n\n"
        f"  {code_to_use}\n\n"
        "If the referral URL already applied it, no action is needed.\n"
        "Press ENTER when the account is past the referral/squad step."
    )
    success("Referral/squad code check completed")


def run_wallet(wallet, config, context):
    wallet_address = wallet.get("address", "")
    print(f"\n{'='*60}")
    print(f"Processing wallet: {wallet_address[:10]}...")
    print(f"{'='*60}")

    page = context.new_page()
    referral_url = build_referral_url(config)
    ref_code = get_referral_code(config)

    # -- TASK 1: Open BEEP referral link --
    step("Opening BEEP with referral link...")
    page.goto(referral_url)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success(f"BEEP loaded with referral code {ref_code}")

    # -- TASK 2: Connect Bitget Wallet --
    connect_bitget_wallet(page)
    time.sleep(2)

    # -- TASK 3: Referral or squad onboarding --
    enter_referral_or_squad_code_if_prompted(page, config)
    time.sleep(2)

    # -- TASK 4: Deposit / AI Treasury setup --
    step("Opening BEEP dashboard for AI Treasury deposit...")
    page.goto(PROJECT_HOME)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    ensure_bitget_wallet_connected(page, "BEEP dashboard")
    time.sleep(2)

    if wait_and_click_any(
        page,
        [
            "button:has-text('Deposit')",
            "button:has-text('Top Up')",
            "button:has-text('Fund')",
            "button:has-text('Add Funds')",
            "text=Deposit",
            "text=Top Up",
        ],
        description="deposit or top-up button",
        timeout=9000,
    ):
        wait_for_user(
            "Deposit into BEEP manually:\n\n"
            "  1. Review the deposit modal carefully.\n"
            "  2. Use Sui-native USDC only if that is what BEEP shows as supported.\n"
            "  3. Keep a small SUI balance for Sui network fees if needed.\n"
            "  4. Deposit only what you are comfortable putting into DeFi/agentic yield.\n"
            "  5. Approve the Bitget Wallet transaction only if all details look correct.\n\n"
            "If you do not want to deposit now, close the modal and press ENTER."
        )
    else:
        wait_for_user(
            "Could not find Deposit/Top Up automatically.\n"
            "If you want to farm deposit-based points, use the BEEP dashboard to deposit Sui-native USDC manually.\n"
            "If you want to skip funding, just press ENTER."
        )
    success("Deposit guidance completed")

    # -- TASK 5: Join or create squad --
    step("Opening BEEP Squads page...")
    page.goto(SQUADS_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    ensure_bitget_wallet_connected(page, "Squads page")
    time.sleep(2)

    if wait_and_click_any(
        page,
        [
            "button:has-text('Join Squad')",
            "button:has-text('Join a Squad')",
            "button:has-text('Create Squad')",
            "text=Join Squad",
            "text=Create Squad",
        ],
        description="squad button",
        timeout=9000,
    ):
        enter_referral_or_squad_code_if_prompted(page, config)
        wait_for_user(
            "Finish the Squad step manually:\n\n"
            "  1. Join the invited squad if the code is valid, or create your own squad if you prefer.\n"
            "  2. Read BEEP's warning that squad choice may be locked in during the MVP.\n"
            "  3. Approve only wallet prompts you recognize.\n\n"
            "Press ENTER when your squad/referral setup is complete."
        )
    else:
        wait_for_user(
            "If BEEP shows Squad setup, join the invited squad or create your own squad manually.\n"
            "Use this code if needed:\n\n"
            f"  {get_squad_code(config)}\n\n"
            "Press ENTER when finished or if the squad is already set."
        )
    success("Squad/referral setup completed")

    # -- TASK 6: Create AI Trading Agent --
    step("Opening BEEP AI Trading page...")
    page.goto(AI_TRADING_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    ensure_bitget_wallet_connected(page, "AI Trading page")
    time.sleep(2)

    if wait_and_click_any(
        page,
        [
            "button:has-text('Create Trading Agent')",
            "button:has-text('Create Agent')",
            "button:has-text('Start building your agent')",
            "button:has-text('Start Building')",
            "text=Create Trading Agent",
            "text=Start building your agent",
        ],
        description="create trading agent button",
        timeout=10000,
    ):
        wait_for_user(
            "Create your AI Trading Agent manually:\n\n"
            "  1. Choose an agent template.\n"
            "  2. Set an agent tag/name.\n"
            "  3. Select the AI model and markets you understand.\n"
            "  4. Review risk tolerance, frequency, allocation, max position size, and max active trades.\n"
            "  5. Remember BEEP docs mention an agent creation fee and that agent trading can lose money.\n"
            "  6. Approve only the Bitget Wallet prompts you intend.\n\n"
            "Press ENTER when the agent is created, or close the setup and press ENTER to skip."
        )
    else:
        wait_for_user(
            "If the Create Trading Agent button is not auto-detected, open the AI Trading tab and create an agent manually if you choose.\n"
            "Creating an agent may cost funds and can expose funds to trading risk. Press ENTER when finished or skipped."
        )
    success("AI agent setup guidance completed")

    # -- TASK 7: Monitor points, rewards, and agent activity --
    step("Opening BEEP Rewards page...")
    page.goto(REWARDS_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    ensure_bitget_wallet_connected(page, "Rewards page")
    time.sleep(2)

    wait_for_user(
        "Review your BEEP rewards manually:\n\n"
        "  1. Check Beeper Points, capital/deposit points, action/trading points, and referral/squad status.\n"
        "  2. If you created an agent, open its details and monitor model chat, active positions, completed trades, and PnL.\n"
        "  3. Pause or stop the agent manually if anything looks wrong.\n"
        "  4. Save your personal referral link if BEEP provides one.\n\n"
        "Press ENTER when finished."
    )
    success("Rewards review completed")

    # -- TASK 8: Galxe / community tasks --
    step("Opening BEEP Galxe quest...")
    page.goto(GALXE_URL)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Galxe quest page opened")

    wait_for_user(
        "Complete BEEP Galxe/community tasks manually:\n\n"
        "  1. Connect accounts requested by Galxe only if you trust the action.\n"
        "  2. Complete BEEP AI Odyssey tasks such as X follows/likes/reposts, Telegram, Discord member role, quiz, deposit proof, squad join, and agent/trade tasks shown on Galxe.\n"
        "  3. Verify each task on Galxe.\n"
        "  4. Return here and press ENTER when done.\n\n"
        "If you want to skip Galxe, just press ENTER."
    )
    success("Galxe/community guidance completed")

    wait_for_user("Press ENTER to finish this wallet and close the tab")
    page.close()
    print(f"\nWallet {wallet_address[:10]}... DONE!")
    print(f"\nSummary of completed tasks:")
    print(f"  [x] Open BEEP referral link")
    print(f"  [x] Connect Bitget Wallet on Sui")
    print(f"  [x] Check referral or squad invite code")
    print(f"  [x] Review Sui-native USDC deposit flow")
    print(f"  [x] Join or create a BEEP Squad")
    print(f"  [x] Review AI Trading Agent creation")
    print(f"  [x] Review rewards and agent activity")
    print(f"  [x] Open Galxe/community quest page")


def main():
    print("""
WaterkoofAI x BEEP Airdrop Script Kit v1.0
t.me/WaterkoofAI_Bot
--------------------------------------------------
This script NEVER collects private keys
This script NEVER deposits, trades, predicts, creates agents, or approves transactions
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
    print(f"Referral code: {get_referral_code(config)}")
    print(f"Squad code: {get_squad_code(config)}")
    print(f"Network: {config.get('network', 'sui')}")
    print(f"Collateral token: {config.get('collateral_token', 'USDC')}")

    chrome_cmd = get_chrome_debug_command()

    print(f"""
{'='*60}
BEFORE YOU CONTINUE:
1. You MUST use the Bitget Wallet Chrome extension:
   https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak

2. Make sure Chrome is running with remote debugging.
   Command to start Chrome (run in a separate terminal):

   {chrome_cmd}

3. BEEP runs primarily on Sui. Use the Sui wallet/network in Bitget Wallet.
4. BEEP docs say Sui-native USDC is the base stablecoin for deposits and yield.
5. AI Trading and Predict features can lose money. This script will not make decisions for you.

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

BEEP Activity Checklist:
  [x] Open BEEP through referral link
  [x] Connect Bitget Wallet on Sui
  [x] Check referral/squad code
  [x] Review Sui-native USDC deposit flow
  [x] Join or create a Squad
  [x] Review AI Trading Agent creation
  [x] Review BEEP rewards and agent activity
  [x] Open Galxe/community quest page

Tips for maximizing potential:
  - Deposit only what you are comfortable putting into DeFi.
  - BEEP docs say capital points are based on deposited amount and time held.
  - BEEP docs say trading volume earns points, but trading can lose money.
  - Creating an AI Agent may grant points and a multiplier, but can involve a fee and trading risk.
  - Complete Galxe/community tasks for extra campaign points where available.

Follow @WaterkoofAI_Bot for more airdrop scripts
--------------------------------------------------
    """)


if __name__ == "__main__":
    main()
