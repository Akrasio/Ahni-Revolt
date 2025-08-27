from dataclasses import dataclass
from dotenv import dotenv_values


@dataclass
class Config:
    """
    This class is used to store the bot's configuration.
    You can load it from a dictionary or from a .env file (recommended).
    By default in this Discord bot template, we use from_env classmethod.
    """
    revolt_token: str
    revolt_prefix: str
    revolt_owner_ids: list[str] = None
    lewds_api_url: str = "None"
    lewds_api_key: str = "None"
    revolt_api_url str = "https://api.revolt.chat"
    @classmethod
    def from_dict(self, **kwargs) -> "Config":
        """ Create a Config object from a dictionary. """
        kwargs_overwrite = {}

        for k, v in kwargs.items():
            new_key = k.lower()

            if v.isdigit():
                kwargs_overwrite[new_key] = int(v)
            else:
                kwargs_overwrite[new_key] = v

        return Config(**kwargs_overwrite)

    @classmethod
    def from_env(self, filename: str = ".env") -> "Config":
        """ Create a Config object from a .env file. """
        return Config.from_dict(**dotenv_values(filename))
