import os
from pathlib import Path
from copy import deepcopy

from nornir.core.task import Result, Task

from ruamel.yaml import YAML
from ruamel.yaml.parser import ParserError
from jinja2 import Environment, FileSystemLoader, StrictUndefined


def render_templates(
    task: Task, 
    src_path: str,
    dst_path: str,
<<<<<<< HEAD
    dst_prefix: str = None,
=======
    dst_suffix: str = None,
>>>>>>> c8cc41cb2cf4f1456b21912d4384ac96f96d87c6
    **kwargs
    ) -> Result:
    """
    Loads intents from intent files
    
    Arguments:

    Examples:

    """
    env = Environment(
        loader=FileSystemLoader(src_path), trim_blocks=True, lstrip_blocks=True,
        undefined=StrictUndefined
    )
    yml = YAML(typ="safe")
<<<<<<< HEAD
    if dst_prefix:
        dst_path = Path(dst_path) / str(dst_prefix)
    
    dst_path = Path(dst_path) / task.host.name

    if not dst_path.exists():
        dst_path.mkdir(parents=True)
=======
    dst_path = Path(dst_path) / task.host.name
    if not dst_path.exists():
        dst_path.mkdir()
>>>>>>> c8cc41cb2cf4f1456b21912d4384ac96f96d87c6

    for template in env.list_templates(extensions="j2"):
        t = env.get_template(template)
        text = t.render(hostname=task.host.name, **kwargs)
        if not "_target_scope" in text:
            continue
        try:
            _ = yml.load(text)
        except ParserError as e:
            raise ValueError(f'Cannot parse rendered {template}: {e}')
<<<<<<< HEAD

        filename = dst_path / str(template.split(".")[0] + ".yml")
=======
        if dst_suffix:
            filename = dst_path / str(template.split(".")[0] + "_" + str(dst_suffix) + ".yml")
        else:
            filename = dst_path / str(template.split(".")[0] + ".yml")
>>>>>>> c8cc41cb2cf4f1456b21912d4384ac96f96d87c6

        with open(filename, "w") as f:
            f.write(text)

    return Result(host=task.host, result={})


