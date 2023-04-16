import time
from typing import Protocol, OrderedDict
from bs4 import BeautifulSoup
import requests
import dateparser

from resources import models as resource_models
from items import models as item_models


class ItemsRepositoriesInterface(Protocol):

    def parse(self, data: OrderedDict) -> None: ...


class ItemsRepositoriesV1:

    def parse(self, data: OrderedDict) -> None:
        resource = resource_models.Resource.objects.get(resource_id=data['res_id'])
        url = resource.resource_url
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f'Ошибка при обращении к ресурсу {resource.resource_name}: {e}')

        soup = BeautifulSoup(response.content, 'html.parser')
        top_tags = soup.find_all(resource.top_tag['tag'], attrs=resource.top_tag['attrs'])

        for top_tag in top_tags:
            cont = soup.find(resource.top_tag['tag'], attrs=resource.top_tag['attrs'])
            if cont:
                a_tag = cont.find('a')
                if a_tag:
                    url = a_tag['href']
                else:
                    url = top_tag['href']
            if not url.startswith(f'{resource.resource_url}'):
                url = f'{resource.resource_url}' + url
            # Creating item with res_id and link
            item = item_models.Item(res_id=resource, link=url)

            # Content
            try:
                content_response = requests.get(item.link)
                content_response.raise_for_status()
            except requests.RequestException as e:
                print(f"Ошибка при обращении к новости {item.link}: {e}")
                continue

            content_soup = BeautifulSoup(content_response.content, 'html.parser')
            content_tag = content_soup.find_all(resource.bottom_tag['tag'], attrs=resource.bottom_tag['attrs'])

            # Title
            title_tag = content_soup.find(resource.title_cut['tag'], attrs=resource.title_cut['attrs'])

            if title_tag:
                item.title = title_tag.text.strip()

            # Date
            date_tag = content_soup.find(resource.date_cut['tag'], attrs=resource.date_cut['attrs'])

            text = ''
            for content in content_tag:
                text += content.text.strip()
            item.content = text

            if date_tag:
                datetime_str = str(date_tag['datetime'])
                parsed_date = dateparser.parse(datetime_str)
                if parsed_date:
                    item.nd_date = int(parsed_date.timestamp())
                    item.not_date = parsed_date.strftime('%Y-%m-%d')

            item.s_date = int(time.time())
            item.save()


