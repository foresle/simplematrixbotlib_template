### This is a template for writing a bot using simplematrixbotlib

#### Setup

First clone repo and create `.env` and `config.toml`

Examples:

`.env`
```dotenv
USERNAME=@catbot:example.com
PASSWORD=password
SERVER=https://example.com
```

[allowlist and blocklist formats](https://simple-matrix-bot-lib.readthedocs.io/en/latest/examples.html#id2)

`config.toml`
```toml
[simplematrixbotlib.config]
allowlist = []
blocklist = []
admin_id = '@admin:example.com'
```