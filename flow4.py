[
    {
        "id": "583df2b7.264c1c",
        "type": "tab",
        "label": "Flow 3",
        "disabled": false,
        "info": ""
    },
    {
        "id": "6ac3b8ae.eabb48",
        "type": "http in",
        "z": "583df2b7.264c1c",
        "name": "",
        "url": "/pin4",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 210,
        "y": 180,
        "wires": [
            [
                "e3f083d0.5df6d"
            ]
        ]
    },
    {
        "id": "387b62b8.ffdcce",
        "type": "rpi-gpio in",
        "z": "583df2b7.264c1c",
        "name": "GPIO4",
        "pin": "7",
        "intype": "up",
        "debounce": "25",
        "read": false,
        "x": 220,
        "y": 300,
        "wires": [
            [
                "61f28d24.e4c264"
            ]
        ]
    },
    {
        "id": "61f28d24.e4c264",
        "type": "function",
        "z": "583df2b7.264c1c",
        "name": "setGPIO",
        "func": "global.set(\"GPIO\",msg.payload)\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 380,
        "y": 220,
        "wires": [
            [
                "372219b8.e3a1d6"
            ]
        ]
    },
    {
        "id": "e3f083d0.5df6d",
        "type": "function",
        "z": "583df2b7.264c1c",
        "name": "get GPIO",
        "func": "msg.payload = global.get(\"GPIO\");\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 410,
        "y": 140,
        "wires": [
            [
                "5b0c85bb.d4c3ac",
                "372219b8.e3a1d6"
            ]
        ]
    },
    {
        "id": "5b0c85bb.d4c3ac",
        "type": "http response",
        "z": "583df2b7.264c1c",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 640,
        "y": 160,
        "wires": []
    },
    {
        "id": "372219b8.e3a1d6",
        "type": "debug",
        "z": "583df2b7.264c1c",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 660,
        "y": 260,
        "wires": []
    }
]
