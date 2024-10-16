ctx.rule(u'START',u'{PROGRAM}')

ctx.rule(u'PROGRAM', u'{COMPSTMT}')

ctx.rule(u'COMPSTMT', u'{STMT}')
ctx.rule(u'COMPSTMT', u'')
ctx.rule(u'COMPSTMT', u'')
ctx.rule(u'COMPSTMT', u'')
ctx.rule(u'COMPSTMT', u'')

ctx.rule(u'STMT', u'undef {FNAME}')
ctx.rule(u'STMT', u'')
ctx.rule(u'STMT', u'')
ctx.rule(u'STMT', u'')
ctx.rule(u'STMT', u'')

ctx.rule(u'FNAME', u'{IDENTIFIER}')
ctx.rule(u'FNAME', u'..')
ctx.rule(u'FNAME', u'|')
ctx.rule(u'FNAME', u'^')
ctx.rule(u'FNAME', u'&')
ctx.rule(u'FNAME', u'<=>')
ctx.rule(u'FNAME', u'==')
ctx.rule(u'FNAME', u'===')
ctx.rule(u'FNAME', u'=~')
ctx.rule(u'FNAME', u'>')
ctx.rule(u'FNAME', u'>=')
ctx.rule(u'FNAME', u'<')
ctx.rule(u'FNAME', u'<=')
ctx.rule(u'FNAME', u'+')
ctx.rule(u'FNAME', u'-')
ctx.rule(u'FNAME', u'*')
ctx.rule(u'FNAME', u'/')
ctx.rule(u'FNAME', u'%')
ctx.rule(u'FNAME', u'**')
ctx.rule(u'FNAME', u'<<')
ctx.rule(u'FNAME', u'>>')
ctx.rule(u'FNAME', u'~')
ctx.rule(u'FNAME', u'+@')
ctx.rule(u'FNAME', u'-@')
ctx.rule(u'FNAME', u'[]')
ctx.rule(u'FNAME', u'[]=')


ctx.rule(u'CHARS', u'{CHAR}{CHARS}')
ctx.rule(u'CHARS', u'')

ctx.rule(u'IDENTIFIER', u'{CHAR}{CHARS}')

ctx.rule(u'CHAR', u'{LETTER}')

ctx.rule(u'NUMERIC',u'{DIGIT}{NUMERIC}')
ctx.rule(u'NUMERIC',u'{DIGIT}')

ctx.rule(u'DIGIT',u'0')
ctx.rule(u'DIGIT',u'1')
ctx.rule(u'DIGIT',u'2')
ctx.rule(u'DIGIT',u'3')
ctx.rule(u'DIGIT',u'4')
ctx.rule(u'DIGIT',u'5')
ctx.rule(u'DIGIT',u'6')
ctx.rule(u'DIGIT',u'7')
ctx.rule(u'DIGIT',u'8')
ctx.rule(u'DIGIT',u'9')

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