import requests
import sys
import re
import config

SLACK_USER_TOKEN = config.SLACK_USER_TOKEN

def split_message_url(url: str) -> dict:
    """ Slack 投稿の URL から channel と ts を抽出する
    Args:
        url (str): Slack 投稿の URL
    Return:
        dict: channel, ts を格納した辞書
    Raises:
        ValueError: URL スキーマが不正の場合に発生
    """
    splited = list(re.findall('https://yumemi\.slack\.com/archives/(\w+)/p(\d+)(\d{6})', url)[0])
    if len(splited) != 3:
        raise ValueError('URL format is invalid.')

    return {
        'channel': splited[0],
        'ts': splited[1] + '.' + splited[2],
    }

def fetch_message_reactions(channel: str, ts: str) -> list:
    """ Slack API を使って特定の投稿についたリアクションを取得する
    Args:
        channel (str): 対象のメッセージが投稿されたチャンネル
        ts (str): 対象のメッセージが投稿されたタイムスタンプ
    Return:
        list: 各リアクションに関する情報
    """
    return requests.get(
        url='https://slack.com/api/reactions.get',
        headers={
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Bearer {}'.format(SLACK_USER_TOKEN)
        },
        params={
            'channel': channel,
            'full': 'true',
            'timestamp': ts,
        },
    ).json()['message']['reactions']

def count_reactions(reactions: list, user_id: str=None) -> int:
    """ リアクションの合計値を計算する
    Args:
        reactions (list): 各リアクションに関する情報
        user_id (str|None): カウントを除外するユーザー
    Return:
        list: 付与されたリアクションの合計数
    Note:
        user_id を指定した場合，そのユーザーによるリアクションは除外する．
        例えば，投稿者本人が行ったリアクションは除外したい場合などに利用する．
    """
    return sum(int(reaction['count']) - 1 if user_id is not None and user_id in reaction['users'] else int(reaction['count']) for reaction in reactions)

if __name__ == '__main__':
    splited_url = split_message_url(sys.argv[1])
    excluded_user_id = sys.argv[2] if len(sys.argv) == 3 else None

    reactions = fetch_message_reactions(
        channel=splited_url['channel'],
        ts=splited_url['ts'],
    )

    print('count result (without user: {}): {}'.format(excluded_user_id, count_reactions(reactions=reactions, user_id=excluded_user_id)))
