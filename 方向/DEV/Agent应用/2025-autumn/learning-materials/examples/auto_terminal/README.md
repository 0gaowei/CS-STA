# learning_group

这是一个智能体（Agent）应用的示例代码仓库，包含会议记录与示例代码，用于学习与实验 pydantic_ai、coze 与 Agent 开发相关内容。

内容概览：

- `beginning.md`：会议纪要与技术要点
- `example.py`：交互式示例，使用 `pydantic_ai` 定义工具并运行事件循环
- `test.py`：同步运行的简单示例，用于快速验证 Agent 行为
- `assert/`：包含示意图片等资源

快速开始

1. 创建并激活 Python 虚拟环境（可选但推荐）：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. 安装依赖：

```powershell
pip install -r requirements.txt
```

3. 复制你的环境变量（示例）到 `.env` 文件：

```
SILICONFLOW_API_KEY=your_api_key_here
```

4. 运行示例：

交互式：
```powershell
python example.py
```

同步快速测试：
```powershell
python test.py
```

安全与注意事项

- 代码示例中包含执行系统命令的工具（`execute_sys_cmd`），在生产或不受信任输入下不要直接运行。
- 请不要在远程仓库中提交包含密钥的 `.env` 文件。

许可

本仓库采用 MIT 许可，详见 `LICENSE` 文件。
