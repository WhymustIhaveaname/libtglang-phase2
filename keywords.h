const char *keywordsList[]={";", "\'    \'", "\'      \'", "\'        \'", "\'            \'", "\'                    \'", "\'  to  \'", "\' \",\" \'", "\' \":  \'", "\' ( \'", "\' ()\n \'", "\' () \'", "\' (); \'", "\' );\n \'", "\' ); \'", "\' ,\n \'", "\' - \'", "\' --- \'", "\' / \'", "\' // \'", "\' //  \'", "\' 000 \'", "\' 0000 \'", "\' : \'", "\' ; \'", "\' < \'", "\' = \'", "\' > \'", "\' ] \'", "\' _ \'", "\' as \'", "\' cout <<\'", "\' def \'", "\' do \'", "\' else {\n\'", "\' import \'", "\' in \'", "\' install \'", "\' name \'", "\' or \'", "\' print( \'", "\' return \'", "\' sudo  \'", "\' {\n \'", "\' { \'", "\' }\n \'", "\' } \'", "\'\")\n\'", "\'\",\'", "\'\",\n\'", "\'\", \'", "\'\",\"\'", "\'\": \'", "\'\":\"\'", "\'\"https:\'", "\'\"type\": \"supergroup\"\'", "\'#\'", "\'####\'", "\'########\'", "\'################\'", "\'####################\'", "\'#define\'", "\'#define \'", "\'#include <iostream>\'", "\'(\'", "\'()\'", "\'()\n\'", "\'() \'", "\'() {\'", "\'() {\n\'", "\'();\'", "\'(int i = \'", "\')\'", "\')\n\'", "\') =>\'", "\') => {\'", "\') => {\n\'", "\') {\'", "\') {\n\'", "\'))\'", "\'))\n\'", "\'));\n\'", "\'):\n\'", "\');\'", "\');\n\'", "\',\n\'", "\'-\'", "\'---\'", "\'----\'", "\'--------\'", "\'------------\'", "\'----------------\'", "\'--------------------\'", "\'->\'", "\'.log\'", "\'.log(\'", "\'.print\'", "\'/\'", "\'//\'", "\'// \'", "\'////////////////////\'", "\'000\'", "\'0000\'", "\'00000000\'", "\'000000000000\'", "\'0000000000000000\'", "\'00000000000000000000\'", "\'2023-10\'", "\':\'", "\':\n\'", "\': \"\'", "\': [\'", "\': {\'", "\': {\n\'", "\';\'", "\';\n\'", "\'<\'", "\'<-\'", "\'<<\'", "\'<< endl;\n\'", "\'<=\'", "\'<iostream>\'", "\'=\'", "\'==\'", "\'===\'", "\'====\'", "\'========\'", "\'================\'", "\'====================\'", "\'=>\'", "\'=> {\'", "\'>\'", "\'>\n\'", "\'>=\'", "\'>>\'", "\'[\'", "\'\\\'", "\']\'", "\']\n\'", "\'_\'", "\'_name\'", "\'and\'", "\'as\'", "\'asm\'", "\'assert\'", "\'async\'", "\'auto\'", "\'await\'", "\'bool\'", "\'break\'", "\'break;\'", "\'Button\'", "\'case\'", "\'catch\'", "\'CFrame\'", "\'char\'", "\'Character.\'", "\'class\'", "\'command\'", "\'Command\'", "\'compl\'", "\'config\'", "\'console\'", "\'console.log(\'", "\'Console\\\'", "\'const\'", "\'contex\'", "\'continue\'", "\'contract\'", "\'count\'", "\'cout <<\'", "\'cout<<\'", "\'create\'", "\'debugger\'", "\'decltype\'", "\'def\'", "\'default\'", "\'del\'", "\'delete\'", "\'do\'", "\'double\'", "\'elif\'", "\'else\'", "\'end\'", "\'enum\'", "\'except\'", "\'export\'", "\'extends\'", "\'extern\'", "\'false\'", "\'False\'", "\'filter\'", "\'finally\'", "\'float\'", "\'for\'", "\'for (int \'", "\'for i in \'", "\'for(int \'", "\'friend\'", "\'from\'", "\'function\'", "\'function(\'", "\'getElementById(\'", "\'global\'", "\'goto\'", "\'handle\'", "\'header\'", "\'http\'", "\'https\'", "\'https://\'", "\'if\'", "\'if (\'", "\'implements\'", "\'import\'", "\'in\'", "\'in (\'", "\'include\'", "\'index\'", "\'inline\'", "\'input\'", "\'install\'", "\'instanceof\'", "\'int\'", "\'int \'", "\'int(\'", "\'interface\'", "\'is\'", "\'is_bot\'", "\'lambda\'", "\'layer\'", "\'let\'", "\'list\'", "\'load\'", "\'location =\'", "\'long\'", "\'main\'", "\'main()\'", "\'main() {\'", "\'main() {\n\'", "\'main(){\n\'", "\'message_\'", "\'mutable\'", "\'name\'", "\'namespace\'", "\'new\'", "\'new HByte()\'", "\'None\'", "\'not\'", "\'null\'", "\'nullptr\'", "\'operator\'", "\'or\'", "\'package\'", "\'pass\'", "\'Players.LocalPlayer.\'", "\'position\'", "\'print\'", "\'print(\'", "\'printf(\"\'", "\'println\'", "\'println(\'", "\'private\'", "\'protected\'", "\'public\'", "\'quest\'", "\'raise\'", "\'range\'", "\'register\'", "\'reinterpret_cast\'", "\'return\'", "\'self\'", "\'send_\'", "\'Session\'", "\'short\'", "\'signed\'", "\'size\'", "\'sizeof\'", "\'static\'", "\'static_cast\'", "\'str\'", "\'string\'", "\'String\'", "\'struct\'", "\'sudo \'", "\'super\'", "\'switch\'", "\'System\'", "\'System.out.println(\'", "\'template\'", "\'this\'", "\'throw\'", "\'True\'", "\'true\'", "\'try\'", "\'type\":\'", "\'typedef\'", "\'typename\'", "\'typeof\'", "\'union\'", "\'unsigned\'", "\'username\'", "\'using\'", "\'using namespace\'", "\'using namespace std;\'", "\'value\'", "\'var\'", "\'virtual\'", "\'void\'", "\'while\'", "\'width\'", "\'width:\'", "\'with\'", "\'xor\'", "\'{\'", "\'{\n\'", "\'}\'", "\'}\n\'", "\'} \'", "\'} else\'", "\'} else {\'", "\'},\'", "\'},\n\'", };
const char *text_keywordsList[]={"\' / \'", "\' { \'", "\' import \'", "\'  to  \'", "\' _ \'", "\' < \'", "\' ; \'", "\' > \'", "\' def \'", "\' - \'", "\' return \'", "\' } \'", "\' print( \'", "\' //  \'", "\' do \'", "\' name \'", "\' () \'", "\' in \'", "\' install \'", "\' {\n \'", "\'      \'", "\' as \'", "\' (); \'", "\' \":  \'", "\' --- \'", "\' ( \'", "\' sudo  \'", "\' = \'", "\' or \'", "\' 000 \'", "\' 0000 \'", "\' ()\n \'", "\' }\n \'", "\' );\n \'", "\' // \'", "\' : \'", "\' \",\" \'", "\' ] \'", "\' ,\n \'", "\' ); \'", };
