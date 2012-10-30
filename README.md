
SMART Documentation
===================

This is the SMART technical documentation, hosted at
<http://dev.smartplatforms.org>

- See <http://smartplatforms.org> for high-level project info and news
- Need help? Ask a question at <http://groups.google.com/group/smart-app-developers>
- Found an error in these docs? Fork them on Github and send us a pull
  request!
- Want an Atom feed of commits from our Github repositories? Use this:
  <https://github.com/chb/smart_server/commits/master.atom>
  for a feed of the commits to the `smart_server` repository's `master`
  branch. Change the appropriate section of the URL above for other
  repositories and branches.


Installing Jekyll and Friends
-----------------------------

First, you'll need the [Jekyll](https://github.com/mojombo/jekyll)
static site generator installed. The full installation instructions are
[here](https://github.com/mojombo/jekyll/wiki/install), but you probaly
can just do:

    $ gem install jekyll

There are two other libraries to install to generate these documents:

1. `redcarpet`: our preferred Ruby Markdown processor. _Note:_ the
   current version of `redcarpet` is incompatible and won't work with
   `jekyll` so you'll need to install the specific version below:

        $ gem install redcarpet --version=1.17.2

2. `Pygments`: the Python-based syntax highligher, this installation
   instructions for which are at the bottom of the Jekyll page above.

Once the required software is installed, generating the static site (in
the `_site` directory) is simply running

        $ jekyll

on the commandline. In some cases you'll need to do `jekyll --no-auto`
if Jekyll's file change watching is not working. That command will force
all pages to be regenerated.

Jekyll can serve up the site on <http://localhost:4000> by adding
`--server` to the commands above.

        $ jekyll --no-auto --server

will force regeneration of the site (and turn off auto-regeneration) and
start the local webserver.


Generating the API and Datamodel Docs
-------------------------------------

Run the `build_docs.py` script at the top of the repository to
re-generate the API and datamodel documentation from the SMART ontology
included via submodule in the `smart_common` directory.
