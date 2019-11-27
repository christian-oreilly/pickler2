from pathlib import Path
from pickler2 import pickled, register_project_path


def test_pickler(project_name=None, pickling_path=None):

    if project_name is not None:
        register_project_path(project_name, pickling_path)

    file_name = Path("test_pickler.pck")
    if pickling_path is None:
        if file_name.exists():
            file_name.unlink()
    else:
        if (Path(pickling_path) / file_name).exists():
            (Path(pickling_path) / file_name).unlink()

    @pickled(file_name, project_name=project_name)
    def dummy_func1():
        return 1

    dummy_func1()
    if pickling_path is None:
        assert(file_name.exists())
    else:
        assert((Path(pickling_path) / file_name).exists())

    @pickled(file_name, project_name=project_name)
    def dummy_func2():
        return 2

    assert(dummy_func2() == 1)

    dummy_func2(run=True)
    assert(dummy_func2() == 2)


def test_pickler_with_registration():
    test_pickler("test_project", str(Path(__file__).parent / "test"))
