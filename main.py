import sys, textwrap
from PySide6.QtWidgets import QMainWindow, QApplication

from UI.repo_viewer_ui import Ui_repo_viewer

from github import Github
from github import Auth # Authentication is defined via github.Auth

# Using an access token
auth = Auth.Token("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")

# Public Web Github
github_access = Github(auth=auth)


class RepoViwer (QMainWindow, Ui_repo_viewer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # gets the username and repo list from the auth code
        self.user = github_access.get_user()
        self.repos = github_access.get_repos()

        self.le_username.textChanged.connect(self.user_entered)
        self.le_repo_name.textChanged.connect(self.user_entered)
        self.pb_ok.clicked.connect(self.ok_button)
        self.pb_cancel.clicked.connect(self.cancel_button)

    def user_entered(self):
        self.username_entered = self.le_username.text()
        self.repo_entered = self.le_repo_name.text()

    # def ok_button(self):
    #     if self.username_entered != self.user.login:
    #         print('wrong')
    #     elif self.repo_entered not in self.repos:
    #         print('wrongrep')
    #     else:
    #         for repo in self.repos:
    #             contributor_name = ', '.join(contributor.login for contributor in repo.get_contributors())
    #             if self.repo_entered == repo.name:
    #                 self.repo_details.setText(textwrap.dedent
    #                 (f'''
    #                     Repository Details:
                                    
    #                     Repository Name: {repo.name}
    #                     Description: {repo.description}
    #                     URL: {repo.url}
    #                     Stars: {repo.stargazers_count}
    #                     Forks: {repo.forks_count}
    #                     Open Issues: {repo.open_issues_count}

    #                     Contributors: {contributor_name}
    #                 '''))


    def cancel_button(self):
        self.le_username.setText('')
        self.le_repo_name.setText('')

#creates an instance of QApplication and executes the program
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = RepoViwer()
    window.show()

    # terminates the program if it is exited
    sys.exit(app.exec())