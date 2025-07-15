import yaml
import os
import uiautomator2 as u2
from typing import Any

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, "config_uia.yml")


def get_device() -> Any:
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    serial = cfg.get("device_serial", "emulator-5554")
    d = u2.connect(serial)
    if cfg.get("autoinstall", True):
        d.healthcheck()
    d.set_timeout(10.0)
    return d