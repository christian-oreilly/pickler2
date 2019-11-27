import functools
import pickle
from pathlib import Path
from warnings import warn
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


config_path = Path.home() / ".pickler_conf.yaml"


def register_project_path(project_name, pickling_path):
    config = load_config()

    Path(pickling_path).mkdir(parents=True, exist_ok=True)
    config[project_name] = str(pickling_path)

    with config_path.open("w") as stream:
        dump(config, stream, Dumper=Dumper)


def load_config():
    if config_path.exists():
        with config_path.open("r") as stream:
            return load(stream, Loader=Loader)
    return {}


def pickled(file_name, run=None, load=None, project_name=None):
    def pickler_decorator(func):
        @functools.wraps(func)
        def wrapper(file_name, *args, run=run, load=load, project_name=project_name, **kwargs):

            if project_name is not None:
                config = load_config()
                if project_name not in config:
                    raise ValueError("This project is unknown. Please register it first using " +
                                     "register_project_path(project_name, pickling_path).")

                pickling_path = Path(config[project_name])
            else:
                pickling_path = None

            if isinstance(file_name, str):
                file_name = Path(file_name)
            elif not isinstance(file_name, Path):
                raise TypeError("Unrecognized type ({}).".format(type(file_name)))

            if not file_name.is_absolute():
                if pickling_path is not None:
                    file_name = pickling_path / file_name
            else:
                if pickling_path is not None:
                    warn("The file_name passed is absolute. The project pickling path has been ignored.")

            if run or not file_name.exists():
                data = func(*args, **kwargs)
                with file_name.open("wb") as pickle_stream:
                    pickle.dump(data, pickle_stream)
                return data

            with file_name.open("rb") as pickle_stream:
                return pickle.load(pickle_stream)

        return functools.partial(wrapper, file_name)
    return pickler_decorator
