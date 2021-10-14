# Funcion de 4 lineas

## Para obtener JSON a partir de una URL
###    - Test desarrollado para Adrián y Sergio.



1- Como Módulo

```
>>> import getapi
>>> getJsonFromApi("https://ifconfig.co/json")

{'ip': '2806:10be:7:3abe:5ce0:859e:2204:97f9', 'ip_decimal': 53200613184461119908441570127514998777, 'country': 'Mexico', 'country_iso': 'MX', 'country_eu': False, 'region_name': 'Quintana Roo', 'region_code': 'ROO', 'zip_code': '77083', 'city': 'Chetumal', 'latitude': 18.5308, 'longitude': -88.3203, 'time_zone': 'America/Cancun', 'asn': 'AS8151', 'asn_org': 'Uninet S.A. de C.V.', 'hostname': '2806-10be-0007-3abe-5ce0-859e-2204-97f9.ipv6.infinitum.net.mx', 'user_agent': {'product': 'python-requests', 'version': '2.26.0', 'raw_value': 'python-requests/2.26.0'}}

```

2- CLI

```
# python getapi.py https://ifconfig.co/json

{
    "ip": "2806:10be:7:3abe:5ce0:859e:2204:97f9",
    "ip_decimal": 53200613184461119908441570127514998777,
    "country": "Mexico",
    "country_iso": "MX",
    "country_eu": false,
    "region_name": "Quintana Roo",
    "region_code": "ROO",
    "zip_code": "77083",
    "city": "Chetumal",
    "latitude": 18.5308,
    "longitude": -88.3203,
    "time_zone": "America/Cancun",
    "asn": "AS8151",
    "asn_org": "Uninet S.A. de C.V.",
    "hostname": "2806-10be-0007-3abe-5ce0-859e-2204-97f9.ipv6.infinitum.net.mx",
    "user_agent": {
        "product": "python-requests",
        "version": "2.26.0",
        "raw_value": "python-requests/2.26.0"
    }
}

```

2- CLI Interactivo

```
# python getapi.py
Ingresa API url
 > https://ifconfig.co/json

 {
    "ip": "2806:10be:7:3abe:5ce0:859e:2204:97f9",
    "ip_decimal": 53200613184461119908441570127514998777,
    "country": "Mexico",
    "country_iso": "MX",
    "country_eu": false,
    "region_name": "Quintana Roo",
    "region_code": "ROO",
    "zip_code": "77083",
    "city": "Chetumal",
    "latitude": 18.5308,
    "longitude": -88.3203,
    "time_zone": "America/Cancun",
    "asn": "AS8151",
    "asn_org": "Uninet S.A. de C.V.",
    "hostname": "2806-10be-0007-3abe-5ce0-859e-2204-97f9.ipv6.infinitum.net.mx",
    "user_agent": {
        "product": "python-requests",
        "version": "2.26.0",
        "raw_value": "python-requests/2.26.0"
    }
} 

```