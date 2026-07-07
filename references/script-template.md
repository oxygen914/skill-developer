# 脚本模板

只有在需要确定性执行、重复复用、或流程容易出错时才添加 `scripts/`。不要为了“结构完整”创建空脚本。

## 适用场景

- 格式转换、批量处理、校验、渲染、上传等可自动化操作。
- 多次任务会重复写同一段代码。
- 需要统一错误处理、重试、参数校验或输出格式。

## CLI 模板

```python
#!/usr/bin/env python3
"""One-line description of the tool."""

import argparse
import json
import sys
from pathlib import Path


class ToolError(Exception):
    pass


def run(input_path: Path, output_path: Path | None = None) -> dict:
    if not input_path.exists():
        raise ToolError(f"Input not found: {input_path}")

    # Implement deterministic work here.
    result = {
        "ok": True,
        "input": str(input_path),
        "output": str(output_path) if output_path else None,
    }
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        result = run(args.input, args.output)
    except ToolError as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False))
        return 1

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

## 配置读取

需要 token、API key 或路径配置时，优先支持环境变量，再考虑配置文件。配置文件应使用示例文件而非真实凭证。

```python
import os

token = os.getenv("APP_TOKEN")
if not token:
    raise ToolError("Missing APP_TOKEN")
```

## 输出约定

- 脚本输出机器可读 JSON，方便 agent 判断成功或失败。
- 给用户的最终回复转成人类可读摘要，不直接倾倒原始响应。
- 错误信息写清楚用户可采取的下一步。

## 测试

新增或修改脚本后至少运行一个代表性命令：

```bash
python3 scripts/<tool>.py <sample-input>
```

如果脚本会改写文件，先用临时目录或样例文件验证。
