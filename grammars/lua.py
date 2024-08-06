ctx.rule(u'START',u'{PROGRAM}')

ctx.rule(u'PROGRAM',u'{STATEMENT}\n{PROGRAM}')
ctx.rule(u'PROGRAM',u'')

ctx.rule(u'STATEMENT',u';')
ctx.rule(u'STATEMENT',u'')
ctx.rule(u'STATEMENT',u'break')
ctx.rule(u'STATEMENT',u'{VAR} = {EXPR}')
ctx.rule(u'STATEMENT',u'local {VARLIST} = {EXPRLIST}')
ctx.rule(u'STATEMENT',u'{FUNCTION}')
ctx.rule(u'STATEMENT',u'{FUNCTIONCALL}')
ctx.rule(u'STATEMENT',u'{COROUTINE}')
ctx.rule(u'STATEMENT',u'{CONDITIONAL}')
ctx.rule(u'STATEMENT',u'{LOOP}')
ctx.rule(u'STATEMENT',u'return {EXPRLIST}')
ctx.rule(u'STATEMENT',u'goto {LABELNAME}')
ctx.rule(u'STATEMENT',u'::{LABELNAME}::')

ctx.rule(u'LABELNAME',u'labela')
ctx.rule(u'LABELNAME',u'labelb')

ctx.rule(u'FUNCTION',u'{FUNCDEF} ({FUNCTION_ARGS}) {PROGRAM}\nend')

ctx.rule(u'FUNCDEF',u'function {VAR}.{IDENTIFIER}')
ctx.rule(u'FUNCDEF',u'function {VAR}:{IDENTIFIER}')
ctx.rule(u'FUNCDEF',u'local function {IDENTIFIER}')

ctx.rule(u'LAMBDA',u'function ({FUNCTION_ARGS}) {PROGRAM} end')

ctx.rule(u'FUNCTION_ARGS',u'')
ctx.rule(u'FUNCTION_ARGS',u'{FUNCTION_ARGLIST}')

ctx.rule(u'FUNCTION_ARGLIST',u'{VAR}, {FUNCTION_ARGLIST}')
ctx.rule(u'FUNCTION_ARGLIST',u'{VAR}')
ctx.rule(u'FUNCTION_ARGLIST',u'...')

ctx.rule(u'COROUTINE',u'{VAR} = coroutine.create({LAMBDA})')
ctx.rule(u'COROUTINE',u'{VAR} = coroutine.wrap({LAMBDA})')
ctx.rule(u'COROUTINE',u'coroutine.resume({VAR}, {ARGS})')
ctx.rule(u'COROUTINE',u'coroutine.yield({ARGS})')

ctx.rule(u'FUNCTIONCALL',u'{PREFIX_EXPR} {ARGS}')
ctx.rule(u'FUNCTIONCALL',u'{PREFIX_EXPR}:{IDENTIFIER} {ARGS}')
ctx.rule(u'FUNCTIONCALL',u'{PREFIX_EXPR}.{IDENTIFIER} {ARGS}')

ctx.rule(u'ARGS',u'({EXPRLIST})')
ctx.rule(u'ARGS',u'{TABLECONSTRUCTOR}')
ctx.rule(u'ARGS',u'{LITERALSTRING}')

ctx.rule(u'CONDITIONAL',u'if {EXPR} then\n{PROGRAM}\nend')
ctx.rule(u'CONDITIONAL',u'if {EXPR} then\n{PROGRAM}\nelse\n{PROGRAM}\nend')

ctx.rule(u'LOOP',u'while ({EXPR})\ndo\n{PROGRAM}\nend')
ctx.rule(u'LOOP',u'for {VAR}={EXPR}, {EXPR}, {EXPR}\ndo\n{PROGRAM}\nend')
ctx.rule(u'LOOP',u'repeat\n{PROGRAM}\nuntil ({EXPR})')

ctx.rule(u'EXPRLIST',u'{EXPR}, {EXPRLIST}')
ctx.rule(u'EXPRLIST',u'{EXPR}')

ctx.rule(u'EXPR',u'(nil)')
ctx.rule(u'EXPR',u'(false)')
ctx.rule(u'EXPR',u'(true)')
ctx.rule(u'EXPR',u'({NUMERAL})')
ctx.rule(u'EXPR',u'{LITERALSTRING}')
ctx.rule(u'EXPR',u'{TABLECONSTRUCTOR}')
ctx.rule(u'EXPR',u'({VAR}[{EXPR}])')
ctx.rule(u'EXPR',u'({EXPR}{BINOP}{EXPR})')
ctx.rule(u'EXPR',u'({UNOP}{EXPR})')
ctx.rule(u'EXPR',u'{LAMBDA}')
ctx.rule(u'EXPR',u'{VAR}')
ctx.rule(u'EXPR',u'{FUNCTIONCALL}')
ctx.rule(u'EXPR',u'...')

ctx.rule(u'PREFIX_EXPR',u'{IDENTIFIER}')
ctx.rule(u'PREFIX_EXPR',u'({EXPR})')

ctx.rule(u'BINOP',u'+')
ctx.rule(u'BINOP',u'-')
ctx.rule(u'BINOP',u'*')
ctx.rule(u'BINOP',u'/')
ctx.rule(u'BINOP',u'//')
ctx.rule(u'BINOP',u'^')
ctx.rule(u'BINOP',u'%')
ctx.rule(u'BINOP',u'&')
ctx.rule(u'BINOP',u'~')
ctx.rule(u'BINOP',u'|')
ctx.rule(u'BINOP',u'>>')
ctx.rule(u'BINOP',u'<<')
ctx.rule(u'BINOP',u' .. ')
ctx.rule(u'BINOP',u'<')
ctx.rule(u'BINOP',u'<=')
ctx.rule(u'BINOP',u'>')
ctx.rule(u'BINOP',u'>=')
ctx.rule(u'BINOP',u'==')
ctx.rule(u'BINOP',u'~=')
ctx.rule(u'BINOP',u' and ')
ctx.rule(u'BINOP',u' or ')

ctx.rule(u'UNOP',u'-')
ctx.rule(u'UNOP',u' not ')
ctx.rule(u'UNOP',u'#')
ctx.rule(u'UNOP',u'~')

ctx.rule(u'TABLECONSTRUCTOR',u'\\{{FIELDLIST}\\}')
ctx.rule(u'METATABLE',u'{VAR} = setmetatable({VAR}, {TABLECONSTRUCTOR})')

ctx.rule(u'FIELDLIST',u'{FIELD},{FIELDLIST}')
ctx.rule(u'FIELDLIST',u'{FIELD}')

ctx.rule(u'FIELD',u'[{EXPR}]={EXPR}')
ctx.rule(u'FIELD',u'{IDENTIFIER}={EXPR}')
ctx.rule(u'FIELD',u'{EXPR}')

ctx.rule(u'VARLIST',u'{VAR}, {VARLIST}')
ctx.rule(u'VARLIST',u'{VAR}')

ctx.rule(u'VAR',u'{LETTER}{VAR}')

ctx.rule(u'LITERALSTRING',u'"{STRING}"')
ctx.rule(u'LITERALSTRING',u'[[{STRING}]]')

ctx.rule(u'STRING',u'')
ctx.rule(u'STRING',u'{STRCHR}{STRING}')

ctx.rule(u'STRCHR',u'\n')
ctx.rule(u'STRCHR',u'\r')
ctx.rule(u'STRCHR',u' ')
ctx.rule(u'STRCHR',u'\t')
ctx.rule(u'STRCHR',u'0')
ctx.rule(u'STRCHR',u'a')
ctx.rule(u'STRCHR',u'/')
ctx.rule(u'STRCHR',u'.')
ctx.rule(u'STRCHR',u'$')
ctx.rule(u'STRCHR',u'{ESCAPESEQUENCE}')

ctx.rule(u'ESCAPESEQUENCE',u'\\a')
ctx.rule(u'ESCAPESEQUENCE',u'\\b')
ctx.rule(u'ESCAPESEQUENCE',u'\\f')
ctx.rule(u'ESCAPESEQUENCE',u'\\n')
ctx.rule(u'ESCAPESEQUENCE',u'\\r')
ctx.rule(u'ESCAPESEQUENCE',u'\\t')
ctx.rule(u'ESCAPESEQUENCE',u'\\v')
ctx.rule(u'ESCAPESEQUENCE',u'\\z')
ctx.rule(u'ESCAPESEQUENCE',u'\n')
ctx.rule(u'ESCAPESEQUENCE',u'\\x{HEXADECIMAL}')
ctx.rule(u'ESCAPESEQUENCE',u'\\u\\{{HEXADECIMAL}\\}')

ctx.rule(u'NUMERAL',u'{DECIMAL}')
ctx.rule(u'NUMERAL',u'0x{HEXADECIMAL}')

ctx.rule(u'DECIMAL',u'{DECIMALDIGIT}{DECIMALDIGITS}')
ctx.rule(u'DECIMAL',u'{DECIMALDIGIT}{DECIMALDIGITS}e{DECIMALDIGIT}{DECIMALDIGITS}')
ctx.rule(u'DECIMAL',u'{DECIMALDIGIT}{DECIMALDIGITS}e-{DECIMALDIGIT}{DECIMALDIGITS}')
ctx.rule(u'DECIMAL',u'{DECIMALDIGIT}{DECIMALDIGITS}.{DECIMALDIGIT}{DECIMALDIGITS}')
ctx.rule(u'DECIMAL',u'{DECIMALDIGIT}{DECIMALDIGITS}.{DECIMALDIGIT}{DECIMALDIGITS}e{DECIMALDIGIT}{DECIMALDIGITS}')
ctx.rule(u'DECIMAL',u'{DECIMALDIGIT}{DECIMALDIGITS}.{DECIMALDIGIT}{DECIMALDIGITS}e-{DECIMALDIGIT}{DECIMALDIGITS}')

ctx.rule(u'HEXADECIMAL',u'{HEXDIGIT}{HEXDIGITS}')
ctx.rule(u'HEXADECIMAL',u'{HEXDIGIT}{HEXDIGITS}p{HEXDIGIT}{HEXDIGITS}')
ctx.rule(u'HEXADECIMAL',u'{HEXDIGIT}{HEXDIGITS}p-{HEXDIGIT}{HEXDIGITS}')
ctx.rule(u'HEXADECIMAL',u'{HEXDIGIT}{HEXDIGITS}.{HEXDIGIT}{HEXDIGITS}')
ctx.rule(u'HEXADECIMAL',u'{HEXDIGIT}{HEXDIGITS}.{HEXDIGIT}{HEXDIGITS}p{HEXDIGIT}{HEXDIGITS}')
ctx.rule(u'HEXADECIMAL',u'{HEXDIGIT}{HEXDIGITS}.{HEXDIGIT}{HEXDIGITS}p-{HEXDIGIT}{HEXDIGITS}')

ctx.rule(u'DECIMALDIGITS',u'{DECIMALDIGIT}{DECIMALDIGITS}')
ctx.rule(u'DECIMALDIGITS',u'')

ctx.rule(u'HEXDIGITS',u'{HEXDIGIT}{HEXDIGITS}')
ctx.rule(u'HEXDIGITS',u'')

ctx.rule(u'DECIMALDIGIT',u'0')
ctx.rule(u'DECIMALDIGIT',u'1')
ctx.rule(u'DECIMALDIGIT',u'2')
ctx.rule(u'DECIMALDIGIT',u'3')
ctx.rule(u'DECIMALDIGIT',u'4')
ctx.rule(u'DECIMALDIGIT',u'5')
ctx.rule(u'DECIMALDIGIT',u'6')
ctx.rule(u'DECIMALDIGIT',u'7')
ctx.rule(u'DECIMALDIGIT',u'8')
ctx.rule(u'DECIMALDIGIT',u'9')

ctx.rule(u'HEXDIGIT',u'a')
ctx.rule(u'HEXDIGIT',u'b')
ctx.rule(u'HEXDIGIT',u'c')
ctx.rule(u'HEXDIGIT',u'd')
ctx.rule(u'HEXDIGIT',u'e')
ctx.rule(u'HEXDIGIT',u'f')
ctx.rule(u'HEXDIGIT',u'A')
ctx.rule(u'HEXDIGIT',u'B')
ctx.rule(u'HEXDIGIT',u'C')
ctx.rule(u'HEXDIGIT',u'D')
ctx.rule(u'HEXDIGIT',u'E')
ctx.rule(u'HEXDIGIT',u'F')
ctx.rule(u'HEXDIGIT',u'{DECIMALDIGIT}')

ctx.rule(u'IDENTIFIER',u'{LETTER}{IDENTIFIER}')

ctx.rule(u'LETTER',u'_')
ctx.rule(u'LETTER',u'a')
ctx.rule(u'LETTER',u'b')
ctx.rule(u'LETTER',u'c')
ctx.rule(u'LETTER',u'd')
ctx.rule(u'LETTER',u'e')
ctx.rule(u'LETTER',u'f')
ctx.rule(u'LETTER',u'g')
ctx.rule(u'LETTER',u'h')
ctx.rule(u'LETTER',u'i')
ctx.rule(u'LETTER',u'j')
ctx.rule(u'LETTER',u'k')
ctx.rule(u'LETTER',u'l')
ctx.rule(u'LETTER',u'm')
ctx.rule(u'LETTER',u'n')
ctx.rule(u'LETTER',u'o')
ctx.rule(u'LETTER',u'p')
ctx.rule(u'LETTER',u'q')
ctx.rule(u'LETTER',u'r')
ctx.rule(u'LETTER',u's')
ctx.rule(u'LETTER',u't')
ctx.rule(u'LETTER',u'u')
ctx.rule(u'LETTER',u'v')
ctx.rule(u'LETTER',u'w')
ctx.rule(u'LETTER',u'x')
ctx.rule(u'LETTER',u'y')
ctx.rule(u'LETTER',u'z')
ctx.rule(u'LETTER',u'A')
ctx.rule(u'LETTER',u'B')
ctx.rule(u'LETTER',u'C')
ctx.rule(u'LETTER',u'D')
ctx.rule(u'LETTER',u'E')
ctx.rule(u'LETTER',u'F')
ctx.rule(u'LETTER',u'G')
ctx.rule(u'LETTER',u'H')
ctx.rule(u'LETTER',u'I')
ctx.rule(u'LETTER',u'J')
ctx.rule(u'LETTER',u'K')
ctx.rule(u'LETTER',u'L')
ctx.rule(u'LETTER',u'M')
ctx.rule(u'LETTER',u'N')
ctx.rule(u'LETTER',u'O')
ctx.rule(u'LETTER',u'P')
ctx.rule(u'LETTER',u'Q')
ctx.rule(u'LETTER',u'R')
ctx.rule(u'LETTER',u'S')
ctx.rule(u'LETTER',u'T')
ctx.rule(u'LETTER',u'U')
ctx.rule(u'LETTER',u'V')
ctx.rule(u'LETTER',u'W')
ctx.rule(u'LETTER',u'X')
ctx.rule(u'LETTER',u'Y')
ctx.rule(u'LETTER',u'Z')
