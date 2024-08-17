ctx.rule(u'START',u'{PROGRAM}')

ctx.rule(u'PROGRAM',u'{STATEMENTLIST}{RETSTAT}')

ctx.rule(u'STATEMENTLIST',u'{STATEMENT}\n{STATEMENTLIST}')
ctx.rule(u'STATEMENTLIST',u'')

ctx.rule(u'STATEMENT',u';')
ctx.rule(u'STATEMENT',u'break')
ctx.rule(u'STATEMENT',u'{VARLIST} = {EXPRLIST}')
ctx.rule(u'STATEMENT',u'local {ATTRLIST} = {EXPRLIST}')
ctx.rule(u'STATEMENT',u'local {ATTRLIST}')
ctx.rule(u'STATEMENT',u'do\n{PROGRAM}\nend')
ctx.rule(u'STATEMENT',u'{FUNCTION}')
ctx.rule(u'STATEMENT',u'{FUNCTIONCALL}')
ctx.rule(u'STATEMENT',u'{CONDITIONAL}')
ctx.rule(u'STATEMENT',u'{LOOP}')
ctx.rule(u'STATEMENT',u'goto {NAME}')
ctx.rule(u'STATEMENT',u'::{NAME}::')

ctx.rule(u'RETSTAT',u'return ')
ctx.rule(u'RETSTAT',u'return ;')
ctx.rule(u'RETSTAT',u'return {EXPRLIST}')
ctx.rule(u'RETSTAT',u'return {EXPRLIST};')
ctx.rule(u'RETSTAT',u'')

ctx.rule(u'FUNCTION',u'{FUNCDEF} ({FUNCTION_ARGS}) {PROGRAM}\nend')

ctx.rule(u'FUNCDEF',u'function {FUNCNAMELIST}')
ctx.rule(u'FUNCDEF',u'function {FUNCNAMELIST}:{NAME}')
ctx.rule(u'FUNCDEF',u'local function {NAME}')

ctx.rule(u'LAMBDA',u'function ({FUNCTION_ARGS}) {PROGRAM} end')

ctx.rule(u'FUNCTION_ARGS',u'')
ctx.rule(u'FUNCTION_ARGS',u'{FUNCTION_ARGLIST}')

ctx.rule(u'FUNCTION_ARGLIST',u'{NAME}, {FUNCTION_ARGLIST}')
ctx.rule(u'FUNCTION_ARGLIST',u'{NAME}')
ctx.rule(u'FUNCTION_ARGLIST',u'...')

ctx.rule(u'ARGS',u'({EXPRLISTOPT})')
ctx.rule(u'ARGS',u'{TABLECONSTRUCTOR}')
ctx.rule(u'ARGS',u'{LITERALSTRING}')

ctx.rule(u'CONDITIONAL',u'if {EXPR} then\n{PROGRAM}\nend')
ctx.rule(u'CONDITIONAL',u'if {EXPR} then\n{PROGRAM}{ELSEIF}\nelse\n{PROGRAM}\nend')
ctx.rule(u'CONDITIONAL',u'if {EXPR} then\n{PROGRAM}{ELSEIF}\nend')

ctx.rule(u'ELSEIF',u'\nelseif\n{EXPR} then\n{PROGRAM}{ELSEIF}')
ctx.rule(u'ELSEIF',u'')

ctx.rule(u'LOOP',u'while {EXPR}\ndo\n{PROGRAM}\nend')
ctx.rule(u'LOOP',u'for {NAME} = {EXPR}, {EXPRLIST}\ndo\n{PROGRAM}\nend')
ctx.rule(u'LOOP',u'for {NAMELIST} in {EXPRLIST}\ndo\n{PROGRAM}\nend')
ctx.rule(u'LOOP',u'repeat\n{PROGRAM}\nuntil {EXPR}')

ctx.rule(u'EXPRLIST',u'{EXPR}, {EXPRLIST}')
ctx.rule(u'EXPRLIST',u'{EXPR}')

ctx.rule(u'EXPRLISTOPT',u'{EXPRLIST}')
ctx.rule(u'EXPRLISTOPT',u'')

ctx.rule(u'EXPR',u'nil')
ctx.rule(u'EXPR',u'false')
ctx.rule(u'EXPR',u'true')
ctx.rule(u'EXPR',u'{NUMERAL}')
ctx.rule(u'EXPR',u'{LITERALSTRING}')
ctx.rule(u'EXPR',u'{TABLECONSTRUCTOR}')
ctx.rule(u'EXPR',u'{EXPR}{BINOP}{EXPR}')
ctx.rule(u'EXPR',u'{UNOP}{EXPR}')
ctx.rule(u'EXPR',u'{LAMBDA}')
ctx.rule(u'EXPR',u'{FUNCTIONCALL}')
ctx.rule(u'EXPR',u'{PREFIX_EXPR}')
ctx.rule(u'EXPR',u'...')

ctx.rule(u'PREFIX_EXPR',u'{NAME}')
ctx.rule(u'PREFIX_EXPR',u'{PREFIX_EXPR}[{EXPR}]')
ctx.rule(u'PREFIX_EXPR',u'{PREFIX_EXPR}.{NAME}')
ctx.rule(u'PREFIX_EXPR',u'{PREFIX_EXPR} {ARGS}')
ctx.rule(u'PREFIX_EXPR',u'{PREFIX_EXPR}:{NAME} {ARGS}')
ctx.rule(u'PREFIX_EXPR',u'({EXPR})')

ctx.rule(u'FUNCTIONCALL',u'{PREFIX_EXPR} {ARGS}')
ctx.rule(u'FUNCTIONCALL',u'{PREFIX_EXPR}:{NAME} {ARGS}')

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
ctx.rule(u'TABLECONSTRUCTOR',u'\\{\\}')

ctx.rule(u'FIELDLIST',u'{FIELD}{FIELDSEP}{FIELDLIST}')
ctx.rule(u'FIELDLIST',u'{FIELD}{FIELDSEPOPT}')

ctx.rule(u'FIELD',u'[{EXPR}]={EXPR}')
ctx.rule(u'FIELD',u'{NAME}={EXPR}')
ctx.rule(u'FIELD',u'{EXPR}')

ctx.rule(u'FIELDSEP',u',')
ctx.rule(u'FIELDSEP',u';')

ctx.rule(u'FIELDSEPOPT',u'{FIELDSEP}')
ctx.rule(u'FIELDSEPOPT',u'')

ctx.rule(u'FUNCNAMELIST',u'{NAME}.{FUNCNAMELIST}')
ctx.rule(u'FUNCNAMELIST',u'{NAME}')

ctx.rule(u'NAMELIST',u'{NAME}, {NAMELIST}')
ctx.rule(u'NAMELIST',u'{NAME}')

ctx.rule(u'NAME',u'var_{LETTER}')

ctx.rule(u'VARLIST',u'{VAR}, {VARLIST}')
ctx.rule(u'VARLIST',u'{VAR}')

ctx.rule(u'VAR',u'{NAME}')
ctx.rule(u'VAR',u'{PREFIX_EXPR}[{EXPR}]')
ctx.rule(u'VAR',u'{PREFIX_EXPR}.{NAME}')

ctx.rule(u'CHAR',u'{LETTER}')
ctx.rule(u'CHAR',u'{DECIMALDIGIT}')

ctx.rule(u'ATTRLIST',u'{NAME}{ATTR}, {NAMELIST}')
ctx.rule(u'ATTRLIST',u'{NAME}{ATTR}')

ctx.rule(u'ATTR',u'<{NAME}>')
ctx.rule(u'ATTR',u'')

ctx.rule(u'LITERALSTRING',u'{SHORTSTRING}')
ctx.rule(u'LITERALSTRING',u'{LONGSTRING}')

ctx.rule(u'SHORTSTRING',u'"{STRING}"')
ctx.rule(u'SHORTSTRING',u'\'{STRING}\'')

ctx.rule(u'LONGSTRING',u'[[{STRING}]]')
ctx.rule(u'LONGSTRING',u'[=[{STRING}]=]')
ctx.rule(u'LONGSTRING',u'[==[{STRING}]==]')

ctx.rule(u'STRING',u'')
ctx.rule(u'STRING',u'{STRCHR}{STRING}')

ctx.rule(u'STRCHR',u'{DECIMALDIGIT}')
ctx.rule(u'STRCHR',u'{LETTER}')
ctx.rule(u'STRCHR',u'/')
ctx.rule(u'STRCHR',u'.')
ctx.rule(u'STRCHR',u'$')
ctx.rule(u'STRCHR',u'{ESCAPESEQUENCE}')
ctx.rule(u'STRCHR',u'\n')
ctx.rule(u'STRCHR',u'\r')
ctx.rule(u'STRCHR',u' ')
ctx.rule(u'STRCHR',u'\t')

ctx.rule(u'ESCAPESEQUENCE',u'\\a')
ctx.rule(u'ESCAPESEQUENCE',u'\\b')
ctx.rule(u'ESCAPESEQUENCE',u'\\f')
ctx.rule(u'ESCAPESEQUENCE',u'\\n')
ctx.rule(u'ESCAPESEQUENCE',u'\\r')
ctx.rule(u'ESCAPESEQUENCE',u'\\t')
ctx.rule(u'ESCAPESEQUENCE',u'\\v')
ctx.rule(u'ESCAPESEQUENCE',u'\\z')
ctx.rule(u'ESCAPESEQUENCE',u'\\\\')
ctx.rule(u'ESCAPESEQUENCE',u'\\')
ctx.rule(u'ESCAPESEQUENCE',u'\\\'')
ctx.rule(u'ESCAPESEQUENCE',u'\\"')
ctx.rule(u'ESCAPESEQUENCE',u'\\x{HEXDIGIT}{HEXDIGIT}')
ctx.rule(u'ESCAPESEQUENCE',u'\\u\\{{HEXDIGITS}\\}')

ctx.rule(u'EXPONENT',u'e')
ctx.rule(u'EXPONENT',u'E')

ctx.rule(u'BIN_EXPONENT',u'p')
ctx.rule(u'BIN_EXPONENT',u'P')

ctx.rule(u'SIGN',u'-')
ctx.rule(u'SIGN',u'')

ctx.rule(u'NUMERAL',u'{DECIMAL}')
ctx.rule(u'NUMERAL',u'0x{HEXADECIMAL}')
ctx.rule(u'NUMERAL',u'0X{HEXADECIMAL}')

ctx.rule(u'DECIMAL',u'{DECIMALDIGITS}')
ctx.rule(u'DECIMAL',u'{DECIMALDIGITS}{EXPONENT}{SIGN}{DECIMALDIGITS}')
ctx.rule(u'DECIMAL',u'{DECIMALDIGITS}.{DECIMALDIGITS}')
ctx.rule(u'DECIMAL',u'.{DECIMALDIGITS}')
ctx.rule(u'DECIMAL',u'.{DECIMALDIGITS}{EXPONENT}{SIGN}{DECIMALDIGITS}')
ctx.rule(u'DECIMAL',u'{DECIMALDIGITS}.{DECIMALDIGITS}{EXPONENT}{SIGN}{DECIMALDIGITS}')

ctx.rule(u'HEXADECIMAL',u'{HEXDIGITS}')
ctx.rule(u'HEXADECIMAL',u'{HEXDIGITS}{BIN_EXPONENT}{SIGN}{HEXDIGITS}')
ctx.rule(u'HEXADECIMAL',u'{HEXDIGITS}.{HEXDIGITS}')
ctx.rule(u'HEXADECIMAL',u'{HEXDIGITS}.{HEXDIGITS}{BIN_EXPONENT}{SIGN}{HEXDIGITS}')

ctx.rule(u'DECIMALDIGITS',u'{DECIMALDIGIT}{DECIMALDIGITS}')
ctx.rule(u'DECIMALDIGITS',u'{DECIMALDIGIT}')

ctx.rule(u'HEXDIGITS',u'{HEXDIGIT}{HEXDIGITS}')
ctx.rule(u'HEXDIGITS',u'{HEXDIGIT}')

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
