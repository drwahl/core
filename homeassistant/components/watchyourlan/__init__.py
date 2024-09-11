"""The WatchYourLAN integration."""

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from .coordinator import WatchYourLANUpdateCoordinator

PLATFORMS: list[Platform] = [Platform.SENSOR]
type WatchYourLANConfigEntry = ConfigEntry[WatchYourLANUpdateCoordinator]


async def async_setup_entry(
    hass: HomeAssistant, entry: WatchYourLANConfigEntry
) -> bool:
    """Set up WatchYourLAN from a config entry."""

    # Create and store the coordinator, passing the entire ConfigEntry
    coordinator = WatchYourLANUpdateCoordinator(hass)
    await coordinator.async_config_entry_first_refresh()
    entry.runtime_data = coordinator

    # If the setup is successful, forward the entry to other platforms (e.g., sensor)
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
