import pymysql
import adafruit_bme80.basic as adafruit_bme280
import time
import board
import busio
from datetime import datetime

i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address = 0x76)

def salvar_dados(temperatura,umidade,pressao0):
    conexao = pymysql.connect(
        hosy = "localhost",
        user = "estacao",
        password = "estacao_2026",
        database = "estacao_met"
)
    
    try: 
        cursor = conexao.cursor()

        cursor.execute("""
                       INSERT INTO leituras(data_hora,temperatura,umidade,pressao)
                       VALUES(%s,%s,%s,%s)
                       """,(datetime.now(),temperatura,umidade,pressao))
        
        conexao.commit()
        cursor.close()

    finally:
        conexao.close()

while True:
    try:

        t = bme280.temperature
        u = bme280.humidity
        p = bme280.pressure

        salvar_dados(t,u,p)

        print(f"\nTemperatura: {t: .2f} °C")
        print(f"\Umidade: {u: .2f} %")
        print(f"\Pressão: {p: .2f} hPA")
        time.sleep(2)

    except KeyboardInterrupt:
        print("Programa interrompido")
        break
    except Exception as e:
        print("Erro inesperado ocorreu",str(e))
        break
