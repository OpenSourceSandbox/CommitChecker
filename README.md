# ✔️ CommitCheck

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python version](https://img.shields.io/badge/python-3.8-blue)

CommitCheck은 특정 사용자의 일일 GitHub 기여를 추적하고 알리는 간단하면서도 효율적인 도구입니다. 이 도구는 사용자의 GitHub 커밋 활동을 모니터링하고, 일일 커밋에 따라 지정된 Slack 채널에 맞춤 메시지를 보냅니다.

팀 리더나 멘토들이 팀 멤버들의 일일 커밋과 GitHub에서의 기여를 추적하고자 할 때 유용하게 사용할 수 있고, 1일 1커밋 운동에도 도움을 줄 수 있습니다. Slack을 매개체로 사용하여 일일 커밋 업데이트를 게시함으로써 책임감을 느끼고 건강한 코딩 습관을 장려하는 데 도움이 됩니다.

## 필요한 요소
- Python 3
- BeautifulSoup
- slack_sdk
- WebDriver (예: Selenium)

## 사용법
1. CommitCheck 인스턴스를 생성하고 필요한 매개변수를 전달합니다.
   - `git_name`: GitHub의 사용자 이름
   - `slack_token`: Slack API 토큰
   - `slack_channel`: 메시지를 게시할 Slack 채널의 ID
   - `web_driver_manager`: WebDriver 관리자

2. `commit_check()` 메서드를 호출하여 해당 사용자의 일일 커밋을 확인하고 Slack에 메시지를 게시합니다.

```python
from my_web_driver_manager import MyWebDriverManager
from commit_check import CommitCheck

my_checker = CommitCheck(git_name='my_git_username', slack_token='my_slack_token', slack_channel='my_slack_channel', web_driver_manager=MyWebDriverManager())
my_checker.commit_check()
```

이 스크립트는 지정된 사용자의 오늘 날짜에 해당하는 GitHub 커밋 수를 확인하고 이 정보를 사용하여 Slack 메시지를 생성합니다. 만약 사용자가 오늘 아직 커밋을 하지 않았다면, 해당 사용자에게 커밋 알림을 전송합니다. 반대로 사용자가 이미 커밋을 한 경우에는 커밋 횟수와 함께 메시지를 전송합니다.

## 주의 사항
GitHub 웹페이지의 구조가 변경될 경우, 해당 스크립트의 웹 스크랩핑 부분이 올바르게 작동하지 않을 수 있습니다. 이런 경우, 해당 부분을 적절히 수정하여 사용해야 합니다.
