Git Stats All
=============

Import all your [`git-stats`](https://github.com/IonicaBizau/git-stats) from a directory containing all your projects.

Requires [`git-stats-importer`](https://github.com/IonicaBizau/git-stats-importer) installed and in your `PATH`.

Instalation
-----------

```
$ pip install git-stats-all
```

Usage
-----

```
$ git_stats_all -p /some/path/to/projects/directory
```
or you can set a environment variable `GIT_STATS_PROJECTS_PATH` and just run it like this:

```
$ git_stats_all
```

You can also make the output more verbose:

```
$ git_stats_all --verbose
```


LICENSE
-------

This software is distributed using MIT license, see LICENSE file for more details.