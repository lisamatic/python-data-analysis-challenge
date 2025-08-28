#Datenfilterung und Analyse
temperaturMessungen = [8, 9 , 20, 25, 26, 27, 28, 29, 21, 24, 23, 22, 37, 38, 20, 19, 15, 14, 15, 16]
#temperaturMessungen werden normalerweise von Sensoren gegeben - wir würden das jetzt mit der API von unseren SQL daten verknüpfen und so unsere Daten bekommen
#print(len(temperaturMessungen))

# wenn temperatur unter 25° und über 15° ist soll es in eine neue liste: temperaturNormalwerte
def remove_exceptions(data_list):
    temperaturNormalwerte = []   # zuerst hier kein local scope sondern global 
    for temp in data_list: 
        if temp <= 28 and temp >= 15:
            temperaturNormalwerte.append(temp)
    return temperaturNormalwerte
normalReadings = remove_exceptions(temperaturMessungen)
#print(f"Liste Temperatur Normalwerte: {temperaturNormalwerte}")

#wir wollen die durschnittstemperatur berechnen dafür brauchen wir temperaturNormalwerte
def find_temp_mittelwert(filtered_list):
        if not filtered_list:
            print("Die Liste hat 0 Argumente")
            return 0
        totalSum = sum(filtered_list) 
        return totalSum / len(filtered_list)
 

find_temp_mittelwert(normalReadings)
print(f"Temperaturmittelwert: {find_temp_mittelwert(normalReadings)}")
