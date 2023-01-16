#!/bin/bash
# Returns body of requested resource via the GET method
curl -sL "$1" | sed '/^$/d'
