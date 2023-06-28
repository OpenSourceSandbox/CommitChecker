from time import sleep

from bs4 import BeautifulSoup
from slack_sdk import WebClient
from datetime import datetime


class CommitCheck:
    def __init__(self, git_name, slack_token, slack_channel, web_driver_manager):
        self._driver = web_driver_manager.get_driver()
        self._domain = "https://github.com"
        self._soup = None
        self._current_date = None
        self._slack_message = None
        self._git_name = git_name
        self._slack_token = slack_token
        self._slack_channel = slack_channel

    def _post_message_to_slack(self):
        client = WebClient(token=self._slack_token)
        client.chat_postMessage(channel=self._slack_channel, text=self._slack_message)

    def _get_formatted_date(self):
        current_date = datetime.now()
        formatted_date = current_date.strftime('%Y-%m-%d')
        self._current_date = formatted_date

    def commit_check(self):
        self._driver.get(f"{self._domain}/{self._git_name}")
        sleep(1)
        self._soup = BeautifulSoup(self._driver.page_source, "html.parser")
        self._get_formatted_date()
        commit = self._soup.select_one(f'rect[data-date="{self._current_date}"]').text
        commit_count = commit.split(" contributions")[0]
        if commit_count == "0":
            self._slack_message = f"⚠️⚠️ @{self._git_name}님 오늘의 커밋이 없습니다!! ⚠️⚠️\n"
        else:
            self._slack_message = f"📢 @{self._git_name}님 오늘의 커밋은 {commit_count}회 입니다! 📢\n"
        self._post_message_to_slack()
        self._driver.quit()
