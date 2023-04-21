# Developer Note
This package was carried out in a very short time (within 7 days) from the idea to the pre-alpha version to documentation and simple QA testing by myself. Therefore, rather than sufficiently clean code, I tried to implement functions and create an initial interface. Therefore, I appreciate your contributions at any time.

###### Since all API keys and URLs generated during the test phase are destroyed, all URLs and APIs in legacy code cannot be used.

## Dependencies
This package communicates using the REST API or WEBHOOK URL of mobile messengers and applications. It inevitably depends on the interface and API policy of each application. To maintain a simple structure and flexibility, configure methods to communicate with each application in the base folder of ExceptNotifier. If an application's API policy or interface changes, ExceptNotifier will be addressed by updating the major version.

<br>

## Consideration of PDB Adoption
PDB was considered for implementation, but it was excluded to avoid complex dependencies and maintain a clean, extensible package structure focused on the notification function.

<br>

## Debug Information using OPEN AI API
Although it is a redundant feature, a separate class containing openAI debugging information is created to avoid double inheritance. This approach ensures the package is not dependent on the OpenAI API interface and prevents unnecessary code lines from increasing.

<br>

## Refactoring and Optimization
This package may contain unnecessary redundant declarations and local variables (or global variables, depending on the situation). These measures were implemented to avoid unnecessary double inheritance and prevent the package structure from becoming complicated. Additionally, since this package primarily focuses on notifications, millisecond time improvements are not required. Further refactoring will occur after the interface is fully established. This will be implemented after the development stage has matured into the product development stage following beta testing.

<br>

## Regarding other emails
The ExceptNotifier offers Gmail as the primary email service. Due to varying communication methods and detailed interfaces with ***TP servers, it's challenging to accommodate all email*** TP servers. It's also less effective as using other applications is slightly more useful. Furthermore, connecting with Gmail requires more preset variables compared to other classes. As a result, only Gmail is supported, and additional email server support will be implemented upon request. If a new email class function is required, it will be developed once the issue page has received over 50 consent votes. This requirement is immutable and mandatory.

<br>

## Variable and Class naming
In principle, all variable and class names are intuitive, and I keep them easy to refactor until major version 1. Various decorators and package structures are discussed after development stage 5 or higher.
This principle is so that different people can easily refactor, contribute, and react quickly to interface changes in different applications. However, while maintaining these principles, if you have any good ideas, please feel free to suggest them.

In this class, I inherit from Python's exceptionBase and override the excepthook method to create a custom exception handler. To avoid using args, double inheritance, or complicating the structure, I define and use internal variables (declaring them as global variables if necessary). 

Typically, in Python, variable names are mangled by adding a double underscore prefix (__). However, in this case, I chose to use capital letters for internal variables to emphasize their constant-like usage. If you have suggestions for improving class names, method names, or variable names, please feel free to contribute.
##### In this package, a variable name prefixed with an _ signifies that it is used only within a function. Naming focused on function rather than mangling. If a particular method is only used within a class, it is used as the _method name.


<br>

## Python and IPython
I tried to keep the same structure for both Python and Ipython, but I noticed that the behavior of traceback and ExceptBase is slightly different. Significant development has already been carried out with a focus on operation in Python, and it was confirmed that some of the return values ​​are different because IPython's traceback message inevitably includes information about the cell. So we construct a new class to override in IPython. A brush that can be integrated for this

<br>

## Naming in IPython Functions
The ExceptNotifier functions in IPython follow the class naming conventions. This is done to override custom exceptions in IPython and minimize confusion for users. Therefore, unlike Python, it doesn't matter what goes into the except clause, but it's important to remember that the except statement must always contain a raise.


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


## QA Note
QA tests are carried out from Python 3.6 to Python 3.9 environments through Windows, MacBook m1, and Google Colab, focusing on Telegram, Discord, Slack, Line, and Chime applications. QA for the rest proceeds whenever there is a request or whenever I have time to spare, and replaces it with responding to bug reports. After the QA test is conducted, we plan to raise the development stage and recruit QA testers by promoting it.

<br>

## Thanks To
- Thanks to [Myunghak Lee](https://github.com/myeonghak) for providing great ideas on providing debugging information through OpenAI API.

<br>