# MCP Tools

A comprehensive collection of Model Context Protocol (MCP) tools designed to enhance AI assistant capabilities with various data processing, web scraping, database connectivity, and research utilities.

## Features

This MCP server provides the following tools:

### Data Processing
- **Notebook Analysis**: Parse and analyze Jupyter notebooks, extracting code cells, outputs, and metadata
- **PDF Processing**: Extract text content from PDF files
- **Excel/Spreadsheet Handling**: Read and analyze Excel files with pandas

### Web & Research
- **Web Scraping**: Stealth web scraping using Playwright with anti-detection measures
- **News Aggregation**: Fetch latest news using Google News API
- **Academic Research**: Search and download papers from arXiv
- **Wikipedia Integration**: Query Wikipedia for information
- **Web Search**: Perform web searches using Tavily API

### Database Connectivity
- **Multi-Database Support**: Connect to PostgreSQL, MySQL, Oracle, and SQL Server databases
- **SQL Execution**: Run SQL queries and retrieve results
- **Database Inspection**: Explore database schemas and table structures

### Utility Tools
- **HTTP Requests**: Make HTTP requests with customizable headers and methods
- **File System Operations**: Safe file operations within allowed paths

## Installation

### Prerequisites
- Python 3.12 or higher
- uv package manager (recommended)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Rendika7/simple-mcp-tools.git
   cd simple-mcp-tools
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configuration
   ```

4. Run the MCP server:
   ```bash
   uv run python server.py
   ```

## Configuration

Create a `.env` file with the following variables:

```env
# API Keys
TAVILY_API_KEY=your_tavily_api_key_here

# Paths
ARXIV_PAPER_STORAGE_PATH=/path/to/arxiv/papers
ALLOWED_PATHS=/allowed/file/paths

# Browser settings
HEADLESS=false
```

## Usage with Claude Desktop

Add the following configuration to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "mcp-tools": {
      "command": "uv",
      "args": ["run", "python", "server.py"],
      "cwd": "/path/to/mcp-tools"
    }
  }
}
```

An example configuration file is provided as `example_claude_desktop_config.json`.

## Available Tools

### Data Analysis Tools
- `analyze_data_files`: Analyze multiple data files (PDF, Excel, text)
- `analyze_notebook`: Parse Jupyter notebook structure and content
- `extract_pdf_text`: Extract text from PDF documents

### Web Tools
- `web_scrape`: Scrape web pages with stealth capabilities
- `search_news`: Get latest news on topics
- `search_arxiv`: Search academic papers on arXiv
- `wikipedia_search`: Query Wikipedia articles
- `tavily_search`: Perform web searches

### Database Tools
- `connect_database`: Establish database connections
- `execute_sql`: Run SQL queries
- `inspect_database`: Explore database schemas

### Utility Tools
- `make_http_request`: Send HTTP requests
- `list_directory`: List directory contents safely

## Development

### Running Tests
```bash
uv run python test_mcp.py
```

### Project Structure
```
mcp-tools/
├── server.py              # Main MCP server implementation
├── test_mcp.py           # Test suite
├── pyproject.toml        # Project configuration
├── uv.lock              # Dependency lock file
├── .env.example         # Environment variables template
├── example_claude_desktop_config.json  # Claude Desktop config example
└── README.md            # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Author

Rendika7
