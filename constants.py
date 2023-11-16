#!/usr/bin/env python3
# -*- coding: utf-8 -*-

TglangLanguage = (
  'OTHER', # TGLANG_LANGUAGE_OTHER,
  'C', # TGLANG_LANGUAGE_C,
  'C++', # TGLANG_LANGUAGE_CPLUSPLUS,
  'C#', # TGLANG_LANGUAGE_CSHARP,
  'CSS', # TGLANG_LANGUAGE_CSS,
  'DART', # TGLANG_LANGUAGE_DART,
  'DOCKER', # TGLANG_LANGUAGE_DOCKER,
  'FUNC', # TGLANG_LANGUAGE_FUNC,
  'GO', # TGLANG_LANGUAGE_GO,
  'HTML', # TGLANG_LANGUAGE_HTML,
  'JAVA', # TGLANG_LANGUAGE_JAVA,
  'JAVASCRIPT', # TGLANG_LANGUAGE_JAVASCRIPT,
  'JSON', # TGLANG_LANGUAGE_JSON,
  'KOTLIN', # TGLANG_LANGUAGE_KOTLIN,
  'LUA', # TGLANG_LANGUAGE_LUA,
  'NGINX', # TGLANG_LANGUAGE_NGINX,
  'OBJECTIVE_C', # TGLANG_LANGUAGE_OBJECTIVE_C,
  'PHP', # TGLANG_LANGUAGE_PHP,
  'POWERSHELL', # TGLANG_LANGUAGE_POWERSHELL,
  'PYTHON', # TGLANG_LANGUAGE_PYTHON,
  'RUBY', # TGLANG_LANGUAGE_RUBY,
  'RUST', # TGLANG_LANGUAGE_RUST,
  'SHELL', # TGLANG_LANGUAGE_SHELL,
  'SOLIDITY', # TGLANG_LANGUAGE_SOLIDITY,
  'SQL', # TGLANG_LANGUAGE_SQL,
  'SWIFT', # TGLANG_LANGUAGE_SWIFT,
  'TL', # TGLANG_LANGUAGE_TL,
  'TYPESCRIPT',# TGLANG_LANGUAGE_TYPESCRIPT,
  'XML', # TGLANG_LANGUAGE_XML
)

lang2idx = {l:i for i,l in enumerate(TglangLanguage)}
idx2lang = {i:l for i,l in enumerate(TglangLanguage)}

lang2idx['JS'] = lang2idx['JAVASCRIPT']
lang2idx['C SHARP'] = lang2idx['C#']
lang2idx['OBJECTIVE C'] = lang2idx['OBJECTIVE_C']
lang2idx['GOLANG'] = lang2idx['GO']
lang2idx['DJANGO'] = lang2idx['PYTHON']
lang2idx['YAML']  = 101
lang2idx['INI']   = 102
lang2idx['GCODE'] = 103
lang2idx['KQL']   = 104
lang2idx['R']     = 105
lang2idx['CMAKE'] = 106
lang2idx['EXCEL'] = 107
lang2idx['LATEX'] = 108
lang2idx['LISP']  = 109
lang2idx['TERRAFORM'] = 110
lang2idx['MATLAB'] = 111
lang2idx['VERILOG'] = 112
lang2idx['HASKELL'] = 113