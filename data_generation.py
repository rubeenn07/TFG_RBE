# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////  TFG RUBEN BERNSDORF ESTEBAN - CUSTOMER REGISTERS FUSION  //////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

import mysql.connector
import random
import unicodedata
from faker import Faker
import csv
from datetime import datetime, timedelta

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# SQL Workbench Connection
mydb = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='rb10102001',
    port='3306',
    database='tfg'
)

cursor = mydb.cursor()
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Variables
f = Faker()
f_esp = Faker(["es_ES"]) # España
f_por = Faker(["pt_PT"]) # Portugal
f_fra = Faker(["fr_FR"]) # Francia
f_ita = Faker(["it_IT"]) # Italia
f_ger = Faker(["de_DE"]) # Alemania

# Dominios
email_domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com']
t_direccion = ['facturación', 'envío', 'entrega', 'contacto']
size_domains = ['XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL']
color_domains = ["rojo", "azul", "verde", "amarillo", "naranja", "rosa", "morado", "blanco", "negro", "gris", "marrón"]
centre_domains = ["GA001", "GA002", "GA003", "GA004", "GA005", "GA006", "GA007", "GA008", "GA009", "GA010"]
supermarket_domains = ["SUP001", "SUP002", "SUP003", "SUP004", "SUP005"]


abrev_masc = [
    ["Francisco", "Fran"],
    ["Antonio", "Toño"],
    ["Javier", "Javi"],
    ["Manuel", "Manu"],
    ["José", "Pepe"],
    ["Rafael", "Rafa"],
    ["Daniel", "Dani"],
    ["Alberto", "Berto"],
    ["Alejandro", "Alex"],
    ["Ignacio", "Nacho"],
    ["Adrián", "Adri"],
    ["Gabriel", "Gabi"],
    ["Guillermo", "Guille"],
    ["Leonardo", "Leo"],
    ["Nicolás", "Nico"],
    ["Ricardo", "Richi"],
    ["Rodrigo", "Rodri"],
    ["Samuel", "Samu"],
    ["Santiago", "Santi"],
    ["Sebastián", "Sebas"],
    ["Víctor", "Viti"],
    ["Xavier", "Xavi"],
    ["Zacarías", "Zaca"]
]

abrev_fem = [
    ['Isabel', 'Isa'],
    ['Sofía', 'Sofi'],
    ['Lucía', 'Luci'],
    ['Patricia', 'Patri'],
    ['Beatriz', 'Bea'],
    ['Lorena', 'Lore'],
    ['Cristina', 'Cristi'],
    ['Carolina', 'Carol'],
    ['Alicia', 'Ali'],
    ['Miriam', 'Miri'],
    ['Paula', 'Pau'],
    ['Noelia', 'Noe'],
    ['Margarita', 'Mgta.'],
    ['Victoria', 'Vicky'],
    ['Rosario', 'Rosa']
]


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Functions
def calculate_age(date_of_birth):
    actual_date = datetime.now().date()
    age = actual_date.year - date_of_birth.year
    if (date_of_birth.month, date_of_birth.day) > (actual_date.month, actual_date.day):
        age -= 1
    return age


def add_years(date, years):
    new_date = date + timedelta(days=years * 365)
    return new_date


def accent_deletion(string):
    normalized_string = unicodedata.normalize('NFKD', string)
    new_string = normalized_string.translate(dict.fromkeys(ord(caracter) for caracter in normalized_string if unicodedata.category(caracter) == 'Mn'))
    return new_string

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Create Supermarket System files

csv_client_file = open('Supermarket System/cliente.csv', 'w', newline='')
csv_writer_1 = csv.writer(csv_client_file)
csv_writer_1.writerow(['CO_CLIENTE', 'NA_NOMBRE', 'NA_APELLIDO1', 'NA_APELLIDO2', 'CO_SEXO', 'DT_NACIMIENTO', 'NU_EDAD',
                       'CO_NACIONALIDAD', 'DT_ALTA', 'IN_TARJETA_COMPRA'])

csv_document_file = open('Supermarket System/documento.csv', 'w', newline='')
csv_writer_2 = csv.writer(csv_document_file)
csv_writer_2.writerow(['NU_DOCUMENTO', 'DT_CADUCIDAD_DOC', 'IN_VERIFICADO_DOC', 'CO_CLIENTE'])

csv_direction_file = open('Supermarket System/direccion.csv', 'w', newline='')
csv_writer_3 = csv.writer(csv_direction_file)
csv_writer_3.writerow(
    ['ID_DIRECCION', 'TIPO_DIRECCION', 'DIRECCION', 'NUMERO', 'BLOQUE', 'PISO', 'PUERTA', 'CO_POSTAL', 'CIUDAD', 'PAIS',
     'CO_CLIENTE'])

csv_phone_file = open('Supermarket System/telefono.csv', 'w', newline='')
csv_writer_4 = csv.writer(csv_phone_file)
csv_writer_4.writerow(['TELEFONO', 'PREFIJO', 'IN_VERIFICADO_TEL', 'CO_CLIENTE'])

csv_email_file = open('Supermarket System/email.csv', 'w', newline='')
csv_writer_5 = csv.writer(csv_email_file)
csv_writer_5.writerow(['NA_EMAIL', 'IN_VERIFICADO_EMAIL', 'CO_CLIENTE'])

csv_purchase_card_file = open('Supermarket System/tarjeta_compra.csv', 'w', newline='')
csv_writer_6 = csv.writer(csv_purchase_card_file)
csv_writer_6.writerow(['NU_TARJETA', 'TITULAR', 'CVV', 'DT_CADUCIDAD_TAR', 'CO_CLIENTE'])

csv_product_file = open('Supermarket System/articulo.csv', 'w', newline='')
csv_writer_7 = csv.writer(csv_product_file)
csv_writer_7.writerow(['CO_ARTICULO', 'NU_PRECIO', 'CO_TALLA', 'NA_COLOR', 'DT_FABRICACION_ART', 'DT_CADUCIDAD_ART'])

csv_sales_file = open('Supermarket System/venta.csv', 'w', newline='')
csv_writer_8 = csv.writer(csv_sales_file)
csv_writer_8.writerow(
    ['CO_VENTA', 'CO_CLIENTE', 'CO_ARTICULO', 'VL_VENTA', 'TS_VENTA', 'CO_CENTRO_VENTA', 'CO_CANAL_VENTA',
     'IN_TICKET_REGALO'])

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# MAIN PROGRAM
# INITIAL DATA LOADING ON THE DEPARTMENT STORE SYSTEM: 5.000 CLIENTS WITH RELIABLE INFORMATION.

for i in range(0, 5000):

    # To get the nationality (Spanish, Portuguese, French, Italian or German)
    rv_nationality = random.randint(-6, 10)

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # SPANISH CLIENTS
    if rv_nationality <= 6:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_esp.first_name_male()
            CO_SEXO = 'M'
        else:
            NA_NOMBRE = f_esp.first_name_female()
            CO_SEXO = 'F'
        NA_APELLIDO1 = f_esp.last_name()
        NA_APELLIDO2 = f_esp.last_name()
        CO_NACIONALIDAD = 'ESP'
        NU_DOCUMENTO = f_esp.bothify(text="########?", letters="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # PORTUGUESE CLIENTS
    elif rv_nationality == 7:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_por.first_name_male()
            CO_SEXO = 'M'
        else:
            NA_NOMBRE = f_por.first_name_female()
            CO_SEXO = 'F'
        NA_APELLIDO1 = f_por.last_name()
        NA_APELLIDO2 = f_por.last_name()
        CO_NACIONALIDAD = 'POR'
        NU_DOCUMENTO = f.bothify(text="?########", letters="XYZ") + f.random_letter().upper()

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # FRENCH CLIENTS
    elif rv_nationality == 8:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_fra.first_name_male()
            CO_SEXO = 'M'
        else:
            NA_NOMBRE = f_fra.first_name_female()
            CO_SEXO = 'F'
        NA_APELLIDO1 = f_fra.last_name()
        NA_APELLIDO2 = f_fra.last_name()
        CO_NACIONALIDAD = 'FRA'
        NU_DOCUMENTO = f.bothify(text="?########", letters="XYZ") + f.random_letter().upper()

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # ITALIAN CLIENTS
    elif rv_nationality == 9:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_ita.first_name_male()
            CO_SEXO = 'M'
        else:
            NA_NOMBRE = f_ita.first_name_female()
            CO_SEXO = 'F'
        NA_APELLIDO1 = f_ita.last_name()
        NA_APELLIDO2 = f_ita.last_name()
        CO_NACIONALIDAD = 'ITA'
        NU_DOCUMENTO = f.bothify(text="?########", letters="XYZ") + f.random_letter().upper()

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # GERMAN CLIENTS
    else:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_ger.first_name_male()
            CO_SEXO = 'M'
        else:
            NA_NOMBRE = f_ger.first_name_female()
            CO_SEXO = 'F'
        NA_APELLIDO1 = f_ger.last_name()
        NA_APELLIDO2 = f_ger.last_name()
        CO_NACIONALIDAD = 'GER'
        NU_DOCUMENTO = f.bothify(text="?########", letters="XYZ") + f.random_letter().upper()

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # EQUAL DATA FOR ALL NATIONALITIES
    CO_CLIENTE = random.randrange(10 ** 7, 10 ** 8)
    DT_NACIMIENTO = f.date_of_birth(minimum_age=18, maximum_age=99)
    NU_EDAD = calculate_age(DT_NACIMIENTO)
    DT_ALTA = f.date_between(start_date=add_years(datetime.now().date(), -20), end_date='today')
    IN_TARJETA_COMPRA = random.randint(0, 1)

    email_domain = random.choice(email_domains)
    NA_NOMBRE_EMAIL = (NA_NOMBRE + NA_APELLIDO1 + NA_APELLIDO2).lower().replace(" ", "")
    NA_NOMBRE_EMAIL_ST = accent_deletion(NA_NOMBRE_EMAIL)
    NA_EMAIL = f"{NA_NOMBRE_EMAIL_ST}@{email_domain}"
    IN_VERIFICADO_EMAIL = random.randint(0, 1)

    DT_CADUCIDAD_DOC = f.date_between(start_date=add_years(datetime.now().date(), -5),
                                      end_date=add_years(datetime.now().date(), 15))
    IN_VERIFICADO_DOC = random.randint(0, 1)

    NU_TARJETA = f.bothify(text="####-####-####")
    TITULAR = (NA_NOMBRE + ' ' + NA_APELLIDO1 + ' ' + NA_APELLIDO2).upper()
    CVV = random.randint(100, 999)
    DT_CADUCIDAD_TAR = f.date_between(start_date=add_years(datetime.now().date(), -5),
                                      end_date=add_years(datetime.now().date(), 15))

    complete_number = f_esp.phone_number().replace(' ', '')
    PREFIJO = complete_number[:3]
    TELEFONO = complete_number[3:]
    IN_VERIFICADO_TEL = random.randint(0, 1)

    ID_DIRECCION = f_esp.bothify(text="DIR-#####")
    TIPO_DIRECCION = random.choice(t_direccion)
    DIRECCION = f_esp.street_name()
    NUMERO = random.randint(1, 499)

    rv_bloque = random.randint(1, 2)
    if rv_bloque == 1:
        BLOQUE = random.randint(1, 10)
    else:
        BLOQUE = None

    rv_piso = random.randint(1, 2)
    if rv_piso == 1:
        PISO = random.randint(1, 20)
    else:
        PISO = None

    rv_puerta = random.randint(1, 2)
    if rv_puerta == 1:
        PUERTA = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
    else:
        PUERTA = None

    CO_POSTAL = random.randint(10000, 99999)
    CIUDAD = f_esp.city()
    PAIS = 'ESPAÑA'

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # Insert data into MySQL tables
    cursor.execute("INSERT INTO cliente VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (CO_CLIENTE, NA_NOMBRE, NA_APELLIDO1, NA_APELLIDO2, CO_SEXO, DT_NACIMIENTO, NU_EDAD, CO_NACIONALIDAD, DT_ALTA, IN_TARJETA_COMPRA))
    cursor.execute("INSERT INTO email VALUES (%s, %s, %s)", (NA_EMAIL, IN_VERIFICADO_EMAIL, CO_CLIENTE))
    cursor.execute("INSERT INTO documento VALUES (%s, %s, %s, %s)", (NU_DOCUMENTO, DT_CADUCIDAD_DOC, IN_VERIFICADO_DOC, CO_CLIENTE))
    cursor.execute("INSERT INTO direccion VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (ID_DIRECCION, TIPO_DIRECCION, DIRECCION, NUMERO, BLOQUE, PISO, PUERTA, CO_POSTAL, CIUDAD, PAIS, CO_CLIENTE))
    cursor.execute("INSERT INTO telefono VALUES (%s, %s, %s, %s)", (TELEFONO, PREFIJO, IN_VERIFICADO_TEL, CO_CLIENTE))
    if IN_TARJETA_COMPRA == 1:
        cursor.execute("INSERT INTO tarjeta_compra VALUES (%s, %s, %s, %s, %s)", (NU_TARJETA, TITULAR, CVV, DT_CADUCIDAD_TAR, CO_CLIENTE))

    mydb.commit()

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# INITIAL DATA LOADING ON THE SUPERMARKET SYSTEM: 3.000 CLIENTS WITH RELIABLE INFORMATION.

for i in range(0, 3000):

    # To get the nationality (60% Spanish, 10% portuguese, french, italian or german)
    rv_nationality = random.randint(-6, 10)

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # SPANISH CLIENTS
    if rv_nationality <= 6:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_esp.first_name_male()
            CO_SEXO = None
        else:
            NA_NOMBRE = f_esp.first_name_female()
            CO_SEXO = None
        NA_APELLIDO1 = f_esp.last_name()
        NA_APELLIDO2 = f_esp.last_name()
        CO_NACIONALIDAD = None
        NU_DOCUMENTO = f_esp.bothify(text="########?", letters="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # PORTUGUESE CLIENTS
    elif rv_nationality == 7:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_por.first_name_male()
            CO_SEXO = None
        else:
            NA_NOMBRE = f_por.first_name_female()
            CO_SEXO = None
        NA_APELLIDO1 = f_por.last_name()
        NA_APELLIDO2 = f_por.last_name()
        CO_NACIONALIDAD = None
        NU_DOCUMENTO = f.bothify(text="?########", letters="XYZ") + f.random_letter().upper()

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # FRENCH CLIENTS
    elif rv_nationality == 8:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_fra.first_name_male()
            CO_SEXO = None
        else:
            NA_NOMBRE = f_fra.first_name_female()
            CO_SEXO = None
        NA_APELLIDO1 = f_fra.last_name()
        NA_APELLIDO2 = f_fra.last_name()
        CO_NACIONALIDAD = None
        NU_DOCUMENTO = f.bothify(text="?########", letters="XYZ") + f.random_letter().upper()

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # ITALIAN CLIENTS
    elif rv_nationality == 9:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_ita.first_name_male()
            CO_SEXO = None
        else:
            NA_NOMBRE = f_ita.first_name_female()
            CO_SEXO = None
        NA_APELLIDO1 = f_ita.last_name()
        NA_APELLIDO2 = f_ita.last_name()
        CO_NACIONALIDAD = None
        NU_DOCUMENTO = f.bothify(text="?########", letters="XYZ") + f.random_letter().upper()

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # GERMAN CLIENTS
    else:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_ger.first_name_male()
            CO_SEXO = None
        else:
            NA_NOMBRE = f_ger.first_name_female()
            CO_SEXO = None
        NA_APELLIDO1 = f_ger.last_name()
        NA_APELLIDO2 = f_ger.last_name()
        CO_NACIONALIDAD = None
        NU_DOCUMENTO = f.bothify(text="?########", letters="XYZ") + f.random_letter().upper()

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # EQUAL DATA FOR ALL NATIONALITIES
    CO_CLIENTE = random.randrange(10 ** 7, 10 ** 8)
    DT_NACIMIENTO = f.date_of_birth(minimum_age=18, maximum_age=99)
    NU_EDAD = None
    DT_ALTA = f.date_between(start_date=add_years(datetime.now().date(), -20), end_date='today')
    IN_TARJETA_COMPRA = random.randint(0, 1)

    NA_EMAIL = None
    IN_VERIFICADO_EMAIL = None

    DT_CADUCIDAD_DOC = f.date_between(start_date=add_years(datetime.now().date(), -5),
                                      end_date=add_years(datetime.now().date(), 15))
    IN_VERIFICADO_DOC = random.randint(0, 1)

    NU_TARJETA = f.bothify(text="####-####-####")
    TITULAR = (NA_NOMBRE + ' ' + NA_APELLIDO1 + ' ' + NA_APELLIDO2).upper()
    CVV = random.randint(100, 999)
    DT_CADUCIDAD_TAR = f.date_between(start_date=add_years(datetime.now().date(), -5),
                                      end_date=add_years(datetime.now().date(), 15))

    complete_number = f_esp.phone_number().replace(' ', '')
    PREFIJO = complete_number[:3]
    TELEFONO = complete_number[3:]
    IN_VERIFICADO_TEL = random.randint(0, 1)

    ID_DIRECCION = None
    TIPO_DIRECCION = None
    DIRECCION = None
    NUMERO = None
    BLOQUE = None
    PISO = None
    PUERTA = None
    CO_POSTAL = None
    CIUDAD = None
    PAIS = None

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # Write data to Supermarket System files
    csv_writer_1.writerow(
        [CO_CLIENTE, NA_NOMBRE, NA_APELLIDO1, NA_APELLIDO2, CO_SEXO, DT_NACIMIENTO, NU_EDAD, CO_NACIONALIDAD, DT_ALTA,
         IN_TARJETA_COMPRA])
    csv_writer_2.writerow([NU_DOCUMENTO, DT_CADUCIDAD_DOC, IN_VERIFICADO_DOC, CO_CLIENTE])
    csv_writer_3.writerow(
        [ID_DIRECCION, TIPO_DIRECCION, DIRECCION, NUMERO, BLOQUE, PISO, PUERTA, CO_POSTAL, CIUDAD, PAIS, CO_CLIENTE])
    csv_writer_4.writerow([TELEFONO, PREFIJO, IN_VERIFICADO_TEL, CO_CLIENTE])
    csv_writer_5.writerow([NA_EMAIL, IN_VERIFICADO_EMAIL, CO_CLIENTE])
    if IN_TARJETA_COMPRA == 1:
        csv_writer_6.writerow([NU_TARJETA, TITULAR, CVV, DT_CADUCIDAD_TAR, CO_CLIENTE])

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# SECOND DATA LOADING ON THE DEPARTMENT STORE SYSTEM: 2.000 CLIENTS WITH DUPLICATE INFORMATION.


for i in range(0, 1000):

    # To get the nationality (Spanish, Portuguese, French, Italian or German)
    rv_nationality = random.randint(-6, 10)

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # SPANISH CLIENTS
    if rv_nationality <= 6:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_esp.first_name_male()
            CO_SEXO = 'M'
        else:
            NA_NOMBRE = f_esp.first_name_female()
            CO_SEXO = 'F'
        NA_APELLIDO1 = f_esp.last_name()
        NA_APELLIDO2 = f_esp.last_name()
        CO_NACIONALIDAD = 'ESP'
        NU_DOCUMENTO = f_esp.bothify(text="########?", letters="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # PORTUGUESE CLIENTS
    elif rv_nationality == 7:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_por.first_name_male()
            CO_SEXO = 'M'
        else:
            NA_NOMBRE = f_por.first_name_female()
            CO_SEXO = 'F'
        NA_APELLIDO1 = f_por.last_name()
        NA_APELLIDO2 = f_por.last_name()
        CO_NACIONALIDAD = 'POR'
        NU_DOCUMENTO = f.bothify(text="?########", letters="XYZ") + f.random_letter().upper()

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # FRENCH CLIENTS
    elif rv_nationality == 8:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_fra.first_name_male()
            CO_SEXO = 'M'
        else:
            NA_NOMBRE = f_fra.first_name_female()
            CO_SEXO = 'F'
        NA_APELLIDO1 = f_fra.last_name()
        NA_APELLIDO2 = f_fra.last_name()
        CO_NACIONALIDAD = 'FRA'
        NU_DOCUMENTO = f.bothify(text="?########", letters="XYZ") + f.random_letter().upper()

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # ITALIAN CLIENTS
    elif rv_nationality == 9:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_ita.first_name_male()
            CO_SEXO = 'M'
        else:
            NA_NOMBRE = f_ita.first_name_female()
            CO_SEXO = 'F'
        NA_APELLIDO1 = f_ita.last_name()
        NA_APELLIDO2 = f_ita.last_name()
        CO_NACIONALIDAD = 'ITA'
        NU_DOCUMENTO = f.bothify(text="?########", letters="XYZ") + f.random_letter().upper()

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # GERMAN CLIENTS
    else:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_ger.first_name_male()
            CO_SEXO = 'M'
        else:
            NA_NOMBRE = f_ger.first_name_female()
            CO_SEXO = 'F'
        NA_APELLIDO1 = f_ger.last_name()
        NA_APELLIDO2 = f_ger.last_name()
        CO_NACIONALIDAD = 'GER'
        NU_DOCUMENTO = f.bothify(text="?########", letters="XYZ") + f.random_letter().upper()

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # EQUAL DATA FOR ALL NATIONALITIES
    CO_CLIENTE = random.randrange(10 ** 7, 10 ** 8)
    DT_NACIMIENTO = f.date_of_birth(minimum_age=18, maximum_age=99)
    NU_EDAD = calculate_age(DT_NACIMIENTO)
    DT_ALTA = f.date_between(start_date=add_years(datetime.now().date(), -20), end_date='today')
    IN_TARJETA_COMPRA = random.randint(0, 1)

    email_domain = random.choice(email_domains)
    NA_NOMBRE_EMAIL = (NA_NOMBRE + NA_APELLIDO1 + NA_APELLIDO2).lower().replace(" ", "")
    NA_NOMBRE_EMAIL_ST = accent_deletion(NA_NOMBRE_EMAIL)
    NA_EMAIL = f"{NA_NOMBRE_EMAIL_ST}@{email_domain}"
    IN_VERIFICADO_EMAIL = random.randint(0, 1)

    DT_CADUCIDAD_DOC = f.date_between(start_date=add_years(datetime.now().date(), -5),
                                      end_date=add_years(datetime.now().date(), 15))
    IN_VERIFICADO_DOC = random.randint(0, 1)

    NU_TARJETA = f.bothify(text="####-####-####")
    TITULAR = (NA_NOMBRE + ' ' + NA_APELLIDO1 + ' ' + NA_APELLIDO2).upper()
    CVV = random.randint(100, 999)
    DT_CADUCIDAD_TAR = f.date_between(start_date=add_years(datetime.now().date(), -5),
                                      end_date=add_years(datetime.now().date(), 15))

    complete_number = f_esp.phone_number().replace(' ', '')
    PREFIJO = complete_number[:3]
    TELEFONO = complete_number[3:]
    IN_VERIFICADO_TEL = random.randint(0, 1)

    ID_DIRECCION = f_esp.bothify(text="DIR-#####")
    TIPO_DIRECCION = random.choice(t_direccion)
    DIRECCION = f_esp.street_name()
    NUMERO = random.randint(1, 499)

    rv_bloque = random.randint(1, 2)
    if rv_bloque == 1:
        BLOQUE = random.randint(1, 10)
    else:
        BLOQUE = None

    rv_piso = random.randint(1, 2)
    if rv_piso == 1:
        PISO = random.randint(1, 20)
    else:
        PISO = None

    rv_puerta = random.randint(1, 2)
    if rv_puerta == 1:
        PUERTA = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
    else:
        PUERTA = None

    CO_POSTAL = random.randint(10000, 99999)
    CIUDAD = f_esp.city()
    PAIS = 'ESPAÑA'

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # Insert data into MySQL tables

    cursor.execute("INSERT INTO cliente VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
    CO_CLIENTE, NA_NOMBRE, NA_APELLIDO1, NA_APELLIDO2, CO_SEXO, DT_NACIMIENTO, NU_EDAD, CO_NACIONALIDAD, DT_ALTA,
    IN_TARJETA_COMPRA))
    cursor.execute("INSERT INTO email VALUES (%s, %s, %s)", (NA_EMAIL, IN_VERIFICADO_EMAIL, CO_CLIENTE))
    cursor.execute("INSERT INTO documento VALUES (%s, %s, %s, %s)",
                   (NU_DOCUMENTO, DT_CADUCIDAD_DOC, IN_VERIFICADO_DOC, CO_CLIENTE))
    cursor.execute("INSERT INTO direccion VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
    ID_DIRECCION, TIPO_DIRECCION, DIRECCION, NUMERO, BLOQUE, PISO, PUERTA, CO_POSTAL, CIUDAD, PAIS, CO_CLIENTE))
    cursor.execute("INSERT INTO telefono VALUES (%s, %s, %s, %s)", (TELEFONO, PREFIJO, IN_VERIFICADO_TEL, CO_CLIENTE))
    if IN_TARJETA_COMPRA == 1:
        cursor.execute("INSERT INTO tarjeta_compra VALUES (%s, %s, %s, %s, %s)",
                       (NU_TARJETA, TITULAR, CVV, DT_CADUCIDAD_TAR, CO_CLIENTE))

    rv_duplication1 = random.randint(1, 10)  # Determines the duplication type

    if rv_duplication1 % 2 == 0:

        cursor.execute("INSERT INTO cliente VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
        CO_CLIENTE, NA_NOMBRE, NA_APELLIDO1, NA_APELLIDO2, CO_SEXO, DT_NACIMIENTO, NU_EDAD, CO_NACIONALIDAD, DT_ALTA,
        IN_TARJETA_COMPRA))
        cursor.execute("INSERT INTO email VALUES (%s, %s, %s)", (NA_EMAIL, IN_VERIFICADO_EMAIL, CO_CLIENTE))
        cursor.execute("INSERT INTO documento VALUES (%s, %s, %s, %s)",
                       (NU_DOCUMENTO, DT_CADUCIDAD_DOC, IN_VERIFICADO_DOC, CO_CLIENTE))
        cursor.execute("INSERT INTO direccion VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
        ID_DIRECCION, TIPO_DIRECCION, DIRECCION, NUMERO, BLOQUE, PISO, PUERTA, CO_POSTAL, CIUDAD, PAIS, CO_CLIENTE))
        cursor.execute("INSERT INTO telefono VALUES (%s, %s, %s, %s)",
                       (TELEFONO, PREFIJO, IN_VERIFICADO_TEL, CO_CLIENTE))
        if IN_TARJETA_COMPRA == 1:
            cursor.execute("INSERT INTO tarjeta_compra VALUES (%s, %s, %s, %s, %s)",
                           (NU_TARJETA, TITULAR, CVV, DT_CADUCIDAD_TAR, CO_CLIENTE))

    else:
        cursor.execute("INSERT INTO cliente VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
        CO_CLIENTE, NA_NOMBRE, NA_APELLIDO1, None, None, DT_NACIMIENTO, None, None, DT_ALTA, IN_TARJETA_COMPRA))
        cursor.execute("INSERT INTO email VALUES (%s, %s, %s)", (NA_EMAIL, IN_VERIFICADO_EMAIL, CO_CLIENTE))
        cursor.execute("INSERT INTO documento VALUES (%s, %s, %s, %s)",
                       (NU_DOCUMENTO, None, IN_VERIFICADO_DOC, CO_CLIENTE))
        cursor.execute("INSERT INTO direccion VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (ID_DIRECCION, None, DIRECCION, NUMERO, BLOQUE, PISO, PUERTA, None, CIUDAD, PAIS, CO_CLIENTE))
        cursor.execute("INSERT INTO telefono VALUES (%s, %s, %s, %s)", (TELEFONO, PREFIJO, None, CO_CLIENTE))
        if IN_TARJETA_COMPRA == 1:
            cursor.execute("INSERT INTO tarjeta_compra VALUES (%s, %s, %s, %s, %s)",
                           (NU_TARJETA, TITULAR, CVV, DT_CADUCIDAD_TAR, CO_CLIENTE))

    mydb.commit()

# --------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------

# SECOND DATA LOADING ON THE SUPERMARKET SYSTEM: 1.000 CLIENTS WITH DUPLICATE INFORMATION.

for i in range(0, 500):

    # To get the nationality (60% Spanish, 10% portuguese, french, italian or german)
    rv_nationality = random.randint(-6, 10)

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # SPANISH CLIENTS
    if rv_nationality <= 6:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_esp.first_name_male()
            CO_SEXO = None
        else:
            NA_NOMBRE = f_esp.first_name_female()
            CO_SEXO = None
        NA_APELLIDO1 = f_esp.last_name()
        NA_APELLIDO2 = f_esp.last_name()
        CO_NACIONALIDAD = None
        NU_DOCUMENTO = f_esp.bothify(text="########?", letters="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # PORTUGUESE CLIENTS
    elif rv_nationality == 7:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_por.first_name_male()
            CO_SEXO = None
        else:
            NA_NOMBRE = f_por.first_name_female()
            CO_SEXO = None
        NA_APELLIDO1 = f_por.last_name()
        NA_APELLIDO2 = f_por.last_name()
        CO_NACIONALIDAD = None
        NU_DOCUMENTO = f.bothify(text="?########", letters="XYZ") + f.random_letter().upper()

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # FRENCH CLIENTS
    elif rv_nationality == 8:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_fra.first_name_male()
            CO_SEXO = None
        else:
            NA_NOMBRE = f_fra.first_name_female()
            CO_SEXO = None
        NA_APELLIDO1 = f_fra.last_name()
        NA_APELLIDO2 = f_fra.last_name()
        CO_NACIONALIDAD = None
        NU_DOCUMENTO = f.bothify(text="?########", letters="XYZ") + f.random_letter().upper()

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # ITALIAN CLIENTS
    elif rv_nationality == 9:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_ita.first_name_male()
            CO_SEXO = None
        else:
            NA_NOMBRE = f_ita.first_name_female()
            CO_SEXO = None
        NA_APELLIDO1 = f_ita.last_name()
        NA_APELLIDO2 = f_ita.last_name()
        CO_NACIONALIDAD = None
        NU_DOCUMENTO = f.bothify(text="?########", letters="XYZ") + f.random_letter().upper()

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # GERMAN CLIENTS
    else:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_ger.first_name_male()
            CO_SEXO = None
        else:
            NA_NOMBRE = f_ger.first_name_female()
            CO_SEXO = None
        NA_APELLIDO1 = f_ger.last_name()
        NA_APELLIDO2 = f_ger.last_name()
        CO_NACIONALIDAD = None
        NU_DOCUMENTO = f.bothify(text="?########", letters="XYZ") + f.random_letter().upper()

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # EQUAL DATA FOR ALL NATIONALITIES
    CO_CLIENTE = random.randrange(10 ** 7, 10 ** 8)
    DT_NACIMIENTO = f.date_of_birth(minimum_age=18, maximum_age=99)
    NU_EDAD = None
    DT_ALTA = f.date_between(start_date=add_years(datetime.now().date(), -20), end_date='today')
    IN_TARJETA_COMPRA = random.randint(0, 1)

    email_domain = random.choice(email_domains)
    NA_EMAIL = None
    IN_VERIFICADO_EMAIL = None

    DT_CADUCIDAD_DOC = f.date_between(start_date=add_years(datetime.now().date(), -5),
                                      end_date=add_years(datetime.now().date(), 15))
    IN_VERIFICADO_DOC = random.randint(0, 1)

    NU_TARJETA = f.bothify(text="####-####-####")
    TITULAR = (NA_NOMBRE + ' ' + NA_APELLIDO1 + ' ' + NA_APELLIDO2).upper()
    CVV = random.randint(100, 999)
    DT_CADUCIDAD_TAR = f.date_between(start_date=add_years(datetime.now().date(), -5),
                                      end_date=add_years(datetime.now().date(), 15))

    complete_number = f_esp.phone_number().replace(' ', '')
    PREFIJO = complete_number[:3]
    TELEFONO = complete_number[3:]
    IN_VERIFICADO_TEL = random.randint(0, 1)

    ID_DIRECCION = None
    TIPO_DIRECCION = None
    DIRECCION = None
    NUMERO = None
    BLOQUE = None
    PISO = None
    PUERTA = None
    CO_POSTAL = None
    CIUDAD = None
    PAIS = None

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # Write data to Supermarket System files
    csv_writer_1.writerow(
        [CO_CLIENTE, NA_NOMBRE, NA_APELLIDO1, NA_APELLIDO2, CO_SEXO, DT_NACIMIENTO, NU_EDAD, CO_NACIONALIDAD, DT_ALTA,
         IN_TARJETA_COMPRA])
    csv_writer_2.writerow([NU_DOCUMENTO, DT_CADUCIDAD_DOC, IN_VERIFICADO_DOC, CO_CLIENTE])
    csv_writer_3.writerow(
        [ID_DIRECCION, TIPO_DIRECCION, DIRECCION, NUMERO, BLOQUE, PISO, PUERTA, CO_POSTAL, CIUDAD, PAIS, CO_CLIENTE])
    csv_writer_4.writerow([TELEFONO, PREFIJO, IN_VERIFICADO_TEL, CO_CLIENTE])
    csv_writer_5.writerow([NA_EMAIL, IN_VERIFICADO_EMAIL, CO_CLIENTE])
    if IN_TARJETA_COMPRA == 1:
        csv_writer_6.writerow([NU_TARJETA, TITULAR, CVV, DT_CADUCIDAD_TAR, CO_CLIENTE])

    rv_duplication2 = random.randint(1, 10)  # Determines the duplication type
    if rv_duplication2 % 2 == 0:
        csv_writer_1.writerow(
            [CO_CLIENTE, NA_NOMBRE, NA_APELLIDO1, NA_APELLIDO2, CO_SEXO, DT_NACIMIENTO, NU_EDAD, CO_NACIONALIDAD,
             DT_ALTA, IN_TARJETA_COMPRA])
        csv_writer_2.writerow([NU_DOCUMENTO, DT_CADUCIDAD_DOC, IN_VERIFICADO_DOC, CO_CLIENTE])
        csv_writer_3.writerow(
            [ID_DIRECCION, TIPO_DIRECCION, DIRECCION, NUMERO, BLOQUE, PISO, PUERTA, CO_POSTAL, CIUDAD, PAIS,
             CO_CLIENTE])
        csv_writer_4.writerow([TELEFONO, PREFIJO, IN_VERIFICADO_TEL, CO_CLIENTE])
        csv_writer_5.writerow([NA_EMAIL, IN_VERIFICADO_EMAIL, CO_CLIENTE])
        if IN_TARJETA_COMPRA == 1:
            csv_writer_6.writerow([NU_TARJETA, TITULAR, CVV, DT_CADUCIDAD_TAR, CO_CLIENTE])

    else:
        csv_writer_1.writerow(
            [CO_CLIENTE, NA_NOMBRE, None, NA_APELLIDO2, CO_SEXO, DT_NACIMIENTO, NU_EDAD, CO_NACIONALIDAD, None,
             IN_TARJETA_COMPRA])
        csv_writer_2.writerow([NU_DOCUMENTO, DT_CADUCIDAD_DOC, IN_VERIFICADO_DOC, CO_CLIENTE])
        csv_writer_3.writerow(
            [ID_DIRECCION, TIPO_DIRECCION, DIRECCION, NUMERO, BLOQUE, PISO, PUERTA, CO_POSTAL, CIUDAD, PAIS,
             CO_CLIENTE])
        csv_writer_4.writerow([TELEFONO, PREFIJO, None, CO_CLIENTE])
        csv_writer_5.writerow([NA_EMAIL, IN_VERIFICADO_EMAIL, CO_CLIENTE])
        if IN_TARJETA_COMPRA == 1:
            csv_writer_6.writerow([NU_TARJETA, TITULAR, CVV, DT_CADUCIDAD_TAR, CO_CLIENTE])

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# THIRD DATA LOADING ON BOTH SYSTEMS: 1.000 DUPLICATE CLIENTS.

for i in range(0, 1000):

    # To get the nationality (Spanish, Portuguese, French, Italian or German)
    rv_nationality = random.randint(-6, 10)

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # SPANISH CLIENTS
    if rv_nationality <= 6:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_esp.first_name_male()
            CO_SEXO = 'M'
        else:
            NA_NOMBRE = f_esp.first_name_female()
            CO_SEXO = 'F'
        NA_APELLIDO1 = f_esp.last_name()
        NA_APELLIDO2 = f_esp.last_name()
        CO_NACIONALIDAD = 'ESP'
        NU_DOCUMENTO = f_esp.bothify(text="########?", letters="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # PORTUGUESE CLIENTS
    elif rv_nationality == 7:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_por.first_name_male()
            CO_SEXO = 'M'
        else:
            NA_NOMBRE = f_por.first_name_female()
            CO_SEXO = 'F'
        NA_APELLIDO1 = f_por.last_name()
        NA_APELLIDO2 = f_por.last_name()
        CO_NACIONALIDAD = 'POR'
        NU_DOCUMENTO = f.bothify(text="?########", letters="XYZ") + f.random_letter().upper()

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # FRENCH CLIENTS
    elif rv_nationality == 8:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_fra.first_name_male()
            CO_SEXO = 'M'
        else:
            NA_NOMBRE = f_fra.first_name_female()
            CO_SEXO = 'F'
        NA_APELLIDO1 = f_fra.last_name()
        NA_APELLIDO2 = f_fra.last_name()
        CO_NACIONALIDAD = 'FRA'
        NU_DOCUMENTO = f.bothify(text="?########", letters="XYZ") + f.random_letter().upper()

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # ITALIAN CLIENTS
    elif rv_nationality == 9:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_ita.first_name_male()
            CO_SEXO = 'M'
        else:
            NA_NOMBRE = f_ita.first_name_female()
            CO_SEXO = 'F'
        NA_APELLIDO1 = f_ita.last_name()
        NA_APELLIDO2 = f_ita.last_name()
        CO_NACIONALIDAD = 'ITA'
        NU_DOCUMENTO = f.bothify(text="?########", letters="XYZ") + f.random_letter().upper()

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # GERMAN CLIENTS
    else:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_ger.first_name_male()
            CO_SEXO = 'M'
        else:
            NA_NOMBRE = f_ger.first_name_female()
            CO_SEXO = 'F'
        NA_APELLIDO1 = f_ger.last_name()
        NA_APELLIDO2 = f_ger.last_name()
        CO_NACIONALIDAD = 'GER'
        NU_DOCUMENTO = f.bothify(text="?########", letters="XYZ") + f.random_letter().upper()

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # EQUAL DATA FOR ALL NATIONALITIES
    CO_CLIENTE = random.randrange(10 ** 7, 10 ** 8)
    DT_NACIMIENTO = f.date_of_birth(minimum_age=18, maximum_age=99)
    NU_EDAD = calculate_age(DT_NACIMIENTO)
    DT_ALTA = f.date_between(start_date=add_years(datetime.now().date(), -20), end_date='today')
    IN_TARJETA_COMPRA = random.randint(0, 1)

    email_domain = random.choice(email_domains)
    NA_NOMBRE_EMAIL = (NA_NOMBRE + NA_APELLIDO1 + NA_APELLIDO2).lower().replace(" ", "")
    NA_NOMBRE_EMAIL_ST = accent_deletion(NA_NOMBRE_EMAIL)
    NA_EMAIL = f"{NA_NOMBRE_EMAIL_ST}@{email_domain}"
    IN_VERIFICADO_EMAIL = random.randint(0, 1)

    DT_CADUCIDAD_DOC = f.date_between(start_date=add_years(datetime.now().date(), -5),
                                      end_date=add_years(datetime.now().date(), 15))
    IN_VERIFICADO_DOC = random.randint(0, 1)

    NU_TARJETA = f.bothify(text="####-####-####")
    TITULAR = (NA_NOMBRE + ' ' + NA_APELLIDO1 + ' ' + NA_APELLIDO2).upper()
    CVV = random.randint(100, 999)
    DT_CADUCIDAD_TAR = f.date_between(start_date=add_years(datetime.now().date(), -5),
                                      end_date=add_years(datetime.now().date(), 15))

    complete_number = f_esp.phone_number().replace(' ', '')
    PREFIJO = complete_number[:3]
    TELEFONO = complete_number[3:]
    IN_VERIFICADO_TEL = random.randint(0, 1)

    ID_DIRECCION = f_esp.bothify(text="DIR-#####")
    TIPO_DIRECCION = random.choice(t_direccion)
    DIRECCION = f_esp.street_name()
    NUMERO = random.randint(1, 499)

    rv_bloque = random.randint(1, 2)
    if rv_bloque == 1:
        BLOQUE = random.randint(1, 10)
    else:
        BLOQUE = None

    rv_piso = random.randint(1, 2)
    if rv_piso == 1:
        PISO = random.randint(1, 20)
    else:
        PISO = None

    rv_puerta = random.randint(1, 2)
    if rv_puerta == 1:
        PUERTA = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
    else:
        PUERTA = None

    CO_POSTAL = random.randint(10000, 99999)
    CIUDAD = f_esp.city()
    PAIS = 'ESPAÑA'

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    rv_duplication3 = random.randint(1, 10)  # Determines the duplication type
    if rv_duplication3 % 2 == 0:

        # Insert data into MySQL tables
        cursor.execute("INSERT INTO cliente VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
        CO_CLIENTE, NA_NOMBRE, NA_APELLIDO1, NA_APELLIDO2, CO_SEXO, DT_NACIMIENTO, NU_EDAD, CO_NACIONALIDAD, DT_ALTA,
        IN_TARJETA_COMPRA))
        cursor.execute("INSERT INTO email VALUES (%s, %s, %s)", (NA_EMAIL, IN_VERIFICADO_EMAIL, CO_CLIENTE))
        cursor.execute("INSERT INTO documento VALUES (%s, %s, %s, %s)",
                       (NU_DOCUMENTO, DT_CADUCIDAD_DOC, IN_VERIFICADO_DOC, CO_CLIENTE))
        cursor.execute("INSERT INTO direccion VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
        ID_DIRECCION, TIPO_DIRECCION, DIRECCION, NUMERO, BLOQUE, PISO, PUERTA, CO_POSTAL, CIUDAD, PAIS, CO_CLIENTE))
        cursor.execute("INSERT INTO telefono VALUES (%s, %s, %s, %s)",
                       (TELEFONO, PREFIJO, IN_VERIFICADO_TEL, CO_CLIENTE))
        if IN_TARJETA_COMPRA == 1:
            cursor.execute("INSERT INTO tarjeta_compra VALUES (%s, %s, %s, %s, %s)",
                           (NU_TARJETA, TITULAR, CVV, DT_CADUCIDAD_TAR, CO_CLIENTE))
        mydb.commit()

        # Write data to Supermarket System files
        csv_writer_1.writerow(
            [CO_CLIENTE, NA_NOMBRE, NA_APELLIDO1, NA_APELLIDO2, None, DT_NACIMIENTO, None, None, DT_ALTA,
             IN_TARJETA_COMPRA])
        csv_writer_2.writerow([NU_DOCUMENTO, DT_CADUCIDAD_DOC, IN_VERIFICADO_DOC, CO_CLIENTE])
        csv_writer_3.writerow([None, None, None, None, None, None, None, None, None, None, CO_CLIENTE])
        csv_writer_4.writerow([TELEFONO, PREFIJO, IN_VERIFICADO_TEL, CO_CLIENTE])
        csv_writer_5.writerow([None, None, CO_CLIENTE])
        if IN_TARJETA_COMPRA == 1:
            csv_writer_6.writerow([NU_TARJETA, TITULAR, CVV, DT_CADUCIDAD_TAR, CO_CLIENTE])

    else:
        # Insert data into MySQL tables
        cursor.execute("INSERT INTO cliente VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
        CO_CLIENTE, NA_NOMBRE, NA_APELLIDO1, None, CO_SEXO, None, NU_EDAD, CO_NACIONALIDAD, None, IN_TARJETA_COMPRA))
        cursor.execute("INSERT INTO email VALUES (%s, %s, %s)", (NA_EMAIL, IN_VERIFICADO_EMAIL, CO_CLIENTE))
        cursor.execute("INSERT INTO documento VALUES (%s, %s, %s, %s)",
                       (NU_DOCUMENTO, None, IN_VERIFICADO_DOC, CO_CLIENTE))
        cursor.execute("INSERT INTO direccion VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
        ID_DIRECCION, TIPO_DIRECCION, DIRECCION, NUMERO, BLOQUE, PISO, PUERTA, CO_POSTAL, CIUDAD, PAIS, CO_CLIENTE))
        cursor.execute("INSERT INTO telefono VALUES (%s, %s, %s, %s)", (TELEFONO, None, IN_VERIFICADO_TEL, CO_CLIENTE))
        if IN_TARJETA_COMPRA == 1:
            cursor.execute("INSERT INTO tarjeta_compra VALUES (%s, %s, %s, %s, %s)",
                           (NU_TARJETA, TITULAR, CVV, None, CO_CLIENTE))
        mydb.commit()

        # Write data to Supermarket System files
        csv_writer_1.writerow(
            [CO_CLIENTE, NA_NOMBRE, None, NA_APELLIDO2, None, DT_NACIMIENTO, None, None, DT_ALTA, IN_TARJETA_COMPRA])
        csv_writer_2.writerow([NU_DOCUMENTO, DT_CADUCIDAD_DOC, IN_VERIFICADO_DOC, CO_CLIENTE])
        csv_writer_3.writerow([None, None, None, None, None, None, None, None, None, None, CO_CLIENTE])
        csv_writer_4.writerow([TELEFONO, PREFIJO, IN_VERIFICADO_TEL, CO_CLIENTE])
        csv_writer_5.writerow([None, None, CO_CLIENTE])
        if IN_TARJETA_COMPRA == 1:
            csv_writer_6.writerow([NU_TARJETA, TITULAR, None, DT_CADUCIDAD_TAR, CO_CLIENTE])

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# FOURTH DATA LOADING ON BOTH SYSTEMS: 1.000 DUPLICATE CLIENTS, WITH SOME INCONSISTENCIES.

for i in range(0, 1000):

    # To get the nationality (Spanish, Portuguese, French, Italian or German)
    rv_nationality = random.randint(-6, 10)

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # SPANISH CLIENTS
    if rv_nationality <= 6:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_esp.first_name_male()
            CO_SEXO = 'M'
        else:
            NA_NOMBRE = f_esp.first_name_female()
            CO_SEXO = 'F'
        NA_APELLIDO1 = f_esp.last_name()
        NA_APELLIDO2 = f_esp.last_name()
        CO_NACIONALIDAD = 'ESP'
        NU_DOCUMENTO = f_esp.bothify(text="########?", letters="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # PORTUGUESE CLIENTS
    elif rv_nationality == 7:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_por.first_name_male()
            CO_SEXO = 'M'
        else:
            NA_NOMBRE = f_por.first_name_female()
            CO_SEXO = 'F'
        NA_APELLIDO1 = f_por.last_name()
        NA_APELLIDO2 = f_por.last_name()
        CO_NACIONALIDAD = 'POR'
        NU_DOCUMENTO = f.bothify(text="?########", letters="XYZ") + f.random_letter().upper()

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # FRENCH CLIENTS
    elif rv_nationality == 8:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_fra.first_name_male()
            CO_SEXO = 'M'
        else:
            NA_NOMBRE = f_fra.first_name_female()
            CO_SEXO = 'F'
        NA_APELLIDO1 = f_fra.last_name()
        NA_APELLIDO2 = f_fra.last_name()
        CO_NACIONALIDAD = 'FRA'
        NU_DOCUMENTO = f.bothify(text="?########", letters="XYZ") + f.random_letter().upper()

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # ITALIAN CLIENTS
    elif rv_nationality == 9:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_ita.first_name_male()
            CO_SEXO = 'M'
        else:
            NA_NOMBRE = f_ita.first_name_female()
            CO_SEXO = 'F'
        NA_APELLIDO1 = f_ita.last_name()
        NA_APELLIDO2 = f_ita.last_name()
        CO_NACIONALIDAD = 'ITA'
        NU_DOCUMENTO = f.bothify(text="?########", letters="XYZ") + f.random_letter().upper()

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # GERMAN CLIENTS
    else:
        rv_genre = random.randint(1, 10)
        if rv_genre % 2 == 0:
            NA_NOMBRE = f_ger.first_name_male()
            CO_SEXO = 'M'
        else:
            NA_NOMBRE = f_ger.first_name_female()
            CO_SEXO = 'F'
        NA_APELLIDO1 = f_ger.last_name()
        NA_APELLIDO2 = f_ger.last_name()
        CO_NACIONALIDAD = 'GER'
        NU_DOCUMENTO = f.bothify(text="?########", letters="XYZ") + f.random_letter().upper()

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # EQUAL DATA FOR ALL NATIONALITIES
    CO_CLIENTE = random.randrange(10 ** 7, 10 ** 8)
    DT_NACIMIENTO = f.date_of_birth(minimum_age=18, maximum_age=99)
    NU_EDAD = calculate_age(DT_NACIMIENTO)
    DT_ALTA = f.date_between(start_date=add_years(datetime.now().date(), -20), end_date='today')
    IN_TARJETA_COMPRA = random.randint(0, 1)

    email_domain = random.choice(email_domains)
    NA_NOMBRE_EMAIL = (NA_NOMBRE + NA_APELLIDO1 + NA_APELLIDO2).lower().replace(" ", "")
    NA_NOMBRE_EMAIL_ST = accent_deletion(NA_NOMBRE_EMAIL)
    NA_EMAIL = f"{NA_NOMBRE_EMAIL_ST}@{email_domain}"
    IN_VERIFICADO_EMAIL = random.randint(0, 1)

    DT_CADUCIDAD_DOC = f.date_between(start_date=add_years(datetime.now().date(), -5),
                                      end_date=add_years(datetime.now().date(), 15))
    IN_VERIFICADO_DOC = random.randint(0, 1)

    NU_TARJETA = f.bothify(text="####-####-####")
    TITULAR = (NA_NOMBRE + ' ' + NA_APELLIDO1 + ' ' + NA_APELLIDO2).upper()
    CVV = random.randint(100, 999)
    DT_CADUCIDAD_TAR = f.date_between(start_date=add_years(datetime.now().date(), -5),
                                      end_date=add_years(datetime.now().date(), 15))

    complete_number = f_esp.phone_number().replace(' ', '')
    PREFIJO = complete_number[:3]
    TELEFONO = complete_number[3:]
    IN_VERIFICADO_TEL = random.randint(0, 1)

    ID_DIRECCION = f_esp.bothify(text="DIR-#####")
    TIPO_DIRECCION = random.choice(t_direccion)
    DIRECCION = f_esp.street_name()
    NUMERO = random.randint(1, 499)

    rv_bloque = random.randint(1, 2)
    if rv_bloque == 1:
        BLOQUE = random.randint(1, 10)
    else:
        BLOQUE = None

    rv_piso = random.randint(1, 2)
    if rv_piso == 1:
        PISO = random.randint(1, 20)
    else:
        PISO = None

    rv_puerta = random.randint(1, 2)
    if rv_puerta == 1:
        PUERTA = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
    else:
        PUERTA = None

    CO_POSTAL = random.randint(10000, 99999)
    CIUDAD = f_esp.city()
    PAIS = 'ESPAÑA'

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    rv_duplication4 = random.randint(1, 10)  # Determines the duplication type
    if rv_duplication4 % 2 == 0:

        # Insert data into MySQL tables
        cursor.execute("INSERT INTO cliente VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
        CO_CLIENTE, NA_NOMBRE, NA_APELLIDO1, NA_APELLIDO2, CO_SEXO, DT_NACIMIENTO, NU_EDAD, CO_NACIONALIDAD, DT_ALTA,
        IN_TARJETA_COMPRA))
        cursor.execute("INSERT INTO email VALUES (%s, %s, %s)", (NA_EMAIL, IN_VERIFICADO_EMAIL, CO_CLIENTE))
        cursor.execute("INSERT INTO documento VALUES (%s, %s, %s, %s)",
                       (NU_DOCUMENTO, DT_CADUCIDAD_DOC, IN_VERIFICADO_DOC, CO_CLIENTE))
        cursor.execute("INSERT INTO direccion VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
        ID_DIRECCION, TIPO_DIRECCION, DIRECCION, NUMERO, BLOQUE, PISO, PUERTA, CO_POSTAL, CIUDAD, PAIS, CO_CLIENTE))
        cursor.execute("INSERT INTO telefono VALUES (%s, %s, %s, %s)",
                       (TELEFONO, PREFIJO, IN_VERIFICADO_TEL, CO_CLIENTE))
        if IN_TARJETA_COMPRA == 1:
            cursor.execute("INSERT INTO tarjeta_compra VALUES (%s, %s, %s, %s, %s)",
                           (NU_TARJETA, TITULAR, CVV, DT_CADUCIDAD_TAR, CO_CLIENTE))
        mydb.commit()

        # Write data to Supermarket System files
        DT_ALTA_MAL = f.date_between(start_date=add_years(datetime.now().date(), 20),
                                     end_date=add_years(datetime.now().date(), 200))
        DT_CADUCIDAD_TAR_MAL = f.date_between(start_date=add_years(datetime.now().date(), 100),
                                              end_date=add_years(datetime.now().date(), 150))
        NU_DOCUMENTO_MAL = f.bothify(text="????####", letters="HFDV")

        csv_writer_1.writerow(
            [CO_CLIENTE, NA_NOMBRE, NA_APELLIDO1, NA_APELLIDO2, None, DT_NACIMIENTO, None, None, DT_ALTA_MAL,
             IN_TARJETA_COMPRA])
        csv_writer_2.writerow([NU_DOCUMENTO_MAL, DT_CADUCIDAD_DOC, IN_VERIFICADO_DOC, CO_CLIENTE])
        csv_writer_3.writerow([None, None, None, None, None, None, None, None, None, None, CO_CLIENTE])
        csv_writer_4.writerow([TELEFONO, PREFIJO, IN_VERIFICADO_TEL, CO_CLIENTE])
        csv_writer_5.writerow([None, None, CO_CLIENTE])
        if IN_TARJETA_COMPRA == 1:
            csv_writer_6.writerow([NU_TARJETA, TITULAR, CVV, DT_CADUCIDAD_TAR_MAL, CO_CLIENTE])

    else:
        # Insert data into MySQL tables
        cursor.execute("INSERT INTO cliente VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
        CO_CLIENTE, NA_NOMBRE, NA_APELLIDO1, None, CO_SEXO, None, NU_EDAD, CO_NACIONALIDAD, None, IN_TARJETA_COMPRA))
        cursor.execute("INSERT INTO email VALUES (%s, %s, %s)", (NA_EMAIL, IN_VERIFICADO_EMAIL, CO_CLIENTE))
        cursor.execute("INSERT INTO documento VALUES (%s, %s, %s, %s)",
                       (NU_DOCUMENTO, None, IN_VERIFICADO_DOC, CO_CLIENTE))
        cursor.execute("INSERT INTO direccion VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
        ID_DIRECCION, TIPO_DIRECCION, DIRECCION, NUMERO, BLOQUE, PISO, PUERTA, CO_POSTAL, CIUDAD, PAIS, CO_CLIENTE))
        cursor.execute("INSERT INTO telefono VALUES (%s, %s, %s, %s)", (TELEFONO, None, IN_VERIFICADO_TEL, CO_CLIENTE))
        if IN_TARJETA_COMPRA == 1:
            cursor.execute("INSERT INTO tarjeta_compra VALUES (%s, %s, %s, %s, %s)",
                           (NU_TARJETA, TITULAR, CVV, None, CO_CLIENTE))
        mydb.commit()

        # Write data to Supermarket System files
        NA_NOMBRE_MAL = f.first_name()

        csv_writer_1.writerow(
            [CO_CLIENTE, NA_NOMBRE_MAL, NA_APELLIDO1, NA_APELLIDO2, None, DT_NACIMIENTO, None, None, DT_ALTA,
             IN_TARJETA_COMPRA])
        csv_writer_2.writerow([NU_DOCUMENTO, DT_CADUCIDAD_DOC, IN_VERIFICADO_DOC, CO_CLIENTE])
        csv_writer_3.writerow([None, None, None, None, None, None, None, None, None, None, CO_CLIENTE])
        csv_writer_4.writerow([TELEFONO, PREFIJO, IN_VERIFICADO_TEL, CO_CLIENTE])
        csv_writer_5.writerow([None, None, CO_CLIENTE])
        if IN_TARJETA_COMPRA == 1:
            csv_writer_6.writerow([NU_TARJETA, TITULAR, 000, DT_CADUCIDAD_TAR, CO_CLIENTE])

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# FIFTH DATA LOADING ON BOTH SYSTEMS: 500 DUPLICATE CLIENTS, WITH THE SAME INFORMATION BUT EXPRESSED IN ANOTHER WAY.

for i in range(0, 500):

    # ONLY SPANISH CLIENTS
    rv_genre = random.randint(1, 10)
    if rv_genre % 2 == 0:
        s = random.randint(0, (len(abrev_masc) - 1))
        NA_NOMBRE = abrev_masc[s][0]
        NA_ABREV_NOMBRE = abrev_masc[s][1]
        CO_SEXO = 'M'
    else:
        s = random.randint(0, (len(abrev_fem) - 1))
        NA_NOMBRE = abrev_fem[s][0]
        NA_ABREV_NOMBRE = abrev_fem[s][1]
        CO_SEXO = 'F'

    NA_APELLIDO1 = f_esp.last_name()
    NA_APELLIDO2 = f_esp.last_name()
    CO_NACIONALIDAD = 'ESP'
    NU_DOCUMENTO = f_esp.bothify(text="########?", letters="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

    # EQUAL DATA FOR ALL NATIONALITIES
    CO_CLIENTE = random.randrange(10 ** 7, 10 ** 8)
    DT_NACIMIENTO = f.date_of_birth(minimum_age=18, maximum_age=99)
    NU_EDAD = calculate_age(DT_NACIMIENTO)
    DT_ALTA = f.date_between(start_date=add_years(datetime.now().date(), -20), end_date='today')
    IN_TARJETA_COMPRA = random.randint(0, 1)

    email_domain = random.choice(email_domains)
    NA_NOMBRE_EMAIL = (NA_NOMBRE + NA_APELLIDO1 + NA_APELLIDO2).lower().replace(" ", "")
    NA_NOMBRE_EMAIL_ST = accent_deletion(NA_NOMBRE_EMAIL)
    NA_EMAIL = f"{NA_NOMBRE_EMAIL_ST}@{email_domain}"
    IN_VERIFICADO_EMAIL = random.randint(0, 1)

    DT_CADUCIDAD_DOC = f.date_between(start_date=add_years(datetime.now().date(), -5), end_date=add_years(datetime.now().date(), 15))
    IN_VERIFICADO_DOC = random.randint(0, 1)

    NU_TARJETA = f.bothify(text="####-####-####")
    TITULAR = (NA_NOMBRE + ' ' + NA_APELLIDO1 + ' ' + NA_APELLIDO2).upper()
    CVV = random.randint(100, 999)
    DT_CADUCIDAD_TAR = f.date_between(start_date=add_years(datetime.now().date(), -5), end_date=add_years(datetime.now().date(), 15))

    complete_number = f_esp.phone_number().replace(' ', '')
    PREFIJO = complete_number[:3]
    TELEFONO = complete_number[3:]
    IN_VERIFICADO_TEL = random.randint(0, 1)

    ID_DIRECCION = f_esp.bothify(text="DIR-#####")
    TIPO_DIRECCION = random.choice(t_direccion)
    DIRECCION = f_esp.street_name()
    NUMERO = random.randint(1, 499)

    rv_bloque = random.randint(1, 2)
    if rv_bloque == 1:
        BLOQUE = random.randint(1, 10)
    else:
        BLOQUE = None

    rv_piso = random.randint(1, 2)
    if rv_piso == 1:
        PISO = random.randint(1, 20)
    else:
        PISO = None

    rv_puerta = random.randint(1, 2)
    if rv_puerta == 1:
        PUERTA = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
    else:
        PUERTA = None

    CO_POSTAL = random.randint(10000, 99999)
    CIUDAD = f_esp.city()
    PAIS = 'ESPAÑA'

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    rv_duplication4 = random.randint(1, 10)  # Determines the duplication type
    if rv_duplication4 % 2 == 0:

        # Insert data into MySQL tables
        cursor.execute("INSERT INTO cliente VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (CO_CLIENTE, NA_NOMBRE, NA_APELLIDO1, NA_APELLIDO2, CO_SEXO, DT_NACIMIENTO, NU_EDAD, CO_NACIONALIDAD, DT_ALTA, IN_TARJETA_COMPRA))
        cursor.execute("INSERT INTO email VALUES (%s, %s, %s)", (NA_EMAIL, IN_VERIFICADO_EMAIL, CO_CLIENTE))
        cursor.execute("INSERT INTO documento VALUES (%s, %s, %s, %s)", (NU_DOCUMENTO, DT_CADUCIDAD_DOC, IN_VERIFICADO_DOC, CO_CLIENTE))
        cursor.execute("INSERT INTO direccion VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (ID_DIRECCION, TIPO_DIRECCION, DIRECCION, NUMERO, BLOQUE, PISO, PUERTA, CO_POSTAL, CIUDAD, PAIS, CO_CLIENTE))
        cursor.execute("INSERT INTO telefono VALUES (%s, %s, %s, %s)", (TELEFONO, PREFIJO, IN_VERIFICADO_TEL, CO_CLIENTE))
        if IN_TARJETA_COMPRA == 1:
            cursor.execute("INSERT INTO tarjeta_compra VALUES (%s, %s, %s, %s, %s)",(NU_TARJETA, TITULAR, CVV, DT_CADUCIDAD_TAR, CO_CLIENTE))
        mydb.commit()

        # Write data to Supermarket System files
        csv_writer_1.writerow([CO_CLIENTE, NA_ABREV_NOMBRE, NA_APELLIDO1, NA_APELLIDO2, None, DT_NACIMIENTO, None, None, DT_ALTA, IN_TARJETA_COMPRA])
        csv_writer_2.writerow([NU_DOCUMENTO, DT_CADUCIDAD_DOC, IN_VERIFICADO_DOC, CO_CLIENTE])
        csv_writer_3.writerow([None, None, None, None, None, None, None, None, None, None, CO_CLIENTE])
        csv_writer_4.writerow([TELEFONO, PREFIJO, IN_VERIFICADO_TEL, CO_CLIENTE])
        csv_writer_5.writerow([None, None, CO_CLIENTE])
        if IN_TARJETA_COMPRA == 1:
            csv_writer_6.writerow([NU_TARJETA, TITULAR, CVV, DT_CADUCIDAD_TAR, CO_CLIENTE])

    else:
        # Insert data into MySQL tables
        cursor.execute("INSERT INTO cliente VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (CO_CLIENTE, NA_ABREV_NOMBRE, NA_APELLIDO1, None, CO_SEXO, None, NU_EDAD, CO_NACIONALIDAD, None, IN_TARJETA_COMPRA))
        cursor.execute("INSERT INTO email VALUES (%s, %s, %s)", (NA_EMAIL, IN_VERIFICADO_EMAIL, CO_CLIENTE))
        cursor.execute("INSERT INTO documento VALUES (%s, %s, %s, %s)", (NU_DOCUMENTO, None, IN_VERIFICADO_DOC, CO_CLIENTE))
        cursor.execute("INSERT INTO direccion VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (ID_DIRECCION, TIPO_DIRECCION, DIRECCION, NUMERO, BLOQUE, PISO, PUERTA, CO_POSTAL, CIUDAD, PAIS, CO_CLIENTE))
        cursor.execute("INSERT INTO telefono VALUES (%s, %s, %s, %s)", (TELEFONO, None, IN_VERIFICADO_TEL, CO_CLIENTE))
        if IN_TARJETA_COMPRA == 1:
            cursor.execute("INSERT INTO tarjeta_compra VALUES (%s, %s, %s, %s, %s)", (NU_TARJETA, TITULAR, CVV, None, CO_CLIENTE))
        mydb.commit()

        # Write data to Supermarket System files
        csv_writer_1.writerow([CO_CLIENTE, NA_NOMBRE, NA_APELLIDO1, NA_APELLIDO2, None, DT_NACIMIENTO, None, None, DT_ALTA, IN_TARJETA_COMPRA])
        csv_writer_2.writerow([NU_DOCUMENTO, DT_CADUCIDAD_DOC, IN_VERIFICADO_DOC, CO_CLIENTE])
        csv_writer_3.writerow([None, None, None, None, None, None, None, None, None, None, CO_CLIENTE])
        csv_writer_4.writerow([TELEFONO, PREFIJO, IN_VERIFICADO_TEL, CO_CLIENTE])
        csv_writer_5.writerow([None, None, CO_CLIENTE])
        if IN_TARJETA_COMPRA == 1:
            csv_writer_6.writerow([NU_TARJETA, TITULAR, 000, DT_CADUCIDAD_TAR, CO_CLIENTE])

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# FINAL DATA LOADING ON THE DEPARTMENT STORE SYSTEM: 5.000 ARTICLES AND 20.000 SALES.

# 5.000 ARTICLES
for i in range(0, 5000):

    CO_ARTICULO = f.bothify(text="###############")
    NA_COLOR = random.choice(color_domains)
    DT_FABRICACION_ART = f.date_between(start_date=add_years(datetime.now().date(), -15), end_date=add_years(datetime.now().date(), -1))

    rv_talla = random.randint(1, 5)
    rv_dt_caducidad = random.randint(1, 10)
    if rv_talla <= 2:
        CO_TALLA = random.choice(size_domains)
        DT_CADUCIDAD_ART = None
    else:
        CO_TALLA = None
        if rv_dt_caducidad % 2 == 0:
            DT_CADUCIDAD_ART = f.date_between(start_date=DT_FABRICACION_ART, end_date=add_years(DT_FABRICACION_ART, 10))
        else:
            DT_CADUCIDAD_ART = None

    rv_precio = random.randint(1, 20)
    if rv_precio <= 12:
        NU_PRECIO = round(random.uniform(0.99, 500.00), 2)
    elif 12 < rv_precio <= 17:
        NU_PRECIO = round(random.uniform(501.00, 1500.00), 2)
    else:
        NU_PRECIO = round(random.uniform(1501.00, 50000.00), 2)

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # Insert data into MySQL articles table
    cursor.execute("INSERT INTO articulo VALUES (%s, %s, %s, %s, %s, %s)", (CO_ARTICULO, NU_PRECIO, CO_TALLA, NA_COLOR, DT_FABRICACION_ART, DT_CADUCIDAD_ART))
    mydb.commit()

# 20.000 SALES
for i in range(0, 20000):

    CO_VENTA = f.bothify(text="##########")

    # CO_CLIENTE
    cursor.execute("SELECT COUNT(*) FROM cliente")
    total_registros_cli = cursor.fetchone()[0]
    registro_aleatorio_cli = random.randint(1, total_registros_cli)
    cursor.execute("SELECT * FROM cliente LIMIT %s, 1", (registro_aleatorio_cli - 1,))
    cliente = cursor.fetchone()

    CO_CLIENTE = cliente[0]

    # CO_ARTICULO y VL_VENTA
    cursor.execute("SELECT COUNT(*) FROM articulo")
    total_registros_art = cursor.fetchone()[0]
    registro_aleatorio_art = random.randint(1, total_registros_art)
    cursor.execute("SELECT * FROM articulo LIMIT %s, 1", (registro_aleatorio_art - 1,))
    articulo = cursor.fetchone()

    CO_ARTICULO = articulo[0]
    VL_VENTA = articulo[1]

    # RESTO DE CAMPOS
    TS_VENTA = f.date_time_between(start_date=add_years(datetime.now(), -15), end_date=datetime.now() - timedelta(days=1))
    CO_CENTRO_VENTA = random.choice(centre_domains)
    CO_CANAL_VENTA = random.choice(["online", "presencial"])
    IN_TICKET_REGALO = random.randint(0, 1)

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # Insert data into MySQL sales table
    cursor.execute("INSERT INTO ventas VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (CO_VENTA, CO_CLIENTE, CO_ARTICULO, VL_VENTA, TS_VENTA, CO_CENTRO_VENTA, CO_CANAL_VENTA, IN_TICKET_REGALO))
    mydb.commit()


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# FINAL DATA LOADING ON THE SUPERMARKET SYSTEM: 2.500 ARTICLES AND 10.000 SALES.

# 2.500 ARTICLES
for i in range(0, 2500):

    CO_ARTICULO = f.bothify(text="###############")
    NA_COLOR = random.choice(color_domains)
    DT_FABRICACION_ART = f.date_between(start_date=add_years(datetime.now().date(), -15), end_date=add_years(datetime.now().date(), -1))

    rv_talla = random.randint(1, 15)
    rv_dt_caducidad = random.randint(1, 10)
    if rv_talla <= 1:
        CO_TALLA = random.choice(size_domains)
        DT_CADUCIDAD_ART = None
    else:
        CO_TALLA = None
        if rv_dt_caducidad % 2 == 0:
            DT_CADUCIDAD_ART = f.date_between(start_date=DT_FABRICACION_ART, end_date=add_years(DT_FABRICACION_ART, 10))
        else:
            DT_CADUCIDAD_ART = None

    rv_precio = random.randint(1, 20)
    if rv_precio <= 12:
        NU_PRECIO = round(random.uniform(0.99, 30.00), 2)
    elif 12 < rv_precio <= 17:
        NU_PRECIO = round(random.uniform(31.00, 50.00), 2)
    else:
        NU_PRECIO = round(random.uniform(50.00, 70.00), 2)

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # Insert data into Supermarket System article table
    csv_writer_7.writerow([CO_ARTICULO, NU_PRECIO, CO_TALLA, NA_COLOR, DT_FABRICACION_ART, DT_CADUCIDAD_ART])

# 10.000 SALES
for i in range(0, 10000):
    
    CO_VENTA = f.bothify(text="##########")

    # CO_CLIENTE
    with open('Supermarket System/cliente.csv', 'r') as file_1:
        reader_cli = csv.reader(file_1)
        rows_cli = list(reader_cli)
        random_index_cli = random.randint(0, len(rows_cli) - 1)
        cliente = rows_cli[random_index_cli]
        CO_CLIENTE = cliente[0]

    # CO_ARTICULO y VL_VENTA
    with open('Supermarket System/articulo.csv', 'r') as file_2:
        reader_art = csv.reader(file_2)
        rows_art = list(reader_art)
        random_index_art = random.randint(0, len(rows_art) - 1)
        articulo = rows_art[random_index_art]
        CO_ARTICULO = articulo[0]
        VL_VENTA = articulo[1]

    # RESTO DE CAMPOS
    TS_VENTA = f.date_time_between(start_date=add_years(datetime.now(), -15), end_date=datetime.now() - timedelta(days=1))
    CO_CENTRO_VENTA = random.choice(supermarket_domains)

    rv_co_canal_venta = random.randint(1, 20)
    if rv_co_canal_venta <= 17:
        CO_CANAL_VENTA = "presencial"
    else:
        CO_CANAL_VENTA = "online"

    IN_TICKET_REGALO = None

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # Insert data into Supermarket System sales table
    csv_writer_8.writerow([CO_VENTA, CO_CLIENTE, CO_ARTICULO, VL_VENTA, TS_VENTA, CO_CENTRO_VENTA, CO_CANAL_VENTA, IN_TICKET_REGALO])

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Close Supermarket System files

csv_client_file.close()
csv_document_file.close()
csv_direction_file.close()
csv_phone_file.close()
csv_email_file.close()
csv_purchase_card_file.close()
csv_product_file.close()
csv_sales_file.close()
