# Sofia2

> The improved *home assistant*

![Code Size](https://img.shields.io/github/languages/code-size/markovejnovic/sofia2?style=flat-square)
![Language](https://img.shields.io/github/languages/top/markovejnovic/sofia2?style=flat-square)
![Issues](https://img.shields.io/github/issues/markovejnovic/sofia2?style=flat-square)
![License](https://img.shields.io/github/license/markovejnovic/sofia2?style=flat-square)

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Contributing](#contributing)
- [Support](#support)
- [License](#license)
- [Thank you](#thank-you)

## Features

Sofia2 is an improvement on the clunky
[sofia](https://www.github.com/markovejnovic/sofia) software that aimed to
provide an open source unified, simple and modular smart home system.

Sofia2 enables you to use:
* ~~Pre-existing device types (Lights, Speakers, Sensors)~~
* Custom devices that you can easily implement and register based on the base
classes the _Sofia2_ API exposes.
* ~~Devices which control each other independent of user interaction (eg. a
thermometer controlling a heater).~~
* ~~Various views such as a `REST` API, Web Interface, etc.~~
* ~~The ability to make custom view classes reusing the existing code.~~

## Requirements

The only major requirement `sofia2` has is `python >3.6`.

## Installation

### Cloning

First clone the repository:
```bash
git clone https://github.com/markovejnovic/sofia2.git && cd sofia2
```

### Virtualenv

After fetching `python`, `pip` and `virtualenv`, I'd advise you to create a
virtual environment in which Sofia2's dependencies will be installed:
```bash
virtualenv3 venv
. venv/bin/activate # Only for bash (Probably this one if you're not sure)
```

### Dependencies

You can fetch most of the dependencies on *PyPI*, just run:
```bash
pip install -r requirements.txt
```

## Contributing

Currently `sofia2` does not have contributing guidelines.

## Support

If you have a question that you need answered, make an issue here on GitHub and
we'll get back to you as soon as possible.

## License

This software is licensed under the GPLv3 license.

## Thank you
- Thank you [fvcproductions](https://github.com/fvcproductions/) for your
  [README.md](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
  guide.
