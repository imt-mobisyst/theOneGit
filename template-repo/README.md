# Your Project Title

A brief description 

- Licence: 
- Author: 


# Get started 

Simple install and _'hello world'_ procedure


## Documentation

The documentation is on [Markdown](https://en.wikipedia.org/wiki/Markdown) format.
It can be served as a _HTML_ web site thanks to [MkDocs](https://www.mkdocs.org/).

```sh
pip install mkdocs
mkdocs serve
```

You can then refer to the [http://127.0.0.1:8000/](documentation).

This documentation is also on line: [https://imt-mobisyst.github.io/mb6-space](imt-mobisyst.github.io/mb6-space)


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

## Contribute 

### Documentation

Deployment is achieved with a public github repository (_imt-mobisyst.github.io.git_):

```sh
git clone git@github.com:imt-mobisyst/imt-mobisyst.github.io.git ../imt-mobisyst-site
./bin/docs-deploy.sh
```

To notice that the documentation repository can be cloned any where on your computer while the `config.toml` is updated accordingly.
