import asyncio
import json
import traceback

# =========================
# IMPORT ALL TOOLS
# =========================
from server import *

# =========================
# HELPER
# =========================

def print_section(title):
    print("\n" + "="*60)
    print(f"🧪 TEST: {title}")
    print("="*60)

def print_success():
    print("✅ SUCCESS")

def print_fail(e):
    print("❌ FAILED:", str(e))
    traceback.print_exc()

def preview(data, limit=500):
    try:
        if isinstance(data, dict) or isinstance(data, list):
            print(json.dumps(data, indent=2)[:limit])
        else:
            print(str(data)[:limit])
    except:
        print(str(data)[:limit])

async def run_test(name, func, *args, is_async=False, **kwargs):
    print_section(name)
    try:
        if is_async:
            result = await func(*args, **kwargs)
        else:
            result = func(*args, **kwargs)

        preview(result)
        print_success()
    except Exception as e:
        print_fail(e)

# =========================
# MAIN TEST
# =========================

async def main():
    print("\n🚀 START FULL MCP TEST\n")

    # =========================
    # 🌐 WEB & SEARCH
    # =========================
    await run_test("Tavily Search", tavily_search, "AI trends 2025")
    await run_test("Extract URL", extract_url, "https://example.com")

    # =========================
    # 📰 NEWS
    # =========================
    await run_test("Search News", search_news, "AI", is_async=True)
    await run_test("Top News", get_top_news, is_async=True)
    await run_test("Topic News", get_topic_news, "technology", is_async=True)

    # =========================
    # 🧠 WIKIPEDIA
    # =========================
    await run_test("Wikipedia Search", search, "Artificial Intelligence")
    await run_test("Wikipedia Summary", summary, "Artificial Intelligence")

    # =========================
    # 🧬 ARXIV
    # =========================
    await run_test("Search Papers", search_papers, "machine learning")
    # download optional (skip heavy)
    # await run_test("Download Paper", download_paper, "2301.12345")

    # =========================
    # 📊 CRYPTO
    # =========================
    await run_test("Get Price", get_price, "btc,eth", is_async=True)
    await run_test("Top Coins", get_top_coins, is_async=True)
    await run_test("Coin Detail", get_coin_detail, "btc", is_async=True)
    await run_test("Search Coin", search_coin, "bitcoin", is_async=True)
    await run_test("Global Market", get_global_market, is_async=True)

    # =========================
    # 📁 FILE EXPLORER (MCP CUSTOM)
    # =========================
    base_path = ALLOWED_PATHS[0] if ALLOWED_PATHS else None

    if base_path:
        base_path = str(base_path)

        await run_test("List Directory", list_directory, base_path)
        await run_test("Search Files", search_files, base_path, "py")

        # cari file pertama buat dibaca
        files = search_files(base_path, "py").get("matches", [])
        if files:
            await run_test("Read Text File", read_text_file, files[0])

        await run_test("Project Tree", get_project_tree, base_path)

        # optional
        if "get_file_info" in globals():
            await run_test("File Info", get_file_info, base_path)

    else:
        print("⚠️ SKIP FILE TEST (no ALLOWED_PATHS)")

    # =========================
    # 📄 FILE (OPTIONAL)
    # =========================
    try:
        await run_test("Read PDF", read_pdf, "test.pdf")
    except:
        print("⚠️ PDF SKIPPED")

    try:
        await run_test("Read Excel", read_excel, "test.xlsx")
    except:
        print("⚠️ Excel SKIPPED")

    # =========================
    # 📓 NOTEBOOK
    # =========================
    try:
        await run_test("Read Notebook", read_notebook, "test.ipynb")
    except:
        print("⚠️ Notebook SKIPPED")

    # =========================
    # 🧪 IEEE / SCIENCEDIRECT (HEAVY)
    # =========================
    await run_test("Search IEEE", search_ieee, "machine learning", is_async=True)
    # skip sciencedirect (browser heavy)
    # await run_test("Search ScienceDirect", search_sciencedirect, "AI", is_async=True)

    # =========================
    # 🗄️ DATABASE (SKIP SAFE)
    # =========================
    print_section("Database Test (SKIPPED SAFE)")
    print("⚠️ No database provided → skipping connect_database")
    
    # simulate failure test
    result = execute_query("fake_id", "SELECT 1")
    preview(result)

    # =========================
    # DONE
    # =========================
    print("\n🎉 ALL TEST COMPLETED\n")

# =========================
# RUN
# =========================

if __name__ == "__main__":
    asyncio.run(main())