
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="MYAPP",
    settings_files=['app/config/default_settings.yaml'],
    merge_enabled=True,
)
