#!/usr/bin/env python3
# obfuscating git history for fun, profit, privacy, or storytelling

import os
import sys
import git
import datetime
from pathlib import Path
from dotenv import load_dotenv


class GitHistoryStory:

    def __init__(self):

        print('👾 starting...')
        
        self.project_dir = os.path.realpath(os.path.dirname(__file__))
        self.repo = None
        self.REMOTE_BRANCH = None
        self.REMOTE_URL = None
        self.MIN_COMMITS = None
        self.MAX_COMMITS = None
        self.START_DAY = None
        self.START_MONTH = None
        self.START_YEAR = None
        self.END_DAY = None
        self.END_MONTH = None
        self.END_YEAR = None

        self.load_config()

    @staticmethod
    def exit_with_error(text) -> None:
        print(f'❌ {text}')
        sys.exit(1)

    def load_config(self) -> None:
        env_file = Path('.') / '.env'
        if not os.path.isfile(env_file):
            self.exit_with_error('please create an .env file')
        load_dotenv(env_file)
        try:
            self.REMOTE_BRANCH = os.getenv('REMOTE_BRANCH')
            self.REMOTE_URL = os.getenv('REMOTE_URL')
            self.MIN_COMMITS = int(os.getenv('MIN_COMMITS'))
            self.MAX_COMMITS = int(os.getenv('MAX_COMMITS'))     
            self.START_DAY = int(os.getenv('START_DAY'))
            self.START_MONTH = int(os.getenv('START_MONTH'))
            self.START_YEAR = int(os.getenv('START_YEAR'))
            self.END_DAY = int(os.getenv('END_DAY'))
            self.END_MONTH = int(os.getenv('END_MONTH'))
            self.END_YEAR = int(os.getenv('END_YEAR'))

        except KeyError as e:
            self.exit_with_error(f'cannot extract env variables: {e}. exiting.')

    def load_repo(self):
        try:
            print("[👾 loading git repository...")
            self.repo = git.Repo(self.project_dir)
        except git.exc.NoSuchPathError:
            self.exit_with_error("repo not found")
 
    def execute_commit(self, year: int, month: int, day: int):
        action_date = str(datetime.date(year, month, day).strftime('%Y-%m-%d %H:%M:%S'))
        os.environ["GIT_AUTHOR_DATE"] = action_date
        os.environ["GIT_COMMITTER_DATE"] = action_date
        self.repo.index.commit(message=f"commit-{year}-{month:02d}-{day:02d}")

    def create_single_commit(self, year: int, month: int, day: int):
        current_date = datetime.date(year, month, day)
        commits_amount = 1
        print(f'👾 committing {current_date} with {commits_amount} commits...')
        for _ in range(commits_amount):
            self.execute_commit(current_date.year, current_date.month, current_date.day)

    def create_commits(self):
        commit_end_date = datetime.date(self.END_YEAR, self.END_MONTH, self.END_DAY)
        commit_start_date = datetime.date(self.START_YEAR, self.START_MONTH, self.START_DAY)

        while True:
            self.create_single_commit(commit_start_date.year, commit_start_date.month, commit_start_date.day)
            commit_start_date = commit_start_date + datetime.timedelta(days=1)
            if commit_start_date >= commit_end_date:
                break

    def push_to_git(self):
        try:
            origin = self.repo.remote(name=self.REMOTE_BRANCH)
            origin.push()
            print('✅ changes have been pushed!')
        except Exception as e:
            self.exit_with_error(f'error while pushing the code:\n{e}')


if __name__ == "__main__":
    story = GitHistoryStory()
    story.load_repo()
    story.create_commits()
    story.push_to_git()
