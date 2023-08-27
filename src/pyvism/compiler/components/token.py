import dataclasses
import enum

from pyvism.compiler.interface import IToken


# [FLU]: reserved For Later Use


class TokenType(enum.IntEnum):
    COMMENT = enum.auto()  # ** This is a comment **

    # *- Type literal constructors -* #
    INTEGER = enum.auto()  # 123
    REAL = enum.auto()  # 0.1234
    STRING = enum.auto()  # "my string"
    BYTESTRING = enum.auto()  # 'my bytes'

    # *- Constant literals -* #
    TRUE = enum.auto()  # TRUE
    FALSE = enum.auto()  # FALSE
    NIL = enum.auto()  # NIL
    STDOUT = enum.auto()  # STDOUT
    STDERR = enum.auto()  # STDERR
    STDIN = enum.auto()  # STDIN

    # *- Punctuation -* #
    DOT = enum.auto()  # . [FLU]
    COLON = enum.auto()  # :
    SEMICOLON = enum.auto()  # ;
    COMMA = enum.auto()  # ,
    SIGIL = enum.auto()  # $ [FLU]
    EQUAL = enum.auto()  # =
    ARROW = enum.auto()  # =>

    # *- Pairs -* #
    LEFT_PAREN = enum.auto()  # (
    RIGHT_PAREN = enum.auto()  # )
    LEFT_BRACK = enum.auto()  # [
    RIGHT_BRACK = enum.auto()  # ]
    LEFT_BRACE = enum.auto()  # {
    RIGHT_BRACE = enum.auto()  # }
    VERT_BAR = enum.auto()  # |

    # *- Special -* #
    IDENTIFIER = enum.auto()  # @alice, @var_3
    OPERATOR = enum.auto()  # +, /, print
    TYPE = enum.auto()  # Int

    # Emitted once at the end of the token stream
    EOF = enum.auto()


@dataclasses.dataclass(slots=True)
class Token(IToken[TokenType]):
    type: TokenType
    start: int
    end: int
    line_no: int
    lexeme: str
