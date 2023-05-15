# Developer Note
This package was carried out in a very short time (within 7 days) from the idea to the pre-alpha version to documentation and simple QA testing by myself. Therefore, rather than sufficiently clean code, I tried to implement functions and create an initial interface. Therefore, I appreciate your contributions at any time.
- Related blog post: https://dsdanielpark.github.io/package/2023-04-26-about_except_notifier.html

###### Since all API keys and URLs generated during the test phase are destroyed, all URLs and APIs in legacy code cannot be used.

## Applying ExceptNotifier in Python
In Python, I utilize [`sys.excepthook`](https://docs.python.org/ko/3/library/sys.html#sys.excepthook) to invoke the `ExceptNotifier` when an exception arises. The interpreter passes three arguments to `sys.excepthook`: exception class, exception instance, and traceback object. `ExceptNotifier` is a class inheriting from `BaseException`, and it overrides `sys.excepthook` as the top-level exception handler, which is executed right before the system terminates. To handle unraisable exceptions or exceptions occurring in threads, refer to the `sys.unraisablehook()` and `threading.excepthook()` functions, respectively.

## Application of ExceptNotifier in iPython
Strictly, IPython is not a programming language like Python, but a package. To clarify, IPython (Interactive Python) is a package consisting of a command shell for interactive computing across multiple programming languages.

It's a useful package that enables compiling Python code bit by bit in an interactive session through the concept of an interactive shell. However, in IPython, control by `sys.excepthook` occurs just before the prompt is returned, making it impossible to receive a traceback object using `sys.excepthook` and send error messages to messenger apps. Moreover, since it's necessary to inherit from `BaseException`, other functions in IPython also need to be overridden.

Therefore, at first, I considered the [magics](https://ipython.readthedocs.io/en/stable/interactive/magics.html) in cell, but the problem of having to import the magic function every time in the cell can be cumbersome to use, so I decided to use the [`set_custom_exc`](https://ipython.readthedocs.io/en/stable/api/generated/IPython.core.interactiveshell.html) in iPython, which can work even by overriding it once. The `set_custom_exc` allows you to set a custom exception handler that is called when an exception in the exc_tuple occurs in the main loop (especially the run_code() method), and is designed so that the handle can return a structured traceback or None. Therefore, I can receive the traceback and send it to each messenger app. Unlike `sys.excepthook`, the order of top-level exception handling in iPython is different, so just calling raise in the except statement can work properly.

## Using Environment Variables (environ)
 In Python's `except` statement, it was designed to inherit `ExceptionBase`. To pass variables into the class, I decided to use `os.environ` for setting variables and distributing them as a package. As the user's webhook URL or API key won't change, I named the variables in uppercase and gave them unique names to avoid conflicts. To indicate that the variables are used within the class, I added an underscore before the variable name.

## Dependencies
This package communicates using the REST API or WEBHOOK URL of mobile messengers and applications. It inevitably depends on the interface and API policy of each application. To maintain a simple structure and flexibility, configure methods to communicate with each application in the base folder of ExceptNotifier. If an application's API policy or interface changes, ExceptNotifier will be addressed by updating the major version.

## Consideration of PDB Adoption
PDB was considered for implementation, but it was excluded to avoid complex dependencies and maintain a clean, extensible package structure focused on the notification function.

## Debug Information using OPEN AI API
Although it is a redundant feature, a separate class containing openAI debugging information is created to avoid double inheritance. This approach ensures the package is not dependent on the OpenAI API interface and prevents unnecessary code lines from increasing.

## Refactoring and Optimization
This package may contain unnecessary redundant declarations and local variables (or global variables, depending on the situation). These measures were implemented to avoid unnecessary double inheritance and prevent the package structure from becoming complicated. Additionally, since this package primarily focuses on notifications, millisecond time improvements are not required. Further refactoring will occur after the interface is fully established. This will be implemented after the development stage has matured into the product development stage following beta testing.

## Regarding other emails
The ExceptNotifier offers Gmail as the primary email service. Due to varying communication methods and detailed interfaces with ***TP servers, it's challenging to accommodate all email*** TP servers. It's also less effective as using other applications is slightly more useful. Furthermore, connecting with Gmail requires more preset variables compared to other classes. As a result, only Gmail is supported, and additional email server support will be implemented upon request. If a new email class function is required, it will be developed once the issue page has received over 50 consent votes. This requirement is immutable and mandatory.

## Variable and Class naming
In principle, all variable and class names are intuitive, and I keep them easy to refactor until major version 1. Various decorators and package structures are discussed after development stage 5 or higher.
This principle is so that different people can easily refactor, contribute, and react quickly to interface changes in different applications. However, while maintaining these principles, if you have any good ideas, please feel free to suggest them.

In this class, I inherit from Python's exceptionBase and override the excepthook method to create a custom exception handler. To avoid using args, double inheritance, or complicating the structure, I define and use internal variables (declaring them as global variables if necessary). 

Typically, in Python, variable names are mangled by adding a double underscore prefix (__). However, in this case, I chose to use capital letters for internal variables to emphasize their constant-like usage. If you have suggestions for improving class names, method names, or variable names, please feel free to contribute.
##### In this package, a variable name prefixed with an _ signifies that it is used only within a function. Naming focused on function rather than mangling. If a particular method is only used within a class, it is used as the _method name.

## Python and IPython
I tried to keep the same structure for both Python and Ipython, but I noticed that the behavior of traceback and ExceptBase is slightly different. Significant development has already been carried out with a focus on operation in Python, and it was confirmed that some of the return values ​​are different because IPython's traceback message inevitably includes information about the cell. So I construct a new class to override in IPython. A brush that can be integrated for this

## Naming in IPython Functions
The ExceptNotifier functions in IPython follow the class naming conventions. This is done to override custom exceptions in IPython and minimize confusion for users. Therefore, unlike Python, it doesn't matter what goes into the except clause, but it's important to remember that the except statement must always contain a raise.

## About whether the next shell can be executed after sending an except message in ipython with exceptnotifier
In conclusion, it can't work like that. As mentioned several times above, the order of error handling in Ipython is very different. Therefore, it can be quite difficult to create a new structure by inheriting BaseException because the interfaces enforced by Ipython and Python are different. Therefore, it is currently recommended to use only one shell as a try-except statement.

## Doc string style
Applies to the original Sphinx documentation without using the Google Python Style Guide. This is a measure for automatic documentation generation, and was taken because the structure of the package is simple.

## About sub package
Although it can be used without specifying it as a sub package, submodules can function even if they are distributed as individual packages, so define submodules as subpackages with the possibility of future interface changes or distribution of subpackages in mind. In addition, class and function names have been adjusted to avoid confusion in function names in Python and IPython, but they are separated into subpackages for clearer object-oriented programming. This is a temporary measure and may change as development progresses.

## Documentation 
As mentioned above, ExceptNotifier seems to have a complex structure to support various applications, but in reality, it aims for a very simple package structure. Since the package structure was designed like that from the beginning, and usage is simple, Sphinx documentation also performs minimal documentation. Also, since this should be automated by workflow, etc., more complicated documentation will be done through markdown files or blog posts.

## Refactoring
In upcoming updates, I aim to enhance the pylint score, eliminate superfluous inheritance, streamline module imports, reduce redundant function calls, boost efficiency via cProfile, and restructure the package based on use cases. However, performing QA for all applications is a time-consuming process. As a result, I plan to initiate refactoring with the alpha release and complete it by the beta release.

## Release note
|Version|Description|
|:--|:--|
|0.1.1|Package blueprint|
|0.1.2|Started working on scalable messengers or e-mails with high usage. All 0.1.x versions are pre-alpha and primarily used for debugging and improving usability without the OpenAI API.|
|0.1.3|Fixed the package structure.|
|0.1.4|Checked the version range of Python and other dependencies.|
|0.1.5|Connected OpenAI's API through try-except. If you enter two arguments, debugging information by AI is automatically sent.|
|0.1.6|Released for QA testing on Windows and Mac.|
|0.1.8|Synced the version of pypin with conda-forge.|
|0.1.9|Alpha version released.|
|0.1.10|Debugging for WeChat.|
|0.1.11, 0.1.12, 0.1.13|Using Os.environ.|
|0.1.14|Fixed the issue with winsound when importing on Linux.|
|0.1.15|Fixed an os import typo.|
|0.1.16|Fixed winsound in a static method when importing on Linux.|
|0.1.17|Fixed some typos and added small unit tests. It still malfunctions in notebooks, but the Python file is functional.|
|0.1.18|For implementation in IPython, the package structure is separated into py and ipy. Adds a function for telegram in ipython as a test.|
|0.1.19|Adds a function for every applications in ipython.|
|0.1.20|Delete offset arguments in ipython.|
|0.1.21|Delete offset arguments in Slackipython.|
|0.1.22|Revert for fixing offset argument.|
|0.2.0|Pre Alpha Release in 230422. git tag released.|
|0.2.1|Package import error fixed.|
|0.2.2|Discord api text length limit 1900 (actual text length limit is 2000).|
|0.2.3|Reduced unnecessary calls by clarifying module imports and reduced flops using if statements. Fix in EmailNotifierIpython sending dict|
|0.2.4|Fix in EmailNotifierIpython open ai sending dict|
|0.2.5| I've eliminated unnecessary error messages resulting from a missing API key and integrated the bardapi package to enable all packages to receive hints about code errors from Google BARD. No additional QA has been performed for the bardapi package. As unforeseen features emerge, refactoring efforts might be required. Although time constraints prevent me from addressing this now, I'll prioritize refactoring and enhancing code efficiency as soon as possible. To improve readability, as some applications preview the ExceptNotifier Github address poorly, I've removed `http://` from the official Github address.|
|0.2.6| Google Bard officially supports Korean, so you can set the language of Bard Advice to Korean. Additionally, if `_BARD_ADVICE_LANG` is set to korean, debugging hints for code in Korean are provided. Also you can use 'japanese'|
|0.2.7| Fix bard advice function. you can customize your prompt by setting `_PROMPT_COMMAND` |
|0.2.8| Update requirement pacakge `bardapi` |
|0.2.9| Fix without `_BARD_ADVICE_LANG` |
|0.2.10| Update customize prompt in Open AI chatbot |
|0.2.11| Fix check system variable of `_BARD_ADVICE_LANG` and modify some prompt. |

Need Refactoring, QA.

## QA Note
QA tests are carried out from Python 3.6 to Python 3.9 environments through Windows, MacBook m1, and Google Colab, focusing on Telegram, Discord, Slack, Line, and Chime applications. QA for the rest proceeds whenever there is a request or whenever I have time to spare, and replaces it with responding to bug reports. After the QA test is conducted, I plan to raise the development stage and recruit QA testers by promoting it.

## Thanks To
- Thanks to [Myunghak Lee](https://github.com/myeonghak) for providing great ideas on providing debugging information through OpenAI API.
