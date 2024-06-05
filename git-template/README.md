# PROJECT NAME

A little summarize of the project

Somme meta:

- **Licence:** This solution is distributed under the [MIT license](./LICENCE.md) and come with no more guarantee than the devotion of the authors.
- **Authors:** Guillaume Lozenguez

## Get Stated:

Install instructions:

This directory and all the included filles leads on _Git_ repository and the extention to handle large files (LFS).
Make sure you have this two elelement installed on your machine.

With `apt` under a Ubuntu system:

```bash
sudo apt update
sudo apt install git git-lfs
```

On **GitLab**, **GitHub** or **Bitbucket**, it is recommanded to reccord a _ssh_ key in order to make you on your machine identifiable by those web-services.

You can now get all the elements, i.e. clone the distant repository (make a local copy of all it contents and it history) : 

```bash
git clone sshUser@url_to_the_repo/theRepoName
cd theRepoName
ls
```

## Tools:

The projects relies on severals tools that need to be installed and configured.

### Git

- **Git** is a decentralized solution for version management. Its first feature is to allow several contributors to work on a same directory, each one on its own machine.
It permits to share an entire historic of all modifications through a common *repo* on a server, to facilitate fusion of document version (mainly by using text format), and to do it in a safe way.

- A **GitServer**, *Bitbucket*, *GitHub*, [framagit](https://framagit.org) or private install of gitlab (*[gvipers](gvipers.imt-lille-douai.fr)* at IMT Lille Douai), propose solutions based on *git* to share a directory or repository on the cloud with management services (groups, members, access rules).

- **Markdown Documents** is a text format, very simple and directly interpretable on all _git_ server solutions. The format follows the philosophy: **What you see is what you get**
- Going further with Git:
	* [Learn Git](https://try.github.io/)
	* [GitForWindows](https://gitforwindows.org/) a simple IDE for Windows.
	* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

- **Large File System** (LFS) allows user to overpass the main default of _GIT_, generate a entire copie of all the historie over all the files existing at some point in time.


### Project Documentation

Documentation relise on [MkDocs](https://www.mkdocs.org/) to generate statics pages from markdown files (a pythoin tool: `pip install mkdocs`).

Technicaly _MkDocs_ take its ressources into `docs` directory and generate the web pages according to `` configuration filke.

The simple command: `mkdocs serve` permits to serve the documentation on [http://localhost:8000/](http://localhost:8000/), while  `mkdocs build` would generate the html pages.

Deployoment is achieved thanks to a public github repository, cloned locally:

```sh
git clone git@github.com:ktorz-net/ktorz-net.github.io.git ../ktorz-net-site
```

You have to build the static pages with _mkdocs_ and copy the generated files on the public webpages directory.
In short: `./bin/docs-deploy.sh`

```sh
mkdocs build
rm -fr ../ktorz-net-site/hackagames
mv site ../ktorz-net-site/hackagames
git -C ../ktorz-net-site pull
git -C ../ktorz-net-site add hackagames
git -C ../ktorz-net-site commit -m "update from hackagames" 
git -C ../ktorz-net-site push
```


### Slide Presentations

The presentation/slides are prepared using `marp` (an extantion to Markdown permiting to generate slides pdf).
`marp` is fully integrated to VisualCode:

- Get *Marp for VS Code* extention
- On `VS Code settings > working space` search for _Marp themes_:  > `Marp for VS Code > Markdown › Marp: Themes` and add: `slides/style-imt.css`.
- Also authorise html tags. Activate `marp: Enable HTML` in settings.


### Overleaf Web-Editor

[Overleaf](https://www.overleaf.com) is a Latex dedicated web-editor.

It is possible to clone locally overleaf project based on `git` tool.
For instance to clone `PROJECT-NAME` with overleaf code `CODE` : 

```sh
git clone https://$OVERLEAF_ID@git.overleaf.com/CODE ovl-YEAR-PROJECT-KEY
```

Your `$OVERLEAF_ID` is typically your e-mail and the code is the one in the overleaf url of your project.

For instance: 
```sh
export OVERLEAF_ID=guillaume.lozenguez%40imt-nord-europe.fr
git clone https://$OVERLEAF_ID@git.overleaf.com/6374b3bd73dbc0e894cf0901 my_wonderfull_project
```

**Project:**

Type  | Project                       | year | key        |  Code 
------|-------------------------------|------|------------|-------
Draft | my wonderfull project         | 2042 | wonderfull | 6374b3bd73dbc0e894cf0901


