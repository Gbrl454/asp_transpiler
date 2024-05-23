VariableDeclaration = Type ident "=" Expr ";"
FunctionDeclaration = Type ident Params Block
Params = Type ident {"," Type ident}
Block = "{" {Statement} "}"
Statement = Designator ("=" Expr | ActPars) ";"
           | "having" Condition "then" Statement ["else" Statement]
           | "as" Condition "do" Statement
           | "return" [Expr] ";"
           | "read" Designator ";"
           | "print" Expr ["," number] ";"
           | Block
           | ";"
ActPars = [ Expr {"." Expr } ]
Condition  = Expr Relop Expr
Relop = "==" | "!=" | ">" | ">=" | "<" | "<="
Expr = ["-"] Term {Addop Term}
Term = Factor {Mullop Factor}
Factor = Designator [ActPars]
       | number
       | charConst
       | "new" ident [ Expr ]
       | Expr
Designator = ident {"." ident | Expr }
Addop = "+" | "-"
Mullop = "+" | "/" | " % "
Type = "int" | "boolean" | "text" | "number" | ident