grammar Ruby;

start
    : program EOF
    ;

program
    : compstmt
    ;

compstmt
    : stmt term_expr_rep term_opt
    ;

stmt
    : call 'do' block_var_opt compstmt 'end'
    | 'undef' fname
    | 'alias' fname fname
    | stmt 'if' expr
    | stmt 'while' expr
    | stmt 'unless' expr
    | stmt 'until' expr
    | 'begin' '{' compstmt '}'
    | 'end' '{' compstmt '}'
    | lhs '=' command 'do' block_var_opt compstmt 'end'
    | lhs '=' command
    | expr
    ;

expr
    : mlhs '=' mrhs
    | 'return' call_args
    | 'yield' call_args
    | expr 'and' expr
    | expr 'or' expr
    | 'not' expr
    | command
    | '!' command
    | arg
    ;

call
    : function
    | command
    ;

command
    : operation call_args
    | primary '.' operation call_args
    | primary ':' ':' operation call_args
    | 'super' call_args
    ;

function
    : operation call_args_brackets_opt
    | primary '.' operation '(' call_args_opt ')'
    | primary ':' ':' operation '(' call_args_opt ')'
    | primary '.' operation
    | primary ':' ':' operation
    | 'super' '(' call_args_opt ')'
    | 'super'
    ;

arg
    : lhs '=' arg
    | lhs op_asgn arg
    | arg op_bin arg
    | '+' arg
    | '-' arg
    | '!' arg
    | '~' arg
    | 'defined?' arg
    | primary
    ;

primary
    : '(' compstmt ')'
    | literal
    | variable
    | primary ':' ':' identifier
    | ':' ':' identifier
    | primary '[' args_opt ']'
    | '[' args_comma_opt ']'
    | '{' args_assocs_comma_opt '}'
    | 'return' call_args_brackets_opt
    | 'yield' call_args_brackets_opt
    | 'defined?' '(' arg ')'

    | operation call_args_brackets_opt function_body_opt
    | primary '.' operation '(' call_args_opt ')' function_body_opt
    | primary ':' ':' operation '(' call_args_opt ')' function_body_opt
    | primary '.' operation function_body_opt
    | primary ':' ':' operation function_body_opt
    | 'super' '(' call_args_opt ')' function_body_opt
    | 'super' function_body_opt

    | 'if' expr then compstmt elsif_rep else_opt 'end'
    | 'unless' expr then compstmt else_opt 'end'
    | 'while' expr do compstmt 'end'
    | 'until' expr do compstmt 'end'
    | 'case' compstmt when_rep else_opt 'end'
    | 'for' block_var 'in' expr do compstmt 'end'
    | 'begin' compstmt rescue_rep else_opt ensure_opt 'end'
    | 'class' identifier inheritance_opt compstmt 'end'
    | 'module' identifier compstmt 'end'
    | 'def' fname argdecl compstmt 'end'
    | 'def' singleton dots fname argdecl compstmt 'end'
    ;

// created as part of fixing mutually left-recursive rules [function, primary]
function_body_opt
    : '{' block_var_opt compstmt '}'
    | 
    ;

when_rep
    : 'when' mrhs then compstmt
    | 'when' mrhs then compstmt when_rep
    ;

then
    : term
    | 'then'
    | term 'then'
    ;

do
    : term
    | 'do'
    | term 'do'
    ;

block_var
    : lhs
    | mlhs
    ;

mlhs
    : mlhs_item ',' mlhs_item_opt '*' lhs
    | mlhs_item ',' mlhs_item_opt '*'
    | mlhs_item ',' mlhs_item_opt
    | '*' lhs
    ;

mlhs_item
    : lhs
    | '(' mlhs ')'
    ;

lhs
    : primary '[' args_opt ']'
    | primary '.' identifier
    | variable
    ;

mrhs
    : args arg_ast_opt
    | '*' arg
    ;

call_args
    : args
    | args assocs_opt arg_ast_opt arg_amp_opt
    | 'assocs' arg_ast_opt arg_amp_opt
    | '*' arg arg_amp_opt
    | '&' arg
    | command
    ;

args
    : arg ',' args
    | arg
    ;

argdecl
    : '(' arglist ')'
    | arglist term
    ;

arglist
    : identifier identifier_rep identifier_ast_opt identifier_amp_opt
    | '*' identifier identifier_amp_opt
    | '&' identifier
    | /* empty */
    ;

singleton
    : variable
    | '(' expr ')'
    ;

assocs
    : assoc ',' assocs
    | assoc
    ;

assoc
    : arg '=' '>' arg
    ;

variable
    : varname
    | 'nil'
    | 'self'
    ;

literal
    : numeric
    | symbol
    | string
    | string2
    | here_doc
    | REGEXP
    ;

term_opt
    : term
    | /* empty */
    ;

term
    : ';'
    | 
    ;

term_expr_rep
    : term expr term_expr_rep
    | /* empty */
    ;

block_var_opt
    : '|' block_var '|'
    | '|' '|'
    | /* empty */
    ;

arg_ast_opt
    : ',' '*' arg
    | /* empty */
    ;

arg_amp_opt
    : ',' '&' arg
    | /* empty */
    | ',' '&' arg
    | /* empty */
    ;

assocs_opt
    : ',' assocs
    | /* empty */
    ;

call_args_brackets_opt
    : '(' call_args_opt ')'
    | /* empty */
    ;

call_args_opt
    : call_args
    | /* empty */
    ;

args_opt
    : args
    | /* empty */
    ;

args_comma_opt
    : args comma_opt
    | /* empty */
    ;

comma_opt
    : ','
    | /* empty */
    ;

args_assocs_comma_opt
    : args
    | assocs comma_opt
    | /* empty */
    ;

elsif_rep
    : 'elsif ' expr then compstmt elsif_rep
    | /* empty */
    ;

else_opt
    : 'else' compstmt
    | /* empty */
    ;

inheritance_opt
    : '<' identifier
    | /* empty */
    ;

rescue_rep
    : 'rescue' args_opt do compstmt rescue_rep
    | /* empty */
    ;

ensure_opt
    : 'ensure' compstmt
    | /* empty */
    ;

dots
    : '.'
    | ':' ':'
    ;

mlhs_item_opt
    : mlhs_item_rep
    | /* empty */
    ;

mlhs_item_rep
    : mlhs_item ',' mlhs_item_rep
    | mlhs_item
    ;

identifier_ast_opt
    : ',' '*' identifier
    | /* empty */
    ;

identifier_amp_opt
    : ',' '&' identifier
    | /* empty */
    ;

identifier_rep
    : ',' identifier identifier_rep
    | /* empty */
    ;

varname
    : global
    | '@' identifier
    | identifier
    ;

op_asgn
    : '+' '='
    | '-' '='
    | '*' '='
    | '/' '='
    | '%' '='
    | '**='
    | '&' '='
    | '|' '='
    | '^' '='
    | '<<='
    | '>>='
    | '&&='
    | '||='
    ;

op_bin
    : '.' '.'
    | '.' '.' '.'
    | '+'
    | '-'
    | '*'
    | '/'
    | '%'
    | '*' '*'
    | '|'
    | '^'
    | '&'
    | '<=>'
    | '>'
    | '>' '='
    | '<'
    | '<' '='
    | '=' '='
    | '==='
    | '!' '='
    | '=' '~'
    | '!' '~'
    | '<' '<'
    | '>' '>'
    | '&' '&'
    | '|' '|'
    ;

fname_op
    : '.' '.'
    | '|'
    | '^'
    | '&'
    | '<=>'
    | '=' '='
    | '==='
    | '=' '~'
    | '>'
    | '>' '='
    | '<'
    | '<' '='
    | '+'
    | '-'
    | '*'
    | '/'
    | '%'
    | '*' '*'
    | '<' '<'
    | '>' '>'
    | '~'
    | '+' '@'
    | '-' '@'
    | '[' ']'
    | '[' ']' '='
    ;

symbol
    : ':' fname
    | ':' varname
    ;

fname
    : identifier
    | fname_op
    ;

operation
    : identifier
    | identifier '!'
    | identifier '?'
    ;

global
    : '$' identifier
    | '$' any_char
    | '$' '-' any_char
    | '$'
    ;

string
    : '"' str_1 '"'
    | '\'' str_2 '\''
    | '`' str_3 '`'
    ;

str_1
    : /* empty */
    | str_1 str_1_char
    ;

str_2
    : /* empty */
    | str_2 str_2_char
    ;

str_3
    : /* empty */
    | str_3 str_3_char
    ;

str_1_char
    : char
    | bracket
    | '/'
    | '\\' '"'
    | '\''
    | '`'
    ;

str_2_char
    : char
    | bracket
    | '/'
    | '"'
    | '\\' '\''
    | '`'
    ;

str_3_char
    : char
    | bracket
    | '/'
    | '"'
    | '\''
    | '\\' '`'
    ;

string2
    : string2_prefix '{' string2_1 '}'
    | string2_prefix '[' string2_2 ']'
    | string2_prefix '(' string2_3 ')'
    ;

string2_prefix
    : '%' 'Q'
    | '%' 'q'
    | '%' 'x'
    ;

here_doc
    : '<<EOF' any_string 'EOF'
    ;

REGEXP
    : '/' ('\\/'|[\u0000-\u007F && ~[/]])* '/' [iop]
    | '%' 'r' '{' ('\\{' | '\\}' | [\u0000-\u007F] ~('{' | '}'))* '}'
    | '%' 'r' '[' ('\\[' | '\\]' | [\u0000-\u007F] ~('[' | ']'))* ']'
    ;

regexp_str_1
    : /* empty */
    | regexp_str_1 regexp_str_1_char
    ;

regexp_str_1_char
    : char
    | bracket
    | quote
    | '\\' '/'
    ;

string2_1
    : string2_1 string2_1_char
    | /* empty */
    ;

string2_2
    : string2_2 string2_2_char
    | /* empty */
    ;

string2_3
    : string2_3 string2_3_char
    | /* empty */
    ;

string2_1_char
    : char
    | quote
    | '/'
    | '\\' '{'
    | '\\' '}'
    | '('
    | ')'
    | '['
    | ']'
    ;

string2_2_char
    : char
    | quote
    | '/'
    | '{'
    | '}'
    | '('
    | ')'
    | '\\' '['
    | '\\' ']'
    ;

string2_3_char
    : char
    | quote
    | '/'
    | '{'
    | '}'
    | '\\' '('
    | '\\' ')'
    | '['
    | ']'
    ;

any_string
    : any_char any_string
    | /* empty */
    ;

identifier
    : letter ext_string
    ;

ext_string
    : /* empty */
    | ext_string letter
    | ext_string decimaldigit
    ;

numeric
    : hex
    | decimal
    ;

hex
    : hex_prefix hex_seq hex_float_seq hex_float_exp
    ;

hex_prefix
    : '0' 'x'
    | '0' 'X'
    ;

hex_seq
    : hexd hex_seq
    | hexd
    ;

hex_float_seq
    : '.' hex_seq
    | /* empty */
    ;

hex_float_exp
    : hex_float_exp_prefix hex_seq
    | /* empty */
    ;

hex_float_exp_prefix
    : 'p'
    | 'p' '-'
    | 'P'
    | 'P' '-'
    ;

any_char
    : char
    | bracket
    | quote
    | '/'
    ;

decimal
    : dec_prefix dec_seq dec_float_seq dec_float_exp
    ;

dec_prefix
    : '-'
    | '+'
    | /* empty */
    ;

dec_seq
    : decimaldigit dec_seq
    | decimaldigit
    ;

dec_float_seq
    : '.' dec_seq
    | /* empty */
    ;

dec_float_exp
    : dec_float_exp_prefix dec_seq
    | /* empty */
    ;

dec_float_exp_prefix
    : 'e'
    | 'e' '-'
    | 'E'
    | 'E' '-'
    ;

decimaldigit
    : '0'
    | '1'
    | '2'
    | '3'
    | '4'
    | '5'
    | '6'
    | '7'
    | '8'
    | '9'
    ;

hexd
    : 'a'
    | 'b'
    | 'c'
    | 'd'
    | 'e'
    | 'f'
    | 'A'
    | 'B'
    | 'C'
    | 'D'
    | 'E'
    | 'F'
    | '0'
    | '1'
    | '2'
    | '3'
    | '4'
    | '5'
    | '6'
    | '7'
    | '8'
    | '9'
    ;

letter
    : '_'
    | 'a'
    | 'b'
    | 'c'
    | 'd'
    | 'e'
    | 'f'
    | 'g'
    | 'h'
    | 'i'
    | 'j'
    | 'k'
    | 'l'
    | 'm'
    | 'n'
    | 'o'
    | 'p'
    | 'q'
    | 'r'
    | 's'
    | 't'
    | 'u'
    | 'v'
    | 'w'
    | 'x'
    | 'y'
    | 'z'
    | 'A'
    | 'B'
    | 'C'
    | 'D'
    | 'E'
    | 'F'
    | 'G'
    | 'H'
    | 'I'
    | 'J'
    | 'K'
    | 'L'
    | 'M'
    | 'N'
    | 'O'
    | 'P'
    | 'Q'
    | 'R'
    | 'S'
    | 'T'
    | 'U'
    | 'V'
    | 'W'
    | 'X'
    | 'Y'
    | 'Z'
    ;

bracket
    : '('
    | ')'
    | '['
    | ']'
    | '{'
    | '}'
    ;

quote
    : '"'
    | '\''
    | '`'
    ;

char
    : '\u0000'
    | '\u0001'
    | '\u0002'
    | '\u0003'
    | '\u0004'
    | '\u0005'
    | '\u0006'
    | '\u0007'
    | '\b'
    | '\u000b'
    | '\f'
    | '\u000e'
    | '\u000f'
    | '\u0010'
    | '\u0011'
    | '\u0012'
    | '\u0013'
    | '\u0014'
    | '\u0015'
    | '\u0016'
    | '\u0017'
    | '\u0018'
    | '\u0019'
    | '\u001a'
    | '\u001b'
    | '\u001c'
    | '\u001d'
    | '\u001e'
    | '\u001f'
    | '!'
    | '#'
    | '$'
    | '%'
    | '&'
    | '*'
    | '+'
    | ','
    | '-'
    | '.'
    | '0'
    | '1'
    | '2'
    | '3'
    | '4'
    | '5'
    | '6'
    | '7'
    | '8'
    | '9'
    | ':'
    | ';'
    | '<'
    | '='
    | '>'
    | '?'
    | '@'
    | 'A'
    | 'B'
    | 'C'
    | 'D'
    | 'E'
    | 'F'
    | 'G'
    | 'H'
    | 'I'
    | 'J'
    | 'K'
    | 'L'
    | 'M'
    | 'N'
    | 'O'
    | 'P'
    | 'Q'
    | 'R'
    | 'S'
    | 'T'
    | 'U'
    | 'V'
    | 'W'
    | 'X'
    | 'Y'
    | 'Z'
    | '\\'
    | '^'
    | '_'
    | 'a'
    | 'b'
    | 'c'
    | 'd'
    | 'e'
    | 'f'
    | 'g'
    | 'h'
    | 'i'
    | 'j'
    | 'k'
    | 'l'
    | 'm'
    | 'n'
    | 'o'
    | 'p'
    | 'q'
    | 'r'
    | 's'
    | 't'
    | 'u'
    | 'v'
    | 'w'
    | 'x'
    | 'y'
    | 'z'
    | '|'
    | '~'
    | '\u007f'
    ;

WHITESPACE
    : (' ' | '\n' | '\t' | '\r')+ -> skip
    ;
