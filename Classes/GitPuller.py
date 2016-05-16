import subprocess


def git_pull():
    subprocess.call(["git", "pull"])