from github import Github
import sys
tocken="put your tocker here" #put your access tocken here


def createrepo():
    reponame=sys.argv[1]
    git=Github(tocken).get_user()
    git.create_repo(name=reponame)

if __name__ == "__main__":
    createrepo()