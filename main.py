import os
from dotenv import load_dotenv
from e2b import Sandbox

load_dotenv()


def main() -> None:
    """E2B Sandbox 示例代码"""
    api_key: str | None = os.getenv("E2B_API_KEY")
    if not api_key:
        raise ValueError("E2B_API_KEY 未在环境变量中设置")

    sbx: Sandbox = Sandbox.create(api_key=api_key)

    try:
        execution = sbx.commands.run("python -c \"print('hello world')\"")
        print("执行结果:")
        print(execution.stdout)
        if execution.stderr:
            print("错误输出:")
            print(execution.stderr)

        files = sbx.files.list("/")
        print("\n根目录文件:")
        for file in files:
            print(f"  {file.name}")
    finally:
        sbx.kill()


if __name__ == "__main__":
    main()
