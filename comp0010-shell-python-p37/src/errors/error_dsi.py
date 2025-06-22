"""Contains an error class with an impossible case"""
# pylint: disable=too-few-public-methods

from functools import wraps
from typing import Any, Callable

from .errors import BaseShellError


def check_arguments(fn: Callable[..., Any]) -> Callable[..., Any]:
    """
    Ensure that arguments passed to "fn" are non-null.

    Raises:
        DeveloperSkillIssue: If any of the parameters are not supported by
                             the command
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if any(arg is None for arg in args) or any(
                val is None for val in kwargs.values()):
            raise DeveloperSkillIssue('One or more arguments are None')
        return fn(*args, **kwargs)
    return wrapper


class DeveloperSkillIssue(BaseShellError):
    """
    Represents an "impossible case"; should only be used when
    something is truly impossible
    """

    CLUELESS = """
                            .,,,*****/#&@@@@@@@@@@@@@@@&#/*,*,,,
                      ///(&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&(*
                ,(#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%##%%#/,,*,*#@@@@@@@%(*
            ./#@@@@@@&#(#&@@@@@@@&%%%(*,....,/%@@@@@@@@@@@@@@@&&&%&@@@@@@@&&&&%#,
        ,#@@@@@@@%#*.,(&@@@@@#*.                       ,(##%&@@@@@@@@@@@@@@@@@@&/
      /%@@@@&(*.   *#&@@@&(/,.,///////////,.             ,(&@@@@@@@@@@@@@@@@@@@%/
   .(&@@@&#,    .(&@@@@%*,(@@@@@@@@@@@@@@@@@&(.       ,*%@@@@@@@@@&&@@@@@@@@@@@@@&(,
  ,%@@@%*.   .*%&@@@@@@@@@@@@@@@@@%*..,*/#&@@@#.  .,#&@@@&#/(@@@@@&&&@@@&/,/%@@@@@@@%/
  /&@@&/  .*(&@@@@@@@@@@@@@@@@@&%*.      *#@@@#,  ,#@@@@%*.   .*%@@@@@@%/,   ./@@@@@@@@#,
 *&@@@(. /&@@@@@@@@@@@&(/******, ...,/#&@@@@@#*   .*#@@@@@&##(, .        ...*(%@@@@@@@@@@(.
 *&@@@*   .,,.   ,(&@@@@&%%%%%%%&@@@@@@@@%(*.        .,(%&@@@@@@@@@@@@@@@@@@@@@@@#*,*(&@@@#,
 ,%@@@*              *%@@@@@@@@@@@&%#(,.                  .,/#################*.      /&@@@(
(%@@@&*                                                                                (@@@@#.
(%@@&,             ./(/,                                                               .(@@@&(,
(%@@&,             (@@&#*                                                  .,,,,,,,,,,,../%@@@&(.
(%@@&,             *%@@@@%(//*.                                    .**/(%@@@@@@@@@@@@@@@#,,#@@@&*
(%@@@(,              ,#&@@@@@@@&%#((((((((((((((((((((((((((#&@@@@@@@@@@@@@&#///////(%@@@(.*&@@&#.
./&@@@%*               ./%&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&#/*,,.    .*#%&&@@@&/ ./&@@&*
  *%@@@(.                                             .                       ,(@@@@@@%*    ,&@@@(.
  .(@@@@#,                                                                   /&@@@%(,       .(&@@@(
    *&@@@%*                                                                  /&@@%,          ,%@@@&/
     .%@@@&/.                                                                /&@@%,           ,#@@@/
      ,#@@@@(.                                                               /@@@%,           ,%@@@/
       .(@@@@&(,                                                             (@@@%,           ,%@@@/
         ./&@@@&/.                                                         ,(&@@@#.         ./%@@@&*
           ,#&@@@(.                                                       .(@@@@(.          ,&@@@%*
            .(@@@@&#,                         .(&@@&(.                   *%@@@@#           ,(@@@&*
             .*(&@@@%/.                       ./%@@@@@@%/.             ./&@@@%,           /&@@@&/.
                ,#@@@@&(,                        .*#&@@@@@@#*.....,*#&&@@@@&(,          .(&@@@#.
                  ./%@@@@%*                          .*#&@@@@@@@@@@@@@@@&#*          .,#@@@@@(.
                     ,#@@@@&(,                            .*(((((((((*,.            ,#@@@@&(
                      ./%@@@@@@&#/,.                                             ,/%&@@@&/
                          .%#@@@@@@@&%#/,..                                  ,/%&@@@@&%*
                               ,,(%&@@@@@@@&&%//*/*.                   ,*/#&@@@@@&%/,
                                    .,//(%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#*
                                           .,****/#%&&&&&&&&&&&&&&&&&&&%/,*,.
    """  # noqa: E501
    # The lint for line too long is disabled because otherwise the above
    # masterpiece will not look good

    def __str__(self) -> str:
        return (f'{DeveloperSkillIssue.CLUELESS}\nEncountering this error '
                'means the developer has messed something up. Here is what '
                f'happened: {self.message}')
