### Exceptions handling ###


## try - except

try:
    print(5 + "5")
except:
    print("Se ha producido un error")

## try - except - else

try:
    print(5 + 5)
except:
    print("Se ha producido un error")
else: ## Si no se produce error se ejecuta else
    print("No se ha producido un error")


## try - except - else - finally

try:
    print(5 + 5)
except:
    print("Se ha producido un error")
else:
    print("No se ha producido un error")
finally: ## Siempre se ejecuta finally
    print("Continua ejecucion")


## try - except - typerror

try:
    print(5 + "5")
except TypeError:
    print("Se ha producido un error")


## try - except - errror almacenado en variable

try:
    print(5 + "5")
except Exception as error:
    print("Se ha producido un error: " + str(error))