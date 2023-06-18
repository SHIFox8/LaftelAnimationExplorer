import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import laftel  # 라프텔 라이브러리
import requests

# 애니메이션 정보를 가져오는 함수
def get_anime_info(anime_name):
    # 라프텔에서 검색
    search_results = laftel.sync.searchAnime(anime_name)
    # 검색 결과에서 첫 번째 애니메이션 정보 가져오기
    anime_info = laftel.sync.getAnimeInfo(search_results[0].id)
    return anime_info

# 윈도우 생성
window = tk.Tk()
window.title('라프텔 애니 탐색기')
icon_url = 'https://static.laftel.net/og_image_1200x1200.png'
icon_laftel = Image.open(requests.get(icon_url, stream=True).raw)
icon_laftel.save('icon.ico', format='ICO')
window.iconbitmap('icon.ico')

# 애니메이션 이름 입력 라벨과 엔트리 위젯 생성
name_label = tk.Label(window, text='애니 제목:')
name_label.pack(side='left')
name_entry = tk.Entry(window)
name_entry.pack(side='left')

# 애니메이션 정보와 이미지를 표시할 프레임 생성
info_frame = tk.Frame(window)
info_frame.pack()

# 정보와 이미지를 표시할 라벨 위젯 생성
name_label = tk.Label(info_frame, text='이름:')
name_label.pack()
rating_label = tk.Label(info_frame, text='이용가:')
rating_label.pack()
genre_label = tk.Label(info_frame, text='장르:')
genre_label.pack()
air_year_label = tk.Label(info_frame, text='분기')
air_year_label.pack()
laftel_address_label = tk.Label(info_frame, text='라프텔 주소')
laftel_address_label.pack()
end_status_label = tk.Label(info_frame, text='완결 여부')
end_status_label.pack()

# 이미지를 표시할 라벨 위젯 생성
image_label = tk.Label(info_frame)
image_label.pack()

# 줄거리 스크롤바 생성
scrollbar = ttk.Scrollbar(info_frame)
scrollbar.pack(side='right', fill='y')

# 줄거리 텍스트 영역 생성
plot_text = tk.Text(info_frame, height=16, wrap='word', yscrollcommand=scrollbar.set)
plot_text.pack(fill='both', expand=True)

# 애니메이션 정보와 이미지를 업데이트하는 함수
def update_info():
    # 애니메이션 이름 엔트리에서 입력된 값을 가져옴
    anime_name = name_entry.get()
    # 애니메이션 정보 가져오기
    anime_info = get_anime_info(anime_name)
    # 정보 표시
    name_label.config(text=f'이름: {anime_info.name}')
    rating_label.config(text=f'이용가: {anime_info.content_rating}')
    genre_label.config(text=f'장르: {anime_info.tags}')
    air_year_label.config(text=f'분기 : {anime_info.air_year_quarter}')
    laftel_address_label.config(text=f'라프텔 주소 : {anime_info.url}')
    end_status_label.config(text=f'완결여부 : {anime_info.ended}')
    # 이미지 업데이트
    image_url = anime_info.image
    image_anime = Image.open(requests.get(image_url, stream=True).raw)
    photo = ImageTk.PhotoImage(image_anime)
    image_label.config(image=photo)
    image_label.image = photo  # 레퍼런스 유지
    # 줄거리 표시
    plot_text.delete('1.0', 'end')
    plot_text.insert('1.0', anime_info.content)

    scrollbar.config(command=plot_text.yview)  # 스크롤바와 텍스트 영역 연결

#



# 정보 업데이트 버튼 생성
update_button = tk.Button(window, text='검색', command=update_info)
update_button.pack()

# 윈도우 실행
window.mainloop()
