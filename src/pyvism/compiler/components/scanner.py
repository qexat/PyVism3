# pyright: reportImplicitOverride = false

import dataclasses
from pyvism.compiler.components.diagnostic import Error

from pyvism.compiler.components.token import Token
from pyvism.compiler.components.token import TokenType
from pyvism.compiler.interface import IDatabase
from pyvism.compiler.interface import IScanner


@dataclasses.dataclass(slots=True)
class Scanner(IScanner[TokenType]):
    def is_at_end(self, offset: int = 0) -> bool:
        return self.current + offset >= len(self.source)

    def peek(self, offset: int = 0) -> str:
        if self.is_at_end(offset):
            return "\0"
        return self.source[self.current + offset]

    def advance(self, steps: int = 1) -> None:
        self.current += steps

    def consume(self) -> str:
        char = self.peek()
        self.advance()

        return char

    def matches(self, expected: str) -> bool:
        return self.peek() == expected

    def make_token(self, token_type: TokenType) -> None:
        lexeme = self.source[self.start : self.current]
        token = Token(token_type, self.start, self.current, self.line_no, lexeme)
        self.tokens.append(token)

    def make_error(self, id: int) -> None:
        # error = <retreive_error_by_id(id)>
        error = Error(self.__class__, id, "<summary>")
        self.errors.append(error)

    def scan_token(self) -> None:
        char = self.consume()

        match char:
            # Groupings, tuples
            case "(":
                self.make_token(TokenType.LEFT_PAREN)
            case ")":
                self.make_token(TokenType.RIGHT_PAREN)
            # Lists, indexes
            case "[":
                self.make_token(TokenType.LEFT_BRACK)
            case "]":
                self.make_token(TokenType.RIGHT_BRACK)
            # Sets
            case "{":
                self.make_token(TokenType.LEFT_BRACE)
            case "}":
                self.make_token(TokenType.RIGHT_BRACE)
            # Mappings
            case "|":
                self.make_token(TokenType.VERT_BAR)
            # [FLU]
            case ".":
                self.make_token(TokenType.DOT)
            # Type hints
            case ":":
                self.make_token(TokenType.COLON)
            # Statement separator
            case ";":
                self.make_token(TokenType.SEMICOLON)
            # Expression separator
            case ",":
                self.make_token(TokenType.COMMA)
            # [FLU]
            case "$":
                self.make_token(TokenType.SIGIL)
            # Assignement
            case "=":
                # advance only if next char is ">"
                self.advance(is_arrow := self.matches(">"))
                token_type = TokenType.ARROW if is_arrow else TokenType.EQUAL
                self.make_token(token_type)
            case _:
                pass  # REPORT ERROR

    def run(self, database: IDatabase[TokenType]) -> None:
        self.source = database.source.read()

        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.make_token(TokenType.EOF)
        self.push_to_database(database)

    def push_to_database(self, database: IDatabase[TokenType]) -> None:
        database.tokens.extend(self.tokens)
        database.errors.extend(self.errors)
