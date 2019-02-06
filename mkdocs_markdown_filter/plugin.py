import os
import sys
import re
from timeit import default_timer as timer
from datetime import datetime, timedelta

from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin

import jinja2
from jinja2.ext import Extension
import markdown

class MarkdownFilterPlugin(BasePlugin):

    config_scheme = (
    )

    def __init__(self):
        self.enabled = True
        self.dirs = []

    def md_filter(self, text, **kwargs):
        print( "text: " + text )
        md = markdown.Markdown(
            extensions=self.config['markdown_extensions'],
            extension_configs=self.config['mdx_configs'] or {}
        )
        return jinja2.Markup(md.convert(text))

    def on_env(self, env, config, files):
        self.config = config
        env.filters['markdown'] = self.md_filter
        return env

