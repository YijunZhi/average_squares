# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Average Squares'
copyright = '2025, YijunZhi'
author = 'YijunZhi'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',    # 从 docstring 自动生成 API 文档
    'sphinx.ext.autosummary',# 生成摘要页（搭配 :autosummary: 或 autosummary_generate）
    'sphinx.ext.napoleon',   # 支持 NumPy / Google 风格的 docstring
    'sphinx.ext.viewcode',   # 在文档里显示“查看源码”链接
    'sphinx.ext.mathjax',    # 如果有公式，启用 MathJax 渲染（可选）
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
