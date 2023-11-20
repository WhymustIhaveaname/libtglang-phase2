#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

# These are text common words
# text_keywords = ['the', 'be', 'of', 'to', 'in', 'I', 'you', 'it', 'have', 'that', 'do', 'he', 'with', 'on', 'this', "n't", 'we',
#     'that', 'but', 'they', 'say', 'at', 'what', 'his', 'go', 'by', 'get', 'she', 'my', 'can', 'know', 'me', 'your', 'who', 'about',
#     'their', 'will', 'so', 'would', 'make', 'just', 'up', 'think', 'time',
#     'there', 'see', 'her', 'out', 'one', 'come', 'people', 'take', 'year', 'him', 'them', 'some', 'want', 'how', 'when', 'which', 'now',
#     'like', 'other', 'could', 'our', 'into', 'here', 'then', 'than', 'look', 'way', 'more', 'these', 'no', 'thing', 'well', 'because',
#     'also', 'two', 'use', 'tell', 'good', 'first', 'man', 'day', 'find', 'give', 'more']

# These are the keywords which are important in text/code classify, order by importance descending.
# each line is 10 keywords
# del by human: , '---', 'https://', '2023-10', '--------------------', '----------------', '------------', '===================='
# , 'Players.LocalPlayer.', '////////////////////', '                    '
# text_keywords = ['=', '}', '{\n', ':', '_', '(', '}\n', '-', '/', 'print(',
#                  '": ', '()', ');', '    ', 'in', 'sudo ', ';', '<', 'or', '// ',
#                  'install', '","', ');\n', 'import', ' to ', '//', '0000', 'as', ']', '000',
#                  '>', '{', 'name', ',\n', 'def', '()\n', 'return', '();', 'do',
#                  '----', '\\', ' of ', '#', 'not', 'is', 'and', '},', 'package',
#                  'await', ';\n', '>\n', '))', 'else', 'const',  'console.log(', '},\n', 'if', 'var',
#                  '_name', 'list', 'input', ')', '):\n', '=>', '", ', 'http', 'main', 'auto',
#                  'string', ']\n', 'True', '->', 'send_', ' on ', 'String', 'class', 'interface', ' no ',
#                  ' at ', '",\n', 'delete', 'new', 'export', 'Console\\', 'from', ' with ',
#                  '[', 'size', 'config', 'quest', 'load', 'Character.', 'let', 'str', 'async', 'extern',
#                  'del', 'self', ' then ', ' by ', 'println(', 'float', 'try', ')\n', 'extends', 'public',
#                  'int', ' do ', ':\n', '==', 'value', ': {', 'print', 'index', 'end',
#                  ' in ', ' into ', ' up ', '>>', 'pass', '<<', 'Command', 'elif', '====',
#                  'assert', 'null', 'xor', ' like ', '.log(', 'enum', ': "', ' will ', '<iostream>', 'except',
#                  'char', 'double', ' than ', '":"', 'for', ' out ', 'asm', 'CFrame', 'break', 'filter',
#                  'signed', 'debugger', 'in (', 'System', 'layer', 'finally', ' also ', 'main()', 'cout <<',
#                  '#define ', 'username', 'https', ' this ', 'int ', 'command', ' could ',
#                  ' we ', 'header', '<< endl;\n', 'short']

# text_keywords = list(set(text_keywords))  # I selected only the first 40
# text_keywords = [" %s " % (i) for i in text_keywords]
# ktextmax = max(len(k) for k in text_keywords)

# print("%d text_keywords: %s" % (len(text_keywords), text_keywords))
# print("max text_keywords len (ktextmax): %d" % (ktextmax))

# These are the keywords which are important in code classify, order by importance descending.
# each line is 10 keywords
keywords = ['):\n', '",\n', ');\n', '-', '(', '_', ':', '/', ';\n', '}',
            '<', ' = ', '    ', '0000', ')', '=', ';', '>', 'int ', '": ',
            'in', 'const', 'print(', ':\n', ');', 'end', ' {\n ', ') {\n', '","', 'public',
            '}\n', 'new', '      ', ')\n', '        ', 'as', '->', '=>', '{\n',
            'console', 'function', '[', 'let', 'int', ']', 'var', 'import', 'string', 'void',
            '()', 'or', ',\n', '();', 'await', 'String', 'contract', '>\n', '()\n', '\\',
            'load', ' import ', 'sudo ', 'class', ' { ', '<<', ') {', 'contex', 'System.out.println(', ') =>',
            'export', 'return', ' } ', 'width:', 'include', 'quest', 'https://', ' < ', '#include <iostream>',
            'struct', 'auto', '} ', '},', '_name', ') => {\n', 'false', 'cout <<', 'using', 'default',
            'println', '            ', 'main() {\n', 'this.', 'is', ' install ', 'CFrame', 'Character.', ' > ', 'printf("',
            'function(', 'static', '000', 'inline', 'width', 'Players.LocalPlayer.', 'using namespace std;', 'self', '<-', ' // ',
            ': "', 'print', 'https', 'config', 'enum', 'package', '// ', 'header', 'interface', 'template',
            'extends', '>>', 'extern', 'break;', 'true', 'println(', 'goto', 'Session', 'send_', 'mutable',
            'try', 'if (', ' );\n ', ' cout <<', 'Command', '//', 'layer', '<< endl;\n', '#define ', 'cout<<',
            '() {', 'install', ': {', 'sizeof', 'do', ' _ ', ': [', ' do ', 'assert', 'friend',
            '},\n', '#', 'private', 'value', '", ', 'short', '<iostream>', 'getElementById(', 'command', '.log(',
            'typedef', '() ', '));\n', 'virtual', ' ( ', 'finally', 'xor', 'if', 'implements', 'location =',
            ' as ', 'asm', 'null', 'str', 'compl', 'union', 'break', 'global', 'nullptr', 'typename',
            '                    ', ' ] ', '----', ' - ', 'catch', 'typeof', 'operator', ' ; ', '--------', 'in (',
            'username', '() {\n', ') => {', '))', 'debugger', 'else', 'main', 'name', 'True', '////////////////////', '===', 'double', '{']
# bash keywords
keywords += ['&&', '|', '-D', 'apt', 'git', 'echo', '-i', 'grep', 'HEADER', 'pip', 'in', 'cat', '-j']
# sql keywords
keywords += ['FROM','from','SELECT','select','NAME','name','NULL','null','ORDER','order','WHERE','where']
# java keywords
keywords += ['public', 'java', 'String', 'System', 'println', 'return', 'null', 'board', '.org', 'import', 'List', 'static', 'void']
# C# keywords
keywords += ['HByte','Nybble']
# js keywords
keywords += ['await',]

keywords = list(set(i for i in keywords if len(i)<=10))
keywords.sort(key=str.lower)

print([i for i in keywords if len(i)<4])

kmax = max(len(k) for k in keywords)
keyword2idx = {k: i for i, k in enumerate(keywords)}

print("%d keywords: %s" % (len(keywords), keywords))
print("max keywords len (kmax): %d" % (kmax))

kwhist = {i:0 for i in range(kmax+1)}
for k in keywords:
    kwhist[len(k)] += 1
print("keywords hist: %s"%(kwhist))


'''
# manually select keywords from freq stats
# keywords = [
#     '#', '(', ')', '-', '/', ':', ';', '<',
#     '=', '>', '[', '\\', ']', '_', '{', '}',
#     '",', '()', ')\n', '))', ');', ',\n', '->',
#     '//', ':\n', ';\n', '<-', '<<', '<=', '==', '=>',
#     '>\n', '>=', '>>', ']\n', 'as', 'do', 'if', 'in',
#     'is', 'or', '{\n', '}\n', '} ', '},', '")\n',
#     '",\n', '", ', '","', '": ', '":"', '()\n', '() ', '();',
#     ') {', '))\n', '):\n', ');\n', '---', '// ', '000', ': "',
#     ': [', ': {', '===', 'and', 'asm', 'def', 'del', 'end',
#     'for', 'int', 'let', 'new', 'not', 'str', 'try', 'var',
#     'xor', '},\n', '    ', '####', '() {', ') =>', ') {\n',
#     '));\n', '----', '.log', '0000', ': {\n', '====', '=> {', 'auto',
#     'bool', 'case', 'char', 'elif', 'else', 'enum', 'from', 'goto',
#     'http', 'if (', 'int ', 'int(', 'list', 'load', 'long', 'main',
#     'name', 'None', 'null', 'pass', 'self', 'size', 'this', 'true',
#     'True', 'void', 'with', '() {\n', '.log(', '_name', 'async', 'await',
#     'break', 'catch', 'class', 'compl', 'const', 'count', 'false', 'False',
#     'float', 'https', 'index', 'input', 'layer', 'print', 'quest', 'raise',
#     'range', 'send_', 'short', 'sudo ', 'super', 'throw', 'union', 'using',
#     'value', 'while', 'width', ') => {', '.print', 'assert', 'break;', 'Button',
#     'CFrame', 'config', 'contex', 'cout<<', 'create', 'delete', 'double', 'except',
#     'export', 'extern', 'filter', 'friend', 'global', 'handle', 'header', 'import',
#     'inline', 'is_bot', 'lambda', 'main()', 'print(', 'public', 'return', 'signed',
#     'sizeof', 'static', 'string', 'String', 'struct', 'switch', 'System', 'type":',
#     'typeof', 'width:', '} else', '"https:', '#define', ') => {\n', '2023-10', 'Command',
#     'command', 'console', 'cout <<', 'default', 'extends', 'finally', 'include', 'install',
#     'mutable', 'nullptr', 'package', 'println', 'private', 'Session', 'typedef', 'virtual',
#     '        ', ' cout <<', ' else {\n', '########', '#define ', '--------', '00000000', '========',
#     'continue', 'contract', 'debugger', 'decltype', 'for(int ', 'function', 'https://', 'main() {',
#     'main(){\n', 'message_', 'operator', 'position', 'printf("', 'println(', 'register', 'template',
#     'typename', 'unsigned', 'username', '} else {', '(int i = ', 'Console\\',
#     'for (int ', 'for i in ', 'function(', 'interface', 'main() {\n', 'namespace', 'protected', '<iostream>',
#     'Character.', 'implements', 'instanceof', 'location =', 'new HByte()', 'static_cast', '            ', '------------',
#     '000000000000', 'console.log(', 'getElementById(', 'using namespace', '################', '----------------', '0000000000000000',
#     '================', 'reinterpret_cast', '#include <iostream>', 'System.out.println(', '                    ', '"type": "supergroup"',
#     '####################', '--------------------', '////////////////////', '00000000000000000000', '====================', 'Players.LocalPlayer.', 'using namespace std;',
#     "<< endl;\n", "in (", ]

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
'''
