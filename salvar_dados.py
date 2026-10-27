import pymysql

conexao = pymysql.connect(
        hosy = "localhost",
        user = "estacao",
        password = "estacao_2026",
        database = "estacao_met"
)

try:
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id,data_hora,temperatura,umidade,pressao
        FROM leituras
        ORDER BY id DESC
        LIMIT 10
    """)

    linhas = cursor.fetchall()

    print(f"{'ID': <5} | {'Data e Hora':<20} | {'Temperatura (°C)':<17} | {'Umidade (%)':<12} | {'Pressão (hPa)'}:<15")
    print("-" *85)

    for linha in linhas:
        print(f"{linha[0]:<5} | {str(linha[1]):<20} | {linha[2]:<17.2f} | {linha[3]:<12.2f} | {linha[4]:<15.2f}")

finally:
    conexao.close()