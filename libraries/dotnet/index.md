---
layout: page
title: SMART App .NET Library (unofficial)
includenav: smartnav.markdown
---
{% include JB/setup %}


We don't have an officially supported .NET library, but Robert at
<http://USGovXML.com> has been kind enough to share a
working sample SMART ASP.NET app, packaged in a VS2008 Project. The app:

* Serves bootstrap.html and index.html on port 8000
* Parses SMART REST tokens from the supplied cookie
* Issues an OAuth-signed REST call to get medications on the current patient record

Download the project at <http://usgovxml.com/examples/Public/SMARTWebApp.zip>
