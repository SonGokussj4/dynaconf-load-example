import os

from app.config.dynaconfig import settings


def main():
    if settings.name == "default name":
        print("[ OK ] settings.name is 'default name'")

    # Load custom settings - Should override default settings
    print()
    print(f"[ INFO ] Check file exists: ./custom_settings.yaml ... {os.path.exists('./custom_settings.yaml')}")
    settings.load_file(path="./custom_settings.yaml")
    print("[ INFO ] Loaded ./custom_settings.yaml")
    print(f"[ INFO ] --> settings.name: '{settings.name}' (should be 'custom name')")

    # Load custom settings (second try) - Should override default settings
    print()
    print(f"[ INFO ] Check file exists: ../../custom_settings.yaml ... {os.path.exists('../../custom_settings.yaml')}")
    settings.load_file(path="../../custom_settings.yaml")
    print("[ INFO ] Loaded ../../custom_settings.yaml")
    print(f"[ INFO ] --> settings.name: '{settings.name}' (should be 'custom name')")

    print()
    if settings.name == "custom name":
        print("[ OK ] settings.name is 'custom name'")
    else:
        print("[ PROBLEM ] settings.name is not 'custom name'")

    print(settings.to_dict())


if __name__ == "__main__":
    main()
