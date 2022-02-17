# Slack Reactions Counter
<p>
    <img src="https://img.shields.io/badge/python-v3.9.4-blue">
    <img src="https://img.shields.io/badge/requests-v2.25.1-blue">
    <img src="https://img.shields.io/badge/dotenv-v0.19.2-blue">
</p>

Slack の投稿についたリアクションの合計数を計算するプログラムです．


# Usage
## 環境構築
```
$ cp .env.example .env
```

.env の `SLACK_USER_TOKEN` に Slack の USER_TOKEN （`xoxp-` で始まるもの）をセットする．
なお，該当する Slack App には `reactions:read` 権限を付与すること．

```
$ pip install -r requirements.txt
```

## 実行

```
$python main.py <slack_message_url> <?slack_user_id>
```
（slack_user_id は任意パラメータで，該当ユーザーのリアクションのみカウントしない．）

# Otheres
- 利用している Slack API のドキュメント 👉 https://api.slack.com/methods/reactions.get
