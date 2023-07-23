import sys, textwrap
from PySide6.QtWidgets import QMainWindow, QApplication

from UI.repo_viewer_ui import Ui_repo_viewer

from github import Github
from github import Auth # Authentication is defined via github.Auth

# You must enter your own access token here
auth = Auth.Token('')

# Public Web Github allow us to view github users/repos
github_access = Github(auth=auth)


class RepoViwer (QMainWindow, Ui_repo_viewer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # gets the username from the auth code
        self.user = github_access.get_user()
        # gets the list of repositories for that user 
        self.repos = self.user.get_repos()

        # creates a list of the repository names for the self.user
        self.repo_names = [repo.name for repo in self.repos]

        # runs the methods base on the input text or button presses
        self.le_username.textChanged.connect(self.user_entered)
        self.le_repo_name.textChanged.connect(self.user_entered)
        self.pb_ok.clicked.connect(self.ok_button)
        self.pb_cancel.clicked.connect(self.cancel_button)


    # changes the two variables to the input text 
    def user_entered(self):
        self.username_entered = self.le_username.text()
        self.repo_entered = self.le_repo_name.text()

    def ok_button(self):
        '''
            If the username is incorrect we show an error and run the cancel button to reset
            If the repo name is not in the list of repos we return an error and cancel button
        '''
        if self.username_entered != self.user.login:
            self.repo_details.setText('Invalid Username')
            self.cancel_button()
            return

        if self.repo_entered not in self.repo_names:
            self.repo_details.setText('Invalid Repository')
            self.cancel_button()
            return
        
        '''
            If the details are correct we iterate over the list of repos
            The contributor login names are turned into a string separated by a comma 
            When the loop finds the repo.name that matches the input
            We change the text of repo_details to show the name, description, URL, # of stars, # of forks, # of open issues, and contributors
            We use a textwrap.dedent to remove the whitespace before the text (this is really just to better structure the code)
        '''
        for repo in self.repos:
            contributor_name = ', '.join(contributor.login for contributor in repo.get_contributors())
            if self.repo_entered == repo.name:
                self.repo_details.setText(textwrap.dedent
                (f'''
                    Repository Details:
                                
                    Repository Name: {repo.name}
                    Description: {repo.description}
                    URL: {repo.url}
                    Stars: {repo.stargazers_count}
                    Forks: {repo.forks_count}
                    Open Issues: {repo.open_issues_count}

                    Contributors: {contributor_name}
                '''))

    # resets the text boxes to empty
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