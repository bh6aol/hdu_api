# hdu_dormitory_electricity_fee
# bh6aol@gmail.com
# 2023-05-30 09:47:40

import requests
from bs4 import BeautifulSoup
import json

class DEF():
    """
    Params:\n
        community: 生活区名称\n
        building: 楼栋名称\n
        floor: 楼层名称\n
        room: 房间名称\n
    Example:\n
        a = DEF(community="生活一区", building="1栋", floor="1层", room="101")
    @see http://wap.xt.beescrm.com/base/electricity_hd/query/ele_id/7
    
    """
   
    def __init__(self,community: str, building: str, floor: str, room: str) -> None:

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        }

        self.community_dict = {
            "生活一区":"49",
            "生活二区":"50",
            "下沙生活区":"57",
            "下沙教学区":"777",
            "下沙商铺区":"809",
            "G区公寓":"824",
            "东校区":"825",
        }
        self.community_id = self.community_dict[community]

        self.building_list = self.get_building_list()
        for item in self.building_list:
            if item['building_name'] == building:
                self.building_id = item['building_id'] 
                break
        
        self.floor_list = self.get_floor_list()
        for item in self.floor_list:
            if item['floor_name'] == floor:
                self.floor_id = item['floor_id']
                break

        self.room_list = self.get_room_list()
        for item in self.room_list:
            if item['room_name'] == room:
                self.room_id = item['room_id']
                break
    
    def get_building_list(self):
        return requests.post('http://wap.xt.beescrm.com/base/common/getBuildingList', headers=self.headers, data={'id': self.community_id}).json()["data"]
    def get_floor_list(self):
        return requests.post('http://wap.xt.beescrm.com/base/common/getFloorList', headers=self.headers, data={'id': self.building_id}).json()["data"]
    def get_room_list(self):
        return requests.post('http://wap.xt.beescrm.com/base/common/getRoomList', headers=self.headers, data={'id': self.floor_id}).json()["data"]

    
    def get_balance(self) -> float:
        """
        get room balance(unit yuan)
        """
        response = requests.get(
            f'http://wap.xt.beescrm.com/base/electricityHd/queryResult/ele_id/7/community_id/{self.community_id}/building_id/{self.building_id}/floor_id/{self.floor_id}/room_id/{self.room_id}/flag/1',
            headers=self.headers,
        )

        soup = BeautifulSoup(response.text, "html.parser")
        span = soup.find('span', attrs={'class': 'price'})
        remain = float(span.text[:-1])
        return remain
