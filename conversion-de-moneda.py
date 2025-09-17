# Paso 1: Definir el valor actual del Euro y Dolar con respecto al peso Mexicano

tipo_cambio_eur_a_mxn = 23.70 # Mejora consumir la información actualizada de un API o BD
tipo_cambio_usd_a_mxn = 20.75 # Mejora consumir la información actualizada de un API o BD

# Paso 2: Solicitar al usuario el tipo de conversión (Euro a MEx o Dólar a Mex)    

tipo_conversion = input("Ingrese el tipo de conversión (EUR/USD): ")

# Paso 3: Solicitar al usuario el monto a convertir

monto_a_convertir = float(input("Ingrese el monto a convertir: "))

# Paso 4: Realizar la conversiòn utilizando el tipo de cambio correspondiente

if tipo_conversion.upper() == "EUR":
    resultado = monto_a_convertir * tipo_cambio_eur_a_mxn
    print("El resultado de la conversión de EUR a MXN es: ", resultado)
elif tipo_conversion.upper() == "USD":
    resultado = monto_a_convertir * tipo_cambio_usd_a_mxn
    print("El resultado de la conversión de USD a MXN es: ", resultado)
else: 
    print ("No esta disponible este tipo de conversión actualmente")                      