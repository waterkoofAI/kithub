"""
WaterkoofAI x GIWA Airdrop Script Kit v1.0
======================================================
COVERAGE DECLARATION:
- Project: GIWA
- Portal URL: https://sepolia-explorer.giwa.io/
- Total airdrop tasks: 6
- Tasks automated by this Kit: 6 / 6 guided browser steps (wallet approvals and transactions stay manual)
- Manual tasks remaining: Bitget Wallet approvals, faucet claim confirmation, playground transaction approvals, test transfers, and contract deployment confirmation
- Estimated points from this Kit: Helps create repeatable GIWA Sepolia activity across faucet, playground, transfers, and contract deployment
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
5. Run: python giwa_auto.py

Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
"""

import json
import time
import sys
import os
import platform
from playwright.sync_api import sync_playwright

# -- GIWA URLs --
GIWA_DOCS = "https://docs.giwa.io/giwa-chain/en/get-started/connect-to-giwa"
GIWA_FAUCET = "https://faucet.giwa.io/"
BACKUP_FAUCET = "https://faucet.lambda256.io/giwa-sepolia"
GIWA_EXPLORER = "https://sepolia-explorer.giwa.io/"
GIWA_PLAYGROUND = "https://sepolia-playground.giwa.io/"
OWLTO_DEPLOY = "https://owlto.finance/deploy/"
CONFIG_FILE = "STEP2_Fill_your_wallet_info.json"

GIWA_NETWORK_DETAILS = {
    "network_name": "GIWA Sepolia",
    "rpc_url": "https://sepolia-rpc.giwa.io",
    "chain_id": "91342",
    "symbol": "ETH",
    "explorer": GIWA_EXPLORER,
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
                el.scroll_into_view_if_needed(timeout=3000)
                el.click()
                return True
        except Exception:
            continue
    print(f"  {description} not found with any selector")
    return False


def click_giwa_explorer_connect(page):
    """Click the GIWA explorer Chakra Connect dialog trigger."""
    selectors = [
        "button[data-scope='dialog'][data-part='trigger']:has-text('Connect')",
        "button.chakra-drawer__trigger:has-text('Connect')",
        "button.chakra-button.chakra-drawer__trigger:has-text('Connect')",
        "button[aria-haspopup='dialog']:has-text('Connect')",
        "button[aria-expanded='false']:has-text('Connect')",
        "span > button[type='button']:has-text('Connect')",
        "button:has-text('Connect')",
    ]

    for selector in selectors:
        try:
            el = page.locator(selector).first
            el.wait_for(state="visible", timeout=2000)
            el.scroll_into_view_if_needed(timeout=2000)
            el.click(timeout=2000, force=True)
            success("GIWA explorer Connect button clicked")
            return True
        except Exception:
            continue

    try:
        page.get_by_role("button", name="Connect").click(timeout=5000, force=True)
        success("GIWA explorer Connect button clicked")
        return True
    except Exception:
        pass

    try:
        clicked = page.evaluate(
            """
            () => {
                const buttons = Array.from(document.querySelectorAll("button"));
                const exactDialogButton = buttons.find((button) =>
                    button.textContent &&
                    button.textContent.trim() === "Connect" &&
                    button.getAttribute("data-scope") === "dialog" &&
                    button.getAttribute("data-part") === "trigger"
                );
                const fallbackButton = buttons.find((button) =>
                    button.textContent &&
                    button.textContent.trim() === "Connect"
                );
                const button = exactDialogButton || fallbackButton;
                if (!button) return false;
                button.click();
                return true;
            }
            """
        )
        if clicked:
            success("GIWA explorer Connect button clicked")
            return True
    except Exception:
        pass

    print("  GIWA explorer Connect button not found")
    return False


def open_page(page, url, label):
    step(f"Opening {label}...")
    page.goto(url)
    page.wait_for_load_state("domcontentloaded", timeout=30000)
    time.sleep(3)
    success(f"{label} loaded")


def print_giwa_network_details():
    print("\nGIWA Sepolia network details:")
    print(f"  Network:  {GIWA_NETWORK_DETAILS['network_name']}")
    print(f"  RPC URL:  {GIWA_NETWORK_DETAILS['rpc_url']}")
    print(f"  Chain ID: {GIWA_NETWORK_DETAILS['chain_id']}")
    print(f"  Symbol:   {GIWA_NETWORK_DETAILS['symbol']}")
    print(f"  Explorer: {GIWA_NETWORK_DETAILS['explorer']}")


def connect_bitget_wallet(page):
    step("Connecting Bitget Wallet...")
    print("  Required network: GIWA Sepolia (chain ID 91342)")

    if "sepolia-explorer.giwa.io" in page.url:
        connect_clicked = click_giwa_explorer_connect(page)
    else:
        connect_clicked = wait_and_click_any(
            page,
            [
                "header button:has-text('Connect')",
                "nav button:has-text('Connect')",
                "div.connect:has-text('Connect Wallet')",
                "div[class*='connect']:has-text('Connect Wallet')",
                "button:has-text('Connect Wallet')",
                "button:has-text('Connect')",
                "text=Connect Wallet",
                "text=Connect",
                "[aria-label*='Connect']",
            ],
            "Connect Wallet button",
            timeout=10000,
        )

    if not connect_clicked:
        wait_for_user(
            "Connect Bitget Wallet manually:\n\n"
            "  1. Click the Connect Wallet button on the page.\n"
            "  2. Choose Bitget Wallet.\n"
            "  3. Approve the connection in Bitget Wallet.\n"
            "  4. Confirm Bitget Wallet is on GIWA Sepolia (chain ID 91342).\n\n"
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
            "Before approving, confirm the network is GIWA Sepolia:\n"
            "  RPC URL: https://sepolia-rpc.giwa.io\n"
            "  Chain ID: 91342\n"
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
            "  3. Choose Bitget Wallet.\n"
            "  4. Approve the connection manually.\n"
            "  5. Switch to GIWA Sepolia (chain ID 91342).\n\n"
            "Then return here and press ENTER."
        )

    success("Bitget Wallet connection step complete")


def connect_owlto_wallet_if_needed(page):
    step("Checking Owlto wallet connection...")

    connect_clicked = False
    connect_selectors = [
        "div.connect:has-text('Connect Wallet')",
        "div[class*='connect']:has-text('Connect Wallet')",
        "text=Connect Wallet",
        "button:has-text('Connect Wallet')",
    ]

    for selector in connect_selectors:
        try:
            el = page.locator(selector).first
            if el.is_visible(timeout=3000):
                el.scroll_into_view_if_needed(timeout=3000)
                el.click(timeout=5000, force=True)
                connect_clicked = True
                success("Owlto Connect Wallet button clicked")
                break
        except Exception:
            continue

    if not connect_clicked:
        try:
            clicked = page.evaluate(
                """
                () => {
                    const elements = Array.from(document.querySelectorAll("div, button"));
                    const connect = elements.find((element) =>
                        element.textContent &&
                        element.textContent.trim() === "Connect Wallet" &&
                        (element.classList.contains("connect") || element.tagName === "BUTTON")
                    );
                    if (!connect) return false;
                    connect.click();
                    return true;
                }
                """
            )
            if clicked:
                connect_clicked = True
                success("Owlto Connect Wallet button clicked")
        except Exception:
            pass

    if not connect_clicked:
        print("  Owlto Connect Wallet button not visible; wallet may already be connected.")
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
            "Approve the Owlto Bitget Wallet connection manually.\n\n"
            "Before approving, confirm Bitget Wallet is on GIWA Sepolia:\n"
            "  RPC URL: https://sepolia-rpc.giwa.io\n"
            "  Chain ID: 91342\n"
            "  Symbol: ETH\n\n"
            "Do not approve anything you do not understand."
        )
    else:
        wait_for_user(
            "Owlto wallet connection:\n\n"
            "  1. Choose Bitget Wallet in the Owlto wallet list.\n"
            "  2. Approve the connection manually in Bitget Wallet.\n"
            "  3. Confirm Bitget Wallet is on GIWA Sepolia (chain ID 91342).\n\n"
            "If Owlto is already connected, just press ENTER."
        )

    success("Owlto wallet connection step complete")


def select_owlto_giwa_testnet(page):
    step("Selecting GiwaTestnet on Owlto...")

    chain_selectors = [
        "span.chain-name:has-text('GiwaTestnet')",
        "span[class*='chain-name']:has-text('GiwaTestnet')",
        "text=GiwaTestnet",
    ]

    for selector in chain_selectors:
        try:
            el = page.locator(selector).first
            el.wait_for(state="visible", timeout=6000)
            el.scroll_into_view_if_needed(timeout=3000)
            el.click(timeout=5000, force=True)
            success("GiwaTestnet selected on Owlto")
            return True
        except Exception:
            continue

    try:
        clicked = page.evaluate(
            """
            () => {
                const elements = Array.from(document.querySelectorAll("span.chain-name, span[class*='chain-name'], span"));
                const chainName = elements.find((element) =>
                    element.textContent &&
                    element.textContent.trim() === "GiwaTestnet"
                );
                if (!chainName) return false;
                const clickable = chainName.closest("button, [role='button'], li, .chain-item, .chain, div") || chainName;
                clickable.click();
                return true;
            }
            """
        )
        if clicked:
            success("GiwaTestnet selected on Owlto")
            return True
    except Exception:
        pass

    wait_for_user(
        "Select GiwaTestnet manually on Owlto:\n\n"
        "  1. Open the chain/network selector on the deployment page.\n"
        "  2. Choose GiwaTestnet.\n"
        "  3. Confirm the deploy page shows GiwaTestnet before continuing.\n\n"
        "If GiwaTestnet is already selected, press ENTER."
    )
    success("GiwaTestnet selection step complete")
    return False


def guide_network_setup(page):
    open_page(page, GIWA_EXPLORER, "GIWA Sepolia Explorer")
    print_giwa_network_details()
    connect_bitget_wallet(page)

    clicked_add_network = wait_and_click_any(
        page,
        [
            "button:has-text('Add to wallet')",
            "button:has-text('Add Network')",
            "text=Add to wallet",
            "text=Add Network",
        ],
        "Add network button",
        timeout=6000,
    )

    if clicked_add_network:
        wait_for_user(
            "If Bitget Wallet opened a network prompt, review and approve it manually.\n\n"
            "Confirm these exact details:\n"
            "  Network Name: GIWA Sepolia\n"
            "  RPC URL: https://sepolia-rpc.giwa.io\n"
            "  Chain ID: 91342\n"
            "  Symbol: ETH\n"
            "  Explorer: https://sepolia-explorer.giwa.io\n\n"
            "Then switch Bitget Wallet to GIWA Sepolia."
        )
    else:
        wait_for_user(
            "Add or confirm GIWA Sepolia in Bitget Wallet manually:\n\n"
            "  Network Name: GIWA Sepolia\n"
            "  RPC URL: https://sepolia-rpc.giwa.io\n"
            "  Chain ID: 91342\n"
            "  Symbol: ETH\n"
            "  Explorer: https://sepolia-explorer.giwa.io\n\n"
            "If it is already added, switch to GIWA Sepolia and press ENTER."
        )

    success("GIWA Sepolia network setup checked")


def claim_official_faucet(page):
    open_page(page, GIWA_FAUCET, "GIWA Official Faucet")
    connect_bitget_wallet(page)
    wait_for_user(
        "Claim GIWA Sepolia test ETH:\n\n"
        "  1. Confirm your connected Bitget Wallet address.\n"
        "  2. Complete any visible captcha or login check.\n"
        "  3. Click the faucet claim button if available.\n"
        "  4. Wait for the faucet transaction to complete.\n\n"
        "If the faucet is on cooldown or unavailable, just press ENTER to continue."
    )
    success("Official faucet claim step done")


def claim_backup_faucet_if_enabled(page, config):
    if not config.get("use_backup_faucet", False):
        print("  Backup faucet disabled in config; skipping optional backup faucet.")
        return

    open_page(page, BACKUP_FAUCET, "GIWA Backup Faucet")
    wait_for_user(
        "Optional backup faucet:\n\n"
        "  1. Use your Bitget Wallet address only.\n"
        "  2. Complete any required login or verification.\n"
        "  3. Claim GIWA Sepolia test ETH if available.\n\n"
        "If you do not want to use this faucet, just press ENTER."
    )
    success("Backup faucet step done")


def run_playground_tasks(page):
    open_page(page, GIWA_PLAYGROUND, "GIWA Playground")
    connect_bitget_wallet(page)

    step("Running GIWA Playground activity...")

    if click_if_visible(page, "text=Issue Dojang", timeout=5000):
        wait_for_user(
            "Issue Dojang:\n\n"
            "  Approve the Bitget Wallet transaction manually.\n"
            "  Wait until the page confirms the transaction."
        )
        success("Issue Dojang step done")
    else:
        print("  Issue Dojang button may already be completed or hidden.")

    if click_if_visible(page, "text=Claim VerifiedToken", timeout=5000):
        wait_for_user(
            "Claim VerifiedToken:\n\n"
            "  Approve the Bitget Wallet transaction manually.\n"
            "  Wait until the page confirms the transaction."
        )
        success("Claim VerifiedToken step done")
    else:
        print("  Claim VerifiedToken button may already be completed or hidden.")

    if click_if_visible(page, "text=Issue UP ID", timeout=5000):
        wait_for_user(
            "Issue UP ID:\n\n"
            "  Scroll down to create your unique UP ID with a custom name.\n"
            "  Approve the Bitget Wallet transaction manually.\n"
            "  Wait until the page confirms the transaction."
        )
        success("Issue UP ID step done")
    else:
        wait_for_user(
            "Complete any remaining GIWA Playground tasks manually:\n\n"
            "  1. Issue Dojang if it is available.\n"
            "  2. Claim VerifiedToken if it is available.\n"
            "  3. Issue UP ID if it is available.\n"
            "  4. Approve each Bitget Wallet popup manually.\n\n"
            "If all tasks are complete, press ENTER."
        )

    success("GIWA Playground activity complete")


def run_transfer_activity(page):
    open_page(page, GIWA_EXPLORER, "GIWA Sepolia Explorer")
    wait_for_user(
        "Create small GIWA Sepolia transfer activity:\n\n"
        "  1. Open Bitget Wallet while it is on GIWA Sepolia.\n"
        "  2. Send tiny test ETH amounts, for example 0.00001 ETH.\n"
        "  3. Prefer your own spare wallets or trusted test addresses.\n"
        "  4. Manually review and approve each transfer.\n"
        "  5. Return to the explorer and confirm the transfers appear.\n\n"
        "Never send mainnet funds. If you want to skip, just press ENTER."
    )
    success("Manual transfer activity step done")


def deploy_contract_with_owlto(page):
    open_page(page, OWLTO_DEPLOY, "Owlto Contract Deployment")
    connect_owlto_wallet_if_needed(page)
    select_owlto_giwa_testnet(page)
    wait_for_user(
        "Deploy a simple contract on GIWA Sepolia with Owlto:\n\n"
        "  1. Confirm Owlto shows GiwaTestnet as the selected network.\n"
        "  2. Use the default/simple contract deployment option.\n"
        "  3. Review and approve the Bitget Wallet transaction manually.\n"
        "  4. Wait for the deployment hash, then verify it on the explorer.\n\n"
        "If GIWA Sepolia is unavailable or you want to skip, press ENTER."
    )
    success("Owlto deployment step done")


def run_wallet(wallet, config, context):
    print(f"\n{'='*60}")
    print(f"Processing wallet: {wallet['address'][:10]}...")
    print(f"{'='*60}")

    page = context.new_page()

    # TASK 1: Explorer wallet connection and network setup
    guide_network_setup(page)

    # TASK 2: Official faucet
    claim_official_faucet(page)

    # TASK 3: Optional backup faucet
    claim_backup_faucet_if_enabled(page, config)

    # TASK 4: Playground
    run_playground_tasks(page)

    # TASK 5-6: Transfers and contract deployment
    run_transfer_activity(page)
    deploy_contract_with_owlto(page)

    wait_for_user("Press ENTER to finish this wallet and close the tab")
    page.close()
    print(f"\nWallet {wallet['address'][:10]}... DONE!")
    print(f"\nSummary of completed tasks:")
    print(f"  [x] Connected Bitget Wallet on GIWA Sepolia Explorer")
    print(f"  [x] Checked GIWA Sepolia network details")
    print(f"  [x] Claimed or attempted official faucet")
    print(f"  [x] Backup faucet checked if enabled")
    print(f"  [x] Completed or reviewed GIWA Playground tasks")
    print(f"  [x] Created or skipped small manual transfer activity")
    print(f"  [x] Deployed or skipped simple contract via Owlto")


def main():
    print("""
WaterkoofAI x GIWA Airdrop Script Kit v1.0
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
    print(f"Network: {config.get('network', 'giwa-sepolia')}")
    print(f"Backup faucet enabled: {config.get('use_backup_faucet', False)}")

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

4. Make sure Bitget Wallet is on GIWA Sepolia:
   RPC URL: https://sepolia-rpc.giwa.io
   Chain ID: 91342
   Symbol: ETH
   Explorer: https://sepolia-explorer.giwa.io

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

GIWA Activity Checklist:
  [x] Add or confirm GIWA Sepolia network
  [x] Claim GIWA Sepolia test ETH
  [x] Complete GIWA Playground activity
  [x] Send small manual test transfers
  [x] Deploy a simple contract through Owlto if available
  [x] Confirm transactions on the GIWA Sepolia explorer

Tips for maximizing potential:
  - Repeat useful testnet activity over multiple days if the faucet allows it.
  - Keep amounts tiny because this is testnet activity.
  - Use the explorer to confirm each transaction landed on GIWA Sepolia.
  - Never share private keys, seed phrases, or wallet passwords.

Follow @WaterkoofAI_Bot for more airdrop scripts
--------------------------------------------------
    """)


if __name__ == "__main__":
    main()
