#!/usr/bin/env python3
# -*- coding: utf-8 -*-

num_English_words = 20

TglangLanguage = (
    'OTHER',  # TGLANG_LANGUAGE_OTHER,
    'C',  # TGLANG_LANGUAGE_C,
    'C++',  # TGLANG_LANGUAGE_CPLUSPLUS,
    'C#',  # TGLANG_LANGUAGE_CSHARP,
    'CSS',  # TGLANG_LANGUAGE_CSS,
    'DART',  # TGLANG_LANGUAGE_DART,
    'DOCKER',  # TGLANG_LANGUAGE_DOCKER,
    'FUNC',  # TGLANG_LANGUAGE_FUNC,
    'GO',  # TGLANG_LANGUAGE_GO,
    'HTML',  # TGLANG_LANGUAGE_HTML,
    'JAVA',  # TGLANG_LANGUAGE_JAVA,
    'JAVASCRIPT',  # TGLANG_LANGUAGE_JAVASCRIPT,
    'JSON',  # TGLANG_LANGUAGE_JSON,
    'KOTLIN',  # TGLANG_LANGUAGE_KOTLIN,
    'LUA',  # TGLANG_LANGUAGE_LUA,
    'NGINX',  # TGLANG_LANGUAGE_NGINX,
    'OBJECTIVE_C',  # TGLANG_LANGUAGE_OBJECTIVE_C,
    'PHP',  # TGLANG_LANGUAGE_PHP,
    'POWERSHELL',  # TGLANG_LANGUAGE_POWERSHELL,
    'PYTHON',  # TGLANG_LANGUAGE_PYTHON,
    'RUBY',  # TGLANG_LANGUAGE_RUBY,
    'RUST',  # TGLANG_LANGUAGE_RUST,
    'SHELL',  # TGLANG_LANGUAGE_SHELL,
    'SOLIDITY',  # TGLANG_LANGUAGE_SOLIDITY,
    'SQL',  # TGLANG_LANGUAGE_SQL,
    'SWIFT',  # TGLANG_LANGUAGE_SWIFT,
    'TL',  # TGLANG_LANGUAGE_TL,
    'TYPESCRIPT',  # TGLANG_LANGUAGE_TYPESCRIPT,
    'XML',  # TGLANG_LANGUAGE_XML
)

lang2idx = {l: i for i, l in enumerate(TglangLanguage)}
idx2lang = {i: l for i, l in enumerate(TglangLanguage)}

lang2idx['JS'] = lang2idx['JAVASCRIPT']
lang2idx['C SHARP'] = lang2idx['C#']
lang2idx['OBJECTIVE C'] = lang2idx['OBJECTIVE_C']
lang2idx['GOLANG'] = lang2idx['GO']
lang2idx['DJANGO'] = lang2idx['PYTHON']
lang2idx['YAML'] = 101
lang2idx['INI'] = 102
lang2idx['GCODE'] = 103
lang2idx['KQL'] = 104
lang2idx['R'] = 105
lang2idx['CMAKE'] = 106
lang2idx['EXCEL'] = 107
lang2idx['LATEX'] = 108
lang2idx['LISP'] = 109
lang2idx['TERRAFORM'] = 110
lang2idx['MATLAB'] = 111
lang2idx['VERILOG'] = 112
lang2idx['HASKELL'] = 113

keywords = {
    '#', '(', ')', '-', '/', ':', ';', '<',
    '=', '>', '[', '\\', ']', '_', '{', '}',
    '",', '()', ')\n', '))', ');', ',\n', '->',
    '//', ':\n', ';\n', '<-', '<<', '<=', '==', '=>',
    '>\n', '>=', '>>', ']\n', 'as', 'do', 'if', 'in',
    'is', 'or', '{\n', '}\n', '} ', '},', '")\n',
    '",\n', '", ', '","', '": ', '":"', '()\n', '() ', '();',
    ') {', '))\n', '):\n', ');\n', '---', '// ', '000', ': "',
    ': [', ': {', '===', 'and', 'asm', 'def', 'del', 'end',
    'for', 'int', 'let', 'new', 'not', 'str', 'try', 'var',
    'xor', '},\n', '    ', '####', '() {', ') =>', ') {\n',
    '));\n', '----', '.log', '0000', ': {\n', '====', '=> {', 'auto',
    'bool', 'case', 'char', 'elif', 'else', 'enum', 'from', 'goto',
    'http', 'if (', 'int ', 'int(', 'list', 'load', 'long', 'main',
    'name', 'None', 'null', 'pass', 'self', 'size', 'this', 'true',
    'True', 'void', 'with', '() {\n', '.log(', '_name', 'async', 'await',
    'break', 'catch', 'class', 'compl', 'const', 'count', 'false', 'False',
    'float', 'https', 'index', 'input', 'layer', 'print', 'quest', 'raise',
    'range', 'send_', 'short', 'sudo ', 'super', 'throw', 'union', 'using',
    'value', 'while', 'width', ') => {', '.print', 'assert', 'break;', 'Button',
    'CFrame', 'config', 'contex', 'cout<<', 'create', 'delete', 'double', 'except',
    'export', 'extern', 'filter', 'friend', 'global', 'handle', 'header', 'import',
    'inline', 'is_bot', 'lambda', 'main()', 'print(', 'public', 'return', 'signed',
    'sizeof', 'static', 'string', 'String', 'struct', 'switch', 'System', 'type":',
    'typeof', 'width:', '} else', '"https:', '#define', ') => {\n', '2023-10', 'Command',
    'command', 'console', 'cout <<', 'default', 'extends', 'finally', 'include', 'install',
    'mutable', 'nullptr', 'package', 'println', 'private', 'Session', 'typedef', 'virtual',
    '        ', ' cout <<', ' else {\n', '########', '#define ', '--------', '00000000', '========',
    'continue', 'contract', 'debugger', 'decltype', 'for(int ', 'function', 'https://', 'main() {',
    'main(){\n', 'message_', 'operator', 'position', 'printf("', 'println(', 'register', 'template',
    'typename', 'unsigned', 'username', '} else {', '(int i = ', 'Console\\',
    'for (int ', 'for i in ', 'function(', 'interface', 'main() {\n', 'namespace', 'protected', '<iostream>',
    'Character.', 'implements', 'instanceof', 'location =', 'new HByte()', 'static_cast', '            ', '------------',
    '000000000000', 'console.log(', 'getElementById(', 'using namespace', '################', '----------------', '0000000000000000',
    '================', 'reinterpret_cast', '#include <iostream>', 'System.out.println(', '                    ', '"type": "supergroup"',
    '####################', '--------------------', '////////////////////', '00000000000000000000', '====================', 'Players.LocalPlayer.', 'using namespace std;',
    "<< endl;\n", "in (", }

common_English_words = ['the', 'be', 'of', 'to', 'in', 'I', 'you', 'it', 'have', 'that', 'do', 'he', 'with', 'on', 'this', "n't", 'we', 'that', 'but', 'they', 'say', 'at', 'what', 'his', 'go', 'by', 'get', 'she', 'my', 'can', 'know', 'me', 'your', 'who', 'about', 'their', 'will', 'so', 'would', 'make', 'just', 'up', 'think', 'time',
                        'there', 'see', 'her', 'out', 'one', 'come', 'people', 'take', 'year', 'him', 'them', 'some', 'want', 'how', 'when', 'which', 'now', 'like', 'other', 'could', 'our', 'into', 'here', 'then', 'than', 'look', 'way', 'more', 'these', 'no', 'thing', 'well', 'because', 'also', 'two', 'use', 'tell', 'good', 'first', 'man', 'day', 'find', 'give', 'more']
tmp = common_English_words[:num_English_words]
text_keywords = [' '+s+' ' for s in tmp]
text_keywords = list(set(text_keywords))

keywords = list(set(keywords))
keywords.sort(key=str.lower)

kmax = max(len(k) for k in keywords)
keyword2idx = {k: i for i, k in enumerate(keywords)}

print("keywords:\n%s" % (keywords))
print("max keywords len (kmax): %d" % (kmax))

'''
# C keywords
keywords.update({
    'auto', 'double', 'int', 'struct', 'break', 'else', 'long', 'switch',
    'case', 'enum', 'register', 'typedef', 'char', 'extern', 'return', 'union',
    'continue', 'for', 'signed', 'void', 'do', 'if', 'static', 'while',
    'default', 'goto', 'sizeof', 'volatile', 'const', 'float', 'short', 'unsigned'})
# C++ keywords https://www.programiz.com/cpp-programming/keywords-identifiers
keywords.update({
    'alignas', 'decltype', 'namespace', 'struct', 'alignof', 'default', 'new', 'switch',
    'and', 'delete', 'noexcept', 'template', 'and_eq', 'do', 'not', 'this',
    'asm', 'double', 'not_eq', 'thread_local', 'auto', 'dynamic_cast', 'nullptr', 'throw',
    'bitand', 'else', 'operator', 'true', 'bitor', 'enum', 'or', 'try',
    'bool', 'explicit', 'or_eq', 'typedef', 'break', 'export', 'private', 'typeid',
    'case', 'extern', 'protected', 'typename', 'catch', 'false', 'public', 'union',
    'char', 'float', 'register', 'unsigned', 'char16_t', 'for', 'reinterpret_cast', 'using',
    'char32_t', 'friend', 'return', 'virtual', 'class', 'goto', 'short', 'void',
    'compl', 'if', 'signed', 'volatile', 'const', 'inline', 'sizeof', 'wchar_t',
    'constexpr', 'int', 'static', 'while', 'const_cast', 'long', 'static_assert', 'xor',
    'continue', 'mutable', 'static_cast', 'xor_eq', })
# https://www.programiz.com/python-programming/keywords-identifier
keywords.update({
    'False', 'await', 'else', 'import', 'pass', 'None', 'break', 'except', 'in', 'raise',
    'True', 'class', 'finally', 'is', 'return', 'and', 'continue', 'for', 'lambda', 'try',
    'as', 'def', 'from', 'nonlocal', 'while', 'assert', 'del', 'global', 'not', 'with',
    'async', 'elif', 'if', 'or', 'yield', })
# https://www.programiz.com/javascript/keywords-identifiers
keywords.update({
    'await', 'break', 'case', 'catch', 'class', 'const', 'continue', 'debugger', 'default', 'delete',
    'do', 'else', 'enum', 'export', 'extends', 'false', 'finally', 'for', 'function', 'if',
    'implements', 'import', 'in', 'instanceof', 'interface', 'let', 'new', 'null', 'package', 'private',
    'protected', 'public', 'return', 'super', 'switch', 'static', 'this', 'throw', 'try', 'true',
    'typeof', 'var', 'void', 'while', 'with', 'yield', })

frequency_ratio = filter_keywords(keywords)
print('\n')
print([key for key, _ in frequency_ratio])
'''
