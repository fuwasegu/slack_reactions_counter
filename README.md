# Slack Reactions Counter
Slack の投稿についたリアクションの合計数を計算するプログラムです．

# Usage
```
$ cp .env.example .env
```

`SLACK_USER_TOKEN` に Slack の USER_TOKEN （`xoxp-` で始まるもの）をセットする．
なお，Slack App には `reactions:read` 権限を付与すること．

```
$python main.py <slack_message_url> <?slack_user_id>
```
（slack_user_id は任意パラメータ）
