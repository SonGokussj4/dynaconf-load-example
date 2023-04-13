# dynaconf-load-example

Example for loading additional settings with Dynaconf after runtime

## Description

This is a simple example for loading additional settings with Dynaconf after runtime.

## Usage

```bash
# On Windows - Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# Install Dynaconf
python -m pip install dynaconf

# Run the example
python main.py
```

## Project structure

```bash
.
├── README.md
├── app
│   ├── __init__.py
│   ├── app.py
│   └── config
│       ├── __init__.py
│       ├── default_settings.yaml
│       └── dynaconfig.py
├── custom_settings.yaml
└── main.py
```

## The idea

* Run app with `app/config/default_settings.yaml`
* Parse some argument or anything to update settings with `custom_settings.yaml`
* Current `settings.name` value should be `custom name` instead of `default name`
