import getpass
from fabric.api import *
from fabric.contrib.console import confirm


class Site(object):

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def run(self, cmd):
        with cd(self.dir):
            sudo(cmd, user=self.user_id)

    def gitrun(self, cmd):
        with cd(self.gitdir):
            sudo(cmd, user=self.user_id)

    def deploy(self):
        self.git_pull()
        self.update_packages()
        self.run('../../bin/python manage.py syncdb --migrate')
        self.run('../../bin/python manage.py collectstatic --noinput')
        self.restart()

    def git_pull(self):
        # .pyc files can create ghost behavior when .py files are deleted...
        self.gitrun("find . -name '*.pyc' -delete")
        self.gitrun("git fetch origin && git reset --hard origin/master")

    def git_tag(self):
        if confirm("Give new tag for this deployment?"):
            self.gitrun("git tag |tail -n 5")
            tag = prompt('Give new tag for this deployment: ')
            self.gitrun("git tag %s" % tag)
            self.gitrun("git push --tags && git push")

    def update_packages(self):
        self.gitrun("../bin/pip install -r requirements.txt")

    def restart(self):
        header("Running: Restart server script: nginx")
        self.run("killall python || true")
        self.run("../../bin/python manage.py run_gunicorn 127.0.0.1:8888 -D")
        header("Running: Restart server script: nginx")
        run("sudo service nginx restart")

PROD = Site(
    dir='/home/prods/memeblast/memeblast/memeblast',
    gitdir='/home/prods/memeblast/memeblast',
    user_id='web'
)

env.hosts = ['ndv.arkt.is']


@task
def deploy():
    env.user = prompt("Username on prod server:", default=getpass.getuser())

    # Pull on the production branch
    PROD.deploy()

    # Check if we want to tag the deployment
    PROD.git_tag()


def header(text):
    print ("#" * 45) + "\n# %s\n" % text + ("#" * 45)
