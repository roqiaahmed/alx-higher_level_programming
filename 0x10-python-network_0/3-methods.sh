#!/bin/bash
# displays the body of the response
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d" "
