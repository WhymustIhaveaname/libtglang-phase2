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

# keywords = [('CFrame', float('inf')), ('xor', float('inf')), ('if (', float('inf')), ('width:', float('inf')),
# ('#include <iostream>', float('inf')), ('layer.Character.HumanoidRootPart.CFrame', float('inf')), (' else {\n', float('inf')), ('function(', float('inf')),
# ('decltype', float('inf')), ('));\n', float('inf')), ('\xa0 \xa0 \xa0 \xa0 ', float('inf')), ('unsigned', float('inf')),
# ('.print', float('inf')), ('typedef', float('inf')), ('for (int ', float('inf')), ('implements', float('inf')),
# ('trigger.action.outText(', float('inf')), (' \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0', float('inf')), ('break;', float('inf')), (' cout <<', float('inf')),
# ('\xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 ', float('inf')), (') => {\n', float('inf')), ('println(', float('inf')), ('instanceof', float('inf')),
# (') =>', float('inf')), ('static_cast', float('inf')), ('main()', float('inf')), ('for(int ', float('inf')),
# ('getElementById(', float('inf')), ('#define', float('inf')), ('{\n', float('inf')), ('} else {', float('inf')),
# ('Players.LocalPlayer.', float('inf')), ('nullptr', float('inf')), ('main() {\n', float('inf')), ('cout <<', float('inf')),
# ('cout<<', float('inf')), ('(int i = ', float('inf')), ('main() {', float('inf')), ('} else', float('inf')),
# (') => {', float('inf')), ('location =', float('inf')), ('"@openzeppelin/contracts/', float('inf')),
# (': {\n', float('inf')), ('printf("', float('inf')), ('new HByte()', float('inf')), ('using namespace', float('inf')),
# ('#define ', float('inf')), ('typeof', float('inf')), ('await raider.send_message(', float('inf')), ('.log(', float('inf')), ('console.log(', float('inf')), ('reinterpret_cast', float('inf')), ('print(', float('inf')), ('main(){\n', float('inf')), ('() {\n', float('inf')), ('"type": "supergroup"', float('inf')), ('Console\\\\', float('inf')), ('typename', float('inf')), ('\xa0 \xa0 \xa0 \xa0 \xa0 \xa0 ', float('inf')), ('PhpAmqpLib\\\\Message\\\\AMQPMessage', float('inf')), ('<iostream>', float('inf')), ('using namespace std;', float('inf')), ('for i in ', float('inf')), ('println', float('inf')), ('sizeof', float('inf')), ('System.out.println(', float('inf')), ('debugger', float('inf')), ('is_bot', float('inf')), ('Character.', float('inf')), ('},\n', float('inf')), (') {\n', float('inf')), ('extends', float('inf')), ('////////////////////', float('inf')), ('\xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 ', float('inf')), ("<< endl;\n', in ('\xa0 \xa0 ", 4308.959323177666), ('();', 2609.4096299721323), (') {', 2203.11997267384), ('() {', 1648.0481873508204), ('",\n', 1143.3334299746316), (');\n', 1022.8771301699971), ('=> {', 858.3584309118855), ('": ', 807.3337908521236), ('sudo ', 772.522587820697), (': {', 596.5591094837605), (');', 538.5404377647163), ('}\n', 530.3162305764301), ('int(', 438.9890260949358), ('width', 412.0120468377051), ('print', 393.1281613576436), ('")\n', 343.34337236475426), ('else', 294.70306127974743), ('static', 287.5500743554817), ('Button', 274.6746978918034), ('elif', 257.5075292735657), ('catch', 240.34036065532797), ('.log', 227.46498419164968), ('<<', 219.4945130474679), ('const', 210.29781557341198), ('","', 197.83118121969176), ('{', 193.84594564760084), ('}', 187.90458712071074), ('export', 184.54706264605542), ('string', 175.96347833693656), ('_name', 169.03058331803288), ('String', 157.80589614456977), ('<=', 156.65041364141914), ('message_', 154.5045175641394), (';\n', 149.82256248643822), (': "', 146.40679651780087), ('githubusercontent.com', 145.92093325502054), ('return', 131.27834825711193), ('void', 124.46197248222342), ('() ', 124.4619724822234), ('},', 120.170180327664), ('} ', 116.05005985928692), ('console', 115.87838817310455), ('"https:', 115.02002974219268), ('contex', 114.03904867829336), ('false', 111.15741680308919), ('>\n', 108.72540124883885), ('namespace', 107.29480386398569), ('))', 104.1584942125769), ('int ', 100.9094545608607), ('import', 96.56532347758713), ('mutable', 94.41942740030741), ('// ', 91.34629227728955), ('send_', 90.74074841068504), ('":"', 89.61262018720086), ('input', 87.12338073755639), (',\n', 86.73081396702085), (';', 85.74314779627367), ('contract', 84.97748466027667), ('class', 84.45139400907262), ('))\n', 83.1047026291962), ('####################', 81.87418879467216), ('<', 79.814522754941), ('lambda', 77.2522587820697), ('await', 76.82307956661377), ('()', 73.61073816607988), ('template', 72.96046662751029), ('async', 72.1021081965984), ('################', 70.57613765275504), ('",', 70.35088446318018), ('true', 63.9329038196439), ('function', 63.51852388747953), ('public', 57.472694939317556), ('while', 54.362700624419425), ('null', 53.84248339356373), ('break', 52.073744808654396), ('goto', 51.50150585471314), ('double', 51.50150585471314), ('########', 50.27527952483901), (
#     '=>', 49.7219822784324), ('bool', 49.35560977743343), ('position', 49.21255003894811), ('extern', 47.82282686509077), ('inline', 47.209713700153706), ('):\n', 45.8831597614717), ('self', 45.414964253701584), ('Command', 45.20687736135931), ('type":', 44.63463840741805), ('####', 44.19632771929283), ('include', 43.291120863382055), ('super', 40.34284625285862), ('case', 38.87858775306776), ('throw', 38.62612939103485), ('<-', 38.62612939103485), ('def', 36.786789896223674), ('value', 36.63725009989756), ('>', 32.934588312751195), ('>>', 32.0570597667092), ('size', 30.962214829321585), ('new', 30.851143603789513), ('True', 30.457879806550782), ('default', 30.042545081916), ('finally', 30.042545081915996), ('private', 29.088813492013905), ('()\n', 28.799128663305318), ('enum', 28.20320558710481), ('float', 27.311404619923636), ('", ', 27.19095163694027), ('install', 26.791187389067947), ('struct', 25.473863110933383), (': [', 24.92766950045476), ('index', 24.595270424205953), ('\xa0', 24.173810507309682), ('var', 23.731086031093305), ('switch', 23.604856850076853), ('name', 23.4844600404605), ('char', 22.756479331152317), ('\xa0\xa0', 22.446754205195738), ('>=', 22.412692362699236), ('interface', 21.93582656774819), ('layer', 21.849123695938907), ('\xa0\xa0\xa0', 20.956318448389283), ('handle', 20.409856023904837), ('System', 20.196668962632604), ('range', 18.240116656877568), ('signed', 18.12090020813981), ('main', 18.000526318152165), ('Session', 17.984652838153796), ('list', 17.500511698203493), ('00000000000000000000', 17.344760017736725), ('delete', 17.167168618237714), ('pass', 16.967550378490763), ('0000000000000000', 16.877834315683145), ('create', 16.690302823286665), ('filter', 16.308810187325825), ('int', 15.915883167180876), ('_', 15.905448699655933), ('auto', 15.360098237370584), ('quest', 14.734026609353627), ('if', 14.358781134549497), ('False', 14.019854371560799), ('command', 13.37442206304566), ('let', 12.91917026117379), ('(', 12.91463544789489), ('000000000000', 12.677728140770943), (')', 12.50101690640547), ('str', 12.46839617315972), (']', 12.208152836119487), ('[', 12.080386775988082), ('try', 11.779599743365237), ('\\', 11.695394679091386), ('global', 11.587838817310455), (']\n', 11.528579762456706), ('->', 11.44477907882514), ('//', 10.93867829543991), ('register', 10.72948038639857), ('virtual', 10.300301170942626), ('username', 9.57989320214158), ('#', 9.394475914358196), ('short', 9.363910155402388), ('from', 9.223145492935556), (')\n', 9.1856393207805), (':\n', 8.864399499166364), ('header', 8.772234513714874), ('raise', 8.583584309118857), ('union', 8.583584309118857), ('config', 8.477614132463069), ('count', 8.353666872267459), ('\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0', 8.306694492695668), ('del', 8.280634274679366), ('operator', 8.078667585053042), ('=', 8.038351830710017), ('                    ', 7.340071167693921), ('        ', 7.239191658981866), ('00000000', 7.205198507654514), ('except', 7.152986924265715), ('            ', 6.696994844157465), ('for', 6.612467097861924), ('end', 6.567123233325855), ('assert', 6.437688231839142), ('None', 6.1477022754499915), ('using', 6.071315730840167), ('long', 5.72238953941257), ('continue', 5.554083964723966), ('or', 5.322437582356854), ('in', 5.310693904940225), ('package', 4.942063693129039), ('    ', 4.720077582430694), ('this', 4.431362631130467), ('http', 4.40143647967591), ('as', 4.2595410028274205), ('load', 4.138014585503552), ('is', 3.624426802712024), ('do', 3.488488783356176), ('https', 3.425558875657525), ('https://', 3.188761460630603), ('and', 3.1640219533613303), ('/', 3.0167991619648906), ('not', 2.7920230280210783), ('asm', 2.7311404619923634), ('with', 2.6823700965996427), ('friend', 2.1458960772797138), ('compl', 1.8393394948111836), (':', 1.4986815134710056), ('2023-10', 1.357949861403569), ('==', 1.27672386499763), ('0000', 0.9783604555362543), ('--------------------', 0.9065949380123705), ('protected', 0.9035351904335639), ('====================', 0.8677909411416865), ('-', 0.8547349036684899), ('----------------', 0.7232009673462314), ('000', 0.7096009418087493), ('================', 0.6455620511036466), ('------------', 0.5425770265121919), ('===', 0.5136120208316887), ('========', 0.482223837590947), ('====', 0.4461764121076633), ('--------', 0.37852316267867575), ('----', 0.2708796869541767), ('---', 0.252602448991334), ('alignof', 0), ('not_eq', 0), ('thread_local', 0), ('noexcept', 0), ('and_eq', 0), ('yield', 0), ('or_eq', 0), ('const_cast', 0), ('=<', 0), ('bitor', 0), ('char16_t', 0), ('static_assert', 0), ('dynamic_cast', 0), ('volatile', 0), ('typeid', 0), ('wchar_t', 0), ('bitand', 0), ('count <<return', 0), ('constexpr', 0), ('xor_eq', 0), ('nonlocal', 0), ('alignas', 0), ('background-color:                ', 0), ('explicit', 0), ('char32_t', 0)]

keywords = [
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
"<< endl;\n', in ('    ",
]

keywords = list(set(keywords))
keywords.sort(key=str.lower)

kmax = max(len(k) for k in keywords)
keyword2idx = {k:i for i,k in enumerate(keywords)}

print("keywords:\n%s"%(keywords))
print("max keywords len (kmax): %d"%(kmax))

'''
# C keywords
keywords = {
    'auto', 'double', 'int', 'struct', 'break', 'else', 'long', 'switch',
    'case', 'enum', 'register', 'typedef', 'char', 'extern', 'return', 'union',
    'continue', 'for', 'signed', 'void', 'do', 'if', 'static', 'while',
    'default', 'goto', 'sizeof', 'volatile', 'const', 'float', 'short', 'unsigned'}
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
