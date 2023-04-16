from typing import Protocol, OrderedDict

from items import repositories


class ItemsServicesInterface(Protocol):
    repos: repositories.ItemsRepositoriesInterface = repositories.ItemsRepositoriesV1()

    def parse(self, data: OrderedDict) -> None: ...


class ItemsServicesV1:
    repos: repositories.ItemsRepositoriesInterface = repositories.ItemsRepositoriesV1()

    def parse(self, data: OrderedDict) -> None:
        self.repos.parse(data)




