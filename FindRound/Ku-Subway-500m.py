import folium

# 건대입구역 좌표 (위도, 경도)
latitude = 37.540693
longitude = 127.070244

# 지도 생성
m = folium.Map(location=[latitude, longitude], zoom_start=16)

# 반경 500m 원 추가
folium.Circle(
    location=(latitude, longitude),
    radius=500,
    color="blue",
    fill=True,
    fill_color="lightblue",
    fill_opacity=0.5
).add_to(m)

# 건대입구역 마커 추가
folium.Marker(
    [latitude, longitude],
    popup="건대입구역",
    icon=folium.Icon(color="blue")
).add_to(m)

# 지도 저장
m.save("건대입구역_500m.html")
print("✅ 지도 저장 완료!")
