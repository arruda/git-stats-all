# -*- coding: utf-8 -*-

import os
import subprocess
import click


GIT_STATS_PROJECTS_PATH = os.environ.get('GIT_STATS_PROJECTS_PATH', None)


def which(program):
    """
    Return full path to exec if it exist in PATH, or else return None
    """
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:

        if is_exe(program):
            return program

    else:

        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None


def check_can_use_git_stats_importer():
    """
    Verify if the user has the git-stats-importer command in the current PATH
    """
    if not which('git-stats-importer'):
        raise Exception(
            """
            You need to have 'git-stats-importer' installed and in your PATH.
            Ex: npm install -g git-stats-importer
            """
        )


def contained_dirs(dir):
    """
    Lists all dirs in the given path
    taken from: http://stackoverflow.com/a/28200572/680611
    """
    return filter(os.path.isdir,
                  [os.path.join(dir, f) for f in os.listdir(dir)])


def is_git_repo(dir):
    "return True if the given dir has a .git directory inside it"
    return os.path.isdir(os.path.join(dir, '.git'))


def exec_git_stats_importer(dir, verbose):
    "execute the actual command in the given dir"

    if verbose:
        click.echo("Trying to importing project: %s" % dir)
    p = subprocess.Popen(
        ['git-stats-importer'], cwd=dir, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    retval = p.wait()
    output = ""
    for line in p.stdout.readlines():
        output += line
        if verbose:
            click.echo(line)

    if "error Cannot find the remote. Please add it" not in output:
        click.echo("Project imported: %s" % dir)


@click.command()
@click.option('-p',
              'projects_path',
              default=GIT_STATS_PROJECTS_PATH,
              type=click.Path(exists=True, dir_okay=True, resolve_path=True),
              help='Path to your projects directory')
@click.option('--verbose', is_flag=True,
              help='Add this to make the output more verbose')
def git_stats_all(projects_path, verbose):
    check_can_use_git_stats_importer()

    if not projects_path:
        raise Exception(
            "You need to set a projects directory path '-p' or set GIT_STATS_PROJECTS_PATH environment var"
        )

    for dir in contained_dirs(projects_path):
        if is_git_repo(dir):
            exec_git_stats_importer(dir, verbose)


if __name__ == '__main__':
    git_stats_all()
