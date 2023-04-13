from app.config.dynaconfig import settings

def main():

    if settings.name == "default name":
        print("[ OK ] settings.name is 'default name'")

    # Load custom settings - Should override default settings
    settings.load_file(path="./custom_settings.yaml")

    if settings.name == "custom name":
        print("[ OK ] settings.name is 'custom name'")
    else:
        print("[ PROBLEM ] settings.name is not 'custom name'")

    print(settings.to_dict())

if __name__ == "__main__":
    main()
