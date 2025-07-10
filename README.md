# Deep Research MCP

このプロジェクトは、Model Context Protocol (MCP) サーバーを提供し、LangGraphを動力とする研究エージェントを公開します。エージェントは、Google Searchを使用してウェブを検索し、知識のギャップを特定し、検索を反復的に改良し、引用を含むよく支持された回答を提供できるようになるまで、ユーザーのクエリに対する包括的な研究を行います。

<img src="./agent.png" title="エージェントの流れ" alt="エージェントの流れ" width="50%">

このプロジェクトは [google-gemini/gemini-fullstack-langgraph-quickstart](https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart) をフォークし、MCPサーバーとして再構成したものです。

## セットアップ

### 1. リポジトリを取得

```bash
ghq get https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart.git
```

### 2. Gemini API キーを取得

[Google AI Studio](https://aistudio.google.com/app/apikey) でAPIキーを取得してください。

### 3. Claude Desktop設定

`claude_desktop_config.json` に以下を追加：

```json
{
    "mcpServers": {
        "deep_research": {
            "command": "uvx",
            "args": [
                "--from",
                "/Users/<your-username>/ghq/github.com/google-gemini/gemini-fullstack-langgraph-quickstart/backend",
                "--with",
                "langchain-google-genai",
                "--with",
                "langchain-community",
                "--with",
                "langgraph",
                "fastmcp",
                "run",
                "/Users/<your-username>/ghq/github.com/google-gemini/gemini-fullstack-langgraph-quickstart/backend/src/agent/mcp_server.py"
            ],
            "env": {
                "GEMINI_API_KEY": "<YOUR_GEMINI_API_KEY>"
            }
        }
    }
}
```

### 4. Claude Desktopを再起動

設定完了後、Claude Desktopを再起動してください。

## 利用可能なツール

- **research_query**: 引用付きの包括的な研究
- **get_research_sources**: 研究で使用されたソース一覧
- **quick_research**: 高速研究（ループ数少なめ）

## 使用例

```
最新のAI技術の動向について詳しく調べてください
```

## ライセンス

Apache License 2.0
