## Sentencia Match

Una sentencia match recibe una expresion y compara su valor con patrones sucesivos dados en uno o mas bloques case.Esto es similar a grandes rasgos con una sentencia switch

### Ejemplo
```
def htt_errors(status):
    match(status):
        case 400:
            return "Bad Request"
        case 401:
            return  "Not found"

print(htt_errors(401)) 
```