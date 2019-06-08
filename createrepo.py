from github import Github
import sys
tocken="fbe7b881081ab48a50fff9034e08097c296676be" #put your access tocken here


def createrepo():
    reponame=sys.argv[1]
    git=Github(tocken).get_user()
    git.create_repo(name=reponame)

if __name__ == "__main__":
    createrepo()