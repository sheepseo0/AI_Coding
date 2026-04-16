import json

# 기본 주소록 데이터
addressbook = { 
    "양서영" : "01012345678", 
    "김아아" : "01022532236",
    "이아리" : "01019191919",
    "단종" : "01077778888",
    "박지훈" : "01022334455"
}


while True: 
    print("1. 추가 2. 삭제 3. 검색 4. 전체보기 0. 종료")
    menu = input("수행할 기능의 번호를 누르세요:")

    if menu == "1":
        name = input("이름:")
        phonenum = input("전화번호:")
        addressbook[name]=phonenum
        
        with open("addressbook.json", "w", encoding = "utf-8") as f: 
            json.dump(addressbook, f, ensure_ascii = False, indent = 4)
            
    elif menu == "2":
        name = input("삭제: ")
        if name in addressbook:
            del addressbook[name]
            print(f"{name} 정보 삭제 완료")

            with open("addressbook.json", "w", encoding = "utf-8") as f: 
                json.dump(addressbook, f, ensure_ascii = False, indent = 4)

    elif menu == "3":
        name = input("검색: ")
        if name in addressbook:
            print(addressbook[name])
        else:
            print("없음")

    elif menu == "4":
        for name, phonenum in addressbook.items():
            print(name, phonenum)

    elif menu == "0":
        print("프로그램을 종료합니다.")
        break
    

with open("addressbook.json", "w", encoding = "utf-8") as f:
    json.dump(addressbook, f, ensure_ascii = False, indent = 4) 

print("주소록이 저장되었습니다.")


with open("addressbook.json", "r", encoding = "utf-8") as f: 
    addressbook = json.load(f) 

print("현재 주소록:", addressbook) 
