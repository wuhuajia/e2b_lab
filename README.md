# E2B Lab

E2B Python 实验项目，使用 uv 管理依赖。

> 这是一个使用 E2B SDK 的实验项目，演示如何创建和管理 Sandbox 环境。

## 快速开始

### 1. 安装 uv (如已安装可跳过)

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# 或使用 pip
pip install uv
```

### 2. 安装依赖

```bash
uv sync
```

### 3. 配置环境变量

创建 `.env` 文件并添加 E2B API Key：

```bash
E2B_API_KEY=your_api_key_here
```

### 4. 运行

```bash
uv run main.py
```

## 参考文档

- [E2B 快速开始指南](https://e2b.dev/docs/quickstart)
- [uv 文档](https://github.com/astral-sh/uv)
