# 配置文件模板

## 目录

- 标准 config.yaml.example 模板
- 环境变量映射规则
- 配置文件位置优先级
- 配置验证最佳实践
- 敏感信息处理
- 配置模板生成
- 多环境配置

## 标准 config.yaml.example 模板

```yaml
# ~/.<appname>/user_config.yaml
# <Skill 名称> 配置文件

# ─────────────────────────────────────────────────────────────
# 通用凭证 — 所有相关 skill 共享
# ─────────────────────────────────────────────────────────────
credential:
  # API Token（必需）
  # 在 <平台名称> 界面创建 Token 后填写
  # 也可通过 <APP>_TOKEN 环境变量设置（推荐）
  token: ""

  # 项目名称（可选，Token 校验时自动回写）
  project: ""

  # 用户名（可选，Token 校验时自动回写）
  user: ""

# ─────────────────────────────────────────────────────────────
# 服务配置（可选）
# ─────────────────────────────────────────────────────────────
service:
  # API 基础 URL
  base_url: "https://api.example.com"

  # 请求超时时间（秒）
  timeout: 30

  # 最大重试次数
  max_retries: 3

# ─────────────────────────────────────────────────────────────
# <skill-name> 专属配置
# ─────────────────────────────────────────────────────────────
<skill-name>:
  # 临时文件目录
  temp_dir: "/tmp/<appname>"

  # 日志级别: DEBUG, INFO, WARNING, ERROR
  log_level: "INFO"

  # 其他业务配置...
  option1: "value1"
  option2: "value2"
```

---

## 环境变量映射规则

### 命名规范

```
<APP>_<FIELD>  →  config.<section>.<field>
```

### 示例

```yaml
# config.yaml
credential:
  token: "file_token"
  project: "my_project"

service:
  base_url: "https://api.example.com"
  timeout: 30
```

对应的环境变量：

```bash
# 优先级高于配置文件
export APP_TOKEN="env_token"
export APP_PROJECT="env_project"

# 服务配置
export APP_BASE_URL="https://custom.api.com"
export APP_TIMEOUT="60"
```

### Python 实现

```python
def _validate(self):
    """验证配置，环境变量优先"""
    # 必需配置
    self.token = os.getenv('APP_TOKEN') or \
                self.config.get('credential', {}).get('token')

    if not self.token:
        raise ConfigError("缺少 token")

    # 可选配置
    self.project = os.getenv('APP_PROJECT') or \
                  self.config.get('credential', {}).get('project', '')

    self.base_url = os.getenv('APP_BASE_URL') or \
                   self.config.get('service', {}).get(
                       'base_url', 'https://api.example.com'
                   )

    self.timeout = int(os.getenv('APP_TIMEOUT') or \
                      self.config.get('service', {}).get('timeout', 30))
```

---

## 配置文件位置优先级

```
1. 命令行参数（最高优先级）
   python3 script.py --config /path/to/config.yaml

2. 当前项目目录
   ./<appname>/user_config.yaml

3. 用户主目录
   ~/.<appname>/user_config.yaml

4. 系统目录（Linux）
   /etc/<appname>/config.yaml
```

### Python 实现

```python
def _find_config(self) -> str:
    """查找配置文件"""
    # 检查的路径列表（按优先级）
    search_paths = [
        Path.cwd() / '.<appname>' / 'user_config.yaml',
        Path.home() / '.<appname>' / 'user_config.yaml',
        Path('/etc/<appname>/config.yaml'),
    ]

    for path in search_paths:
        if path.exists():
            return str(path)

    raise ConfigError(
        f"配置文件不存在。\n"
        f"请创建 ~/.<appname>/user_config.yaml\n"
        f"参考模板：SKILL_DIR/config.yaml.example"
    )
```

---

## 配置验证最佳实践

### 分层验证

```python
def _validate(self):
    """分层验证配置"""
    # 第一层：必需配置
    self._validate_required()

    # 第二层：格式验证
    self._validate_format()

    # 第三层：业务逻辑验证
    self._validate_business()

def _validate_required(self):
    """验证必需配置"""
    self.token = os.getenv('APP_TOKEN') or \
                self.config.get('credential', {}).get('token')

    if not self.token:
        raise ConfigError(
            "缺少 token。\n"
            "解决方案：\n"
            "1. 设置环境变量: export APP_TOKEN=your_token\n"
            "2. 或在配置文件中填写: credential.token"
        )

def _validate_format(self):
    """验证格式"""
    timeout = self.config.get('service', {}).get('timeout', 30)

    if not isinstance(timeout, int) or timeout <= 0:
        raise ConfigError(
            f"timeout 格式错误: {timeout}\n"
            "应为正整数，如: 30"
        )

def _validate_business(self):
    """验证业务逻辑"""
    max_files = self.config.get('upload', {}).get('max_files', 100)

    if max_files > 1000:
        raise ConfigError(
            f"max_files 超过限制: {max_files}\n"
            "最大值为 1000"
        )
```

---

## 敏感信息处理

### 不要在日志中输出敏感信息

```python
# ❌ 错误
logger.info(f"Config loaded: {self.config}")

# ✅ 正确
logger.info("Config loaded successfully")
logger.debug(f"token: {self.token[:8]}***")  # 只显示前8位
```

### 配置文件权限

```python
import stat

def _check_config_permissions(self):
    """检查配置文件权限"""
    config_path = Path(self.config_path)

    # 检查文件权限
    mode = config_path.stat().st_mode

    if mode & stat.S_IRWXG or mode & stat.S_IRWXO:
        logger.warning(
            f"配置文件权限过于开放: {self.config_path}\n"
            f"建议执行: chmod 600 {self.config_path}"
        )
```

---

## 配置模板生成

### 自动生成配置模板

```python
def generate_config_template(output_path: str):
    """生成配置模板"""
    template = """# ~/.<appname>/user_config.yaml
# <Skill 名称> 配置文件

credential:
  token: ""  # 必需：API Token

service:
  base_url: "https://api.example.com"
  timeout: 30
"""

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(template)

    print(f"配置模板已生成: {output_path}")
```

---

## 多环境配置

### 开发/测试/生产环境

```yaml
# ~/.<appname>/user_config.yaml

# 当前环境: development, testing, production
environment: development

# 不同环境的配置
environments:
  development:
    base_url: "http://localhost:8080"
    log_level: "DEBUG"

  testing:
    base_url: "https://test.api.example.com"
    log_level: "INFO"

  production:
    base_url: "https://api.example.com"
    log_level: "WARNING"

# 通用配置
credential:
  token: ""
```

### Python 实现

```python
def _load_config(self):
    """加载配置"""
    with open(self.config_path, 'r') as f:
        config = yaml.safe_load(f)

    # 根据环境选择配置
    env = os.getenv('APP_ENV') or config.get('environment', 'development')
    env_config = config.get('environments', {}).get(env, {})

    # 合并配置（环境配置优先）
    self.config = {**config, **env_config}
```

使用：

```bash
# 开发环境
export APP_ENV=development

# 生产环境
export APP_ENV=production
```
