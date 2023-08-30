#hdu student card service
# author: BH6AOL <bh6aol@gmail.com>
# date: 2023-08-28

from .cas import CAS
from bs4 import BeautifulSoup

class SC():
    def __init__(self, session) -> None:
        """
        session: 包含cas cookie的requests.session\n
        Example:\n
            cas = CAS("username", "password")
            session = cas.login()
            sc = SC(session)

        """
        self.session = session
        self.session.get('https://ykt.hdu.edu.cn/easytong_portal/ssoLogin')
        
    def get_user_info(self):
        response = self.session.get('https://ykt.hdu.edu.cn/easytong_portal/')
        soup = BeautifulSoup(response.text, "html.parser")
        university_name = soup.find('h4', attrs={'class': 'company-name'}).text.strip()
        login = soup.find('div', attrs={'class': 'login'})
        stu_id = login.span.text.split("：")[1].strip()
        stu_name = login.strong.text.split("，")[1].strip()
        login_time = login.samp.text.split("：")[1].strip()
        school_name = login.samp.nextSibling.nextSibling.nextSibling.text.split("：")[1].strip()
        
        return {
            "university_name": university_name,
            "stu_id": stu_id,
            "stu_name": stu_name,
            "login_time": login_time,
            "school_name": school_name,
        }

    def get_purse_list(self):
        purses_list = []
        response = self.session.get('https://ykt.hdu.edu.cn/easytong_portal/')
        soup = BeautifulSoup(response.text, "html.parser")
        purses = soup.find_all('div', attrs={'class': 'purse-item'})
        for purse in purses:
            money = purse.find('p', attrs={'class': 'money'}).text.strip()
            name = purse.find('h4', attrs={'class': 'purse-tit col-xs-12'}).text.strip()
            purses_list.append({
                "name":name,
                "money":money,
            })
        return purses_list

