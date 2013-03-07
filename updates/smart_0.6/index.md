---
layout: page
title: SMART 0.6 Update Guide (Apps + Containers)
includenav: smartnav.markdown
---
{% include JB/setup %}

<div id="toc"></div>

# What's new in SMART 0.6

## Native Apps Workflow

(Pascal)

## Documents API

(Nikolai)

    mechanism for encapsulating metadata and links stored in external URLs
    documents include patient images, radiography images, EKG data files, scanned documents
    metadata about the file
    SMART could expose the public URL of the resource OR could proxy through the file and expose an obfuscated link (possibly by adding a “raw=true” parameter to the regular API URL)
    The API call returns the complete collection of data files for the patient
    Optional date and file type filters
    The container maintains an index of the available files

### Patient Images

(Nikolai)

### Radiography Images

(Nikolai / Nich)

## Family History API

(Nikolai)

- Demographics (date of birth, date of death)
- Biometrics (height)
- Problems (unlimited)

## Scratchpad API

    App annotation of patient records handled through and extension of the preferences API scoped to the app-record
    “fire-and-forget” type (non-transactional)
    All apps allowed to read each others’ scratchpads
    Data is “opaque” to the container, but self-structured by the app

## Clinical Notes Write API

(Arjun)

## Extended Demographic API

(Nikolai)

    Date of death
    Gestational Age at Birth

## Filters/Pagination

(Arjun)
     
# HOWTO:  Update Your SMART Apps to SMART 0.6

## Update vitals sign height units from m to cm

(Nikolai)

## REST apps

(Pascal / Arjun)

# HOWTO:  Update Your Container to SMART 0.6

## Implement OAuth endpoints

(Pascal)

## Update vitals sign height units from m to cm

(Nikolai)

## Update filters/pagination implementation

(Arjun)

## Implement new APIs (Documents, Family History, Scratchpad)

(Nikolai)

## Extend existing APIs (Demographics, Clinical Notes)

(Nikolai / Arjun)
=