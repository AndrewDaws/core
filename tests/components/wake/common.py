"""Provide common test tools for WWD."""
from __future__ import annotations

from collections.abc import Callable, Coroutine
from pathlib import Path
from typing import Any

from homeassistant.components import wake
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from tests.common import MockPlatform, mock_platform


def mock_wwd_entity_platform(
    hass: HomeAssistant,
    tmp_path: Path,
    integration: str,
    async_setup_entry: Callable[
        [HomeAssistant, ConfigEntry, AddEntitiesCallback],
        Coroutine[Any, Any, None],
    ]
    | None = None,
) -> MockPlatform:
    """Specialize the mock platform for stt."""
    loaded_platform = MockPlatform(async_setup_entry=async_setup_entry)
    mock_platform(hass, f"{integration}.{wake.DOMAIN}", loaded_platform)
    return loaded_platform
