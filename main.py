

from hdu_api.dorm_ele_fee import DEF
from hdu_api.cas import CAS
from hdu_api.stu_card import SC

def main():
    # 大套间照明电剩余
    def_room = DEF("G区公寓","36幢1单元","2层","36号楼1单元203")
    # 小房间空调电剩余
    def_air = DEF("G区公寓","36幢1单元","2层","36号楼1单元203-1")
    room_remain = def_room.get_balance()
    air_remain = def_air.get_balance()
    print("大套间照明电剩余:", room_remain)
    print("小房间空调电剩余:", air_remain)


    cas = CAS("你的学号", "你的密码")
    session = cas.login()
    sc = SC(session)
    print("用户信息:", sc.get_user_info())
    print("钱包信息:", sc.get_purse_list())
    

if __name__ == "__main__":
    main()