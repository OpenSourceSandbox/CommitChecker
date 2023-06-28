from commit_check import CommitCheck
from driver import WebDriverManager

if __name__ == "__main__":
    while True:
        try:
            driver_manager = WebDriverManager()
            commit_chk = CommitCheck("git_name",   # git 이름
                                     "SLACK_TOKEN",  # 자신의 슬랙 토큰
                                     "SLACK_CHANNEL",  # 알림을 보내고 싶은 슬랙 체널 EX) #일반
                                     driver_manager)
            commit_chk.commit_check()
            break
        except Exception as e:
            # print(e)
            continue
