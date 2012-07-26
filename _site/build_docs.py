#!/usr/bin/env python

import subprocess
import tempfile

MARKER = "GENERATED DOCS INSERTED BELOW THIS LINE"

if __name__ == "__main__":
    
    for param in ['api']:
        # generate the doc chunk
        proc = subprocess.Popen(['python ./utils/wiki_apidocs.py', 'api'],
                                stdout=subprocess.PIPE,
                                shell=True)
        chunk = proc.communicate()[0]

        doc_filename = './reference/rest_api/index.md'
        current_doc = open(doc_filename).read()

        # find the first line after the marker
        line_after_marker = current_doc.find('\n', current_doc.find(MARKER))
        
        
    
    