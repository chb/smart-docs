---
layout: page
title: Installing SMART on OS X
includenav: smartnav.markdown
---

{% include JB/setup %}

This walks you through installing an *insecure SMART testing environment* on
Mac OS X. We will be installing everything needed for SMART into the directory
`/Library/SMART`, all the instructions assume that you are running a Terminal
open from this location. Of course you can use your own location, just remember
to return to your `SMART` directory. Tested on OS X Lion and Mountain Lion.

# Install Homebrew

We use [Homebrew][] as package manager to install a few Linux tools. Since this
needs some extra command line tools to compile code, you first have to do
*one* of the following:

* Install [Xcode][] from the App Store (it's free, if large), then open
  `Xcode > Preferences > Downloads > Components` and install the `Command Line
  Tools`

* Download only the [`Command Line Tools`][] from the Apple Developer Center
  (you will need a free developer account for this)


[Homebrew][] is a superb replacement for the old managers Fink and MacPorts and
you will love it! Here's a one-line installer for it:

    $ /usr/bin/ruby -e "$(/usr/bin/curl -fsSL https://raw.github.com/mxcl/homebrew/master/Library/Contributions/install_homebrew.rb)"

If you had Homebrew installed before, make sure to update it:

    $ brew update

[Homebrew]: http://mxcl.github.com/homebrew/
[Xcode]: http://itunes.apple.com/ch/app/xcode/id497799835?l=en&mt=12
[Command Line Tools]: https://developer.apple.com/downloads/index.action


# Install Python Tools 

## `lxml` - an pythonic xml library

Download [lxml][] version 2.3.4 or later (via source tarball), double-click to
unarchive, then build and install:

    $ cd lxml-2.3.4
    $ python setup.py build --static-deps
    $ sudo python setup.py install

## `psycopg2` - an advanced PostgreSQL driver for Python

Download the [latest stable release][psycopg], unarchive, build and install:

    $ cd psycopg2-2.4.5
    $ python setup.py build
    $ sudo python setup.py install

## RDF packages

    $ sudo easy_install -U "rdflib>=3.0.0"  rdfextras


# Install Django 

## Django

You have to use [Django 1.3][django] for now. Download, unarchive and install:

    $ cd Django-1.3.1
    $ sudo python setup.py install


[lxml]: http://pypi.python.org/pypi/lxml/2.3.4#downloads
[psycopg]: http://initd.org/psycopg/
[django]: https://www.djangoproject.com/download/


# PostgreSQL

It's easiest to use the [Mac installer][postgres-mac] because it also sets up
the `postgres` user which is needed.

* Download the latest installer (I used 9.1.4) and run it. You can keep most
  default settings:
  
  - Install into `/Library/PostgreSQL/9.1`
  - Port `5432`
  - Remember your password!
  - Locale `en_US.UTF-8` (any `.UTF-8` will do)

* Create a PostgreSQL user for your SMART service. We will be using *smart*,
  use your own password:
      
        $ sudo su - postgres
        $ createuser --superuser smart
        $ psql postgres
        $ postgres=# \password smart
        $ postgres=# \q

*Caveat*: When using Postgres < 9.1 see the [instructions][] on how to change
the Postgres config to use md5 passwords. Also, if you haven't configured
postgres to use UTF-8, you seemingly need to use `pg_createcluster` which does
not ship on the Mac. You're on your own.

[postgres-mac]: http://www.postgresql.org/download/macosx/
[instructions]: https://github.com/chb/smart_server


# Tomcat and openrdf-sesame

* Install Tomcat

      $ brew install tomcat

* Configure Tomcat: The environment variable *$CATALINA_HOME* needs to point
  to the tomcat base directory. So in your Bash `.profile` add:

      $ export CATALINA_HOME=/usr/local/Cellar/tomcat/7.0.28/libexec

  If you don't use Bash adjust accordingly. Reload your profile file with:

      $ source ~/.profile

* Install openrdf-sesame

        $ curl -O http://downloads.sourceforge.net/project/sesame/Sesame%202/2.6.5/openrdf-sesame-2.6.5-sdk.tar.gz
        $ tar -xzvf openrdf-sesame-2.6.5-sdk.tar.gz
        $ mkdir $CATALINA_HOME/.aduna
        $ cp -r openrdf-sesame-2.6.5/war/* $CATALINA_HOME/webapps/
          
* Launch Tomcat and check its availability
  
        $ CATALINA_HOME/bin/startup.sh
  
You should now be able to access `http://localhost:8080/openrdf-workbench/`.


# Automated SMART install

We're now ready to get the latest and greatest from SMART.

* Download the SMART manager
  
        $ curl -O https://raw.github.com/chb/smart_server/master/load_tools/smart_manager.py

* Run the manager. This will install the current `master` branch of all SMART
  repositories that we need. If you want the bleeding edge `dev` version, add a
  `-d` switch to the following command

        $ python smart_manager.py -a

This will fetch all needed repositories, run an installer that asks you for some
configurations, generate patient sample data and in the end run the server.


# Running SMART

If you've just run the automated install, you only need to start Tomcat via
`$CATALINA_HOME/bin/startup.sh`, in the future:

## To start SMART (and Tomcat):

    $ CATALINA_HOME/bin/startup.sh
    $ python smart_manager.py -v -w

## To stop SMART (and Tomcat):

    $ python smart_manager.py -k
    $ CATALINA_HOME/bin/shutdown.sh

Nobody is stopping you from putting these two commands in a start- and/or stop
script, of course. :)