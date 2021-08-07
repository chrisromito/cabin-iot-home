#!/usr/bin/env bash
clear_cache() {
    find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
}

clear_cache
