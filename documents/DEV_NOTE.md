# Developer Note
## Dependencies
This package communicates using the REST API or WEBHOOK URL of mobile messengers and applications. It inevitably depends on the interface and API policy of each application. To maintain a simple structure and flexibility, configure methods to communicate with each application in the base folder of ExceptNotifier. If an application's API policy or interface changes, it will be addressed by updating the major version.

## Consideration of PDB Adoption
PDB was considered for implementation, but it was excluded to avoid complex dependencies and maintain a clean, extensible package structure focused on the notification function.

## Debug Information using OPEN AI API
Although it is a redundant feature, a separate class containing openAI debugging information is created to avoid double inheritance. This approach ensures the package is not dependent on the OpenAI API interface and prevents unnecessary code lines from increasing.

## Refactoring and Optimization
This package may contain unnecessary redundant declarations and local variables (or global variables, depending on the situation). These measures were implemented to avoid unnecessary double inheritance and prevent the package structure from becoming complicated. Additionally, since this package primarily focuses on notifications, millisecond time improvements are not required. Further refactoring will occur after the interface is fully established. This will be implemented after the development stage has matured into the product development stage following beta testing.

# Release note
|Version|Description|
|:--|:--|
|0.1.1|Package blueprint|
|0.1.2|Package Structure testing|
|0.1.3|Proceed with the first commit by working with scalable messengers or e-mails with high usage. All 0.1.x versions are pre-alpha versions and are used for debugging and usability improvement.|