import logging

from maize.data_layer.data_layer import DataLayer
from maize.server.server import MaizeServer


class DataLayerAPI:
    data_layer: DataLayer

    def __init__(self, data_layer: DataLayer) -> None:
        self.data_layer = data_layer

    # def _set_state_changed_callback(self, callback: Callable):
    #     self.full_node.state_changed_callback = callback

    @property
    def server(self) -> MaizeServer:
        return self.data_layer.server

    @property
    def log(self) -> logging.Logger:
        return self.data_layer.log

    @property
    def api_ready(self) -> bool:
        return self.data_layer.initialized
