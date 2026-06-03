"""
WaterkoofAI x Monster Strategy (mnstr.xyz) Airdrop Script Kit v1.1
======================================================
COVERAGE DECLARATION:
- Project: Monster Strategy (mnstr.xyz)
- Portal URL: https://mnstr.xyz
- Total airdrop tasks: 6
- Tasks automated by this Kit: 6 / 6 guided browser steps (paid actions stay optional and manual)
- Manual tasks remaining: Fresh burner wallet setup, Bitget Wallet approvals, optional pack purchases, optional marketplace trades, and any real-fund actions
- Estimated points from this Kit: Weekly leaderboard based (no fixed point system)
- Tested on: Windows on 2026-05-13
- Wallet used: Bitget Wallet (Chrome extension)

SECURITY NOTICE:
- This script is open source and fully auditable
- Your private keys are NEVER collected or uploaded
- Use a fresh burner wallet only; do NOT use or import your main wallet
- Bitget Wallet signing steps require manual approval
- Pack purchases require YOUR manual confirmation and are disabled by default
- For educational purposes only. Use at your own risk.

HOW TO USE:
1. Drop STEP1_Drop_me_to_any_AI.md into any AI chat for guided setup
2. Fill in STEP2_Fill_your_wallet_info.json with your burner wallet details
3. Install Bitget Wallet Chrome extension:
   https://web3.bitget.com/share/2kwRSC?inviteCode=waterkoof
4. Start Chrome with remote debugging (see If_you_dont_use_AI_read_me.txt)
5. Run: python mnstr_auto.py

Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
"""

import json
import time
import sys
import os
import platform
from playwright.sync_api import sync_playwright

# ── Monster Strategy (mnstr.xyz) URLs ──
MNSTR_HOME        = "https://mnstr.xyz"
MNSTR_PACKS       = "https://mnstr.xyz/packs/"
MNSTR_STARTER     = "https://mnstr.xyz/packs/starter/"
MNSTR_MONSTER     = "https://mnstr.xyz/packs/monster/"
MNSTR_ULTRA       = "https://mnstr.xyz/packs/ultra/"
MNSTR_MARKETPLACE = "https://mnstr.xyz/marketplace/"
MNSTR_VAULT       = "https://mnstr.xyz/vault/"
MNSTR_LEADERBOARD = "https://mnstr.xyz/leaderboard/"
CONFIG_FILE = "STEP2_Fill_your_wallet_info.json"

# ── Pack tier URL mapping ──
PACK_URLS = {
    "starter": MNSTR_STARTER,
    "monster": MNSTR_MONSTER,
    "ultra":   MNSTR_ULTRA,
}


# ─────────────────────────────────────────────
#  Chrome debug command (auto-detects OS)
#  Do not modify this function.
# ─────────────────────────────────────────────

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


# ─────────────────────────────────────────────
#  Helper functions
# ─────────────────────────────────────────────

def load_config():
    if not os.path.exists(CONFIG_FILE):
        print(f"ERROR: {CONFIG_FILE} not found.")
        print("Please make sure STEP2_Fill_your_wallet_info.json is in the same folder.")
        sys.exit(1)
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


def config_flag_enabled(value):
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in ("true", "yes", "1", "enabled")
    return False


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
    """
    Click an element only if it is visible on the page.
    Returns True if clicked, False if not found.
    Use this for tasks that might already be completed.
    """
    try:
        el = page.locator(selector).first
        if el.is_visible(timeout=timeout):
            el.click()
            return True
    except Exception:
        pass
    return False


def safe_click(page, selector, description="element", timeout=6000):
    """
    Try to click an element, with error handling and description for logging.
    Returns True if clicked, False otherwise.
    """
    try:
        el = page.locator(selector).first
        el.wait_for(state="visible", timeout=timeout)
        el.click()
        return True
    except Exception as e:
        print(f"  Could not click {description}: {e}")
        return False


def wait_and_click_any(page, selectors, description="button", timeout=6000):
    """
    Try multiple selectors and click the first one found.
    Useful when button text varies across UI versions.
    """
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


# ─────────────────────────────────────────────
#  Bitget Wallet connection helper
#  mnstr.xyz flow: Sign In → Continue with a wallet → Bitget extension
# ─────────────────────────────────────────────

def connect_bitget_wallet(page):
    """
    Connect Bitget Wallet on mnstr.xyz
    Auto-detects extension first.
    """

    step("Connecting Bitget Wallet via mnstr.xyz Sign In...")

    # ── STEP 1: Sign In ─────────────────────
    signin_selectors = [
        "button:has-text('Sign In')",
        "button:has-text('Sign in')",
        "text=Sign In",
        "text=Sign in",
    ]

    signin_clicked = wait_and_click_any(
        page,
        signin_selectors,
        description="Sign In button",
        timeout=10000
    )

    if not signin_clicked:
        wait_for_user(
            "Could not find Sign In automatically.\n"
            "Please click Sign In manually then press ENTER."
        )

    time.sleep(2)
    success("Sign In popup opened")

    # ── STEP 2: Continue with wallet ─────────────────────
    wallet_option_clicked = wait_and_click_any(
        page,
        [
            "button:has-text('Continue with a wallet')",
            "button:has-text('Continue with wallet')",
            "text=Continue with a wallet",
            "text=Continue with wallet",
        ],
        description="Continue with wallet",
        timeout=8000
    )

    if not wallet_option_clicked:
        wait_for_user(
            "Click 'Continue with a wallet' manually then press ENTER."
        )

    time.sleep(2)
    success("Wallet mode selected")

    # ── STEP 3: Detect extension automatically ─────────────────────
    step("Checking for Bitget Wallet extension...")

    extension_detected = False

    extension_selectors = [
        "button:has-text('Bitget Wallet')",
        "text=Bitget Wallet",
        "text=BitKeep",
    ]

    for selector in extension_selectors:
        try:
            if page.locator(selector).first.is_visible(timeout=2000):
                extension_detected = True
                break
        except Exception:
            pass

    # ── EXTENSION INSTALLED ─────────────────────
    if extension_detected:

        step("Bitget Wallet extension detected — connecting directly...")

        wait_and_click_any(
            page,
            extension_selectors,
            description="Bitget Wallet",
            timeout=5000
        )

        time.sleep(2)

        wait_for_user(
            "Approve the connection inside Bitget Wallet extension popup.\n"
            "After approval press ENTER."
        )

        success("Bitget Wallet connected via extension")
        return

    # ── EXTENSION NOT INSTALLED ─────────────────────
    print("\n" + "="*50)
    print("BITGET WALLET EXTENSION NOT DETECTED")
    print("="*50)
    print("\nPlease install the Bitget Wallet extension:")
    print("https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak")

    wait_for_user(
        "1. Install Bitget Wallet Chrome extension in this Chrome-Debug profile.\n"
        "2. Create a fresh burner wallet in Bitget Wallet.\n"
        "3. Do NOT import or use your main wallet.\n"
        "4. Re-open wallet connect on mnstr.xyz.\n"
        "5. Choose Bitget Wallet only.\n"
        "6. Approve the connection manually.\n\n"
        "Press ENTER when connected."
    )

    success("Bitget Wallet connected manually")


# ─────────────────────────────────────────────
#  Burner wallet flow — Monster Strategy (mnstr.xyz)
# ─────────────────────────────────────────────

def run_wallet(wallet, config, context):
    print(f"\n{'='*60}")
    print(f"Processing wallet: {wallet['address'][:10]}...")
    print(f"{'='*60}")

    page = context.new_page()

    # ── TASK 1: Open Monster Strategy homepage ──
    step("Opening Monster Strategy (mnstr.xyz)...")
    referral_code = config.get("referral_code")
    home_url = MNSTR_HOME

    if referral_code and referral_code != "YOUR_REFERRAL_CODE":
        home_url = f"{MNSTR_HOME}?ref={referral_code}"

    page.goto(home_url)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Monster Strategy loaded")

    # ── TASK 2: Connect Bitget Wallet ──
    connect_bitget_wallet(page)
    time.sleep(2)

    # ── TASK 3: Review packs; purchases are opt-in and manual ──
    pack_tier = config.get("pack_tier", "starter").lower()
    pack_url = PACK_URLS.get(pack_tier, MNSTR_STARTER)

    step(f"Navigating to {pack_tier.capitalize()} Packs...")
    page.goto(pack_url)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success(f"{pack_tier.capitalize()} Packs page loaded")

    tier_prices = {"starter": "$50", "monster": "$250", "ultra": "$1,250"}
    tier_price = tier_prices.get(pack_tier, "varies")
    pack_purchase_enabled = config_flag_enabled(config.get("pack_purchase_enabled", False))
    max_budget = config.get("max_pack_budget_usd", 0)
    payment_token = config.get("payment_token", "USDC")

    if pack_purchase_enabled:
        wait_for_user(
            f"OPTIONAL paid pack purchase — {pack_tier.capitalize()} ({tier_price} per pack)\n\n"
            "  SECURITY RULES:\n"
            "  1. Use a fresh burner wallet only.\n"
            "  2. Do NOT use or import your main wallet.\n"
            f"  3. Fund the burner with no more than your intended budget: ${max_budget} plus gas.\n"
            "  4. Review the pack tier, odds, and payment amount carefully.\n"
            f"  5. Use your chosen payment token only if intended: {payment_token}.\n"
            "  6. Click the pack purchase button manually in the browser if you choose to buy.\n"
            "  7. Manually approve the Bitget Wallet popup only after checking every detail.\n\n"
            "  If you do not want to buy a pack, just press ENTER to skip."
        )
        success("Optional pack purchase step reviewed")
    else:
        wait_for_user(
            f"Pack page review only — {pack_tier.capitalize()} ({tier_price} per pack)\n\n"
            "  Paid pack purchasing is disabled in STEP2_Fill_your_wallet_info.json.\n"
            "  This script will not click any Open, Buy, Rip, Pull, or purchase button.\n\n"
            "  In the browser:\n"
            "  1. Review the pack tier, odds, and cost.\n"
            "  2. Do not buy from a main wallet.\n"
            "  3. Press ENTER here when done reviewing.\n\n"
            "  To enable a paid pack later, set pack_purchase_enabled to true and use a fresh burner wallet only."
        )
        success("Pack page review done")

    # ── TASK 4: Browse Marketplace ──
    step("Navigating to Marketplace...")
    page.goto(MNSTR_MARKETPLACE)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Marketplace loaded")

    wait_for_user(
        "Marketplace — Browse only by default:\n\n"
        "  In the browser:\n"
        "  1. Browse available cards on the marketplace\n"
        "  2. Do not buy or list cards from a main wallet\n"
        "  3. Any marketplace buy/list action must be manual and burner-wallet-only\n"
        "  4. If you choose to trade, review every price and wallet popup carefully\n"
        "  5. Come back here and press ENTER when done\n\n"
        "  Tip: Review activity safely first. Only trade with funds you are willing to risk."
    )
    success("Marketplace activity done")

    # ── TASK 5: Check Vault ──
    step("Navigating to Vault...")
    page.goto(MNSTR_VAULT)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Vault loaded")

    wait_for_user(
        "Vault — Your collected cards:\n\n"
        "  In the browser:\n"
        "  1. Review your collected graded cards\n"
        "  2. Cards are stored in a secure, insured vault\n"
        "  3. Do not enter shipping details unless you intentionally want physical delivery\n"
        "  4. Any delivery, sale, or buyback action is manual and optional\n"
        "  5. Come back here and press ENTER\n\n"
        "  If your vault is empty, just press ENTER to continue."
    )
    success("Vault check done")

    # ── TASK 6: Check Leaderboard & Points ──
    step("Navigating to Leaderboard...")
    lb_page = context.new_page()
    lb_page.goto(MNSTR_LEADERBOARD)
    lb_page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success("Leaderboard loaded")

    wait_for_user(
        "Leaderboard — Weekly points ranking:\n\n"
        "  In the browser tab showing the Leaderboard:\n"
        "  1. Check your current weekly points and ranking\n"
        "  2. Points reset every Sunday — plan activity accordingly\n"
        "  3. Top players win bonus cards and free spins\n"
        "  4. Note your position for tracking progress\n"
        "  5. Come back here and press ENTER\n\n"
        "  Tips for maximizing points:\n"
        "  - If you intentionally buy packs, spread activity throughout the week\n"
        "  - Stay active on the marketplace\n"
        "  - Look for Double Points events\n"
        "  - Starter packs may give better points-per-dollar"
    )
    success("Leaderboard check done")

    # ── Optional: Open Additional Packs ──
    step("Optional: Review extra pack strategy...")
    wait_for_user(
        "Extra pack strategy review:\n\n"
        "  Paid packs are optional and should only be done from a fresh burner wallet.\n\n"
        "  Strategy tips:\n"
        "  - Spread pack openings over multiple days\n"
        "  - Starter packs ($50) are most cost-effective for points\n"
        "  - Monster packs ($250) offer better card value odds\n"
        "  - Ultra packs ($1,250) have the highest mythic chance\n"
        "  - Watch for Double Points events!\n\n"
        "  This script will not buy another pack for you.\n"
        "  If you choose to buy manually, use only a minimally funded burner wallet.\n\n"
        "  Press ENTER when done reviewing."
    )
    success("Additional pack strategy reviewed")

    # ── FINAL STEP: Close tabs ──
    wait_for_user("Press ENTER to finish this wallet and close the tabs")
    lb_page.close()
    page.close()
    print(f"\nWallet {wallet['address'][:10]}... DONE!")
    print(f"\nSummary of completed tasks:")
    print(f"  [x] Connected Bitget Wallet to mnstr.xyz")
    print(f"  [x] Pack page reviewed ({pack_tier.capitalize()})")
    print(f"  [x] Marketplace browsing reviewed")
    print(f"  [x] Vault review")
    print(f"  [x] Leaderboard & points check")
    print(f"  [x] Additional pack strategy review")


# ─────────────────────────────────────────────
#  Entry point
# ─────────────────────────────────────────────

def main():
    print("""
WaterkoofAI x Monster Strategy (mnstr.xyz) Airdrop Script Kit v1.1
t.me/WaterkoofAI_Bot
--------------------------------------------------
This script NEVER collects private keys
Burner wallet REQUIRED - never use or import a main wallet
Use at your own risk - For educational purposes only
Wallet: Bitget Wallet (Chrome extension)
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
    print(f"Burner wallet required: {config.get('burner_wallet_required', True)}")

    # Display configured pack settings
    pack_tier = config.get("pack_tier", "starter").capitalize()
    tier_prices = {"Starter": "$50", "Monster": "$250", "Ultra": "$1,250"}
    pack_purchase_enabled = config_flag_enabled(config.get("pack_purchase_enabled", False))

    print(f"\nPack settings:")
    print(f"  Pack tier:       {pack_tier} ({tier_prices.get(pack_tier, 'varies')} per pack)")
    print(f"  Paid purchase:   {'enabled' if pack_purchase_enabled else 'disabled by default'}")
    print(f"  Max budget:      ${config.get('max_pack_budget_usd', 0)}")

    chrome_cmd = get_chrome_debug_command()

    print(f"""
{'='*60}
BEFORE YOU CONTINUE:
1. Make sure Bitget Wallet Chrome extension is installed:
   https://chrome.google.com/webstore/detail/bitkeep-crypto-nft-wallet/jiidiaalihmmhddjgbnbgdfflelocpak

2. Create a fresh burner wallet in Bitget Wallet inside the Chrome-Debug profile.
   DO NOT import or use your main wallet.
   DO NOT paste any seed phrase or private key into this script.

3. Make sure Chrome is running with remote debugging.
   Command to start Chrome (run in a separate terminal):

   {chrome_cmd}

4. Paid pack purchases are optional and disabled by default.
   If you enable them, fund the burner wallet only with your intended spend plus gas:
   - Starter: $50 per pack
   - Monster: $250 per pack
   - Ultra:   $1,250 per pack
   Accepted: USDC, ETH, USDm

If Chrome is already open and ready, just press ENTER.
{'='*60}
    """)
    input("Press ENTER when Chrome is open and ready...")

    with sync_playwright() as p:
        try:
            browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
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

Monster Strategy Activity Checklist:
  [x] Connected wallet to mnstr.xyz
  [x] Pack page reviewed safely
  [x] Marketplace reviewed safely
  [x] Vault — reviewed collected cards
  [x] Leaderboard — checked weekly points

Tips for maximizing points & potential airdrop:
  - Never use or import your main wallet for this kit
  - Use a fresh burner wallet with only the funds you are willing to spend
  - If you intentionally buy packs, spread activity throughout the week
  - Stay active on the marketplace safely
  - Points reset every Sunday — plan accordingly
  - Watch for Double Points events
  - Starter packs give best points-per-dollar for leaderboard
  - Keep valuable cards in vault for long-term potential

Follow @WaterkoofAI_Bot for more airdrop scripts
--------------------------------------------------
    """)


if __name__ == "__main__":
    main()
