import folium

m = folium.Map()

tooltip_1 = 'Centr Baku'
tooltip_2 = 'Doroga Bku' 

folium.Marker([40.395359, 49.867424] , popup=tooltip_1, tooltip=tooltip_1).add_to(m)
folium.Marker([40.377251, 49.902736] , popup=tooltip_2, tooltip=tooltip_2).add_to(m)

# 40.395359, 49.867424

# 40.377251, 49.902736

m.save('Karta.html')
