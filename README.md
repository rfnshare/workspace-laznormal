[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
<!-- PROJECT LOGO -->

<br />
<p align="center">
  <a href="https://github.com/rfnshare/workspace-laznormal">
    <img src="Daraz-Emblem.png" alt="Logo" height="100">
  </a>

  <h3 align="center">App Automation</h3>

  <p align="center">
    ...
    <br />
    <a href="#"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#">View Demo</a>
    ·
    <a href="https://github.com/rfnshare/workspace-laznormal/issues">Report Bug</a>
    ·
    <a href="#">Request Feature</a>
  </p>
Introduction

This is an appium based framework that interacts with Daraz Android App and can be used to automate given below

1. Login Into App
2. **Change App Build status to Online/Stage**

# Setup

1. Clone this repository
    ```
    git clone https://github.com/rfnshare/workspace-laznormal.git
    ```

2. If you clone this repository before then run this on the project's root directory
    ```
    git pull
    ```
3. Copy APK file, create a folder name apk in project root directory & paste it in project apk folder.
    ```
    apk/appname.apk
    ```
   Make sure you connect you android device/emulator & set uid in TestCase/base_test.py.
4. Go to the project's root directory and install requirements(Recommended create virtual env first).
    ```
    pip install -r requirements.txt
    ```
   
5. For App Status Change, Run this script.
    ```
    python -m unittest TestCase.test_changeStatus

    ```
   This will open a app in the android device & Change the app build status.

6. For Login Run this script.
    ```
    python -m unittest TestCase.test_login

    ```
   This will open a app in the android device & login into Daraz.

7. Generate HTML reports with run script include log.
    ```
    Will add later

    ```
   This will create an HTML/allure report. You can find report in project's root directory

### Usage


For more examples,  please refer to the [Documentation](https://example.com)

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/rfnshare/workspace-laznormal/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/Feature`)
3. Commit your Changes (`git commit -m 'Add some Feature'`)
4. Push to the Branch (`git push origin feature/Feature`)
5. Open a Pull Request

<!-- CONTACT -->
## Contact

Abdullah Al Faroque - [@rfnshare](https://twitter.com/rfnshare) - aalfaroque@gmail.com

Project Link: [Android Automation](https://github.com/rfnshare/workspace-laznormal.git)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/badge/contributors-0-yellow?style=for-the-badge
[contributors-url]: https://github.com/rfnshare/workspace-laznormal/graphs/contributors
[forks-shield]: https://img.shields.io/badge/froks-0-blue?style=for-the-badge
[forks-url]: https://github.com/rfnshare/workspace-laznormal/network/members
[stars-shield]: https://img.shields.io/badge/stars-0-red?style=for-the-badge
[stars-url]: https://github.com/rfnshare/workspace-laznormal/stargazers
[issues-shield]: https://img.shields.io/badge/issues-0-success?style=for-the-badge
[issues-url]: https://github.com/rfnshare/workspace-laznormal/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/rfnshare
