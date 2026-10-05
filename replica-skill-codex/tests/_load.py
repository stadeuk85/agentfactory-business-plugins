"""Load a script from a bundled Replica skill folder."""

import importlib.util
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_ROOT = os.path.join(ROOT, "skills")


def load(folder, name):
    path = os.path.join(SKILLS_ROOT, folder, name + ".py")
    spec = importlib.util.spec_from_file_location("replica_" + name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod
